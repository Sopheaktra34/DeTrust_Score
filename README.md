# 🔍 DeTrust Score Predictor

**DeTrust Score Predictor** is a Python‑based trust scoring system designed to classify users as *Good (Group A)* or *Default (Group B)* using machine learning models and a rule‑based trust scoring algorithm. It also provides a detailed breakdown of trust components for explainability.

This project includes:
- A **Streamlit web app** for interactive trust scoring.
- Models such as **XGBoost** and **Random Forest**.
- A **rule‑based scoring system** that computes Stability, Network, and Behavior scores.
- Feature contribution explanations to understand why scores rise or fall.

---

## 🚀 Features

✔ Interactive web interface with Streamlit  
✔ Predicts user trust category (Good vs Default)  
✔ Displays:  
- Overall trust score  
- ML prediction probability  
- Component scores (Stability, Network, Behavior)  
- Feature‑level contribution breakdown  
✔ Supports XGBoost and Random Forest models  

---

## 🛠️ How It Works

The system calculates trust using a hybrid approach:

1. **Machine Learning Models**  
   Trained models (XGBoost, Random Forest) classify the user based on input features.

2. **Rule‑based Trust Scoring**  
   Computes three components:
   - **Stability**: Account age, profile completeness, email verification, login consistency
   - **Network**: Social connectivity and influence
   - **Behavior**: Messaging habits, responsiveness, toxicity, spam indicators

3. **Explainability**  
   Each component includes a breakdown of feature contributions to help interpret the score.

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Sopheaktra34/DeTrust_Score.git
