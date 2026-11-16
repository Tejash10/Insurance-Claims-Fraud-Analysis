import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Reproducible results
np.random.seed(42)

# Number of records
n = 100000

# ---------------------------------------------------
# 1. Basic IDs
# ---------------------------------------------------

claim_ids = [f"CLM{str(i).zfill(6)}" for i in range(1, n + 1)]
policy_ids = [f"POL{str(np.random.randint(1, 50001)).zfill(6)}" for _ in range(n)]

# ---------------------------------------------------
# 2. Customer information
# ---------------------------------------------------

ages = np.random.randint(18, 76, n)

genders = np.random.choice(
    ["Male", "Female"],
    n,
    p=[0.58, 0.42]
)

regions = np.random.choice(
    ["Gujarat", "Maharashtra", "Delhi", "Rajasthan",
     "Karnataka", "Tamil Nadu", "Uttar Pradesh", "Madhya Pradesh"],
    n
)

cities = np.random.choice(
    ["Ahmedabad", "Mumbai", "Surat", "Vadodara",
     "Delhi", "Jaipur", "Bengaluru", "Chennai",
     "Pune", "Rajkot", "Vapi", "Indore"],
    n
)

# ---------------------------------------------------
# 3. Policy information
# ---------------------------------------------------

policy_types = np.random.choice(
    ["Comprehensive", "Third Party", "Basic"],
    n,
    p=[0.50, 0.30, 0.20]
)

customer_tenure = np.random.randint(1, 16, n)

previous_claims = np.random.poisson(1.2, n)
previous_claims = np.clip(previous_claims, 0, 8)

# ---------------------------------------------------
# 4. Claim information
# ---------------------------------------------------

claim_types = np.random.choice(
    ["Auto", "Health", "Property", "Life", "Travel", "Other"],
    n,
    p=[0.28, 0.25, 0.18, 0.10, 0.12, 0.07]
)

incident_types = np.random.choice(
    ["Accident", "Illness", "Theft", "Fire",
     "Natural Disaster", "Damage", "Other"],
    n
)

claim_status = np.random.choice(
    ["Approved", "Rejected", "Pending", "Under Review"],
    n,
    p=[0.68, 0.10, 0.12, 0.10]
)

# ---------------------------------------------------
# 5. Claim amount
# ---------------------------------------------------

claim_amount = np.random.lognormal(
    mean=9.5,
    sigma=1.0,
    size=n
)

claim_amount = np.clip(claim_amount, 500, 250000)

claim_amount = np.round(claim_amount, 2)

# ---------------------------------------------------
# 6. Incident details
# ---------------------------------------------------

police_report = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.55, 0.45]
)

witness_count = np.random.randint(0, 6, n)

claim_delay_days = np.random.randint(0, 31, n)

# ---------------------------------------------------
# 7. Dates
# ---------------------------------------------------

start_date = datetime(2023, 1, 1)

claim_dates = [
    start_date + timedelta(days=int(x))
    for x in np.random.randint(0, 1095, n)
]

# ---------------------------------------------------
# 8. Fraud detection logic
# ---------------------------------------------------

fraud_probability = np.full(n, 0.015)

# High claim amount
fraud_probability += np.where(
    claim_amount > 100000, 0.12, 0
)

# Many previous claims
fraud_probability += np.where(
    previous_claims >= 4, 0.10, 0
)

# Short claim delay
fraud_probability += np.where(
    claim_delay_days <= 2, 0.04, 0
)

# No police report
fraud_probability += np.where(
    police_report == "No", 0.03, 0
)

# No witnesses
fraud_probability += np.where(
    witness_count == 0, 0.04, 0
)

# Clip probability
fraud_probability = np.clip(
    fraud_probability,
    0,
    0.80
)

fraud_indicator = (
    np.random.random(n) < fraud_probability
).astype(int)

# ---------------------------------------------------
# 9. Risk score
# ---------------------------------------------------

risk_score = (
    (claim_amount / 250000) * 40
    + (previous_claims / 8) * 20
    + np.where(police_report == "No", 15, 0)
    + np.where(witness_count == 0, 10, 0)
    + (claim_delay_days <= 2) * 10
    + fraud_indicator * 20
)

risk_score = np.clip(
    risk_score + np.random.normal(0, 5, n),
    0,
    100
)

risk_score = np.round(risk_score, 2)

# ---------------------------------------------------
# 10. Risk category
# ---------------------------------------------------

risk_category = pd.cut(
    risk_score,
    bins=[-1, 30, 60, 100],
    labels=["Low", "Medium", "High"]
)

# ---------------------------------------------------
# 11. Create DataFrame
# ---------------------------------------------------

df = pd.DataFrame({
    "Claim_ID": claim_ids,
    "Policy_ID": policy_ids,
    "Age": ages,
    "Gender": genders,
    "Region": regions,
    "City": cities,
    "Policy_Type": policy_types,
    "Customer_Tenure_Years": customer_tenure,
    "Previous_Claims": previous_claims,
    "Claim_Type": claim_types,
    "Incident_Type": incident_types,
    "Claim_Amount": claim_amount,
    "Claim_Date": claim_dates,
    "Claim_Status": claim_status,
    "Police_Report": police_report,
    "Witness_Count": witness_count,
    "Claim_Delay_Days": claim_delay_days,
    "Fraud_Indicator": fraud_indicator,
    "Risk_Score": risk_score,
    "Risk_Category": risk_category
})

# ---------------------------------------------------
# 12. Save CSV
# ---------------------------------------------------

output_path = "../Data/insurance_claims.csv"

df.to_csv(
    output_path,
    index=False
)

print("========================================")
print("Insurance Claims Dataset Created!")
print("========================================")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Fraudulent Claims: {df['Fraud_Indicator'].sum():,}")
print(f"Fraud Rate: {df['Fraud_Indicator'].mean() * 100:.2f}%")
print(f"Total Claim Amount: ${df['Claim_Amount'].sum():,.2f}")
print(f"Average Claim Amount: ${df['Claim_Amount'].mean():,.2f}")
print("========================================")
print(f"Saved to: {output_path}")