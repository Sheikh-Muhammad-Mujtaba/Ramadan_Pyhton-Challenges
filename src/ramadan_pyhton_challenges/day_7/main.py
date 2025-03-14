import streamlit as st  
import pandas as pd  
import datetime  
import csv  
import os  
import calendar  

# Set page configuration
st.set_page_config(
    page_title="Mood Tracker",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    /* Main Background and Typography */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Nunito', 'Helvetica Neue', sans-serif;
        color: #2c3e50;
    }

    /* Gradient Header Styling */
    .stApp h1, .stApp .stTitle {
        background-clip: text;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 2rem;
        text-align: center;
        animation: gradientShift 8s ease infinite;
        background-size: 300% 300%;
    }

    .stSelectbox>label {
        color: black;    
    }
    
    /* Subheader Styling */
    .stApp h2, .stApp h3, .stApp .stSubheader {
        background-clip: text;
        font-weight: 600;
        margin-top: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e0e0e0;
    }

    /* Gradient Animation */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(90deg, #6b5b95, #45b7d8);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(107, 91, 149, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #45b7d8, #6b5b95);
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(107, 91, 149, 0.4);
    }

    /* Success Message Styling */
    .stAlert {
        background: linear-gradient(90deg, rgba(107, 91, 149, 0.1), rgba(69, 183, 216, 0.1));
        border-left: 4px solid #6b5b95;
        border-radius: 8px;
        padding: 1rem;
        color: #2c3e50;
        animation: fadeIn 0.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }


    /* Mood Emoji Styling */
    .mood-emoji {
        font-size: 1.5rem;
        margin-right: 0.5rem;
        transition: transform 0.3s ease;
    }

    .mood-emoji:hover {
        transform: scale(1.2);
    }

    /* Calendar Grid Styling */
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 0.5rem;
        margin: 1rem 0;
    }

    .calendar-day {
        background-color: white;
        border-radius: 8px;
        padding: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }

    .calendar-day:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .calendar-day.empty {
        background-color: transparent;
        box-shadow: none;
    }

    .calendar-day.happy {
        background: linear-gradient(135deg, #fff8e1, #ffecb3);
        border-left: 3px solid #ffc107;
    }

    .calendar-day.sad {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-left: 3px solid #2196f3;
    }

    .calendar-day.angry {
        background: linear-gradient(135deg, #ffebee, #ffcdd2);
        border-left: 3px solid #f44336;
    }

    .calendar-day.neutral {
        background: linear-gradient(135deg, #f5f5f5, #e0e0e0);
        border-left: 3px solid #9e9e9e;
    }

    /* Mood Statistics Styling */
    .stat-card {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .stat-value {
        font-weight: 600;
        font-size: 1.2rem;
        color: #6b5b95;
    }

    /* Footer Styling */
    .footer {
        margin-top: 2rem;
        text-align: center;
        font-size: 0.9rem;
        color: #6c757d;
    }

       /* Mood Emoji Animation */
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .emoji-bounce {
        display: inline-block;
        animation: bounce 2s ease infinite;
    }

    /* Add custom styling for mood entries */
    .mood-entry {
        display: flex;
        align-items: center;
        padding: 0.5rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        background-color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }

    .mood-entry:hover {
        transform: translateX(5px);
    }

    .mood-date {
        font-weight: 600;
        margin-right: 1rem;
        color: #6b5b95;
    }

    .mood-happy {
        color: #ffc107;
    }

    .mood-sad {
        color: #2196f3;
    }

    .mood-angry {
        color: #f44336;
    }

    .mood-neutral {
        color: #9e9e9e;
    }

    /* Add a gradient border to the page */
    .main .block-container {
        border-radius: 12px;
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.8);
        box-shadow: 0 0 0 3px #6b5b95, 0 0 0 6px #45b7d8;
        margin: 1rem;
    }
</style>
    """
    ,
    unsafe_allow_html=True,
)

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Ensure mood file exists and has correct columns
def initialize_mood_file():
    if not os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])  # Write headers

# Load mood data safely
def load_mood_data():
    initialize_mood_file()
    return pd.read_csv(MOOD_FILE)

# Save mood data function
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Streamlit app title
st.title("😊 Mood Tracker")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["😊 Happy", "😢 Sad", "😠 Angry", "😐 Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    save_mood_data(today, mood[2:])
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:
    st.subheader("📊 Mood Trends Over Time")
    
    # Convert date strings to datetime objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data["Mood"].value_counts()
    
    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)
    
    # Display mood statistics
    st.subheader("📈 Mood Statistics")
    st.write(f"Total Entries: {len(data)}")
    st.write(f"Most Frequent Mood: {mood_counts.idxmax()} ({mood_counts.max()} times)")
    
    # Mood Calendar Visualization
    st.subheader("📅 Mood Calendar")
    data["Year"] = data["Date"].dt.year
    data["Month"] = data["Date"].dt.month
    data["Day"] = data["Date"].dt.day
    
    selected_year = st.selectbox("Select Year", sorted(data["Year"].unique(), reverse=True))
    selected_month : int = st.selectbox("Select Month", data["Month"].unique())
    
    filtered_data = data[(data["Year"] == selected_year) & (data["Month"] == selected_month)]
    cal = calendar.monthcalendar(selected_year, selected_month)
    
    st.write(f"### {calendar.month_name[selected_month]} {selected_year}")
    
    # Render calendar in a grid format
    days_of_week = "Mon | Tue | Wed | Thu | Fri | Sat | Sun"
    st.markdown(f"**{days_of_week}**")
    
    for week in cal:
        week_str = " | ".join([f"{day:2}" if day != 0 else "  " for day in week])
        st.markdown(week_str)
    
    # Display mood entries for the selected month
    st.subheader(f"📝 Mood Entries for {calendar.month_name[selected_month]} {selected_year}")
    st.write(filtered_data[["Date", "Mood"]])

# Footer
st.markdown("---")
st.markdown("<div class='footer''>Built with ❤️ by Mujtaba </div>",    unsafe_allow_html=True,)
