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

# ── Custom CSS ───────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .page-header {
        font-size: 2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
    }

    .page-subheader {
        font-size: 0.95rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }

    .chart-card {
        background: white;
        border-radius: 12px;
        padding: 1.3rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        margin-bottom: 1.2rem;
    }

    .chart-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.8rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #f1f5f9;
    }

    .insight-box {
        background: #fefce8;
        border-left: 3px solid #eab308;
        border-radius: 6px;
        padding: 0.8rem 1rem;
        margin-top: 0.6rem;
        font-size: 0.85rem;
        color: #713f12;
        font-weight: 500;
    }

    .insight-box.blue {
        background: #eff6ff;
        border-left-color: #3b82f6;
        color: #1e3a8a;
    }

    .insight-box.green {
        background: #f0fdf4;
        border-left-color: #22c55e;
        color: #14532d;
    }

    .insight-box.purple {
        background: #faf5ff;
        border-left-color: #a855f7;
        color: #581c87;
    }

    .insight-box.red {
        background: #fef2f2;
        border-left-color: #ef4444;
        color: #7f1d1d;
    }

    .filter-bar {
        background: #f8fafc;
        border-radius: 10px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 1.2rem;
        border: 1px solid #e2e8f0;
    }

    .category-pill {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 50px;
        font-size: 0.7rem;
        font-weight: 600;
        margin-right: 0.4rem;
    }

    .category-pill.tech {
        background: #dbeafe;
        color: #1e40af;
    }

    .category-pill.furniture {
        background: #fef3c7;
        color: #92400e;
    }

    .category-pill.office {
        background: #d1fae5;
        color: #065f46;
    }

    .footer {
        text-align: center;
        padding: 1.5rem 0;
        color: #94a3b8;
        font-size: 0.75rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Page Header ──────────────────────────────────────────
st.markdown('<div class="page-header">Product Performance</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subheader">Category analysis, product rankings, and portfolio insights</div>', unsafe_allow_html=True)

# ── Category Pills ───────────────────────────────────────
st.markdown("""
<div style="margin-bottom: 1.2rem;">
    <span class="category-pill tech">Technology</span>
    <span class="category-pill furniture">Furniture</span>
    <span class="category-pill office">Office Supplies</span>
</div>
""", unsafe_allow_html=True)

# ── Filters ──────────────────────────────────────────────
with st.container():
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    filters = create_filters()
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 1: Sales & Profit by Category ──────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Sales by Category</div>', unsafe_allow_html=True)
    st.plotly_chart(
        sales_by_category(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box blue">
        Technology is the highest revenue-generating product category, 
        contributing significantly to overall sales volume.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Profit by Category</div>', unsafe_allow_html=True)
    st.plotly_chart(
        profit_by_category(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box green">
        Office Supplies delivers stronger profitability than Furniture despite lower sales, 
        indicating higher margin efficiency.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 2: Subcategory Treemap ─────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Subcategory Revenue Distribution</div>', unsafe_allow_html=True)
    st.plotly_chart(
        subcategory_treemap(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box purple">
        Revenue is concentrated within a small number of high-performing sub-categories. 
        Focus marketing efforts on these high-value segments.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 3: Top Products ────────────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Top Products by Sales</div>', unsafe_allow_html=True)
    st.plotly_chart(
        top_products_by_sales(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box">
        A small group of products drives a significant share of total revenue. 
        These hero products should be prioritized in inventory and promotion strategies.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 4: Lowest Performing Products ──────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Lowest Performing Products</div>', unsafe_allow_html=True)
    st.plotly_chart(
        lowest_performing_products(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box red">
        Several products contribute minimal revenue and may require portfolio review. 
        Consider bundling, promotion, or discontinuation for these underperformers.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Product data refreshed from Superstore Dataset | Analytics powered by Plotly
</div>
""", unsafe_allow_html=True)
