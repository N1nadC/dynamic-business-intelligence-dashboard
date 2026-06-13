import streamlit as st
from components.filters import create_filters
from components.kpi_cards import get_kpi_data
from components.charts.executive_charts import (
    monthly_sales_trend,
    monthly_profit_trend,
    sales_by_region,
    profit_by_region
)

st.set_page_config(layout="wide")

st.title("Executive Overview")

filters = create_filters()

kpis = get_kpi_data(filters)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"${kpis['sales']:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${kpis['profit']:,.2f}"
    )

with col3:
    st.metric(
        "Profit Margin",
        f"{kpis['margin']:.2f}%"
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Total Orders",
        f"{kpis['orders']:,}"
    )

with col5:
    st.metric(
        "Total Customers",
        f"{kpis['customers']:,}"
    )

with col6:
    st.metric(
        "Average Order Value",
        f"${kpis['aov']:,.2f}"
    )

st.plotly_chart(
    monthly_sales_trend(filters),
    width="stretch"
)
st.info(
    "💡 Sales demonstrate steady long-term growth, with strongest performance during Q4."
)


st.plotly_chart(
    monthly_profit_trend(filters),
    width="stretch"
)
st.info(
    "💡 Profit growth closely follows revenue growth, indicating healthy business scalability."
)

# st.plotly_chart(
#     sales_by_region(filters),
#     width="stretch"
# )

# st.plotly_chart(
#     profit_by_region(filters),
#     width="stretch"
# )

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        sales_by_region(filters),
        width="stretch"
    )
    st.info(
    "💡 The West region consistently generates the highest sales contribution."
    )

with col2:
    st.plotly_chart(
        profit_by_region(filters),
        width="stretch"
    )
    st.info(
    "💡 West and East regions contribute the largest share of overall profit."
    )