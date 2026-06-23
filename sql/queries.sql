-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Maximum NAV
SELECT MAX(nav) AS max_nav
FROM fact_nav;

-- 4. Minimum NAV
SELECT MIN(nav) AS min_nav
FROM fact_nav;

-- 5. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6. SIP transactions count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 7. Redemption transactions count
SELECT COUNT(*) AS redemption_count
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 8. Funds with expense ratio below 1%
SELECT amfi_code, expense_ratio
FROM fact_performance
WHERE expense_ratio < 1;

-- 9. Average Sharpe Ratio
SELECT AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance;

-- 10. Funds by Risk Grade
SELECT risk_grade, COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;

-- 9. Average Sharpe Ratio
SELECT AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance;

-- 10. Funds by Risk Grade
SELECT risk_grade, COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;