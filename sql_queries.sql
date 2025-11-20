USE sales_insights;

SELECT * FROM sales_insights.sales_data;

SELECT CONCAT(ROUND(SUM(sales) /1000000,2)," Million") as Total_sales
FROM sales_data;

SELECT CONCAT(ROUND(SUM(profit) /1000000,2)," Million") as Total_profit
FROM sales_data;

SELECT COUNT(order_id) as Total_orders
FROM sales_data;

SELECT region,CONCAT(ROUND(SUM(sales) /1000000,2)," Million") as revenue
FROM sales_data
GROUP BY region
ORDER BY revenue DESC;

SELECT region,CONCAT(ROUND(SUM(profit) /1000000,2)," Million") as profits
FROM sales_data
GROUP BY region
ORDER BY profits DESC;

SELECT product_name, SUM(sales) as revenue
FROM sales_data
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;


SELECT product_name, SUM(profit) as profits
FROM sales_data
GROUP BY product_name
ORDER BY profits DESC
LIMIT 10;


SELECT category,sub_category,SUM(sales) as total_sales
FROM sales_data
GROUP BY category,sub_category
ORDER BY total_sales DESC;

SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       ROUND(SUM(sales), 2) AS monthly_sales
FROM sales_data
GROUP BY month
ORDER BY month;


SELECT segment,SUM(profit) as total_profit
FROM sales_data
GROUP BY segment
ORDER BY total_profit DESC;
