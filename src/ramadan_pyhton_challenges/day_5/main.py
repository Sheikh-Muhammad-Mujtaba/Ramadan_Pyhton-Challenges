import streamlit as st
import random
import time
import requests


# Page configuration
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Main app container styling */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title styling */
    .stTitle {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #ffd93d ;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d);
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        text-transform: uppercase;
        box-shadow: 0px 4px 10px rgba(255, 107, 107, 0.3);
        width: 100%;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 15px rgba(255, 217, 61, 0.4);
    }

    .stButton>button:active {
        transform: scale(0.98);
        box-shadow: 0px 2px 8px rgba(255, 217, 61, 0.3);
    }

    /* Success message styling */
    .stSuccess {
        background: linear-gradient(145deg, rgba(0, 255, 0, 0.1), rgba(0, 200, 0, 0.1)) !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00;
        border-radius: 12px;
        padding: 12px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 255, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }

    .stSuccess:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(0, 255, 0, 0.2);
    }

    /* Subheader styling */
    .stSubheader {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 1rem;
    }

    /* Card styling for sections */
    .card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown('<div class="stTitle">Money Making Machine 💰</div>', unsafe_allow_html=True)

# Function to generate money
def generate_money():
    money = random.randint(1, 1000)
    return money

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side-hustles?apiKey=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles['side_hustle']
        else:
            return 'Freelancing - Create a profile on Upwork and start freelancing'
    except:
        return 'Something went wrong. Please try again later'

# Function to fetch money quotes
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money-quotes?QuoteRange=1&All=false")
        if response.status_code == 200:
            quotes = response.json()
            return quotes['money_quote'][0]
        else:
            return 'Your time is limited, don’t waste it living someone else’s life. Don’t be trapped by dogma, which is living with the results of other people’s thinking.'
    except:
        return 'Something went wrong. Please try again later'

# Layout using columns
col1, col2, col3 = st.columns(3)

# Column 1: Generate Money
with col1:
    st.markdown('<div class="stSubheader">Generate Money 💵</div>', unsafe_allow_html=True)
    if st.button("Generate Money", key="generate_money"):
        with st.spinner("Counting your money..."):
            time.sleep(2)
            amount = generate_money()
            st.success(f"Congratulations! You have generated ${amount}")

# Column 2: Side Hustle Ideas
with col2:
    st.markdown('<div class="stSubheader">Side Hustle Ideas 💡</div>', unsafe_allow_html=True)
    if st.button("Get Side Hustle Idea", key="side_hustle"):
        with st.spinner("Fetching your side hustle idea..."):
            time.sleep(2)
            hustle = fetch_side_hustle()
            st.success(f"{hustle}")

# Column 3: Money-Making Quotes
with col3:
    st.markdown('<div class="stSubheader">Money-Making Quotes 💬</div>', unsafe_allow_html=True)
    if st.button("Get Money Quote", key="money_quote"):
        with st.spinner("Fetching your money quote..."):
            time.sleep(2)
            quote = fetch_money_quote()
            st.success(f"{quote}")

# Footer
st.markdown(
    """
    <div style="position: relative; bottom: -30vh; border-top: 2px solid #595854; padding-top: 20px; text-align: center; margin-top: 2rem; color: #ffffff99;">
        Made with ❤️ by Mujtaba | Powered by Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)