**🏏 IPL Score Predictor**
A machine learning project that predicts the final score of an IPL innings in real-time using live match features like current run rate, wickets fallen, and team information.

**📌 Table of Contents**

**Project Overview
Methodology
Features Used
Model Training & Evaluation
Key Findings
How to Run
Project Structure
Future Improvements****

**Project Overview**
The IPL Score Predictor estimates the total runs a batting team will score in an innings, given the match situation at any point during the first 6–20 overs. This is a regression problem — the model outputs a continuous predicted score rather than a win/loss label.
The goal is to provide a reliable, data-driven score estimate that could be used for:

                       -> Match analysis dashboards
                       -> Fantasy cricket tools
                       -> Broadcasting score projection overlay

**Methodology**
**1. Problem Framing**
The task is framed as a supervised regression problem. Each data point represents a snapshot of an ongoing innings (e.g., after 10 overs), and the target variable is the final score at the end of that innings.

**2. Data Collection & Preprocessing**

Historical IPL match ball-by-ball data was sourced (Kaggle IPL datasets).
Each over-level snapshot was extracted as an independent sample.
Features were engineered from raw ball-by-ball logs.
Missing values were handled via median imputation for numeric fields and mode for categorical ones.
Overs less than 5.0 are dropped as they contains very less info regarding upcoming game and we can't predict from just 30 balls as 8/2 at 3.1 can also become 200/4.
Corrected name errors and repalced them with original team names.
Categorical variables (team names) were encoded using Label Encoding / One-Hot Encoding.

**3. Feature Engineering**
**Key derived features created from raw match data:**
**FeatureDescription**
We used one hot coding to code name of batting and bowling teams as mathematical ML models such XGBoost does only mathematical calculation and were not able to understand text.

**Visualisation of data**
-> Used displot to check distribution of final score.
-> Used correlation matrix to check multicollinearity and relationship with target variable.

**Model Selection**
Used mutliple models but after compairing all, Random forest regressor results are most valid and satisfying.

**Deployment**
Finally, after saving the trained model, I deployed model on hugging face and pushed my app UI to git.
And after all, the model was uploaded to streamlit and is ready to use.

**Link**: https://ipl-score-predictor-igaganhere.streamlit.app/



## All of the steps and decision are based on results in iplproject.ipynb
