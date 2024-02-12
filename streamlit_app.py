from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "astronot.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")


# Page configuration
st.set_page_config(page_title="Welcome to DS-UPB", page_icon="")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Display header with personalized name
st.header(f" UPB Data Science Playground ! ", anchor=False)

if st.button("Let's Go."):
    st.write("coming soon stay tuned, 🇮🇩️ 🇮🇩️")

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-robot", height=300)

col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("assets/me.jpeg")

with col2:
    st.write("Asep Muhidin")
    st.write("Pelita Bangsa Univesity Lecturer ")
