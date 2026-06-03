-- Write your query below

-- SELECT name FROM customers
-- WHERE orders.customer_id != customers.id

SELECT c.name 
FROM customers c
LEFT JOIN orders o 
ON c.id = o.customer_id
WHERE o.customer_id IS NULL