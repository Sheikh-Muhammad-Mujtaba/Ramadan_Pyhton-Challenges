import streamlit as st
import random
import time

st.set_page_config(
    page_title="Cybersecurity Quiz App",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
 <style>
    /* Cybersecurity Theme - Base Styles */
    .stApp {
        background-color: #0a0e17;
        color: #e0e0e0;
        font-family: 'Courier New', monospace;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(0, 212, 255, 0.05) 0%, rgba(0, 212, 255, 0) 40%),
            linear-gradient(to bottom, rgba(6, 36, 52, 0.8) 0%, rgba(0, 0, 0, 0.9) 100%);
        background-attachment: fixed;
    }

    /* Header with Gradient Text */
    .stApp h1, .stApp .stTitle {
        -webkit-background-clip: text;
        background-clip: text;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0, 247, 255, 0.3);
        animation: pulse 3s infinite alternate;
        letter-spacing: 1px;
    }

    /* Subheaders with different gradient */
    .stApp h2, .stApp h3, .stApp .stSubheader {
        -webkit-background-clip: text;
        animation: pulse 0.1s infinite alternate;
        font-weight: bold;
        letter-spacing: 0.5px;
    }

    /* Matrix-like animation for the title */
    @keyframes pulse {
        0% { opacity: 0.8; text-shadow: 0 0 5px rgba(0, 247, 255, 0.3); }
        100% { opacity: 1; text-shadow: 0 0 15px rgba(0, 247, 255, 0.7), 0 0 30px rgba(0, 247, 255, 0.4); }
    }

    /* Glowing border animation */
    @keyframes borderGlow {
        0% { box-shadow: 0 0 5px #00f5ff; }
        50% { box-shadow: 0 0 20px #00f5ff; }
        100% { box-shadow: 0 0 5px #00f5ff; }
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #003366, #004080);
        color: #e0e0e0;
        border: 1px solid #00a8ff;
        border-radius: 5px;
        padding: 10px 24px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        animation: borderGlow 3s infinite;
    }

    .stButton>button:hover {
        background: linear-gradient(45deg, #004080, #0066cc);
        transform: translateY(-2px);
        box-shadow: 0 0 15px #00f5ff;
    }

    /* Radio buttons */
    .stRadio>div {
        flex-direction: column;
        align-items: start;
    }

    .stRadio [data-baseweb="radio"] {
        background-color: rgba(0, 30, 60, 0.7);
        border: 1px solid #004080;
        border-radius: 5px;
        padding: 10px 15px;
        margin: 5px 0;
        width: 100%;
        transition: all 0.3s ease;
    }

    .stRadio [data-baseweb="radio"]:hover {
        background-color: rgba(0, 60, 120, 0.7);
        border-color: #00a8ff;
        box-shadow: 0 0 10px rgba(0, 168, 255, 0.5);
        transform: translateX(5px);
    }

    /* Success and error messages */
    .stAlert {
        border: 2px solid;
        border-radius: 5px;
        animation: fadeIn 0.5s ease-in;
    }

    .element-container .stAlert[data-baseweb="notification"] {
        background-color: rgba(0, 20, 40, 0.8);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Success message */
    .element-container .stAlert.success {
        border-color: #00ff88;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }

    /* Error message */
    .element-container .stAlert.error {
        border-color: #ff3860;
        box-shadow: 0 0 10px rgba(255, 56, 96, 0.5);
    }

    /* Correct and incorrect answers */
    .correct {
        color: #00ff88;
        font-weight: bold;
        text-shadow: 0 0 5px rgba(0, 255, 136, 0.5);
    }

    .incorrect {
        color: #ff3860;
        font-weight: bold;
        text-shadow: 0 0 5px rgba(255, 56, 96, 0.5);
    }

    /* Dividers */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 168, 255, 0), rgba(0, 168, 255, 0.75), rgba(0, 168, 255, 0));
        margin: 20px 0;
    }

    /* Caption styling */
    .stApp .caption {
        color: #00a8ff;
        font-style: italic;
    }

    /* Typing animation for questions */
    .stSubheader {
        overflow: hidden;
        border-right: 2px solid #00a8ff;
        white-space: nowrap;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #00a8ff }
    }

    /* Digital counter for score */
    .digital-counter {
        font-family: 'Courier New', monospace;
        background-color: rgba(0, 20, 40, 0.8);
        border: 1px solid #00a8ff;
        border-radius: 5px;
        padding: 5px 10px;
        color: #00ff88;
        display: inline-block;
    }

    /* Background grid effect */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0, 40, 70, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 40, 70, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
        z-index: -1;
    }

    /* Binary code animation in the background */
    @keyframes binary {
        0% { opacity: 0.1; }
        50% { opacity: 0.2; }
        100% { opacity: 0.1; }
    }

    .binary-code {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        font-family: 'Courier New', monospace;
        font-size: 10px;
        color: #00a8ff;
        opacity: 0.1;
        z-index: -2;
        overflow: hidden;
        animation: binary 5s infinite;
    }

    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background-color: rgba(0, 20, 40, 0.9);
    }

    /* Lock icon animation */
    .lock-icon {
        display: inline-block;
        animation: lockPulse 2s infinite alternate;
    }

    @keyframes lockPulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.2); }
    }
