import streamlit as st

import streamlit as st

from components.filters import create_filters
from components.charts.product_charts import (
    sales_by_category,
    profit_by_category,
    subcategory_treemap,
    top_products_by_sales,
    lowest_performing_products
)
st.set_page_config(
    layout="wide"
)

st.title("Product Performance")

filters = create_filters()

st.plotly_chart(
    sales_by_category(filters),
    width="stretch"
)
st.info(
    "💡 Technology is the highest revenue-generating product category."
)

st.plotly_chart(
    profit_by_category(filters),
    width="stretch"
)
st.info(
    "💡 Office Supplies delivers stronger profitability than Furniture despite lower sales."
)

st.plotly_chart(
    subcategory_treemap(filters),
    width="stretch"
)
st.info(
    "💡 Revenue is concentrated within a small number of high-performing sub-categories."
)

st.plotly_chart(
    top_products_by_sales(filters),
    width="stretch"
)
st.info(
    "💡 A small group of products drives a significant share of total revenue."
)

st.plotly_chart(
    lowest_performing_products(filters),
    width="stretch"
)
st.info(
    "💡 Several products contribute minimal revenue and may require portfolio review."
)
