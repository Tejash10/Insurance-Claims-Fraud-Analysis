import pandas as pd

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("../Data/insurance_claims.csv")

print("\n========== DATASET SHAPE ==========")
print(df.shape)


# ==========================================
# 2. FIRST 5 ROWS
# ==========================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())


# ==========================================
# 3. COLUMN NAMES
# ==========================================

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())


# ==========================================
# 4. DATA TYPES
# ==========================================

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# ==========================================
# 5. MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ==========================================
# 6. DUPLICATE ROWS
# ==========================================

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())


# ==========================================
# 7. CLAIM AMOUNT SUMMARY
# ==========================================

print("\n========== CLAIM AMOUNT SUMMARY ==========")
print(df["Claim_Amount"].describe())


# ==========================================
# 8. FRAUD ANALYSIS
# ==========================================

print("\n========== FRAUD ANALYSIS ==========")

fraud_count = df["Fraud_Indicator"].sum()
total_claims = len(df)

fraud_percentage = (fraud_count / total_claims) * 100

print("Total Claims:", total_claims)
print("Fraudulent Claims:", fraud_count)
print(f"Fraud Rate: {fraud_percentage:.2f}%")


# ==========================================
# 9. CLAIMS BY TYPE
# ==========================================

print("\n========== CLAIMS BY TYPE ==========")
print(df["Claim_Type"].value_counts())


# ==========================================
# 10. CLAIMS BY REGION
# ==========================================

print("\n========== CLAIMS BY REGION ==========")
print(df["Region"].value_counts())


# ==========================================
# 11. RISK CATEGORY
# ==========================================

print("\n========== RISK CATEGORY ==========")
print(df["Risk_Category"].value_counts())


# ==========================================
# 12. DATA CLEANING
# ==========================================

print("\n========== CLEANING ==========")

# Remove duplicate records
df = df.drop_duplicates()

# Convert date column
df["Claim_Date"] = pd.to_datetime(df["Claim_Date"])

# Fill missing numerical values
df["Previous_Claims"] = df["Previous_Claims"].fillna(0)
df["Witness_Count"] = df["Witness_Count"].fillna(0)

# Fill missing categorical values
df["Claim_Status"] = df["Claim_Status"].fillna("Unknown")
df["Police_Report"] = df["Police_Report"].fillna("Unknown")

print("Cleaning completed!")


# ==========================================
# 13. SAVE CLEANED DATASET
# ==========================================

df.to_csv(
    "../Data/insurance_claims_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")