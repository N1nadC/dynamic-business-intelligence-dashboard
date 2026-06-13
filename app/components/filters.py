import pandas as pd
import streamlit as st

from database.connection import engine


def get_filter_options():

    years = pd.read_sql(
        """
        SELECT DISTINCT
            CAST(strftime('%Y', order_date) AS INTEGER) AS order_year
        FROM orders
        ORDER BY order_year
        """,
        engine
    )

    regions = pd.read_sql(
        """
        SELECT DISTINCT region
        FROM locations
        ORDER BY region
        """,
        engine
    )

    categories = pd.read_sql(
        """
        SELECT DISTINCT category
        FROM products
        ORDER BY category
        """,
        engine
    )

    subcategories = pd.read_sql(
        """
        SELECT DISTINCT sub_category
        FROM products
        ORDER BY sub_category
        """,
        engine
    )

    return (
        years,
        regions,
        categories,
        subcategories
    )


def create_filters():

    years, regions, categories, subcategories = get_filter_options()

    st.sidebar.header("Filters")

    selected_years = st.sidebar.multiselect(
        "Year",
        years["order_year"].tolist()
    )

    selected_regions = st.sidebar.multiselect(
        "Region",
        regions["region"].tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        categories["category"].tolist()
    )

    selected_subcategories = st.sidebar.multiselect(
        "Sub-Category",
        subcategories["sub_category"].tolist()
    )

    return {
        "years": selected_years,
        "regions": selected_regions,
        "categories": selected_categories,
        "subcategories": selected_subcategories
    }