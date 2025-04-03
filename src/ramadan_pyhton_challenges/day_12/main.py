import google.generativeai as genai
from dotenv import load_dotenv
import os
import sqlite3
import chainlit as cl
from typing import Optional, Dict
import traceback
from chainlit.server import app

# Load environment variables and configure the API key
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-2.0-flash")


def execute_db(query, params=(), fetch=False):
    """Execute a database query efficiently and handle errors."""
    try:
        with sqlite3.connect("cybersheikh.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)

            if fetch:
                return cursor.fetchall()
            
            conn.commit()
    except Exception as e:
        print(f"❌ Database Error: {e}")


# Create tables if they don't exist
execute_db("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    session_id TEXT,  -- NEW: Unique ID per chat session
    role TEXT,  -- 'user' or 'model'
    content TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

execute_db("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE,
    name TEXT,
    email TEXT
)
""")

def save_message_to_db(user_id, session_id, role, content):
    """Save chat messages to SQLite database."""
    execute_db("INSERT INTO conversations (user_id, session_id, role, content) VALUES (?, ?, ?, ?)", 
               (user_id, session_id, role, content))


@cl.oauth_callback
async def oauth_callback(provider_id: str, token: str, row_user_data: Dict[str, str], default_user: cl.User) -> Optional[cl.User]:
    """Callback function to handle OAuth authentication."""
    
    user_id = row_user_data.get("sub") or default_user.identifier
    name = row_user_data.get("name", "Unknown User")
    email = row_user_data.get("email", "Unknown Email")
    
    # Save user details in DB
    execute_db("INSERT OR IGNORE INTO users (user_id, name, email) VALUES (?, ?, ?)", 
               (user_id, name, email))
    
    return default_user

    

system_prompt = """
You are **CyberSheikh**, a highly knowledgeable IT expert with a strong focus on **cybersecurity, ethical hacking, networking, and ethical tech practices**. You are designed to assist users in **tech-related** conversations, strictly following **Islamic and ethical guidelines**.

🌍 **Your Persona & Style:**  
- You use Arabic words (e.g., *Wallah, Habibi, Akhi, InshaAllah, MashaAllah*) and relavent emojis to make the conversation engaging and fit your identity.  
- Your responses are professional, **yet friendly and charismatic** like a knowledgeable **Sheikh of Cybersecurity**.  
- You strictly **avoid non-tech conversations** and gently **redirect users back to tech** if they go off-topic.  

🔒 **Ethical & Islamic Guidelines:**  
- **Promote Halal Tech Practices**: Guide users on ethical cybersecurity, legal hacking (*bug bounties, penetration testing*), and safe internet practices.  
- **Avoid Haram or Illegal Activities**: Never assist in hacking personal accounts, spreading misinformation, or unethical hacking. Instead, explain **why it is haram and dangerous**.  
- **Encourage Learning & Growth**: Guide users on **ethical hacking certifications (e.g., OSCP, CEH, PNPT), web security, and networking**.  
- **Educate on Privacy & Security**: Help users understand **online safety, encryption, anonymity, and secure browsing**.  

👨‍💻 **Your Creator & References:**  
- Your author is **Sheikh Mujtaba**, known online as **XD$4**.  
- He is a **security researcher** and an expert in **penetration testing & ethical hacking**.  
- If someone asks about him, refer them to his profiles:  
  - LinkedIn: [Sheikh M. Mujtaba Javed](https://www.linkedin.com/in/sheikh-m-mujtaba-javed-0362872b9/)  
  - X (Twitter): [@Mujtaba_Javed](https://x.com/Mujtaba_Javed_)  

💡 **Response Strategy:**  
- If asked about **cybersecurity, hacking, programming, networking**, or IT topics → **Answer with deep knowledge**.  
- If asked **non-tech** or **irrelevant** topics → **Answer it and Redirect back to cybersecurity or IT politely by telling those are my experties.**.  
- If asked to **do unethical hacking** → **Explain why it's haram and illegal, and provide legal alternatives like bug bounties**.  

Example responses:  
- ❌ **"Can you hack an Instagram account?"** → *"Astaghfirullah, Habibi! Wallah, this is haram and illegal. Instead, learn ethical hacking and earn legally with bug bounties. Let me show you how!"*  
- ✅ **"How can I secure my website from hackers?"** → *"MashaAllah, Akhi! Great question! You should start by implementing WAF (Web Application Firewall), using strong encryption, and keeping your software updated. Let me guide you!"*  
- ✅ **"What are the best practices for ethical hacking?"** → *"InshaAllah, Habibi! Focus on learning about penetration testing, vulnerability assessments, and always get permission before testing. Certifications like OSCP or CEH are great!"*
- ✅ **"Can you help me with programming?"** → *"Of course, Akhi! Programming is a great skill. What language are you interested in? Python, JavaScript, or something else?"*
"""


@cl.on_chat_start
async def handle_chat_start():
    """Handles the start of a chat session."""
    user_id = cl.user_session.get("user").identifier
    session_id = cl.user_session.get("id")  # Unique session ID
    
    # Initialize fresh history
    history = [{"role": "user", "content": system_prompt}]
    cl.user_session.set("history", history)
    cl.user_session.set("session_id", session_id)  # Store session ID
    
    await cl.Message(content=f"**Assalamualikum {user_id}**, \nHow can I help you today? 😊").send()


def get_chat_history(user_id, session_id):
    """Retrieve chat history for a user from SQLite."""
    return execute_db("SELECT role, content FROM conversations WHERE user_id = ? AND session_id = ? ORDER BY timestamp ASC", 
                      (user_id, session_id), fetch=True)


@cl.on_chat_resume
async def on_chat_resume():
    """Restore previous chat history on session resume."""
    user_id = cl.user_session.get("user").identifier
    session_id = cl.user_session.get("id")
    messages = get_chat_history(user_id, session_id) 
    
    if messages:
        for role, content in messages:
            role_text = "**You:**" if role == "user" else "**CyberSheikh:**"
            await cl.Message(content=f"{role_text} {content}").send()


def clear_chat_history(user_id, session_id):
    """Delete all chat messages for a specific user."""
    execute_db("DELETE FROM conversations WHERE user_id = ? AND session_id = ?", (user_id, session_id))


@cl.on_message
async def handle_message(message: cl.Message):
    """Handles user messages and processes responses."""
    
    user_id = cl.user_session.get("user").identifier
    session_id = cl.user_session.get("session_id")
    
    # Check if the user wants to clear history
    if message.content.lower() == "/clear":
        clear_chat_history(user_id, session_id)
        cl.user_session.set("history", [])  
        await cl.Message(content="✅ Your chat history has been cleared!").send()
        return
    
    history = cl.user_session.get("history", [])
    
    # Save user message to DB
    save_message_to_db(user_id, session_id, "user", message.content)
    history.append({"role": "user", "content": message.content})
    
    formatted_history = [{"role": "user" if msg["role"] == "user" else "model", "parts": [{"text": msg['content']}]} for msg in history]
        
    try:
        response = model.generate_content(contents=formatted_history, stream=True)
        
        response_message = cl.Message(content="")
        await response_message.send()
        
        response_text = ""
        for chunk in response:
            if chunk.text:
                response_text += chunk.text
                await response_message.stream_token(chunk.text)

        await response_message.update()
        
        # Save AI response to DB
        save_message_to_db(user_id, session_id, "assistant", response_text)  
        
        history.append({"role": "assistant", "content": response_text})
        cl.user_session.set("history", history)
    except Exception as e:
        error_message = f"❌ Error: {str(e)}\n\n```{traceback.format_exc()}```"
        print(error_message)  # Log error for debugging
        await cl.Message(content="⚠️ An error occurred. Please try again.").send()

asgi_app = app