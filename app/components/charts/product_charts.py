import pandas as pd
import plotly.express as px

from database.connection import engine
from components.query_builder import build_where_clause


def sales_by_category(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        p.category,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY p.category

    ORDER BY total_sales DESC
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="category",
        y="total_sales",
        text="total_sales"
    )

    fig.update_layout(
        title="Sales by Category",
        height=500
    )

    return fig

def profit_by_category(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        p.category,
        ROUND(SUM(s.profit), 2) AS total_profit

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY p.category

    ORDER BY total_profit DESC
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="category",
        y="total_profit",
        text="total_profit"
    )

    fig.update_layout(
        title="Profit by Category",
        height=500
    )

    return fig

def subcategory_treemap(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        p.category,
        p.sub_category,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY
        p.category,
        p.sub_category
    """

    df = pd.read_sql(query, engine)

    fig = px.treemap(
        df,
        path=["category", "sub_category"],
        values="total_sales",
        title="Sales by Sub-Category"
    )

    fig.update_layout(
        height=600
    )

    return fig

def top_products_by_sales(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        p.product_name,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY p.product_name

    ORDER BY total_sales DESC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="total_sales",
        y="product_name",
        orientation="h"
    )

    fig.update_layout(
        title="Top 10 Products by Sales",
        height=600,
        yaxis={"categoryorder": "total ascending"}
    )

    return fig

def lowest_performing_products(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        p.product_name,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY p.product_name

    ORDER BY total_sales ASC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="total_sales",
        y="product_name",
        orientation="h"
    )

    fig.update_layout(
        title="Lowest Performing Products by Sales",
        height=600
    )

    return fig