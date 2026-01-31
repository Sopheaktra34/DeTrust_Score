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

account_age_days
complete_profile
verified_email
avg_response_time
messages_per_day
consistent_logins
random_logins
connects_with_other_users
spammy_chat_behavior
toxic_message_count_prior


- Target: `1 = Good User`, `0 = Default Risk`

Dataset path: `data/detrust_dataset.xlsx` (or generated in the notebook)

---

## 4. Project Structure

DeTrust_Score/
│
├─ data/ # Dataset files
│ └─ detrust_dataset.xlsx
│
├─ model/ # Pre-trained ML models
│ ├─ xgb_model.json
│ └─ rf_model.pkl
│
├─ notebooks/ # Jupyter notebooks for experiments
│ ├─ Phase1.ipynb
│ └─ Phase2.ipynb
│
├─ streamlit.py # Main Streamlit app
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
└─ utils.py # Helper functions for scoring


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
6.2 Python Environment Setup
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
7. Running the Streamlit App
streamlit run streamlit.py
Fill in Account Info, Behavior Info, and Network Info

Click Predict Trust Score

View:

Overall Trust Score

Component Scores

Feature Contribution (+/- points)

Prediction Probability (Good/Default)

Recommendations

8. Trust Score Interpretation
Score	Category
800–850	Excellent
740–799	Very Good
670–739	Good
580–669	Fair
500–579	Poor
<500	Very Poor
9. Model Evaluation
Classification: Good vs Default

Probability prediction for user trust

Transparency via feature contributions

Weighted scoring for stability, network, and behavior

10. Conclusion
This project demonstrates a reproducible, interpretable approach for user trust scoring using machine learning and rule-based scoring. It allows for detailed insights into why a user is classified as Good or Default Risk, providing actionable recommendations for improvement.

🗂️ Download Link
You can download the trained models, dataset, and example outputs here:

🔗 GitHub Repository

11. Screenshots / Demo
Add screenshots or GIFs of your Streamlit app here (optional but recommended).

Main dashboard view

Component score breakdown

Feature contribution (+/- points)

Prediction and recommendations


---

If you want, I can **also generate a version that already includes badges** for Python version, Streamlit, and license — this makes your GitHub README look super professional.  

Do you want me to do that?
