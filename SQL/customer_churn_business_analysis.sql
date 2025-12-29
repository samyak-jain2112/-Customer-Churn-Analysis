CREATE DATABASE churn_db;
USE churn_db;

CREATE TABLE customers (
    RowNumber INT,
    CustomerId BIGINT,
    Surname VARCHAR(50),
    CreditScore INT,
    Geography VARCHAR(20),
    Gender VARCHAR(10),
    Age INT,
    Tenure INT,
    Balance DOUBLE,
    NumOfProducts INT,
    HasCrCard INT,
    IsActiveMember INT,
    EstimatedSalary DOUBLE,
    Exited INT
);

SHOW TABLES;

select count(*) from customers;

select * from customers limit 5;

#creating customer_features view 
CREATE VIEW customer_features AS
SELECT
    *,
    Balance / (CreditScore + 1) AS CreditUtilization,
    Balance / (EstimatedSalary + 1) AS BalanceToSalaryRatio,
    (NumOfProducts + HasCrCard + IsActiveMember) AS InteractionScore
FROM customers;

#some of the business questions 

#1 What is the overall customer churn rate and how severe is the problem?
#Helps leadership understand retention health and urgency of action.

SELECT
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_customers,
    ROUND(100 * SUM(Exited)/COUNT(*), 2) AS churn_rate
FROM customers;
## churn rate is 20.37%

#2 Which geographical regions contribute the most to customer churn?
#Allows region-specific retention strategies instead of generic campaigns.
SELECT
    Geography,
    COUNT(*) AS customers,
    SUM(Exited) AS churned,
    ROUND(100 * SUM(Exited)/COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY Geography
ORDER BY churn_rate DESC;
##Germany contributes most to the customer churn

#3 Churn Concentration->Which regions contribute the highest share of total churn?
#Even if churn rate is moderate, high-volume regions may cause maximum losses.
SELECT
    Geography,
    COUNT(*) AS churned_customers,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS churn_share_percent
FROM customers
WHERE Exited = 1
GROUP BY Geography
ORDER BY churn_share_percent DESC;
## both france and germany are almost had equal share 

# 4 Customer Engagement Impact ->Does customer activity level influence churn behavior?
#Helps identify disengaged users who need proactive outreach.
SELECT
    IsActiveMember,
    COUNT(*) AS customers,
    SUM(Exited) AS churned,
    ROUND(100 * SUM(Exited)/COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY IsActiveMember;
##Inactive customers show nearly double the churn rate compared to active customers, indicating that engagement is one of the strongest drivers of customer retention.

# 5 Age-Based Churn Patterns -> Which age groups are more likely to churn?
#Enables demographic-specific product and communication strategies.
SELECT
    CASE
        WHEN Age < 30 THEN '<30'
        WHEN Age BETWEEN 30 AND 45 THEN '30-45'
        WHEN Age BETWEEN 46 AND 60 THEN '46-60'
        ELSE '60+'
    END AS AgeGroup,
    COUNT(*) AS customers,
    SUM(Exited) AS churned,
    ROUND(100 * SUM(Exited)/COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY AgeGroup;
##Churn risk increases with age, peaking sharply in the 46–60 segment, which shows over 50% churn and should be prioritized for targeted retention strategies

# 6 Financial Stress Indicators -> Do customers with higher credit utilization show higher churn risk?
#Identifies financially stressed customers who may exit due to risk or dissatisfaction.
SELECT
    utilization_quartile,
    COUNT(*) AS customers,
    ROUND(100 * SUM(Exited) / COUNT(*), 2) AS churn_rate
FROM (
    SELECT
        Exited,
        NTILE(4) OVER (ORDER BY CreditUtilization) AS utilization_quartile
    FROM customer_features
) t
GROUP BY utilization_quartile
ORDER BY utilization_quartile;
##Churn risk increases steadily with credit utilization, indicating that financially stressed customers are significantly more likely to churn and should be proactively targeted.

#7 — High-Value Churn PRIORITIZATION -> Among churned customers, which ones caused the highest financial loss and should be prioritized first?
#Not all churn is equally costly. This helps prioritize retention spend.

SELECT
    CustomerId,
    Geography,
    Balance,
    EstimatedSalary,
    CreditUtilization,
    ROW_NUMBER() OVER (
        ORDER BY Balance DESC, CreditUtilization DESC
    ) AS loss_priority_rank
FROM customer_features
WHERE Exited = 1
LIMIT 10;
##Churn impact is highly skewed—losing a small set of high-balance customers causes disproportionate financial loss, so retention efforts should be prioritized by revenue impact, not churn volume.

# #8 — Multi-Dimensional Interaction Analysis -> Does being active reduce churn equally across all age groups?
#Retention strategies should differ for young vs older customers.
SELECT
    AgeGroup,
    IsActiveMember,
    COUNT(*) AS customers,
    ROUND(100 * SUM(Exited)/COUNT(*), 2) AS churn_rate
FROM (
    SELECT
        Exited,
        IsActiveMember,
        CASE
            WHEN Age < 30 THEN '<30'
            WHEN Age BETWEEN 30 AND 45 THEN '30-45'
            WHEN Age BETWEEN 46 AND 60 THEN '46-60'
            ELSE '60+'
        END AS AgeGroup
    FROM customers
) t
GROUP BY AgeGroup, IsActiveMember
ORDER BY AgeGroup, IsActiveMember;
##Customer activity significantly reduces churn, but its impact is highly age-dependent—engagement is especially critical for retaining older customers.

#9 — Risk Segmentation -> How can customers be grouped into actionable churn risk segments?
SELECT
    CustomerId,
    Geography,
    CreditUtilization,
    InteractionScore,
    IsActiveMember,
    CASE
        WHEN CreditUtilization > 0.8 AND IsActiveMember = 0 THEN 'High Risk'
        WHEN CreditUtilization BETWEEN 0.4 AND 0.8 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS RiskSegment
FROM customer_features;
##Customers were segmented into actionable churn risk groups using explainable financial and engagement indicators, enabling targeted and cost-effective retention strategies

#10 — Revenue at Risk by Segment -> How much money is at risk due to churn in each risk segment?
SELECT
    RiskSegment,
    COUNT(*) AS churned_customers,
    ROUND(SUM(Balance), 2) AS revenue_at_risk
FROM (
    SELECT
        Balance,
        Exited,
        CASE
            WHEN CreditUtilization > 0.8 AND IsActiveMember = 0 THEN 'High Risk'
            WHEN CreditUtilization BETWEEN 0.4 AND 0.8 THEN 'Medium Risk'
            ELSE 'Low Risk'
        END AS RiskSegment
    FROM customer_features
    WHERE Exited = 1
) t
GROUP BY RiskSegment
ORDER BY revenue_at_risk DESC;
##Although fewer in number, high-risk customers account for the majority of revenue at risk, making them the most critical segment for targeted retention efforts.
