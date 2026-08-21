#importing necessary libraries
import sys
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from groq import Groq
import json

#Markdown title for the app
st.markdown("# Plan Generator")

#Getting user input for name and fitness goals and other parameters
name = st.text_input("Enter your name:")
Fitness_Goals = st.selectbox("Fitness Goals", ["Build Muscle", "Lose Fat", "Endurance", "General Fitness"])
Experience_Level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
Available_Equipment = st.selectbox("Available Equipment", ["None", "Basic (Dumbbells, Resistance Bands)", "Full Gym"])
Time_Commitment = st.selectbox("Time Commitment", ["30 minutes/day", "1 hour/day", "2 hours/day"])
Timeframe = st.text_input("Enter your timeframe (e.g., 1 Days, 3 months, 6 months):")
Injuries_Limitations = st.text_input("Injuries / Limitations: Optional*")

#assigning the groq api key from the environment variable
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY is not set. Please set it in your environment variables.")

#Initializing the Groq client and ChatGroq model
try:
    groq_chat = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-120b", temperature=0.7, max_tokens=500)
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")

#Generating the plan when the button is clicked
if st.button("Generate Plan"):
    if not Timeframe:
        st.error("Please enter a valid timeframe.")
        exit()
    try:
        response = groq_chat.invoke(
        f"""Generate a workout plan for {name} with the following parameters:
        Fitness Goals: {Fitness_Goals}
        Experience Level: {Experience_Level}
        Available Equipment: {Available_Equipment}
        Time Commitment: {Time_Commitment}
        Timeframe: {Timeframe}
        Injuries / Limitations: {Injuries_Limitations if Injuries_Limitations else 'None'}
        Please provide a detailed workout plan including exercises, sets, reps, and any other relevant information.
        with weekly breakdown and also day by day plan for the given timeframe. The plan should be structured in a way that is easy to follow and implement.)
        """
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        response = None

    st.write(f"""Generated Plan for {name} includig below contect: \n
        Fitness Goals: {Fitness_Goals} \n
        Experience Level: {Experience_Level} \n
        Available Equipment: {Available_Equipment} \n
        Time Commitment: {Time_Commitment} \n
        Timeframe: {Timeframe} \n
        Injuries / Limitations: {Injuries_Limitations} \n
        """)
    st.write(response.content)
