import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Set page configuration
st.set_page_config(page_title="Time Zone App", page_icon="⏲", layout="wide")

# Custom CSS for styling
st.markdown("""
   <style>
    /* Gradient background for the entire app */
    .stApp {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
    }
    
    .stAppHeader {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
    }

    /* Style for tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 4px 4px 0 0;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    .stTabs [aria-selected="true"] {
        background-color: white;
        color: #4CAF50;
    }

    /* Style for buttons */
    .stButton button {
        width: 100%;
        background-color: white;
        color: #4CAF50;
        padding: 10px 24px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        font-weight: bold;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #f0f2f6;
        color: #45a049;
    }

    /* Style for success messages */
    .stAlert {
        border-radius: 8px;
        background-color: #02f292;
        color: #155724;
        text-align: center;
        border: 1px solid #02def2;
    }

    /* Style for headings */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white;
    }

    /* Style for time display in tabs */
    .stMetric>div {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 4px;
        color: #4CAF50;
    }

    /* Style for input fields */
    .stTimeInput>div, .stSelectbox>div {
        background-color: rgba(255, 255, 255, 0.9);
        color: #000000;
        border-radius: 4px;
        padding: 10px;
    }

    /* Footer styling */
    .footer {
        margin-top: 20px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
        color: white;
        text-align: start;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🌍 Time Zone App")
st.markdown("""
    **Welcome to the Time Zone App!**  
    This app helps you view the current time in multiple time zones and convert time between different time zones.
    """)

# Section 1: Display current time in tabs for selected time zones
st.subheader("🕒 Current Time in Selected Time Zones")

# Create tabs for each time zone
tabs = st.tabs(TIME_ZONES)

# Display current time in each tab
for i, tz in enumerate(TIME_ZONES):
    with tabs[i]:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.metric(label="Current Time", value=current_time)

# Section 2: Time conversion
st.subheader("⏳ Convert Time Between Time Zones")
col1, col2, col3 = st.columns(3)

with col1:
    current_time = st.time_input("Current Time", value=datetime.now().time())

with col2:
    from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

with col3:
    to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <strong>Tips:</strong><br/>
        - Use the tabs above to view the current time in different time zones.<br/>
        - Use the time converter below to convert a specific time from one time zone to another.<br/>
    </div>
    """, unsafe_allow_html=True)