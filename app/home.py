import streamlit as st

st.set_page_config(
    page_title="Dynamic Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dynamic Business Intelligence Dashboard")

st.markdown("### Developed by Ninad Chaudhari")

st.divider()

st.header("Project Overview")

st.write("""
This project analyzes the Superstore retail dataset and demonstrates
a complete Business Intelligence workflow from data cleaning and
database design to interactive dashboard development and deployment.
""")

st.divider()

st.header("Analytics Pipeline")

st.markdown("""
Raw Dataset → Pandas Cleaning → MySQL Database → SQL Analytics
→ Power BI Dashboard → Streamlit Deployment
""")

st.divider()

st.header("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Orders", "5,003")

with col2:
    st.metric("Customers", "793")

with col3:
    st.metric("Products", "1,861")

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

st.divider()

st.header("Dashboard Navigation")

st.info("""
Use the sidebar to explore:

• Executive Overview

• Product Performance

• Regional Analysis
""")