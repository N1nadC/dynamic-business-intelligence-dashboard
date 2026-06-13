TOTAL_SALES = """
SELECT ROUND(SUM(sales), 2) AS total_sales
FROM sales;
"""

TOTAL_PROFIT = """
SELECT ROUND(SUM(profit), 2) AS total_profit
FROM sales;
"""

TOTAL_ORDERS = """
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM orders;
"""

TOTAL_CUSTOMERS = """
SELECT COUNT(*) AS total_customers
FROM customers;
"""

AVERAGE_ORDER_VALUE = """
SELECT ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2)
AS avg_order_value
FROM sales;
"""

PROFIT_MARGIN = """
SELECT ROUND(
    (SUM(profit) / SUM(sales)) * 100,
    2
) AS profit_margin
FROM sales;
"""