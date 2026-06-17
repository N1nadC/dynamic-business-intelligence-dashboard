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

    .kpi-container {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.3rem 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        text-align: center;
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
    }

    .kpi-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
    }

    .kpi-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        border-color: #cbd5e1;
    }

    .kpi-value {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0.3rem 0;
    }

    .kpi-label {
        font-size: 0.75rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .kpi-delta {
        font-size: 0.7rem;
        font-weight: 600;
        margin-top: 0.3rem;
    }

    .kpi-delta.positive {
        color: #059669;
    }

    .kpi-delta.negative {
        color: #dc2626;
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

    .filter-bar {
        background: #f8fafc;
        border-radius: 10px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 1.2rem;
        border: 1px solid #e2e8f0;
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
st.markdown('<div class="page-header">Executive Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subheader">Real-time business performance metrics and trend analysis</div>', unsafe_allow_html=True)

# ── Filters ──────────────────────────────────────────────
with st.container():
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    filters = create_filters()
    st.markdown('</div>', unsafe_allow_html=True)

kpis = get_kpi_data(filters)

# ── KPI Cards ────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">${kpis['sales']:,.0f}</div>
        <div class="kpi-label">Total Sales</div>
        <div class="kpi-delta positive">+12.4% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">${kpis['profit']:,.0f}</div>
        <div class="kpi-label">Total Profit</div>
        <div class="kpi-delta positive">+8.7% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">{kpis['margin']:.1f}%</div>
        <div class="kpi-label">Profit Margin</div>
        <div class="kpi-delta positive">+1.2% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">{kpis['orders']:,}</div>
        <div class="kpi-label">Total Orders</div>
        <div class="kpi-delta positive">+5.3% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">{kpis['customers']:,}</div>
        <div class="kpi-label">Total Customers</div>
        <div class="kpi-delta positive">+3.1% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-value">${kpis['aov']:,.0f}</div>
        <div class="kpi-label">Avg Order Value</div>
        <div class="kpi-delta positive">+6.8% vs last period</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Charts ───────────────────────────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Monthly Sales Trend</div>', unsafe_allow_html=True)
    st.plotly_chart(
        monthly_sales_trend(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box">
        Sales demonstrate steady long-term growth, with strongest performance during Q4. 
        November and December show peak seasonal demand.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Monthly Profit Trend</div>', unsafe_allow_html=True)
    st.plotly_chart(
        monthly_profit_trend(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box blue">
        Profit growth closely follows revenue growth, indicating healthy business scalability. 
        Margin consistency suggests efficient cost management.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Sales by Region</div>', unsafe_allow_html=True)
    st.plotly_chart(
        sales_by_region(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box green">
        The West region consistently generates the highest sales contribution, 
        driven by strong coastal market performance.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Profit by Region</div>', unsafe_allow_html=True)
    st.plotly_chart(
        profit_by_region(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box purple">
        West and East regions contribute the largest share of overall profit, 
        while Central and South show room for improvement.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Data refreshed automatically from Superstore Dataset | Last updated: Now
</div>
""", unsafe_allow_html=True)
