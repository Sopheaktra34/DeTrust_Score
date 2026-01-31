import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import networkx as nx
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

df = pd.read_excel("data/detrust_dataset.xlsx")

# 1. STABILITY SCORE COMPONENT (30%)
def calculate_stability_score(row):
    """Calculate stability score (30% weight)"""
    # Account age: older = better (0-40 points)
    age_score = max(0, min(row['account_age_days'] / 10, 40))
    
    # Profile completeness: complete = better (0-30 points)
    profile_score = int(row['complete_profile']) * 30
    
    # Verified email bonus (0-10 points)
    verified_score = int(row['verified_email']) * 10
    
    # Login consistency (0-20 points)
    total_logins = row['consistent_logins'] + row['random_logins']
    consistency_score = (
        (row['consistent_logins'] / total_logins) * 20
        if total_logins > 0 else 0
    )

    stability_score = (
        age_score +
        profile_score +
        verified_score +
        consistency_score
    )

    return min(stability_score, 100)

# 2. NETWORK SCORE COMPONENT (30%)
import networkx as nx

# pagerank_scores = nx.pagerank(G, alpha=0.85)

def calculate_network_score(row, pagerank_scores=None):
    """
    Network score based on observable social connectivity and influence.
    Score range: 0 to 80.
    """
    connections = max(0, row['connects_with_other_users'])
    account_age = max(0, row['account_age_days'])
    user_id = row['user_id']

    # 1. Social Reach (0–40)
    connection_score = min(connections * 4, 40)

    # 2. Network Maturity (0–25)
    stability_bonus = min(account_age / 40, 25)

    # 3. Social Influence (0–25)
    influence_score = 0
    if pagerank_scores is not None:
        influence_score = min(pagerank_scores.get(user_id, 0) * 100, 25)

    # 4. Isolation Risk Penalty (0–25)
    isolation_penalty = (5 - connections) * 5 if connections < 5 else 0

    # Total network score
    network_score = connection_score + stability_bonus + influence_score - isolation_penalty

    return max(0, min(network_score, 80))


# 3. BEHAVIOR SCORE COMPONENT (40%)

def calculate_behavior_score(row):
    """
    Behavior score based on responsiveness, activity quality, 
    and NLP-derived toxicity signals.

    Score range: 0 to 80
    """
    
    # Defensive guards
    avg_response = max(0, row['avg_response_time'])
    messages = max(0, row['messages_per_day'])
    toxic_count = max(0, row['toxic_message_count_prior'])
    spam_flag = int(row['spammy_chat_behavior'])

    if avg_response <= 5:
        response_score = 30
    elif avg_response <= 10:
        response_score = 25
    elif avg_response <= 20:
        response_score = 20
    elif avg_response <= 30:
        response_score = 15
    else:
        response_score = 10

    # Activity quality (0–25)
    if 10 <= messages <= 40:
        activity_score = 25
    elif 5 <= messages < 10 or 40 < messages <= 60:
        activity_score = 20
    elif messages < 5:
        activity_score = 15
    else:
        activity_score = 10  # Excessive → spam risk

    # Toxicity history (0–25)
    if toxic_count == 0:
        toxicity_score = 25
    elif toxic_count <= 2:
        toxicity_score = 20
    elif toxic_count <= 5:
        toxicity_score = 15
    elif toxic_count <= 10:
        toxicity_score = 10
    else:
        toxicity_score = 5

    # Spam penalty (0–20)
    spam_penalty = spam_flag * 20

    behavior_score = (
        response_score +
        activity_score +
        toxicity_score -
        spam_penalty
    )

    return max(0, min(behavior_score, 80))

# 4. CREDIT SCORE CALCULATOR (300-850 Scale)
def calculate_credit_score(row):
    """Final credit score (300 to 850), normalized components"""

    stability = calculate_stability_score(row)          # 0–100
    network = calculate_network_score(row) / 80 * 100   # normalize
    behavior = calculate_behavior_score(row) / 80 * 100 # normalize

    # Apply weights (30%, 30%, 40%)
    weighted_score = (
        stability * 0.30 +
        network * 0.30 +
        behavior * 0.40
    )
    
    # Scale from 0-100 to 300-850
    credit_score = 300 + (weighted_score / 100) * 550

    # Round to nearest integer
    return int(np.clip(credit_score, 300, 850))

# Categorize scores
def categorize_score(score):
    score = int(score)
    if score >= 800: return "Excellent"
    elif score >= 740: return "Very Good"
    elif score >= 670: return "Good"
    elif score >= 580: return "Fair"
    elif score >= 500: return "Poor"
    else: return "Very Poor"