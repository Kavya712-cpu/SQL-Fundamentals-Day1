SELECT * FROM sales;

SELECT customer_name, amount FROM sales;

SELECT * FROM sales WHERE amount > 5000;

SELECT * FROM sales WHERE city = 'Bangalore';

SELECT * FROM sales WHERE amount > 5000 AND city = 'Bangalore';

SELECT * FROM sales WHERE city = 'Bangalore' OR city = 'Mysore';

SELECT * FROM sales WHERE NOT city = 'Bangalore';

SELECT * FROM sales WHERE customer_name LIKE 'A%';

SELECT * FROM sales WHERE city IN ('Bangalore','Mysore','Chennai');

SELECT * FROM sales WHERE amount BETWEEN 2000 AND 8000;