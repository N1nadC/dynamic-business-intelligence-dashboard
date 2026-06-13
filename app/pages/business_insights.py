import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("💡 Business Insights")

st.markdown(
    """
    Strategic findings and recommendations derived from
    the Superstore Business Intelligence Dashboard.
    """
)

st.divider()

st.header("Executive Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", "$2.29M")

with col2:
    st.metric("Total Profit", "$284.15K")

with col3:
    st.metric("Profit Margin", "12.01%")

col4, col5 = st.columns(2)

with col4:
    st.metric("Orders", "5,003")

with col5:
    st.metric("Customers", "793")
    

st.divider()

st.header("Key Findings")

st.success(
    "Technology is the highest-performing category in both sales and profitability."
)

st.success(
    "The West region consistently generates the highest sales and profit."
)

st.success(
    "California and New York are the strongest-performing states."
)

st.success(
    "Q4 significantly outperforms other quarters, with November being the strongest month."
)

st.success(
    "Furniture generates strong sales but comparatively weak profit margins."
)

st.divider()

st.header("Strategic Recommendations")

st.info(
    """
    🚀 Expand Technology Product Portfolio

    Technology products generate the highest sales and profit.
    Additional inventory investment and product expansion may
    accelerate future revenue growth.
    """
)

st.info(
    """
    💰 Improve Furniture Profitability

    Furniture generates substantial revenue but relatively low profit.
    Pricing, discounting, and supplier costs should be reviewed.
    """
)

st.info(
    """
    📍 Increase Investment in High-Performing Regions

    The West and East regions consistently outperform other regions
    and represent the strongest opportunities for growth.
    """
)

st.info(
    """
    📦 Optimize Underperforming Products

    Low-performing products should be reviewed for promotion,
    bundling, repositioning, or discontinuation.
    """
)

st.info(
    """
    📅 Prepare for Seasonal Demand Peaks

    Sales activity increases significantly during Q4.
    Inventory planning and marketing campaigns should be aligned
    with expected year-end demand.
    """
)

st.divider()

st.header("Project Methodology")

st.markdown("""
### Analytics Pipeline

Raw CSV Dataset

⬇️

Pandas Data Cleaning

⬇️

MySQL Database Design

⬇️

SQL Analytics & Business Queries

⬇️

Power BI Dashboard Development

⬇️

Streamlit Web Application
""")

st.divider()

st.header("Technology Stack")

st.markdown("""
- Python
- Pandas
- MySQL
- SQLAlchemy
- SQL
- Power BI
- Plotly
- Streamlit
""")