"""
NIC Venture Forge - Landing Page
National Incubation Center (NIC)
Developed by Abdullah Khalid Khan | Designed for National Incubation Center
"""

import streamlit as st

# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="NIC Venture Forge | National Incubation Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# CUSTOM BRANDING & CSS INJECTION (NIC BRAND SYSTEM)
# ==============================================================================
NIC_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0F172A;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        letter-spacing: -0.02em;
    }

    /* Top decoration bar */
    .nic-topbar {
        height: 4px;
        background: linear-gradient(90deg, #0D5C46 0%, #10B981 50%, #F59E0B 100%);
        border-radius: 4px;
        margin-bottom: 24px;
    }

    /* Hero Banner Container */
    .hero-container {
        background: linear-gradient(135deg, #063A2C 0%, #0D5C46 55%, #107C5F 100%);
        border-radius: 20px;
        padding: 48px 40px;
        color: #FFFFFF;
        box-shadow: 0 20px 40px -15px rgba(13, 92, 70, 0.35);
        position: relative;
        overflow: hidden;
        margin-bottom: 36px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .hero-container::before {
        content: "";
        position: absolute;
        top: -60px;
        right: -60px;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(13, 92, 70, 0) 70%);
        border-radius: 50%;
    }

    .nic-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        padding: 6px 16px;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #A7F3D0;
        border: 1px solid rgba(167, 243, 208, 0.3);
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 2.85rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 16px;
        color: #FFFFFF;
    }

    .hero-title span {
        background: linear-gradient(90deg, #6EE7B7 0%, #FDE68A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        line-height: 1.6;
        color: #E2E8F0;
        max-width: 820px;
        margin-bottom: 24px;
        font-weight: 400;
    }

    /* Stats strip */
    .stat-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.12);
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 0.9rem;
        color: #F8FAFC;
        margin-right: 10px;
        margin-bottom: 8px;
    }

    .stat-pill strong {
        color: #FBBF24;
    }

    /* Card System */
    .feature-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 28px 24px;
        height: 100%;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.05);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        display: flex;
        flex-direction: column;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 32px -8px rgba(13, 92, 70, 0.15);
        border-color: #10B981;
    }

    .card-icon {
        width: 52px;
        height: 52px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin-bottom: 18px;
        background: #ECFDF5;
        color: #0D5C46;
        border: 1px solid #A7F3D0;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 10px;
    }

    .card-desc {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.55;
    }

    /* Step Card */
    .step-card {
        background: #F8FAFC;
        border-left: 4px solid #0D5C46;
        border-radius: 0 12px 12px 0;
        padding: 20px 24px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    .step-number {
        font-weight: 800;
        color: #0D5C46;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    .step-heading {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 4px;
    }

    .step-body {
        font-size: 0.92rem;
        color: #475569;
        line-height: 1.5;
    }

    /* Deliverables Matrix */
    .deliverable-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
        display: flex;
        align-items: flex-start;
        gap: 14px;
    }

    .deliverable-number {
        background: #0D5C46;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.85rem;
        width: 28px;
        height: 28px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        margin-top: 2px;
    }

    .deliverable-text h4 {
        margin: 0 0 2px 0;
        font-size: 1rem;
        font-weight: 600;
        color: #0F172A;
    }

    .deliverable-text p {
        margin: 0;
        font-size: 0.88rem;
        color: #64748B;
    }

    /* Call to Action Box */
    .cta-banner {
        background: linear-gradient(135deg, #0A4333 0%, #0F172A 100%);
        border-radius: 18px;
        padding: 36px 32px;
        color: #FFFFFF;
        text-align: center;
        margin: 40px 0 28px 0;
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: 0 16px 36px -10px rgba(13, 92, 70, 0.3);
    }

    .cta-title {
        font-size: 1.85rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 10px;
    }

    .cta-desc {
        color: #CBD5E1;
        font-size: 1.05rem;
        max-width: 680px;
        margin: 0 auto 20px auto;
        line-height: 1.55;
    }

    /* Footer */
    .nic-footer {
        margin-top: 60px;
        padding: 24px 0 32px 0;
        border-top: 1px solid #E2E8F0;
        text-align: center;
        color: #64748B;
        font-size: 0.9rem;
    }

    .nic-footer-credit {
        font-weight: 600;
        color: #0D5C46;
    }

    .nic-footer-tagline {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-top: 4px;
    }

    /* Sidebar Tweaks */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }

    .sidebar-brand-box {
        padding: 16px;
        background: linear-gradient(135deg, #0D5C46 0%, #063A2C 100%);
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
</style>
"""
st.markdown(NIC_CSS, unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR BRANDING & QUICK NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand-box">
            <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #6EE7B7;">
                National Incubation Center
            </div>
            <div style="font-size: 1.35rem; font-weight: 800; margin-top: 4px;">
                NIC Venture Forge
            </div>
            <div style="font-size: 0.8rem; color: #E2E8F0; margin-top: 4px;">
                Pakistan's Flagship Startup Engine
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🧭 Platform Navigation")
    st.page_link("app.py", label="Home & Overview", icon="🏠")
    st.page_link("pages/1_🚀_Idea_Generator.py", label="Launch Idea Generator", icon="🚀")

    st.markdown("---")
    st.markdown("### 🏛️ Incubation Network")
    st.markdown(
        """
        - **NIC Islamabad** (National Hub)
        - **NIC Karachi** (Sindh Tech Corridor)
        - **NIC Lahore** (Punjab Innovation Zone)
        - **NIC Peshawar** (KP Frontier)
        - **NIC Quetta** (Balochistan Hub)
        """
    )

    st.markdown("---")
    st.markdown("### ⚡ AI Core Engine")
    st.caption("Powered by **Groq LPU™ Inference Engine** running **OpenAI GPT-OSS 120B / LLaMA** at ultra-low latency.")

# ==============================================================================
# MAIN PAGE CONTENT
# ==============================================================================

# Decorative top bar
st.markdown('<div class="nic-topbar"></div>', unsafe_allow_html=True)

# Hero Section
st.markdown(
    """
    <div class="hero-container">
        <div class="nic-badge">
            <span>🏛️</span> National Incubation Center (NIC)
        </div>
        <h1 class="hero-title">
            Turn Rough Ideas Into <span>Investor-Grade Plans</span>
        </h1>
        <p class="hero-subtitle">
            <strong>NIC Venture Forge</strong> is an elite Generative AI co-pilot designed for Pakistani student innovators,
            aspiring founders, and incubation cohort applicants. Powered by the Groq LPU engine and OpenAI GPT-OSS 120B / LLaMA,
            it synthesizes your problem statement into an accelerator-ready venture blueprint in seconds.
        </p>
        <div>
            <div class="stat-pill">⚡ <strong>Speed:</strong> ~3.8s Groq Inference</div>
            <div class="stat-pill">🧠 <strong>Model:</strong> OpenAI GPT-OSS 120B</div>
            <div class="stat-pill">📋 <strong>Output:</strong> 7 Investor Sections</div>
            <div class="stat-pill">🇵🇰 <strong>Focus:</strong> Pakistan & Emerging Markets</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Prominent CTA Button
cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
with cta_col2:
    st.page_link(
        "pages/1_🚀_Idea_Generator.py",
        label="👉 Launch Venture Forge Generator",
        icon="🚀",
        use_container_width=True,
    )

st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# VALUE PROPOSITION CARDS (WHY NIC VENTURE FORGE)
# ==============================================================================
st.markdown("## 💡 Why NIC Venture Forge?")
st.markdown(
    "<p style='color: #64748B; font-size: 1.05rem; margin-top: -8px; margin-bottom: 24px;'>"
    "Bridging the critical gap between university ideation and venture-backed execution."
    "</p>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-icon">🎯</div>
            <div class="card-title">NIC Incubation Rubric</div>
            <div class="card-desc">
                Outputs are calibrated to match the exact evaluation criteria of NIC selection committees,
                venture partners, and early-stage angel syndicates in Pakistan.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-icon">⚡</div>
            <div class="card-title">Groq LPU Speed</div>
            <div class="card-desc">
                Leverages Groq's revolutionary Language Processing Units (LPUs) to generate deep, multi-page,
                high-reasoning startup analyses at speeds over 250 tokens per second.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-icon">🗺️</div>
            <div class="card-title">Localized Context</div>
            <div class="card-desc">
                Understands the unique dynamics of Tier-1 vs. Rural Pakistani markets, informal logistics,
                cash-on-delivery realities, and emerging market regulatory frameworks.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 36px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# THE 3-STEP FOUNDER JOURNEY
# ==============================================================================
st.markdown("## 🛣️ How It Works (Founder Journey)")
st.markdown(
    "<p style='color: #64748B; font-size: 1.05rem; margin-top: -8px; margin-bottom: 24px;'>"
    "From raw insight to investor deck script in three simple steps."
    "</p>",
    unsafe_allow_html=True,
)

step_col1, step_col2, step_col3 = st.columns(3)

with step_col1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">Step 01</div>
            <div class="step-heading">Define Your Problem</div>
            <div class="step-body">
                Input your problem statement, target sectors (AgriTech, FinTech, HealthTech, etc.),
                and technological angles (e.g. WhatsApp bots, micro-credit, offline sync).
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step_col2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">Step 02</div>
            <div class="step-heading">AI Partner Synthesis</div>
            <div class="step-body">
                The LLaMA 3.3 70B model acts as a veteran accelerator director, stress-testing assumptions,
                unit economics, and execution feasibility.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step_col3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">Step 03</div>
            <div class="step-heading">Export & Pitch</div>
            <div class="step-body">
                Receive a complete, 7-section investor-grade startup plan. Download as a formatted Markdown
                document ready for pitch decks and grant proposals.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 36px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# WHAT YOU GET: THE 7 INVESTOR-GRADE SECTIONS
# ==============================================================================
st.markdown("## 📦 What You Get (The 7 Deliverables)")
st.markdown(
    "<p style='color: #64748B; font-size: 1.05rem; margin-top: -8px; margin-bottom: 20px;'>"
    "Every generated plan produces an exhaustive, investor-aligned breakdown:"
    "</p>",
    unsafe_allow_html=True,
)

deliv_col1, deliv_col2 = st.columns(2)

with deliv_col1:
    st.markdown(
        """
        <div class="deliverable-box">
            <div class="deliverable-number">1</div>
            <div class="deliverable-text">
                <h4>Startup Identity & Punchy Tagline</h4>
                <p>Memorable brand names with strategic branding rationale and positioning.</p>
            </div>
        </div>
        <div class="deliverable-box">
            <div class="deliverable-number">2</div>
            <div class="deliverable-text">
                <h4>Executive Summary & Core Insight</h4>
                <p>The unfair advantage, macro tailwinds, and why this solution wins today.</p>
            </div>
        </div>
        <div class="deliverable-box">
            <div class="deliverable-number">3</div>
            <div class="deliverable-text">
                <h4>Customer Persona & Pain Points</h4>
                <p>Specific user archetypes, quantifiable pain metrics, and willingness to pay.</p>
            </div>
        </div>
        <div class="deliverable-box">
            <div class="deliverable-number">4</div>
            <div class="deliverable-text">
                <h4>6-Week MVP Roadmap</h4>
                <p>Sprint-by-sprint development blueprint to build and launch with minimal capital.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with deliv_col2:
    st.markdown(
        """
        <div class="deliverable-box">
            <div class="deliverable-number">5</div>
            <div class="deliverable-text">
                <h4>Monetization & Business Model</h4>
                <p>Revenue streams, pricing strategy, customer lifetime value (LTV) hypotheses.</p>
            </div>
        </div>
        <div class="deliverable-box">
            <div class="deliverable-number">6</div>
            <div class="deliverable-text">
                <h4>90-Day Go-To-Market (GTM) Playbook</h4>
                <p>Low-cost acquisition hacks, pilot partnerships, and growth flywheels.</p>
            </div>
        </div>
        <div class="deliverable-box">
            <div class="deliverable-number">7</div>
            <div class="deliverable-text">
                <h4>60-Second Demo Day Pitch Script</h4>
                <p>Verbatim script calibrated for NIC Demo Day judges and venture investors.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==============================================================================
# BOTTOM CALL TO ACTION
# ==============================================================================
st.markdown(
    """
    <div class="cta-banner">
        <div class="cta-title">Ready to Forge Your Venture?</div>
        <div class="cta-desc">
            Take your problem statement from the classroom or whiteboard directly to an accelerator-grade pitch.
            No credit card or setup fees required.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

cta_btn_col1, cta_btn_col2, cta_btn_col3 = st.columns([1, 2, 1])
with cta_btn_col2:
    st.page_link(
        "pages/1_🚀_Idea_Generator.py",
        label="🚀 Open 1_🚀_Idea_Generator Page",
        icon="✨",
        use_container_width=True,
    )

# ==============================================================================
# MANDATORY DEVELOPER FOOTER
# ==============================================================================
st.markdown(
    """
    <div class="nic-footer">
        <div class="nic-footer-credit">
            Developed by Abdullah Khalid Khan | Designed for National Incubation Center
        </div>
        <div class="nic-footer-tagline">
            NIC Venture Forge &bull; Powered by Groq LPU &bull; LLaMA 3.3 70B &bull; Production Release v1.0
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
