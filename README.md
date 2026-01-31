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
```
2. Navigate to the project directory:
```bash
cd DeTrust_Score
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Run the App
To start the Streamlit app:
```bash
streamlit run streamlit.py
```
---

## 📊 Usage
The web interface asks for the following input categories:

🏦 1. Account Info
- Account age (days)
- Profile completeness percentage
- Email verification status

🧠 2. Behavioral Info
- Average response time
- Message count
- Login patterns
- Toxic / spam behavior

🌐 3. Network Info
- Number of connections with other users

After entering these values, click Predict Trust Score to view:
- Trust category (Good / Default)
- Prediction probabilities
- Component scores
- Feature contribution details

---

🧠 How Trust Score Is Calculated (Trust Score combines) :
- Machine learning classification
- Rule‑based scoring of Stability, Network, and Behavior
- Weighted overall score on a 300–850 scale
Each component’s contribution is shown to explain why the score increased or decreased.

---

DeTrust_Score/
├── data/                      # Datasets
├── model/                     # Saved ML models
├── streamlit.py               # Main app
├── scoring.py                 # Feature scoring logic
├── requirements.txt           # Python dependencies
├── Phase1.ipynb               # Generate Data and EDA
├── Phase2.ipynb               # Defind Scoring Function
├── Phase3.ipynb               # Train model (XGB and RF)
└── README.md                  # Project documentation (this file)
└── 
└── api.py                     # Testing API
