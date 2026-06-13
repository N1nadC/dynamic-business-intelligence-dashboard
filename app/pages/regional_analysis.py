import streamlit as st

from components.filters import create_filters
from components.charts.regional_charts import (
    top_states_by_sales,
    top_cities_by_sales,
    sales_distribution_by_region,
    sales_map_by_state,
    top_states_by_profit
)

st.set_page_config(
    layout="wide"
)

st.title("Regional Analysis")

filters = create_filters()

st.plotly_chart(
    top_states_by_sales(filters),
    width="stretch"
)
st.info(
    "💡 California and New York are the strongest revenue-generating markets."
)

st.plotly_chart(
    top_cities_by_sales(filters),
    width="stretch"
)
st.info(
    "💡 Major metropolitan areas drive a substantial portion of total sales."
)

st.plotly_chart(
    sales_distribution_by_region(filters),
    width="stretch"
)
st.info(
    "💡 Sales are concentrated primarily within the West and East regions."
)

st.plotly_chart(
    sales_map_by_state(filters),
    width="stretch"
)
st.info(
    "💡 Revenue performance is strongest across major coastal markets."
)


st.plotly_chart(
    top_states_by_profit(filters),
    width="stretch"
)
st.info(
    "💡 High-profit states closely align with top revenue-generating markets."
)
# st.plotly_chart(
#     city_sales_bubble_map(filters),
#     width="stretch"
# )