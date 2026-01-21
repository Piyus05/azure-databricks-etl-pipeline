
SELECT product, SUM(quantity) AS total_qty
FROM sales
GROUP BY product;
