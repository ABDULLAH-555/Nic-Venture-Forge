import streamlit as st
# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="NIC Venture Forge",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# CUSTOM BRANDING & CSS INJECTION (ELITE DARK MODE DESIGN SYSTEM)
# ==============================================================================
NIC_DARK_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap');

    /* Global App Background & Dark Theme Overrides */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0B0F19 !important;
        color: #F8FAFC !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        letter-spacing: -0.02em;
        color: #F8FAFC !important;
    }

    p, span, label {
        color: #94A3B8;
    }

    /* Top decorative emerald gradient bar */
    .nic-topbar {
        height: 4px;
        background: linear-gradient(90deg, #059669 0%, #10B981 50%, #06B6D4 100%);
        border-radius: 4px;
        margin-bottom: 24px;
        box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
    }

    /* Hero Banner Container */
    .hero-container {
        background: linear-gradient(135deg, rgba(6, 58, 44, 0.85) 0%, rgba(15, 23, 42, 0.95) 55%, rgba(11, 15, 25, 0.98) 100%);
        border-radius: 24px;
        padding: 44px 40px;
        color: #FFFFFF;
        box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.7), 0 0 35px rgba(16, 185, 129, 0.12);
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
        border: 1px solid rgba(16, 185, 129, 0.35);
        backdrop-filter: blur(16px);
    }

    .hero-container::before {
        content: "";
        position: absolute;
        top: -80px;
        right: -80px;
        width: 320px;
        height: 320px;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(6, 182, 212, 0.1) 40%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .hero-container::after {
        content: "";
        position: absolute;
        bottom: -60px;
        left: -60px;
        width: 240px;
        height: 240px;
        background: radial-gradient(circle, rgba(5, 150, 105, 0.2) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .nic-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.15);
        backdrop-filter: blur(8px);
        padding: 6px 16px;
        border-radius: 100px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #34D399;
        border: 1px solid rgba(52, 211, 153, 0.4);
        margin-bottom: 18px;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }

    .hero-title {
        font-size: 2.9rem;
        font-weight: 900;
        line-height: 1.15;
        margin-top: 0;
        margin-bottom: 16px;
        color: #FFFFFF !important;
    }

    .hero-title span {
        background: linear-gradient(90deg, #34D399 0%, #10B981 50%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .hero-subtitle {
        font-size: 1.12rem;
        line-height: 1.65;
        color: #CBD5E1 !important;
        max-width: 860px;
        margin-bottom: 24px;
        font-weight: 400;
    }

    .hero-subtitle strong {
        color: #F8FAFC !important;
    }

    /* Glass Chips Grid */
    .chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 8px;
    }

    .stat-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(30, 41, 59, 0.7);
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.88rem;
        color: #E2E8F0 !important;
        border: 1px solid rgba(51, 65, 85, 0.8);
        backdrop-filter: blur(10px);
        transition: all 0.2s ease;
    }

    .stat-chip:hover {
        background: rgba(51, 65, 85, 0.85);
        border-color: rgba(16, 185, 129, 0.5);
        transform: translateY(-2px);
    }

    .stat-chip strong {
        color: #34D399 !important;
    }

    /* Hero & Action CTA Button Styling */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 6px 0 16px 0 !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #10B981 0%, #047857 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Outfit', 'Inter', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        border: 1px solid #34D399 !important;
        border-radius: 12px !important;
        padding: 0.65rem 2.2rem !important;
        box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3) !important;
        transition: all 0.25s ease-in-out !important;
        max-width: 380px !important;
        width: 100% !important;
        margin: 0 auto !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
    }

    div.stButton > button p,
    div.stButton > button span,
    div.stButton > button div {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.4 !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #34D399 0%, #059669 100%) !important;
        color: #0F172A !important;
        box-shadow: 0 0 22px rgba(52, 211, 153, 0.6) !important;
        transform: translateY(-2px) !important;
        border-color: #6EE7B7 !important;
    }

    div.stButton > button:hover p,
    div.stButton > button:hover span,
    div.stButton > button:hover div {
        color: #0F172A !important;
    }

    div.stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
        box-shadow: 0 2px 10px rgba(16, 185, 129, 0.4) !important;
    }

    /* Equal height columns support in Streamlit */
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
    }

    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] > div {
        display: flex !important;
        flex-direction: column !important;
        flex: 1 1 auto !important;
        height: 100% !important;
    }

    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] [data-testid="stMarkdownContainer"] {
        display: flex !important;
        flex-direction: column !important;
        flex: 1 1 auto !important;
        height: 100% !important;
    }

    /* Feature Cards System */
    .feature-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 28px 24px;
        min-height: 290px;
        height: 100%;
        box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.4);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 36px -8px rgba(0, 0, 0, 0.6), 0 0 25px rgba(16, 185, 129, 0.2);
        border-color: #10B981;
    }

    .card-icon {
        width: 52px;
        height: 52px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin-bottom: 18px;
        background: rgba(16, 185, 129, 0.15);
        color: #34D399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        flex-shrink: 0;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #F8FAFC !important;
        margin-bottom: 10px;
        flex-shrink: 0;
    }

    .card-desc {
        font-size: 0.95rem;
        color: #94A3B8 !important;
        line-height: 1.6;
        flex-grow: 1;
    }

    /* Step Card */
    .step-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-left: 4px solid #10B981;
        border-radius: 0 14px 14px 0;
        padding: 22px 24px;
        margin-bottom: 16px;
        min-height: 180px;
        height: 100%;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
    }

    .step-card:hover {
        transform: translateX(4px);
        border-left-color: #34D399;
        background: #243248;
    }

    .step-number {
        font-weight: 800;
        color: #34D399 !important;
        font-size: 0.85rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .step-heading {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC !important;
        margin-bottom: 6px;
    }

    .step-body {
        font-size: 0.92rem;
        color: #94A3B8 !important;
        line-height: 1.55;
    }

    /* Deliverables Matrix */
    .deliverable-box {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 12px;
        display: flex;
        align-items: flex-start;
        gap: 16px;
        transition: all 0.2s ease;
    }

    .deliverable-box:hover {
        border-color: rgba(16, 185, 129, 0.4);
        background: #243248;
        transform: translateY(-2px);
    }

    .deliverable-number {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 0.9rem;
        width: 32px;
        height: 32px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
    }

    .deliverable-text h4 {
        margin: 0 0 4px 0;
        font-size: 1.05rem;
        font-weight: 700;
        color: #F8FAFC !important;
    }

    .deliverable-text p {
        margin: 0;
        font-size: 0.88rem;
        color: #94A3B8 !important;
        line-height: 1.5;
    }

    /* Bottom Call to Action Banner */
    .cta-banner {
        background: linear-gradient(135deg, rgba(6, 58, 44, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border-radius: 20px;
        padding: 40px 32px 32px 32px;
        color: #FFFFFF;
        text-align: center;
        margin: 44px 0 24px 0;
        border: 1px solid rgba(16, 185, 129, 0.4);
        box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.7), 0 0 30px rgba(16, 185, 129, 0.15);
    }

    .cta-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 9999px;
        background: rgba(16, 185, 129, 0.15);
        color: #34D399;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 12px;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .cta-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin-bottom: 12px;
    }

    .cta-desc {
        color: #CBD5E1 !important;
        font-size: 1.05rem;
        max-width: 680px;
        margin: 0 auto 24px auto;
        line-height: 1.6;
    }

    /* Fixed Bottom Footer */
    .nic-footer {
        margin-top: 64px;
        padding: 28px 0 36px 0;
        border-top: 1px solid #1E293B;
        text-align: center;
        color: #64748B;
        font-size: 0.92rem;
    }

    .nic-footer-credit {
        font-weight: 700;
        color: #34D399 !important;
        font-size: 1rem;
        margin-bottom: 0;
    }

    .nic-footer-tagline {
        font-size: 0.82rem;
        color: #64748B !important;
    }

    /* Sidebar Dark Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B !important;
    }

    section[data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }

    .sidebar-brand-box {
        padding: 18px;
        background: linear-gradient(135deg, rgba(6, 58, 44, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 14px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }

    div[data-testid="stPageLink-NavLink"] {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        padding: 8px 14px !important;
        transition: all 0.2s ease !important;
        margin-bottom: 6px !important;
    }

    div[data-testid="stPageLink-NavLink"]:hover {
        border-color: #10B981 !important;
        background: #243248 !important;
    }

    /* Hide Streamlit default multipage navigation list */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
"""
st.markdown(NIC_DARK_CSS, unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR BRANDING & QUICK NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand-box">
            <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #34D399;">
                National Incubation Center
            </div>
            <div style="font-size: 1.45rem; font-weight: 900; margin-top: 4px; color: #FFFFFF;">
                NIC Venture Forge
            </div>
            <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px;">
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
    st.caption("Powered by **Groq LPU™ Inference Engine** running **LLaMA 3.3 70B Versatile** at ultra-low latency.")

# ==============================================================================
# MAIN PAGE CONTENT
# ==============================================================================

# Decorative top bar
st.markdown('<div class="nic-topbar"></div>', unsafe_allow_html=True)

# Hero Section
st.markdown(
    """
    <div class="hero-container">
        <h1 class="hero-title">
            Turn Rough Ideas Into <span>Investor-Grade Plans</span>
        </h1>
        <p class="hero-subtitle">
            Empowering the next generation of builders. <strong>NIC Venture Forge</strong> instantly translates real-world market friction into scalable business models, validation roadmaps, and incubation-ready pitch decks powered by ultra-fast Generative AI.
        </p>
        <div class="chips-container">
            <div class="stat-chip">⚡ <strong>Speed:</strong> ~3.8s Groq Inference</div>
            <div class="stat-chip">🧠 <strong>Model:</strong> LLaMA 3.3 70B</div>
            <div class="stat-chip">📋 <strong>Output:</strong> 7 Investor Sections</div>
            <div class="stat-chip">🇵🇰 <strong>Focus:</strong> Pakistan & Emerging Markets</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Prominent Hero Call-to-Action Action Button
cta_col1, cta_col2, cta_col3 = st.columns([1, 2.5, 1])
with cta_col2:
    if st.button("🚀 Launch Venture Forge Generator →", key="hero_cta_button", use_container_width=True):
        st.switch_page("pages/1_🚀_Idea_Generator.py")

st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# VALUE PROPOSITION CARDS (WHY NIC VENTURE FORGE)
# ==============================================================================
st.markdown("## 💡 Why NIC Venture Forge?")
st.markdown(
    "<p style='color: #94A3B8; font-size: 1.05rem; margin-top: -8px; margin-bottom: 24px;'>"
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
    "<p style='color: #94A3B8; font-size: 1.05rem; margin-top: -8px; margin-bottom: 24px;'>"
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
    "<p style='color: #94A3B8; font-size: 1.05rem; margin-top: -8px; margin-bottom: 20px;'>"
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
        <div class="cta-badge">⚡ ACCELERATE YOUR LAUNCH</div>
        <div class="cta-title">Ready to Forge Your Venture?</div>
        <div class="cta-desc">
            Take your problem statement from the classroom or whiteboard directly to an accelerator-grade pitch.
            No credit card or setup fees required.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

bottom_cta_col1, bottom_cta_col2, bottom_cta_col3 = st.columns([1, 2.5, 1])
with bottom_cta_col2:
    if st.button("🚀 Launch Venture Forge Generator →", key="bottom_cta_button", use_container_width=True):
        st.switch_page("pages/1_🚀_Idea_Generator.py")

# ==============================================================================
# MANDATORY DEVELOPER FOOTER
# ==============================================================================
st.markdown(
    """
    <div class="nic-footer">
        <div class="nic-footer-credit">
            Designed & Developed for National Incubation Center | Developed by Abdullah Khalid Khan
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
