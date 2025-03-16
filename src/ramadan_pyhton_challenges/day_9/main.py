import streamlit as st
from datetime import datetime
import os

# Set up the page configuration
st.set_page_config(page_title="Advanced Calculator", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS styling
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_path, "r") as file:
        css = file.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Call the function at the beginning
load_css()


# Initialize session state
if 'calculation' not in st.session_state:
    st.session_state.calculation = ''
if 'history' not in st.session_state:
    st.session_state.history = []

# Calculation function
def perform_calculation():
    try:
        result = eval(st.session_state.calculation)
        st.session_state.history.insert(0, {
            'expression': st.session_state.calculation,
            'result': result,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.session_state.calculation = str(result)
    except:
        st.session_state.calculation = 'Error'

# History management functions
def clear_history():
    st.session_state.history = []

def delete_history_item(index):
    del st.session_state.history[index]

# Main app
st.title("🧮 Advanced Calculator")

# Calculator display
display = st.text_input(
    label="", 
    value=st.session_state.calculation, 
    key="display", 
    disabled=True, 
    placeholder="0"
)

# Calculator buttons
buttons = [
    ['C', '←', '(', ')'],
    ['7', '8', '9', '÷'],
    ['4', '5', '6', 'x'],
    ['1', '2', '3', '−'],
    ['0', '.', '=', '&#43;']
]

for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        with cols[i]:
            if st.button(label, key=f"btn_{label}"):
                if label == 'C':
                    st.session_state.calculation = ''
                elif label == '←':
                    st.session_state.calculation = st.session_state.calculation[:-1]
                elif label == '=':
                    perform_calculation()
                elif label == '÷':
                    st.session_state.calculation += "/"
                elif label == 'x':
                    st.session_state.calculation += "*"
                elif label == '−':
                    st.session_state.calculation += "-"
                elif label == '&#43;':
                    st.session_state.calculation += "+"
                else:
                    if st.session_state.calculation == 'Error':
                        st.session_state.calculation = label
                    else:
                        st.session_state.calculation += label
                st.rerun()

# History sidebar
with st.sidebar:
    st.header("History 📚")
    
    if st.button("🗑️ Clear All History"):
        clear_history()
        st.rerun()
    

    
    for idx, item in enumerate(st.session_state.history):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="history-item">
                <div>
                    <small>{item['timestamp']}</small><br>
                    <b>{item['expression']} = {item['result']}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("🗑️", key=f"delete_{idx}"):
                delete_history_item(idx)
                st.rerun()
                
    if st.download_button(
        label="📥 Download History",
        data="\n".join([f"{item['timestamp']}: {item['expression']} = {item['result']}" 
              for item in st.session_state.history]),
        file_name="calculator_history.txt",
        mime="text/plain"
    ):
        pass