import streamlit as st

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

    .hero-insight {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        border-radius: 16px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .hero-insight::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(59,130,246,0.12) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-title {
        font-size: 1.7rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 0.4rem;
    }

    .hero-desc {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 1rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #e2e8f0;
        display: inline-block;
    }

    .metric-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.3rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        transition: all 0.2s ease;
        text-align: center;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        border-color: #cbd5e1;
    }

    .metric-value {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0.3rem 0;
    }

    .metric-label {
        font-size: 0.78rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .finding-card {
        background: white;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        border-left: 3px solid #22c55e;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        margin-bottom: 0.8rem;
        transition: all 0.2s ease;
    }

    .finding-card:hover {
        transform: translateX(3px);
        box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }

    .finding-text {
        font-size: 0.95rem;
        color: #1e293b;
        font-weight: 500;
        line-height: 1.5;
    }

    .recommendation-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.3rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        margin-bottom: 0.8rem;
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
    }

    .recommendation-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 3px;
        height: 100%;
        background: linear-gradient(180deg, #3b82f6, #60a5fa);
    }

    .recommendation-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border-color: #cbd5e1;
    }

    .rec-title {
        font-size: 1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .rec-text {
        font-size: 0.9rem;
        color: #475569;
        line-height: 1.6;
        padding-left: 0.3rem;
    }

    .pipeline-container {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
    }

    .pipeline-step {
        display: flex;
        align-items: center;
        padding: 0.9rem 1.2rem;
        background: white;
        border-radius: 10px;
        margin-bottom: 0.6rem;
        border-left: 3px solid #3b82f6;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        transition: all 0.2s ease;
    }

    .pipeline-step:hover {
        border-left-color: #1e40af;
        transform: translateX(3px);
    }

    .pipeline-step:last-child {
        margin-bottom: 0;
    }

    .pipeline-icon {
        font-size: 1rem;
        font-weight: 800;
        margin-right: 0.8rem;
        width: 28px;
        text-align: center;
        color: #3b82f6;
    }

    .pipeline-text {
        font-weight: 600;
        color: #1e293b;
        font-size: 0.95rem;
    }

    .tech-badge {
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.2rem;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease;
    }

    .tech-badge:hover {
        background: #e2e8f0;
        border-color: #cbd5e1;
    }

    .priority-high {
        display: inline-block;
        background: #fee2e2;
        color: #991b1b;
        padding: 0.15rem 0.5rem;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 700;
        margin-left: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    .priority-medium {
        display: inline-block;
        background: #fef3c7;
        color: #92400e;
        padding: 0.15rem 0.5rem;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 700;
        margin-left: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    .priority-low {
        display: inline-block;
        background: #dbeafe;
        color: #1e40af;
        padding: 0.15rem 0.5rem;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 700;
        margin-left: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #94a3b8;
        font-size: 0.8rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ─────────────────────────────────────────
st.markdown("""
<div class="hero-insight">
    <div class="hero-title">Business Insights</div>
    <div class="hero-desc">Strategic findings and actionable recommendations derived from the Superstore Business Intelligence Dashboard.</div>
</div>
""", unsafe_allow_html=True)

# ── Executive Summary ────────────────────────────────────
st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">$2.29M</div>
        <div class="metric-label">Total Sales</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">$284.15K</div>
        <div class="metric-label">Total Profit</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">12.01%</div>
        <div class="metric-label">Profit Margin</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">5,003</div>
        <div class="metric-label">Total Orders</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">793</div>
        <div class="metric-label">Unique Customers</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Key Findings ─────────────────────────────────────────
st.markdown('<div class="section-title">Key Findings</div>', unsafe_allow_html=True)

st.markdown("""
<div class="finding-card">
    <div class="finding-text">Technology is the highest-performing category in both sales and profitability.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="finding-card">
    <div class="finding-text">The West region consistently generates the highest sales and profit.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="finding-card">
    <div class="finding-text">California and New York are the strongest-performing states.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="finding-card">
    <div class="finding-text">Q4 significantly outperforms other quarters, with November being the strongest month.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="finding-card">
    <div class="finding-text">Furniture generates strong sales but comparatively weak profit margins.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Strategic Recommendations ────────────────────────────
st.markdown('<div class="section-title">Strategic Recommendations</div>', unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-card">
    <div class="rec-title">
        Expand Technology Product Portfolio
        <span class="priority-high">High Priority</span>
    </div>
    <div class="rec-text">
        Technology products generate the highest sales and profit. Additional inventory investment 
        and product expansion may accelerate future revenue growth.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-card">
    <div class="rec-title">
        Improve Furniture Profitability
        <span class="priority-high">High Priority</span>
    </div>
    <div class="rec-text">
        Furniture generates substantial revenue but relatively low profit. Pricing, discounting, 
        and supplier costs should be reviewed to improve margins.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-card">
    <div class="rec-title">
        Increase Investment in High-Performing Regions
        <span class="priority-medium">Medium Priority</span>
    </div>
    <div class="rec-text">
        The West and East regions consistently outperform other regions and represent the 
        strongest opportunities for growth and market expansion.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-card">
    <div class="rec-title">
        Optimize Underperforming Products
        <span class="priority-medium">Medium Priority</span>
    </div>
    <div class="rec-text">
        Low-performing products should be reviewed for promotion, bundling, repositioning, 
        or discontinuation to improve portfolio efficiency.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-card">
    <div class="rec-title">
        Prepare for Seasonal Demand Peaks
        <span class="priority-low">Low Priority</span>
    </div>
    <div class="rec-text">
        Sales activity increases significantly during Q4. Inventory planning and marketing 
        campaigns should be aligned with expected year-end demand.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Project Methodology ────────────────────────────────────
st.markdown('<div class="section-title">Project Methodology</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pipeline-container">
    <div class="pipeline-step">
        <div class="pipeline-icon">1</div>
        <div class="pipeline-text">Raw CSV Dataset</div>
    </div>
    <div class="pipeline-step">
        <div class="pipeline-icon">2</div>
        <div class="pipeline-text">Pandas Data Cleaning & Preprocessing</div>
    </div>
    <div class="pipeline-step">
        <div class="pipeline-icon">3</div>
        <div class="pipeline-text">MySQL Database Design & Schema</div>
    </div>
    <div class="pipeline-step">
        <div class="pipeline-icon">4</div>
        <div class="pipeline-text">SQL Analytics & Business Queries</div>
    </div>
    <div class="pipeline-step">
        <div class="pipeline-icon">5</div>
        <div class="pipeline-text">Power BI Dashboard Development</div>
    </div>
    <div class="pipeline-step">
        <div class="pipeline-icon">6</div>
        <div class="pipeline-text">Streamlit Web Application Deployment</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Technology Stack ─────────────────────────────────────
st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Pandas</span>
    <span class="tech-badge">MySQL</span>
    <span class="tech-badge">SQLAlchemy</span>
    <span class="tech-badge">SQL</span>
    <span class="tech-badge">Power BI</span>
    <span class="tech-badge">Plotly</span>
    <span class="tech-badge">Streamlit</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <p>Data sourced from Superstore Retail Dataset | All insights are for analytical purposes</p>
    <p>Built with Streamlit & Plotly</p>
</div>
""", unsafe_allow_html=True)
