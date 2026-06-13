import pandas as pd
from database.connection import engine
from components.query_builder import build_where_clause


# def build_where_clause(filters):

#     conditions = []

#     if filters["years"]:
#         years = ",".join(map(str, filters["years"]))
#         conditions.append(f"YEAR(o.order_date) IN ({years})")

#     if filters["regions"]:
#         regions = "', '".join(filters["regions"])
#         conditions.append(f"l.region IN ('{regions}')")

#     if filters["categories"]:
#         categories = "', '".join(filters["categories"])
#         conditions.append(f"p.category IN ('{categories}')")

#     if filters["subcategories"]:
#         subcategories = "', '".join(filters["subcategories"])
#         conditions.append(f"p.sub_category IN ('{subcategories}')")

#     if conditions:
#         return "WHERE " + " AND ".join(conditions)

#     return ""


def get_kpi_data(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        ROUND(SUM(s.sales), 2) AS total_sales,
        ROUND(SUM(s.profit), 2) AS total_profit,
        ROUND((SUM(s.profit)/SUM(s.sales))*100, 2) AS profit_margin,
        COUNT(DISTINCT o.order_id) AS total_orders,
        COUNT(DISTINCT o.customer_id) AS total_customers,
        ROUND(SUM(s.sales)/COUNT(DISTINCT o.order_id), 2) AS avg_order_value

    FROM sales s
    JOIN orders o
        ON s.order_id = o.order_id
    JOIN products p
        ON s.product_id = p.product_id
    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}
    """

    df = pd.read_sql(query, engine)

    return {
        "sales": df["total_sales"][0] or 0,
        "profit": df["total_profit"][0] or 0,
        "margin": df["profit_margin"][0] or 0,
        "orders": df["total_orders"][0] or 0,
        "customers": df["total_customers"][0] or 0,
        "aov": df["avg_order_value"][0] or 0
    }