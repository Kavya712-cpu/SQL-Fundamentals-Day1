
Query 1
SELECT * FROM sales;

Query 2
SELECT Customer_name, Amount
FROM sales;

Query 3
SELECT *
FROM sales
WHERE Amount > 5000;

Query 4
SELECT *
FROM sales
WHERE City = 'Bangalore';

Query 5
SELECT *
FROM sales
WHERE Amount > 5000 AND City = 'Bangalore';

Query 6
SELECT *
FROM sales
WHERE City = 'Bangalore' OR City = 'Mysore';

Query 7
SELECT *
FROM sales
WHERE NOT City = 'Bangalore';

Query 8
SELECT *
FROM sales
WHERE Customer_name LIKE 'A%';

Query 9 
SELECT *
FROM sales
WHERE City IN ('Bangalore', 'Mysore', 'Chennai');

Query 10
SELECT *
FROM sales
WHERE Amount BETWEEN 2000 AND 8000;

Query 11
SELECT *
FROM sales
WHERE Phone IS NULL;
