1
SELECT c.customer_name, c.city, o.product, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

2
SELECT c.customer_name, c.city, o.product, o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

3--[SQL do not support right join so we need to use left join in reverse to get the same output]
SELECT c.customer_name, c.city, o.product, o.amount
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id;

4--SQLite does not support FULL OUTER JOIN directly, so we'll use UNION to achieve the same result.
SELECT c.customer_name, c.city, o.product, o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id

UNION

SELECT c.customer_name, c.city, o.product, o.amount
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id;

5--self join
SELECT A.customer_name AS Customer1,
       B.customer_name AS Customer2,
       A.city
FROM customers A
JOIN customers B
ON A.city = B.city
WHERE A.customer_id < B.customer_id;

6--Table Alias
SELECT c.customer_name, o.product, o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;