</style>

<!-- Add binary code background -->
<div class="binary-code">
01001000 01100001 01100011 01101011 01100101 01110010 00100000 01000101 01110100 01101000 01101001 01100011 01110011 00100000 
01000011 01111001 01100010 01100101 01110010 01110011 01100101 01100011 01110101 01110010 01101001 01110100 01111001 00100000 
01010000 01110010 01101111 01110100 01100101 01100011 01110100 01101001 01101111 01101110 00100000 01000110 01101001 01110010 
01100101 01110111 01100001 01101100 01101100 00100000 01000101 01101110 01100011 01110010 01111001 01110000 01110100 01101001 
01101111 01101110 00100000 01010011 01100101 01100011 01110101 01110010 01101001 01110100 01111001 00100000 01010000 01110010 
01101001 01110110 01100001 01100011 01111001 00100000 01000100 01100001 01110100 01100001
</div>

<!-- Custom title with animation -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Add lock icon animation to title
    const title = document.querySelector('.stTitle');
    if (title) {
        const text = title.textContent;
        if (text.includes('🔒')) {
            title.innerHTML = text.replace('🔒', '<span class="lock-icon">🔒</span>');
        }
    }
});
</script>
    """,
    unsafe_allow_html=True,
)

st.title("🔒 Cybersecurity Quiz Application")

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_count" not in st.session_state:
    st.session_state.question_count = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = []
if "results" not in st.session_state:
    st.session_state.results = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Define questions
questions = [
    {
        "question": "What is the primary purpose of a firewall?",
        "options": [
            "To detect viruses",
            "To block unauthorized access",
            "To encrypt data",
            "To monitor network traffic",
        ],
        "answer": "To block unauthorized access",
        "level": "Beginner",
    },
    {
        "question": "Which of the following is a strong password?",
        "options": [
            "password123",
            "P@ssw0rd!",
            "12345678",
            "qwerty",
        ],
        "answer": "P@ssw0rd!",
        "level": "Beginner",
    },
    {
        "question": "What does VPN stand for?",
        "options": [
            "Virtual Private Network",
            "Virtual Public Network",
            "Verified Private Network",
            "Virtual Proxy Network",
        ],
        "answer": "Virtual Private Network",
        "level": "Beginner",
    },
    {
        "question": "What is phishing?",
        "options": [
            "A type of malware",
            "A method of fishing",
            "A social engineering attack",
            "A type of encryption",
        ],
        "answer": "A social engineering attack",
        "level": "Intermediate",
    },
    {
        "question": "What is the purpose of two-factor authentication (2FA)?",
        "options": [
            "To increase internet speed",
            "To provide backup storage",
            "To add an extra layer of security",
            "To encrypt emails",
        ],
        "answer": "To add an extra layer of security",
        "level": "Intermediate",
    },
    {
        "question": "Which protocol is used for secure communication over the internet?",
        "options": [
            "HTTP",
            "FTP",
            "HTTPS",
            "SMTP",
        ],
        "answer": "HTTPS",
        "level": "Intermediate",
    },
    {
        "question": "What is a zero-day vulnerability?",
        "options": [
            "A vulnerability that has been known for zero days",
            "A vulnerability that is exploited before the vendor is aware of it",
            "A vulnerability that only occurs once",
            "A vulnerability that cannot be patched",
        ],
        "answer": "A vulnerability that is exploited before the vendor is aware of it",
        "level": "Intermediate",
    },
    {
        "question": "What is the main goal of a DDoS attack?",
        "options": [
            "To steal data",
            "To encrypt files",
            "To overwhelm a system with traffic",
            "To gain unauthorized access",
        ],
        "answer": "To overwhelm a system with traffic",
        "level": "Intermediate",
    },
    {
        "question": "What is the role of a Security Operations Center (SOC)?",
        "options": [
            "To develop software",
            "To monitor and respond to security incidents",
            "To manage employee schedules",
            "To conduct marketing campaigns",
        ],
        "answer": "To monitor and respond to security incidents",
        "level": "Intermediate",
    },
    {
        "question": "What is the most common target of ransomware attacks?",
        "options": [
            "Individuals",
            "Small businesses",
            "Large corporations",
            "Government agencies",
        ],
        "answer": "Large corporations",
        "level": "Intermediate",
    },
]

# Function to get a new random question
def get_new_question():
    available_questions = [q for q in questions if q not in st.session_state.answered_questions]
    if available_questions:
        st.session_state.current_question = random.choice(available_questions)
        st.session_state.answered_questions.append(st.session_state.current_question)
    else:
        st.session_state.current_question = None

# Function to reset the game
def reset_game():
    st.session_state.current_question = None
    st.session_state.score = 0
    st.session_state.question_count = 0
    st.session_state.total_questions = 0
    st.session_state.answered_questions = []
    st.session_state.results = []
    st.session_state.game_over = False

# Start screen for selecting the number of questions
if st.session_state.total_questions == 0:
    st.subheader("Welcome to the Cybersecurity Quiz!")
    options = st.selectbox(
        "Choose the number of questions you want to answer:",
        (3, 5, 8, 10),
    )
    if st.button("Start Quiz"):
        st.session_state.total_questions = options
        get_new_question()
        st.rerun()
else:
    # Check if the game is over
    if st.session_state.question_count >= st.session_state.total_questions:
        st.session_state.game_over = True

    # Display the game if it's not over
    if not st.session_state.game_over:
        # Get the current question from session state
        question = st.session_state.current_question

        # Display the question and options
        st.write(f"You selected {st.session_state.total_questions} Questions")
        st.subheader(f"Question {st.session_state.question_count + 1}: {question['question']}")
        st.caption(f"Level: {question['level']}")

        # Create radio buttons for the options
        selected_option = st.radio("Choose your answer", question["options"], key="answer")

        # Submit button to check the answer
        if st.button("Submit Answer"):
            if selected_option == question["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
                st.session_state.results.append((question["question"], selected_option, question["answer"], True))
            else:
                st.error(f"❌ Incorrect! The correct answer is **{question['answer']}**")
                st.session_state.results.append((question["question"], selected_option, question["answer"], False))

            # Increment question count
            st.session_state.question_count += 1

            # Wait for 2 seconds before showing the next question
            time.sleep(2)

            # Get a new question
            get_new_question()

            # Rerun the app to display the next question
            st.rerun()

    # Display end-of-game summary
    if st.session_state.game_over:
        st.subheader("🎉 Game Over! 🎉")
        st.write(f"Your final score is **{st.session_state.score}** out of **{st.session_state.total_questions}**.")
        if st.session_state.score == st.session_state.total_questions:
                st.balloons()
                st.write("You answer all Questions correct")
        # Display results with correct and incorrect answers
        st.subheader("Your Answers:")
        for result in st.session_state.results:
            question, user_answer, correct_answer, is_correct = result
            if is_correct:
                st.markdown(f"✅ **{question}**")
                st.markdown(f"Your answer: <span class='correct'>{user_answer}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"❌ **{question}**")
                st.markdown(f"Your answer: <span class='incorrect'>{user_answer}</span>", unsafe_allow_html=True)
                st.markdown(f"Correct answer: <span class='correct'>{correct_answer}</span>", unsafe_allow_html=True)
            st.write("---")

        # Play again button
        if st.button("Play Again"):
            reset_game()
            st.rerun()