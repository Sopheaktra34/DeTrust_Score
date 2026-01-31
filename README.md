# Project Name: DeTrust Score Predictor

Please read till the end to see links to the dataset and source code.

---

## 1. Project Overview

This project implements a **DeTrust Score system** to predict user trustworthiness using a combination of **machine learning** and **rule-based scoring**. The system classifies users as **Good User ✅** or **Default Risk ❌** and provides a detailed breakdown of their **stability, network, and behavior scores**.

The project includes:

- Model training and evaluation (XGBoost and Random Forest)
- Rule-based scoring for transparency
- A Streamlit-based frontend for interactive predictions
- Feature-level contribution analysis (+/- points)

---

## 2. Score Components

The system calculates three main scores:

1. **Stability Score (0–100)**  
   - Account Age  
   - Profile Completeness  
   - Verified Email  
   - Login Consistency  

2. **Network Score (0–100)**  
   - Connections with other users  
   - Account Maturity  
   - Social Influence (Pagerank optional)  

3. **Behavior Score (0–100)**  
   - Average Response Time  
   - Daily Message Activity  
   - Toxicity  
   - Spammy Behavior  

**Total DeTrust Score:** Weighted sum of the three components scaled to **300–850**.

---

## 3. Dataset Description

- Generated synthetic dataset for demonstration
- Features per user:
   - user_id
   - device_id
   - ip_address
   - account_created_at
   - account_age_days
   - login_timestamp
   - avg_response_time
   - consistent_logins
   - random_logins
   - changing_ip_addresses
   - verified_email
   - complete_profile
   - incomplete_profile
   - messages_per_day
   - toxic_message_count_prior
   - spammy_chat_behavior
   - connects_with_other_users
   - target
     
- Target: `1 = Good User`, `0 = Default Risk`

Dataset path: `data/detrust_dataset.xlsx` (or generated in the notebook)

---

## 4. Project Structure
```
DeTrust_Score/
│
├─ data/ # Dataset files
│ └─ detrust_dataset.xlsx
│
├─ model/ ML models
│ ├─ xgb_model.json
│ └─ rf_model.pkl
│
├─ Phase1.ipynb # Generate and EDA on data
|
├─ Phase2.ipynb # Rule base Engine and api
|
├─ Phase3.ipynb # Training ML model
|
├─ README.md # Project documentation
|
├─ api.py
|
├─ requirements.txt # Python dependencies
|
├─ scoring.py   # scoring function
|
├─ streamlit.py # Main Streamlit app

```

---

## 5. Software Requirements

- Python 3.8+  
- Streamlit  
- XGBoost  
- Scikit-learn  
- NumPy  
- Joblib  
- NetworkX (optional for pagerank)  

All Python dependencies are listed in `requirements.txt`.

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
```
# Windows
venv\Scripts\activate

# Linux/Mac
```bas
source venv/bin/activate
```
3. Install dependencies:
```bash 
pip install -r requirements.txt
```

## 7. Running the Streamlit App
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

## 8. Trust Score Interpretation

The Trust Score ranges from **300 to 850** and is divided into categories for easier understanding:

## 8. Trust Score Interpretation

The final Trust Score ranges from 0–850 and is interpreted as follows:

| Trust Score| Category    |
|------------|-------------|
| 800 – 850  | Excellent   |
| 740 – 799  | Very Good   |
| 670 – 739  | Good        |
| 580 – 669  | Fair        |
| 500 – 579  | Poor        |
| < 500      | Very Poor   |

> Notes: 
> - Higher scores indicate lower risk and better trustworthiness.
> - Scores are calculated from weighted contributions of **Stability**, **Network**, and **Behavior**.


## 9. Model Evaluation
- Classification: Good vs Default
- Probability prediction for user trust
- Transparency via feature contributions
- Weighted scoring for stability, network, and behavior

## 10. Conclusion
This project demonstrates a reproducible, interpretable approach for user trust scoring using machine learning and rule-based scoring. It allows for detailed insights into why a user is classified as Good or Default Risk, providing actionable recommendations for improvement.
