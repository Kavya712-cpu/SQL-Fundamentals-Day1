table
CREATE TABLE employee_sales (
    id INTEGER PRIMARY KEY,
    region TEXT,
    amount INTEGER
);

INSERT INTO employee_sales (id, region, amount)
VALUES
(1, 'South', 5000),
(2, 'North', 3000),
(3, 'South', 7000),
(4, 'East', 4000),
(5, 'West', 6000),
(6, 'North', 3500),
(7, 'South', 2500),
(8, 'East', 8000);

1
SELECT *
FROM employee_sales
WHERE amount > (
    SELECT AVG(amount)
    FROM employee_sales
);

2
SELECT *
FROM employee_sales e1
WHERE amount = (
    SELECT MAX(amount)
    FROM employee_sales e2
    WHERE e1.region = e2.region
);

3.Creates a temporary table called AverageSales.
Stores the average sales amount.
Displays all sales where the amount is greater than the average.

WITH AverageSales AS (
    SELECT AVG(amount) AS avg_amount
    FROM employee_sales
)
SELECT *
FROM employee_sales
WHERE amount > (
    SELECT avg_amount
    FROM AverageSales
);

4.Chain Two CTEs
WITH TotalSales AS (
    SELECT region, SUM(amount) AS total_amount
    FROM employee_sales
    GROUP BY region
),
AverageSales AS (
    SELECT AVG(total_amount) AS avg_total
    FROM TotalSales
)
SELECT *
FROM TotalSales
WHERE total_amount > (
    SELECT avg_total
    FROM AverageSales
);

