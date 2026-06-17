import streamlit as st

st.set_page_config(
    page_title="Business Intelligence Dashboard",
    page_icon="",
    layout="wide"
)

# ── Custom CSS ───────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero Section ── */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        border-radius: 16px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .hero-container::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -20%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(59,130,246,0.12) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
        padding: 0.35rem 0.9rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        border: 1px solid rgba(59, 130, 246, 0.25);
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #f8fafc;
        margin: 0.8rem 0 0.4rem 0;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        font-weight: 400;
        margin-bottom: 1.2rem;
    }

    .hero-author {
        color: #64748b;
        font-size: 0.9rem;
    }

    .hero-author strong {
        color: #60a5fa;
        font-weight: 600;
    }

    /* ── Section Headers ── */
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid;
        display: inline-block;
    }

    /* ── Metric Cards ── */
    .metric-card {
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid;
        transition: all 0.2s ease;
        text-align: center;
    }

    .metric-card:hover {
        transform: translateY(-2px);
    }

    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        margin: 0.4rem 0;
    }

    .metric-label {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    /* ── Pipeline ── */
    .pipeline-container {
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid;
    }

    .pipeline-step {
        display: flex;
        align-items: center;
        padding: 0.9rem 1.2rem;
        border-radius: 10px;
        margin-bottom: 0.6rem;
        border-left: 3px solid #3b82f6;
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
        font-size: 1.2rem;
        margin-right: 0.8rem;
        width: 28px;
        text-align: center;
        color: #3b82f6;
    }

    .pipeline-text {
        font-weight: 600;
        font-size: 0.95rem;
    }

    /* ── Tech Badges ── */
    .tech-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.2rem;
        border: 1px solid;
        transition: all 0.2s ease;
    }

    /* ── Nav Cards ── */
    .nav-card {
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid;
        transition: all 0.2s ease;
        height: 100%;
    }

    .nav-card:hover {
        transform: translateY(-4px);
        border-color: #3b82f6;
    }

    .nav-icon {
        font-size: 1.6rem;
        margin-bottom: 0.6rem;
        color: #3b82f6;
    }

    .nav-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .nav-desc {
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* ── Overview Text ── */
    .overview-text {
        font-size: 1rem;
        line-height: 1.8;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0;
        font-size: 0.8rem;
        border-top: 1px solid;
        margin-top: 2rem;
    }

    /* ── LIGHT MODE ── */
    @media (prefers-color-scheme: light) {
        .section-header {
            color: #0f172a;
            border-color: #e2e8f0;
        }
        .metric-card {
            background: #ffffff;
            border-color: #e2e8f0;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        }
        .metric-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            border-color: #cbd5e1;
        }
        .metric-value { color: #0f172a; }
        .metric-label { color: #64748b; }
        .pipeline-container {
            background: #f8fafc;
            border-color: #e2e8f0;
        }
        .pipeline-step {
            background: white;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }
        .pipeline-text { color: #1e293b; }
        .tech-badge {
            background: #f1f5f9;
            color: #334155;
            border-color: #e2e8f0;
        }
        .tech-badge:hover {
            background: #e2e8f0;
            border-color: #cbd5e1;
        }
        .nav-card {
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }
        .nav-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }
        .nav-title { color: #0f172a; }
        .nav-desc { color: #64748b; }
        .overview-text {
            color: #475569;
            background: white;
            border-color: #e2e8f0;
        }
        .footer {
            color: #94a3b8;
            border-color: #e2e8f0;
        }
    }

    /* ── DARK MODE ── */
    @media (prefers-color-scheme: dark) {
        .section-header {
            color: #f1f5f9;
            border-color: #334155;
        }
        .metric-card {
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        }
        .metric-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border-color: #475569;
        }
        .metric-value { color: #f1f5f9; }
        .metric-label { color: #94a3b8; }
        .pipeline-container {
            background: #1e293b;
            border-color: #334155;
        }
        .pipeline-step {
            background: #0f172a;
            box-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }
        .pipeline-text { color: #e2e8f0; }
        .tech-badge {
            background: #334155;
            color: #e2e8f0;
            border-color: #475569;
        }
        .tech-badge:hover {
            background: #475569;
            border-color: #64748b;
        }
        .nav-card {
            background: #1e293b;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }
        .nav-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.3);
        }
        .nav-title { color: #f1f5f9; }
        .nav-desc { color: #94a3b8; }
        .overview-text {
            color: #cbd5e1;
            background: #1e293b;
            border-color: #334155;
        }
        .footer {
            color: #64748b;
            border-color: #334155;
        }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ───────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">Business Intelligence</div>
    <div class="hero-title">Dynamic BI Dashboard</div>
    <div class="hero-subtitle">Superstore Retail Analytics & Strategic Insights</div>
    <div class="hero-author">Developed by <strong>Ninad Chaudhari</strong></div>
</div>
""", unsafe_allow_html=True)

# ── Project Overview ─────────────────────────────────────
st.markdown('<div class="section-header">Project Overview</div>', unsafe_allow_html=True)
st.markdown("""
<div class="overview-text">
This project analyzes the <strong>Superstore retail dataset</strong> and demonstrates a complete 
Business Intelligence workflow from raw data cleaning and database design to interactive 
dashboard development and cloud deployment. Every insight is data-driven and actionable.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Dataset Summary ──────────────────────────────────────
st.markdown('<div class="section-header">Dataset Summary</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">5,003</div>
        <div class="metric-label">Total Orders</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">793</div>
        <div class="metric-label">Unique Customers</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">1,861</div>
        <div class="metric-label">Products</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Analytics Pipeline ───────────────────────────────────
st.markdown('<div class="section-header">Analytics Pipeline</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section-header">Technology Stack</div>', unsafe_allow_html=True)

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

# ── Dashboard Navigation ─────────────────────────────────
st.markdown('<div class="section-header">Dashboard Navigation</div>', unsafe_allow_html=True)

st.markdown("""
<div style="margin-bottom: 1.5rem; font-size: 0.95rem;">
    Use the sidebar to explore interactive analytics modules:
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-icon">[CHART]</div>
        <div class="nav-title">Executive Overview</div>
        <div class="nav-desc">High-level KPIs, sales trends, and regional performance at a glance.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-icon">[BOX]</div>
        <div class="nav-title">Product Performance</div>
        <div class="nav-desc">Category breakdowns, top products, and portfolio optimization insights.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-icon">[MAP]</div>
        <div class="nav-title">Regional Analysis</div>
        <div class="nav-desc">Geographic sales distribution, state-level maps, and city rankings.</div>
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
