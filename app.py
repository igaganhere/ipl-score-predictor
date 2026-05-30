import streamlit as st
from huggingface_hub import hf_hub_download
import joblib
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load Model
model_path = hf_hub_download(
    repo_id="igaganhere/ipl-score-predictor",
    filename="ml_model.pkl"
)
model = joblib.load(model_path)

# Teams
batting_teams = [
    'Chennai Super Kings', 'Deccan Chargers', 'Delhi Daredevils',
    'Gujarat Lions', 'Kings XI Punjab', 'Kochi Tuskers Kerala',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Pune Warriors',
    'Rajasthan Royals', 'Rising Pune Supergiants',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]
bowling_teams = [
    'Chennai Super Kings', 'Deccan Chargers', 'Delhi Daredevils',
    'Gujarat Lions', 'Kings XI Punjab', 'Kochi Tuskers Kerala',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Pune Warriors',
    'Rajasthan Royals', 'Rising Pune Supergiant', 'Rising Pune Supergiants',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

# UI
st.title("🏏 IPL Score Predictor")
st.markdown("Predict the final score of an IPL innings in real time!")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", batting_teams)
    runs = st.number_input("Current Runs", min_value=0)
    overs = st.number_input("Overs Completed", min_value=5.0, max_value=19.5, step=0.1)
    runs_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0)

with col2:
    bowling_team = st.selectbox("Bowling Team", bowling_teams)
    wickets = st.number_input("Wickets Lost", min_value=0, max_value=10)
    wickets_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=10)

if st.button("Predict Score 🚀"):
    # Encode
    batting_array  = [1 if team == batting_team else 0 for team in batting_teams]
    bowling_array  = [1 if team == bowling_team else 0 for team in bowling_teams]
    prediction_array = batting_array + bowling_array + [runs, wickets, overs, runs_last_5, wickets_last_5]
    prediction_array = np.array([prediction_array])

    pred = model.predict(prediction_array)
    st.success(f"🏏 Predicted Final Score: **{int(round(pred[0]))} runs**")