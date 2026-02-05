# Project Name: DeTrust Score Predictor

Please read till the end to see links to the dataset and source code.

---
  
## 1. Project Overview

This project implements a **DeTrust Score system** to predict user trustworthiness using a combination of **machine learning** (XGBoost and Random Forest) with **rule-based scoring** to provide transparent and interpretable trust scores for users. The system classifies users as **Good User** or **Default Risk** and provides a detailed breakdown of their **stability, network, and behavior scores**, producing a final score ranging from 300 to 850.

The project includes:

- Model training and evaluation (XGBoost and Random Forest)
- Rule-based scoring for transparency
- A Streamlit-based frontend for interactive predictions
- Feature-level contribution analysis (+/- points)

---

## Features

- **Dual Scoring Approach**: Machine learning predictions combined with rule-based calculations for transparency
- **Interactive Web App**: Streamlit-based interface for real-time predictions
- **REST API**: FastAPI endpoints for programmatic access
- **Feature Contribution Analysis**: Detailed breakdown of score components and their impacts
- **Model Comparison**: Choose between XGBoost and Random Forest models
- **Comprehensive Evaluation**: Classification metrics and probability outputs

## 2. Score Components

The system calculates three main scores:

1. **Stability Score (0-100)** - Account reliability and consistency
   - Account age
   - Profile completeness
   - Email verification
   - Login consistency

2. **Network Score (0-100)** - Social connections and influence
   - User connections
   - Account maturity
   - Social influence metrics
   - Pagerank Influence (optional)  

3. **Behavior Score (0-100)** - Activity patterns and quality
   - Response times
   - Message activity
   - Toxicity levels
   - Spam behavior

**Total DeTrust Score:** Weighted sum of the three components scaled to **300–850**.

---

## 3. Dataset Description

The project uses a synthetic dataset (`data/detrust_dataset.xlsx`) with the following features:

- `user_id`: Unique user identifier
- `device_id`: Device information
- `ip_address`: IP address data
- `account_created_at`: Account creation timestamp
- `account_age_days`: Account age in days
- `login_timestamp`: Last login time
- `avg_response_time`: Average response time
- `consistent_logins`: Number of consistent logins
- `random_logins`: Number of random/inconsistent logins
- `changing_ip_addresses`: IP address changes
- `verified_email`: Email verification status
- `complete_profile`: Profile completeness percentage
- `messages_per_day`: Daily message count
- `toxic_message_count_prior`: Prior toxic messages
- `spammy_chat_behavior`: Spam behavior indicators
- `connects_with_other_users`: Network connections
- `target`: Binary target (1 = Good User, 0 = Default Risk)

---

## 4. Project Structure
```
DeTrust_Score/
│
├── data/
│ └── detrust_dataset.xlsx # Main dataset
│
├── model/
│ ├── xgb_model.json # Trained XGBoost model
│ └── rf_model.pkl # Trained Random Forest model
│
├── Phase1.ipynb # Data generation and EDA
├── Phase2.ipynb # Rule-based engine and API development
├── Phase3.ipynb # ML model training and evaluation
│
├── api.py # FastAPI application
├── scoring.py # Scoring functions and utilities
├── streamlit.py # Streamlit web application
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
└── pycache/ # Python cache files

```

---

## 5. Requirements

- Python 3.8+
- Libraries listed in `requirements.txt`:
  - streamlit==1.29.0
  - xgboost==1.7.6
  - scikit-learn==1.3.2
  - pandas==2.1.1
  - numpy==1.27.4
  - matplotlib==3.8.0
  - seaborn==0.12.3
  - networkx==3.1
  - joblib==1.3.2
  - fastapi (for API)

---

## 6. Installation (Step-by-step Commands)

### 6.1 Clone Repository

```bash
git clone https://github.com/Sopheaktra34/DeTrust_Score.git
cd DeTrust_Score
```
### 6.2 Python Environment Setup
1. Create a virtual environment:
```bash
python -m venv venv
```
2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```
```bas
# Linux/Mac
source venv/bin/activate
```
3. Install dependencies:
```bash 
pip install -r requirements.txt
```
## 7. Running the API
```bash
uvicorn api:app --reload
```
The API will be available at http://localhost:8000//docs

API Endpoints
- GET /: Health check
- GET /score/{user_id}: Get precomputed score for a user
- GET /score/live/{user_id}: Calculate live score for a user
- Example API response:
```bash
{
  "user_id": 123,
  "credit_score": 750,
  "category": "Very Good"
}
```

## 8. Running the Streamlit App
```bash
streamlit run streamlit.py
```
1. Fill in Account Info, Behavior Info, and Network Info
2. Click Predict Trust Score
3. View:
- Overall Trust Score
- Component Scores
- Feature Contribution (+/- points)
- Prediction Probability (Good/Default)

## 9. Trust Score Interpretation

The Trust Score ranges from **300 to 850** and is divided into categories for easier understanding:

| Trust Score| Category    |             |
|------------|-------------|-------------|
| 800 – 850  | Excellent   |             |
| 740 – 799  | Very Good   |
| 670 – 739  | Good        |
| 580 – 669  | Fair        |
| 500 – 579  | Poor        |
| < 500      | Very Poor   |

> Notes: 
> - Higher scores indicate lower risk and better trustworthiness.
> - Scores are calculated from weighted contributions of **Stability**, **Network**, and **Behavior**.


## 10. Model Evaluation
- Classification: Good vs Default
- Probability prediction for user trust
- Transparency via feature contributions
- Weighted scoring for stability, network, and behavior

## 11. Conclusion
This project demonstrates a reproducible, interpretable approach for user trust scoring using machine learning and rule-based scoring. It allows for detailed insights into why a user is classified as Good or Default Risk, providing actionable recommendations for improvement.
