import streamlit as st
import random
import string


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    
    
    if use_digits:
        characters += string.digits
        
        
    if use_special:
        characters += string.punctuation
        
    return ''.join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="wide")
st.markdown("""
    <style>
        /* Main container */
        .stApp {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding: 2rem;
            font-family: 'Arial', sans-serif;
            color: #ffffff;
        }
        
        .stAppHeader {
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            background: linear-gradient(135deg, #6a11cb, #2575fc);
        }
        
        /* Title */
        h1 {
            color: #ffffff;
            text-align: center;
            margin-bottom: 1.5rem;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        /* Slider */
        .stSlider {
            margin-bottom: 1.5rem;
        }
        
    
        [data-testid="stSlider"] > div > div > div > div {
            width: 15px !important;
            height: 15px !important;
            background-color: #ff6f61 !important;
            border: 2px solid #ffffff !important;
        }

        [data-testid="stSlider"] > div > div > div > div > div {
            color: #ffffff !important;
        }

        [data-testid="stSlider"] > div > div > .st-an {
            height: 8px !important;
            background: linear-gradient(90deg, #ff6f61, #ffcc5c) !important;
            border: 1px solid #ffffff !important;
        }
      
        /* Checkboxes */
        .stCheckbox {
            margin-bottom: 1.5rem;
        }
        
        .stCheckbox label {
            color: #ffffff;
            font-size: 1.1rem;
        }
        
        /* Button */
        .stButton>button {
            background: linear-gradient(135deg, #ff6f61, #ffcc5c);
            color: #ffffff;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            border: none;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            color: #ffffff;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
        }
         
        .stButton>button:focus:not(:active) {
            color: #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        /* Generated Password */
        .stCode {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            margin-top: 1.5rem;
            color: #ffffff;
            font-size: 1.2rem;
            text-align: center;
        }
        
        /* Footer */
        .footer {
            position: absolute;
            border-top: 2px solid rgba(255, 255, 255, 0.2);
            padding-top: 1rem;
            width: 100%;
            bottom: -20vh;
            text-align: center;
            margin-top: 2rem;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9rem;
        }
        
       
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Password Generator")
length = st.slider("📏 Length of password", min_value=8, max_value=30, value=16)
use_digits = st.checkbox("🔢 Use digits")
use_special = st.checkbox("✨ Use special characters")

if st.button("Generate Password 🚀"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"**🔒 Generated Password:**")
    st.code(password, language="text")


st.markdown('<div class="footer">Made with ❤️ by Mujtaba | 🌟 Enjoy your secure passwords!</div>', unsafe_allow_html=True)
