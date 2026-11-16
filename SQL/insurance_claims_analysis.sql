CREATE DATABASE insurance_claims_db;

USE insurance_claims_db;

USE insurance_claims_db;

CREATE TABLE insurance_claims (
    Claim_ID VARCHAR(20),
    Policy_ID VARCHAR(20),
    Age INT,
    Gender VARCHAR(20),
    Region VARCHAR(50),
    City VARCHAR(50),
    Policy_Type VARCHAR(50),
    Customer_Tenure_Years INT,
    Previous_Claims INT,
    Claim_Type VARCHAR(50),
    Incident_Type VARCHAR(50),
    Claim_Amount DECIMAL(12,2),
    Claim_Date DATE,
    Claim_Status VARCHAR(30),
    Police_Report VARCHAR(10),
    Witness_Count INT,
    Claim_Delay_Days INT,
    Fraud_Indicator INT,
    Risk_Score DECIMAL(5,2),
    Risk_Category VARCHAR(20)
);

USE insurance_claims_db;

SELECT COUNT(*) AS Total_Records
FROM insurance_claims;

SELECT COUNT(*) AS Total_Claims
FROM insurance_claims;

SELECT 
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims;

SELECT 
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM insurance_claims;

SELECT 
    COUNT(*) AS Fraudulent_Claims
FROM insurance_claims
WHERE Fraud_Indicator = 1;

SELECT 
    Claim_Type,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims
GROUP BY Claim_Type
ORDER BY Total_Claim_Amount DESC;

SELECT 
    Region,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims
GROUP BY Region
ORDER BY Number_of_Claims DESC;

SELECT 
    Claim_Type,
    COUNT(*) AS Total_Claims,
    SUM(Fraud_Indicator) AS Fraudulent_Claims,
    ROUND(
        SUM(Fraud_Indicator) * 100.0 / COUNT(*),
        2
    ) AS Fraud_Rate
FROM insurance_claims
GROUP BY Claim_Type
ORDER BY Fraud_Rate DESC;

SELECT COUNT(*) AS Total_Claims
FROM insurance_claims;

SELECT 
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims;

SELECT 
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM insurance_claims;

SELECT 
    MIN(Claim_Amount) AS Minimum_Claim,
    MAX(Claim_Amount) AS Maximum_Claim
FROM insurance_claims;

SELECT 
    Claim_Status,
    COUNT(*) AS Number_of_Claims
FROM insurance_claims
GROUP BY Claim_Status
ORDER BY Number_of_Claims DESC;

SELECT 
    Claim_Type,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM insurance_claims
GROUP BY Claim_Type
ORDER BY Total_Claim_Amount DESC;

SELECT 
    Region,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims
GROUP BY Region
ORDER BY Total_Claim_Amount DESC;

SELECT
    CASE
        WHEN Fraud_Indicator = 1 THEN 'Fraudulent'
        ELSE 'Legitimate'
    END AS Claim_Category,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims
GROUP BY Fraud_Indicator;

SELECT
    Claim_Type,
    COUNT(*) AS Total_Claims,
    SUM(Fraud_Indicator) AS Fraudulent_Claims,
    ROUND(
        SUM(Fraud_Indicator) * 100.0 / COUNT(*),
        2
    ) AS Fraud_Rate
FROM insurance_claims
GROUP BY Claim_Type
ORDER BY Fraud_Rate DESC;

SELECT
    Claim_ID,
    Claim_Type,
    Claim_Amount,
    Previous_Claims,
    Risk_Score,
    Risk_Category
FROM insurance_claims
WHERE Risk_Category = 'High'
ORDER BY Risk_Score DESC
LIMIT 20;

SELECT
    YEAR(Claim_Date) AS Claim_Year,
    MONTH(Claim_Date) AS Claim_Month,
    COUNT(*) AS Number_of_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM insurance_claims
GROUP BY YEAR(Claim_Date), MONTH(Claim_Date)
ORDER BY Claim_Year, Claim_Month;