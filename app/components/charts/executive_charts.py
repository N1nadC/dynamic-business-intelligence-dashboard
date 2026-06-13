import pandas as pd
import plotly.express as px

from database.connection import engine
from components.query_builder import build_where_clause


def monthly_sales_trend(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        CAST(strftime('%Y', o.order_date) AS INTEGER) AS year,

        CASE CAST(strftime('%m', o.order_date) AS INTEGER)
            WHEN 1 THEN 'January'
            WHEN 2 THEN 'February'
            WHEN 3 THEN 'March'
            WHEN 4 THEN 'April'
            WHEN 5 THEN 'May'
            WHEN 6 THEN 'June'
            WHEN 7 THEN 'July'
            WHEN 8 THEN 'August'
            WHEN 9 THEN 'September'
            WHEN 10 THEN 'October'
            WHEN 11 THEN 'November'
            WHEN 12 THEN 'December'
        END AS month_name,

        CAST(strftime('%m', o.order_date) AS INTEGER) AS month_num,

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
        year,
        month_num

    ORDER BY
        year,
        month_num
    """

    df = pd.read_sql(query, engine)

    fig = px.line(
        df,
        x="month_name",
        y="total_sales",
        color="year",
        markers=True,
        category_orders={
            "month_name": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]
        }
    )

    fig.update_layout(
        title="Monthly Sales Trend",
        height=450
    )

    return fig


def monthly_profit_trend(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        CAST(strftime('%Y', o.order_date) AS INTEGER) AS year,

        CASE CAST(strftime('%m', o.order_date) AS INTEGER)
            WHEN 1 THEN 'January'
            WHEN 2 THEN 'February'
            WHEN 3 THEN 'March'
            WHEN 4 THEN 'April'
            WHEN 5 THEN 'May'
            WHEN 6 THEN 'June'
            WHEN 7 THEN 'July'
            WHEN 8 THEN 'August'
            WHEN 9 THEN 'September'
            WHEN 10 THEN 'October'
            WHEN 11 THEN 'November'
            WHEN 12 THEN 'December'
        END AS month_name,

        CAST(strftime('%m', o.order_date) AS INTEGER) AS month_num,

        ROUND(SUM(s.profit), 2) AS total_profit

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY
        year,
        month_num

    ORDER BY
        year,
        month_num
    """

    df = pd.read_sql(query, engine)

    fig = px.line(
        df,
        x="month_name",
        y="total_profit",
        color="year",
        markers=True,
        category_orders={
            "month_name": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]
        }
    )

    fig.update_layout(
        title="Monthly Profit Trend",
        height=450
    )

    return fig


def sales_by_region(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.region,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.region

    ORDER BY total_sales DESC
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="region",
        y="total_sales",
        text="total_sales"
    )

    fig.update_layout(
        title="Sales by Region",
        height=450
    )

    return fig


def profit_by_region(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.region,
        ROUND(SUM(s.profit), 2) AS total_profit

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.region

    ORDER BY total_profit DESC
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="region",
        y="total_profit",
        text="total_profit"
    )

    fig.update_layout(
        title="Profit by Region",
        height=450
    )

    return fig