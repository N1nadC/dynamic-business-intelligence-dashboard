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

    .region-badge {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 50px;
        font-size: 0.7rem;
        font-weight: 600;
        margin-right: 0.4rem;
    }

    .region-badge.west {
        background: #dbeafe;
        color: #1e40af;
    }

    .region-badge.east {
        background: #d1fae5;
        color: #065f46;
    }

    .region-badge.central {
        background: #fef3c7;
        color: #92400e;
    }

    .region-badge.south {
        background: #fee2e2;
        color: #991b1b;
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
st.markdown('<div class="page-header">Regional Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subheader">Geographic sales distribution, state performance, and market insights</div>', unsafe_allow_html=True)

# ── Region Pills ─────────────────────────────────────────
st.markdown("""
<div style="margin-bottom: 1.2rem;">
    <span class="region-badge west">West</span>
    <span class="region-badge east">East</span>
    <span class="region-badge central">Central</span>
    <span class="region-badge south">South</span>
</div>
""", unsafe_allow_html=True)

# ── Filters ──────────────────────────────────────────────
with st.container():
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    filters = create_filters()
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 1: Top States & Cities ─────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Top States by Sales</div>', unsafe_allow_html=True)
    st.plotly_chart(
        top_states_by_sales(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box blue">
        California and New York are the strongest revenue-generating markets, 
        representing major coastal economic hubs.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Top Cities by Sales</div>', unsafe_allow_html=True)
    st.plotly_chart(
        top_cities_by_sales(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box green">
        Major metropolitan areas drive a substantial portion of total sales. 
        Urban centers show strong consumer demand.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 2: Sales Distribution ────────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Sales Distribution by Region</div>', unsafe_allow_html=True)
    st.plotly_chart(
        sales_distribution_by_region(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box purple">
        Sales are concentrated primarily within the West and East regions, 
        with Central and South showing growth potential.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 3: Sales Map ─────────────────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Sales Heatmap by State</div>', unsafe_allow_html=True)
    st.plotly_chart(
        sales_map_by_state(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box red">
        Revenue performance is strongest across major coastal markets. 
        The map reveals clear geographic concentration patterns.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 4: Top States by Profit ────────────────────────
with st.container():
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-header">Top States by Profit</div>', unsafe_allow_html=True)
    st.plotly_chart(
        top_states_by_profit(filters),
        use_container_width=True,
        config={'displayModeBar': False}
    )
    st.markdown("""
    <div class="insight-box">
        High-profit states closely align with top revenue-generating markets. 
        Profit concentration validates the focus on high-value geographic segments.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Regional data sourced from Superstore Dataset | Map visualizations powered by Plotly
</div>
""", unsafe_allow_html=True)
