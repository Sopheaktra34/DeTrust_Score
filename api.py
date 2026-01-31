from fastapi import FastAPI, HTTPException
import pandas as pd
from scoring import calculate_credit_score, categorize_score

app = FastAPI(
    title="DeTrust Phase 2 – Rule-Based Credit Scoring API",
    description="Rule-based, explainable credit score (300–850)",
    version="1.2"
)

DATA_PATH = "data/detrust_scored.xlsx"

try:
    df = pd.read_excel(DATA_PATH)

    # Extract numeric id from user_id like "user_3" → 3
    df["numeric_id"] = df["user_id"].str.extract(r'(\d+)').astype(int)

except FileNotFoundError:
    df = None
    print("⚠️ Dataset not found. API will compute scores on the fly.")


@app.get("/")
def root():
    return {"status": "DeTrust Phase 2 API is running"}


# Precomputed score
@app.get("/score/{user_id}")
def get_user_score(user_id: int):

    if df is None:
        raise HTTPException(status_code=500, detail="Dataset not loaded")

    # LOOKUP USING numeric_id
    user_row = df[df["numeric_id"] == user_id]

    if user_row.empty:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")

    row = user_row.iloc[0]
    score = int(row["credit_score"])
    category = categorize_score(score)

    return {
        "user_id": user_id,
        "credit_score": score,
        "category": category
    }

# Live scoring
@app.get("/score/live/{user_id}")
def get_user_score_live(user_id: int):

    if df is None:
        raise HTTPException(status_code=500, detail="Dataset not loaded")

    # LOOKUP USING numeric_id
    user_row = df[df["numeric_id"] == user_id]

    if user_row.empty:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")

    row = user_row.iloc[0]
    score = calculate_credit_score(row)

    return {
        "user_id": user_id,
        "credit_score": score,
        "category": categorize_score(score)
    }
