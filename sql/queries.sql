USE superstore_db;

-- =====================================
-- TOTAL SALES
-- =====================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM sales;

-- =====================================
-- TOTAL PROFIT
-- =====================================

SELECT
    ROUND(SUM(profit), 2) AS total_profit
FROM sales;

-- =====================================
-- TOP 10 PRODUCTS BY SALES
-- =====================================

SELECT
    p.product_name,
    ROUND(SUM(s.sales), 2) AS total_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 10;

-- =====================================
-- SALES BY REGION
-- =====================================

SELECT
    l.region,
    ROUND(SUM(s.sales), 2) AS total_sales
FROM sales s
JOIN orders o
    ON s.order_id = o.order_id
JOIN locations l
    ON o.location_id = l.location_id
GROUP BY l.region
ORDER BY total_sales DESC;

-- =====================================
-- MOST PROFITABLE CATEGORY
-- =====================================

SELECT
    p.category,
    ROUND(SUM(s.profit), 2) AS total_profit
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;

-- =====================================
-- AVERAGE SHIPPING DAYS
-- =====================================

SELECT
    ROUND(AVG(shipping_days), 2) AS avg_shipping_days
FROM sales;