import pandas as pd
import plotly.express as px

from database.connection import engine
from components.query_builder import build_where_clause
import streamlit as st


CITY_COORDINATES = {
    "New York City": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Seattle": (47.6062, -122.3321),
    "San Francisco": (37.7749, -122.4194),
    "Philadelphia": (39.9526, -75.1652),
    "Houston": (29.7604, -95.3698),
    "Chicago": (41.8781, -87.6298),
    "San Diego": (32.7157, -117.1611),
    "Detroit": (42.3314, -83.0458),
    "Jacksonville": (30.3322, -81.6557),
    "San Antonio": (29.4241, -98.4936),
    "Newark": (39.6837, -75.7497),
    "Dallas": (32.7767, -96.7970),
    "Lafayette": (40.4167, -86.8753),
    "Atlanta": (33.7490, -84.3880),
    "Minneapolis": (44.9778, -93.2650),
    "Springfield": (38.7893, -77.1872),
    "Providence": (41.8240, -71.4128),
    "Columbus": (39.9612, -82.9988),
    "Henderson": (37.8362, -87.5900)
}

def top_states_by_sales(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.state,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.state

    ORDER BY total_sales DESC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="total_sales",
        y="state",
        orientation="h"
    )

    fig.update_layout(
        title="Top 10 States by Sales",
        height=600,
        yaxis={"categoryorder": "total ascending"}
    )

    return fig

def top_cities_by_sales(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.city,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.city

    ORDER BY total_sales DESC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="total_sales",
        y="city",
        orientation="h"
    )

    fig.update_layout(
        title="Top 10 Cities by Sales",
        height=600,
        yaxis={"categoryorder": "total ascending"}
    )

    return fig

def sales_distribution_by_region(filters):

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
    """

    df = pd.read_sql(query, engine)

    fig = px.pie(
        df,
        names="region",
        values="total_sales",
        title="Sales Distribution by Region"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        height=600
    )

    return fig

def sales_map_by_state(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.state,
        ROUND(SUM(s.sales), 2) AS total_sales

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.state
    """

    df = pd.read_sql(query, engine)

    fig = px.choropleth(
        df,
        locations="state",
        locationmode="USA-states",
        color="total_sales",
        scope="usa",
        hover_name="state",
        color_continuous_scale="Blues",
        title="US Sales by State"
    )

    fig.update_layout(
        height=700
    )

    return fig

# def city_sales_bubble_map(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.city,
        l.state,
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
        l.city,
        l.state

    ORDER BY total_sales DESC

    LIMIT 20
    """

    df = pd.read_sql(query, engine)

    df = df[df["city"].isin(CITY_COORDINATES.keys())].copy()

    if df.empty:
        return px.scatter_geo(
            title="Top Sales Cities (No Data Available)"
        )

    df["lat"] = df["city"].map(
        lambda city: CITY_COORDINATES[city][0]
    )

    df["lon"] = df["city"].map(
        lambda city: CITY_COORDINATES[city][1]
    )

    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        size="total_sales",
        hover_name="city",
        hover_data={
            "state": True,
            "total_sales": ":,.2f"
        },
        scope="usa",
        title="Top Sales Cities"
    )

    fig.update_traces(
        marker=dict(
            sizemode="area",
            sizeref=2000,
            line_width=1
        )
    )

    fig.update_geos(
        showcountries=True,
        showsubunits=True,
        fitbounds="locations"
    )

    fig.update_layout(
        height=700
    )

    return fig

def top_states_by_profit(filters):

    where_clause = build_where_clause(filters)

    query = f"""
    SELECT
        l.state,
        ROUND(SUM(s.profit), 2) AS total_profit

    FROM sales s

    JOIN orders o
        ON s.order_id = o.order_id

    JOIN products p
        ON s.product_id = p.product_id

    JOIN locations l
        ON o.location_id = l.location_id

    {where_clause}

    GROUP BY l.state

    ORDER BY total_profit DESC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="total_profit",
        y="state",
        orientation="h"
    )

    fig.update_layout(
        title="Top 10 States by Profit",
        height=600,
        yaxis={"categoryorder": "total ascending"}
    )

    return fig