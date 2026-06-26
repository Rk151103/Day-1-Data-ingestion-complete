-- 1. Show all records from Axis Bluechip
SELECT * FROM Axis_Bluechip;

-- 2. Total number of NAV records
SELECT COUNT(*) FROM Axis_Bluechip;

-- 3. Highest NAV
SELECT MAX(nav) AS Highest_NAV FROM Axis_Bluechip;

-- 4. Lowest NAV
SELECT MIN(nav) AS Lowest_NAV FROM Axis_Bluechip;

-- 5. Average NAV
SELECT AVG(nav) AS Average_NAV FROM Axis_Bluechip;

-- 6. Latest NAV
SELECT * FROM Axis_Bluechip
ORDER BY date DESC
LIMIT 1;

-- 7. Earliest NAV
SELECT * FROM Axis_Bluechip
ORDER BY date ASC
LIMIT 1;

-- 8. Total records in SBI Bluechip
SELECT COUNT(*) FROM SBI_Bluechip;

-- 9. Highest NAV in HDFC Top 100 Direct
SELECT MAX(nav) FROM HDFC_Top_100_Direct;

-- 10. Average NAV in ICICI Bluechip
SELECT AVG(nav) FROM ICICI_Bluechip;