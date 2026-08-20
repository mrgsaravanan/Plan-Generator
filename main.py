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
Timeframe = st.selectbox("Timeframe", ["1 day ", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"])
Injuries_Limitations = st.text_input("Injuries / Limitations: Optional*")

#assigning the groq api key from the environment variable
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY is not set. Please set it in your environment variables.")

#Initializing the Groq client and ChatGroq model
groq_chat = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-120b", temperature=0.7, max_tokens=500)

#Generating the plan when the button is clicked
if st.button("Generate Plan"):
    response = groq_chat.invoke(
    f"""Generating a plan for {name} with the following parameters:
    Fitness Goals: {Fitness_Goals}
    Experience Level: {Experience_Level}
    Available Equipment: {Available_Equipment}
    Time Commitment: {Time_Commitment}
    Timeframe: {Timeframe}
    Injuries / Limitations: {Injuries_Limitations if Injuries_Limitations else 'None'}"""
    )
    st.write(response.content)
