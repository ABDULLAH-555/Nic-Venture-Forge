
import os
import re
import time
from datetime import datetime
import streamlit as st

# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Idea Generator | NIC Venture Forge",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# CUSTOM BRANDING & CSS INJECTION (NIC BRAND SYSTEM)
# ==============================================================================
GENERATOR_CSS = """
<style>
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
        margin-bottom: 20px;
    }

    /* Generator Page Header */
    .header-banner {
        background: linear-gradient(135deg, #063A2C 0%, #0D5C46 60%, #107C5F 100%);
        border-radius: 16px;
        padding: 30px 32px;
        color: #FFFFFF;
        box-shadow: 0 16px 36px -12px rgba(13, 92, 70, 0.3);
        margin-bottom: 28px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .header-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        padding: 4px 14px;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #A7F3D0;
        border: 1px solid rgba(167, 243, 208, 0.3);
        margin-bottom: 12px;
    }

    .header-title {
        font-size: 2.1rem;
        font-weight: 800;
        margin-top: 0;
        margin-bottom: 8px;
        color: #FFFFFF;
    }

    .header-desc {
        color: #E2E8F0;
        font-size: 1.02rem;
        margin: 0;
        max-width: 850px;
    }

    /* Form Container */
    .form-wrapper {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.04);
        margin-bottom: 24px;
    }

    /* Output Card */
    .output-hero {
        background: #FFFFFF;
        border: 2px solid #10B981;
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 12px 32px -8px rgba(13, 92, 70, 0.15);
        margin-top: 24px;
        margin-bottom: 24px;
    }

    .badge-pill {
        display: inline-block;
        padding: 4px 12px;
        background: #ECFDF5;
        color: #0D5C46;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 600;
        border: 1px solid #A7F3D0;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    /* Presets bar */
    .preset-chip {
        display: inline-block;
        padding: 6px 14px;
        background: #F1F5F9;
        color: #334155;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid #CBD5E1;
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
        margin-bottom: 0;
    }

    .nic-footer-tagline {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-top: 4px;
    }

    /* Primary Button Polish */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0D5C46 0%, #107C5F 100%) !important;
        border: none !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 12px 28px !important;
        border-radius: 10px !important;
        box-shadow: 0 6px 16px -2px rgba(13, 92, 70, 0.35) !important;
        transition: all 0.25s ease !important;
    }

    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 24px -2px rgba(13, 92, 70, 0.45) !important;
    }

    /* Sidebar Brand */
    .sidebar-brand-box {
        padding: 16px;
        background: linear-gradient(135deg, #0D5C46 0%, #063A2C 100%);
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }

    /* Hide Streamlit default multipage navigation list */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
"""
st.markdown(GENERATOR_CSS, unsafe_allow_html=True)

# ==============================================================================
# SECURE API KEY RESOLUTION (PRODUCTION COMPLIANT)
# ==============================================================================
def get_groq_api_key() -> str:
    """
    Securely resolves the Groq API key strictly adhering to production requirements:
    1. Checks st.secrets["GROQ_API_KEY"]
    2. Fallback check for session-level override (for testing UI without restarting)
    3. Fallback check for environment variable
    """
    api_key = None

    # Priority 1: Native Streamlit Secrets (Required production standard)
    try:
        if "GROQ_API_KEY" in st.secrets:
            candidate = st.secrets["GROQ_API_KEY"]
            if candidate and candidate.strip() and not candidate.startswith("gsk_your_groq_api_key"):
                api_key = candidate.strip()
    except Exception:
        pass

    # Priority 2: Session state key (Allows live testing in UI if user wishes)
    if not api_key and "custom_groq_key" in st.session_state and st.session_state["custom_groq_key"]:
        api_key = st.session_state["custom_groq_key"].strip()

    # Priority 3: OS Environment Variable
    if not api_key:
        env_key = os.getenv("GROQ_API_KEY")
        if env_key and env_key.strip() and not env_key.startswith("gsk_your_groq_api_key"):
            api_key = env_key.strip()

    return api_key or ""


# ==============================================================================
# SIDEBAR NAVIGATION & ENGINE STATUS
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
                Venture Co-Pilot &bull; Page 2
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🧭 Platform Navigation")
    st.page_link("app.py", label="Home & Overview", icon="🏠")
    st.page_link("pages/1_🚀_Idea_Generator.py", label="Launch Idea Generator", icon="🚀")

    st.markdown("---")
    st.markdown("### ⚙️ Engine Telemetry")

    current_api_key = get_groq_api_key()
    if current_api_key:
        masked_key = f"{current_api_key[:6]}...{current_api_key[-4:]}"
        st.success(f"🟢 **Groq API Connected**\n\nKey: `{masked_key}`")
    else:
        st.error("🔴 **Groq API Key Missing**")
        st.info(
            "Please configure `GROQ_API_KEY` in `.streamlit/secrets.toml` or provide it below for this session."
        )

    # Optional dynamic key input for evaluator convenience
    with st.expander("🔑 Session Key Override", expanded=not bool(current_api_key)):
        session_key_input = st.text_input(
            "Enter Groq API Key:",
            type="password",
            value=st.session_state.get("custom_groq_key", ""),
            placeholder="gsk_...",
            help="Your key is kept strictly in memory for this session and is never logged or stored.",
        )
        if session_key_input:
            st.session_state["custom_groq_key"] = session_key_input
            if session_key_input != current_api_key:
                st.rerun()

    st.markdown("---")
    st.markdown("### 🎯 Model Selection")

    AVAILABLE_MODELS = {
        "openai/gpt-oss-120b": "OpenAI GPT-OSS 120B (Active Groq Model / Flagship MoE)",
        "llama-3.1-8b-instant": "LLaMA 3.1 8B Instant (Ultra-Fast ~560 t/s)",
        "llama-3.3-70b-versatile": "LLaMA 3.3 70B Versatile",
    }

    selected_model_id = st.selectbox(
        "Active AI Model:",
        options=list(AVAILABLE_MODELS.keys()),
        format_func=lambda x: AVAILABLE_MODELS[x],
        index=0,
        help="Primary model for plan synthesis. Configured for OpenAI GPT-OSS 120B on Groq LPUs.",
    )

# ==============================================================================
# SAMPLE FOUNDER PRESETS (1-CLICK EVALUATION)
# ==============================================================================
PRESET_IDEAS = {
    "🌾 AgriTech Cold-Chain (Punjab)": {
        "problem": "Smallholder citrus and tomato farmers in Sargodha and Multan face 35-40% post-harvest spoilage because refrigerated transport is monopolized by large brokers who charge predatory commissions and delay pickups.",
        "themes": ["AgriTech", "Logistics & Supply Chain", "CleanTech & ClimateTech"],
        "keywords": "Solar-powered micro cold storage, WhatsApp booking bot, Pay-as-you-store micro-payments, Urdu voice agent, IoT temperature sensors",
        "market": "Rural & Semi-Urban Pakistan",
        "model": "B2B2C (Marketplace / Hybrid)",
        "stage": "Incubation Cohort Candidate",
    },
    "💳 FinTech Micro-Credit (Informal Retail)": {
        "problem": "Over 2.5 million neighborhood Kiryana store owners in Pakistan cannot access formal working capital loans from banks due to lack of audited financial books, forcing them into loan sharks charging 10% monthly interest.",
        "themes": ["FinTech", "AI & SaaS", "E-Commerce & Retail"],
        "keywords": "Digital ledger (Khata) telemetry, alternative credit scoring, Raast instant disbursement, Daily micro-repayments, WhatsApp invoice scanner",
        "market": "Tier-1 Pakistan (Karachi, Lahore, Islamabad)",
        "model": "B2B (Business-to-Business)",
        "stage": "Seed-Ready",
    },
    "🩺 SehatUrdu AI (Health Triage)": {
        "problem": "Primary healthcare clinics in second-tier cities (Gujranwala, Sukkur, Mardan) face a severe shortage of female doctors, leading rural mothers to delay maternal triage or rely on unqualified dispensers for prescription drugs.",
        "themes": ["HealthTech", "AI & SaaS"],
        "keywords": "Urdu voice diagnostic assistant, tele-triage routing, offline sync for low-connectivity clinics, verified prescription cross-checker, WhatsApp bot",
        "market": "Rural & Semi-Urban Pakistan",
        "model": "B2B2C (Marketplace / Hybrid)",
        "stage": "Ideation / Pre-Seed",
    },
}

def load_preset(preset_key: str):
    """Callback to load a preset into session state."""
    preset = PRESET_IDEAS[preset_key]
    st.session_state["input_problem"] = preset["problem"]
    st.session_state["input_themes"] = preset["themes"]
    st.session_state["input_keywords"] = preset["keywords"]
    st.session_state["input_market"] = preset["market"]
    st.session_state["input_model"] = preset["model"]
    st.session_state["input_stage"] = preset["stage"]


# ==============================================================================
# PROMPT ENGINEERING (NIC ACCELERATOR DIRECTOR PERSONA)
# ==============================================================================
def construct_master_prompt(
    problem: str,
    themes: list,
    keywords: str,
    market: str,
    model: str,
    stage: str,
) -> str:
    """
    Constructs an authoritative, investor-grade master prompt calibrating LLaMA 3.3 70B
    as a Senior NIC Venture Partner & Accelerator Director.
    """
    themes_str = ", ".join(themes) if themes else "General Technology"

    return f"""You are the Managing Partner and Chief Accelerator Director at the National Incubation Center (NIC) Pakistan. You possess over 18 years of venture capital, seed-stage accelerator, and early-stage startup building experience across emerging markets, having evaluated over 3,000 startup applications and funded dozens of breakout companies.

You have received an incubation application with the following founder inputs:

- **Target Sector / Themes:** {themes_str}
- **Target Market:** {market}
- **Proposed Business Model:** {model}
- **Venture Stage:** {stage}
- **Tech Angles & Keywords:** {keywords if keywords.strip() else 'Modern scalable tech stack'}
- **Core Problem Statement:**
"{problem}"

---

### YOUR OBJECTIVE
Synthesize these inputs into a comprehensive, investor-grade, accelerator-ready venture blueprint.
Your tone must be authoritative, razor-sharp, commercially astute, realistic, and tailored specifically to the realities of {market} and emerging market execution.

Do NOT provide generic platitudes. Provide exact metrics, realistic pricing, granular weekly roadmaps, and local market nuances.

You MUST follow this EXACT 7-section structure with the verbatim headers specified below:

# 🚀 NIC VENTURE FORGE: INVESTOR-GRADE STARTUP PLAN

## 1. Startup Name & Punchy Tagline
- **Suggested Startup Name:** Provide a memorable, culturally resonant, and globally brandable name.
- **Tagline:** A punchy, 8-word-or-less value proposition.
- **Brand Architecture & Naming Rationale:** Explain why this name works, domain viability, and brand positioning.

## 2. Executive Summary & Core Insight
- **The Core Problem:** The structural market failure being solved.
- **The Unfair Advantage ("Why Now?"):** Specific regulatory, technological, or consumer shifts enabling this solution today.
- **The Solution Hook:** What the product does in simple, non-jargon language.
- **Target TAM / SAM / SOM:** Estimated market size numbers calibrated for {market}.

## 3. Target Customer & Problem Persona
- **Primary Persona:** Name, demographic, exact daily workflow, and pain points.
- **Quantified Pain Point:** Financial loss, lost hours, or frustration metrics currently experienced.
- **Current Alternatives & Why They Fail:** Competitors, informal workarounds, and their shortcomings.
- **Willingness to Pay Indicator:** How and why this persona will part with their hard-earned money.

## 4. Minimum Viable Product (MVP) Scope (6-Week Roadmap)
Provide a week-by-week, resource-constrained build plan to reach launch in 6 weeks:
- **Week 1-2 (Foundation & Wireframes):** Core architecture, database schema, user journeys.
- **Week 3-4 (Core Feature Build):** Key integration (e.g. {keywords}), APIs, security.
- **Week 5 (Internal Alpha & Closed Pilot):** Testing with 10 friendly anchor users, bug squashing.
- **Week 6 (Public Beta Launch & Tracking):** Live deployment, telemetry, first 50 transactions.

## 5. Monetization & Business Model
- **Primary Revenue Stream:** Transaction fees, monthly subscription, markup, or take-rate.
- **Pricing Strategy:** Realistic local pricing in PKR (or USD where applicable).
- **Unit Economics Snapshot:**
  - Estimated Customer Acquisition Cost (CAC)
  - Estimated Average Revenue Per User (ARPU)
  - Estimated Lifetime Value (LTV) and LTV:CAC Ratio hypothesis
- **Path to Breakeven:** Volume or user threshold required to reach operational profitability.

## 6. 90-Day Go-To-Market (GTM) Strategy
- **Days 1–30 (The Anchor Launch):** Guerilla customer acquisition, university campus hacks, or trade association partnerships.
- **Days 31–60 (Channel Expansion):** B2B referral loops, localized content distribution, and conversion optimization.
- **Days 61–90 (Flywheel & NIC Incubation Milestone):** Metrics needed to qualify for NIC Cohort Demo Day, seed investor outreach, and press coverage.

## 7. 60-Second NIC Elevator Pitch Deck Script
Provide a high-conviction, word-for-word pitch script that a founder can memorize and recite in 60 seconds before NIC Demo Day judges and venture capital partners.
Structure it with:
- **The Hook (0-10s):** Gripping stat or problem imagery.
- **The Solution (10-25s):** What we built and our secret sauce.
- **Traction & Market (25-45s):** The size of the opportunity and early signals.
- **The Ask (45-60s):** Incubation cohort acceptance and seed capital ask.

---
Produce the entire investor document now with rich Markdown formatting, bold highlights, bullet points, and tables where appropriate.
"""


# ==============================================================================
# MAIN GENERATOR PAGE
# ==============================================================================

# Decorative top bar
st.markdown('<div class="nic-topbar"></div>', unsafe_allow_html=True)

# Header Banner
st.markdown(
    """
    <div class="header-banner">
        <h1 class="header-title">NIC Idea & Plan Generator</h1>
        <p class="header-desc">
            Transform raw problem statements and industry themes into comprehensive, investor-ready startup blueprints.
            Powered by <strong>LLaMA 3.3 70B Versatile</strong> running on the Groq LPU accelerator.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Quick Preset Buttons
st.markdown("##### ⚡ Quick Start: Load a Pre-Engineered NIC Cohort Case Study")
preset_cols = st.columns([1, 1, 1, 1])

with preset_cols[0]:
    if st.button("🌾 AgriTech Punjab", use_container_width=True, help="Load cold-chain logistics problem"):
        load_preset("🌾 AgriTech Cold-Chain (Punjab)")
        st.rerun()

with preset_cols[1]:
    if st.button("💳 FinTech Retail", use_container_width=True, help="Load informal retail khata micro-credit"):
        load_preset("💳 FinTech Micro-Credit (Informal Retail)")
        st.rerun()

with preset_cols[2]:
    if st.button("🩺 HealthTech Voice", use_container_width=True, help="Load Urdu maternal health triage"):
        load_preset("🩺 SehatUrdu AI (Health Triage)")
        st.rerun()

with preset_cols[3]:
    if st.button("🔄 Reset Form", use_container_width=True, help="Clear form inputs"):
        for key in ["input_problem", "input_themes", "input_keywords", "input_market", "input_model", "input_stage"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# VENTURE FORM INPUTS
# ==============================================================================
with st.container():
    st.markdown("### 📝 1. Founder Input Form")

    # Core Problem Statement (st.text_area)
    default_problem = st.session_state.get(
        "input_problem",
        "Smallholder farmers in Punjab face 40% post-harvest spoilage due to lack of cold-chain visibility and middlemen exploitation, resulting in lost income and high consumer food prices.",
    )
    problem_input = st.text_area(
        "Core Problem Statement (What real-world market failure or customer pain are you solving?)*",
        value=default_problem,
        height=130,
        placeholder="Describe the painful reality, who suffers from it, how much money/time they lose, and why existing alternatives are inadequate...",
        help="Be specific about the customer's pain, the geographic context, and the financial or operational bottleneck.",
    )

    # Row 1: Industry Themes & Specific Keywords
    input_row1_col1, input_row1_col2 = st.columns([1, 1])

    with input_row1_col1:
        theme_options = [
            "AgriTech",
            "FinTech",
            "HealthTech",
            "EdTech",
            "CleanTech",
            "CleanTech & ClimateTech",
            "AI & SaaS",
            "Logistics & Supply Chain",
            "E-Commerce & Retail",
            "E-Commerce & Quick Commerce",
            "GovTech & CivicTech",
            "PropTech & Real Estate",
            "Industrial IoT & Hardware",
            "Media & Creator Economy",
        ]
        raw_themes = st.session_state.get("input_themes", ["AgriTech", "Logistics & Supply Chain"])
        if not isinstance(raw_themes, list):
            raw_themes = [raw_themes] if raw_themes else ["AgriTech"]
        valid_defaults = [t for t in raw_themes if t in theme_options]
        if not valid_defaults:
            valid_defaults = ["AgriTech", "Logistics & Supply Chain"]

        selected_themes = st.multiselect(
            "Industry Themes / Sectors*",
            options=theme_options,
            default=valid_defaults,
            help="Select one or more sectors applicable to your venture.",
        )

    with input_row1_col2:
        default_keywords = st.session_state.get(
            "input_keywords",
            "WhatsApp bot, solar micro-cold-storage, Urdu voice interface, IoT temperature sensors, pay-as-you-store micro-credit",
        )
        keywords_input = st.text_input(
            "Specific Keywords / Tech Angles / Unfair Advantage*",
            value=default_keywords,
            placeholder="e.g. WhatsApp AI bot, offline-first sync, micro-credit scoring, IoT sensors, Raast payment gateway",
            help="Keywords that dictate the technology choice, distribution hack, or unique operational moat.",
        )

    # Row 2: Target Market, Business Model & Venture Stage
    input_row2_col1, input_row2_col2, input_row2_col3 = st.columns([1, 1, 1])

    with input_row2_col1:
        market_options = [
            "Tier-1 Pakistan (Karachi, Lahore, Islamabad)",
            "Rural & Semi-Urban Pakistan",
            "Pan-Pakistan (Omnichannel)",
            "MENA Region (Middle East & North Africa)",
            "Global Emerging Markets",
            "Global Enterprise / Cross-Border",
        ]
        default_market_idx = 1
        if "input_market" in st.session_state and st.session_state["input_market"] in market_options:
            default_market_idx = market_options.index(st.session_state["input_market"])

        target_market = st.selectbox(
            "Target Market / Geography*",
            options=market_options,
            index=default_market_idx,
            help="The primary beachhead market where you will execute the first 90 days.",
        )

    with input_row2_col2:
        model_options = [
            "B2B (Business-to-Business)",
            "B2C (Business-to-Consumer)",
            "B2B2C (Marketplace / Hybrid)",
            "D2C (Direct-to-Consumer)",
            "SaaS (Software-as-a-Service)",
            "Transaction / Commission Take-Rate",
        ]
        default_model_idx = 2
        if "input_model" in st.session_state and st.session_state["input_model"] in model_options:
            default_model_idx = model_options.index(st.session_state["input_model"])

        business_model = st.selectbox(
            "Proposed Business Model*",
            options=model_options,
            index=default_model_idx,
            help="How the platform intends to monetize transactions or software services.",
        )

    with input_row2_col3:
        stage_options = [
            "Ideation / Pre-Seed",
            "Incubation Cohort Candidate",
            "Prototype / MVP Ready",
            "Early Traction / Pilot",
            "Seed-Ready",
        ]
        default_stage_idx = 1
        if "input_stage" in st.session_state and st.session_state["input_stage"] in stage_options:
            default_stage_idx = stage_options.index(st.session_state["input_stage"])

        venture_stage = st.selectbox(
            "Current Venture Stage",
            options=stage_options,
            index=default_stage_idx,
            help="Your current stage helps calibrate the MVP scope and fundraising ask.",
        )

# ==============================================================================
# GENERATION ACTION & GROQ API CALL
# ==============================================================================
st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
generate_clicked = st.button(
    "🚀 Generate Investor-Grade Startup Plan",
    type="primary",
    use_container_width=True,
    help="Triggers the Groq LPU engine to run LLaMA 3.3 70B Versatile on your parameters.",
)

# Execute Generation
if generate_clicked:
    # Validation
    if not problem_input or len(problem_input.strip()) < 15:
        st.warning("⚠️ Please provide a sufficiently descriptive problem statement (at least 15 characters).")
        st.stop()

    groq_api_key = get_groq_api_key()
    if not groq_api_key:
        st.error(
            "🚫 **Groq API Key Not Found**\n\n"
            "To generate the investor plan, please ensure `GROQ_API_KEY` is configured in `.streamlit/secrets.toml` "
            "or enter it in the **Session Key Override** expander in the sidebar."
        )
        st.stop()

    # Import Groq SDK safely
    try:
        from groq import Groq, APIConnectionError, RateLimitError, APIStatusError, AuthenticationError
    except ImportError:
        st.error(
            "🚫 The `groq` library is not installed in the active Python environment. "
            "Please run: `pip install -r requirements.txt`"
        )
        st.stop()

    # Build Prompt
    master_prompt = construct_master_prompt(
        problem=problem_input.strip(),
        themes=selected_themes,
        keywords=keywords_input.strip(),
        market=target_market,
        model=business_model,
        stage=venture_stage,
    )

    # Execute with Streaming, Auto-Fallback & Robust Error Handling
    st.markdown("---")
    st.markdown("### ⚡ Synthesizing Plan on Groq LPU...")

    start_time = time.time()
    try:
        client = Groq(api_key=groq_api_key)

        # Candidate models prioritizing selected model
        candidate_models = [selected_model_id]
        for fallback in ["openai/gpt-oss-120b", "llama-3.1-8b-instant", "llama-3.3-70b-versatile"]:
            if fallback not in candidate_models:
                candidate_models.append(fallback)

        completion_stream = None
        active_model_used = None
        fallback_notice = None

        with st.spinner("🧠 NIC Venture Partner Persona active... Formulating 7 investor sections..."):
            for candidate in candidate_models:
                try:
                    create_params = {
                        "model": candidate,
                        "messages": [
                            {
                                "role": "system",
                                "content": (
                                    "You are the Chief Accelerator Director at the National Incubation Center (NIC) Pakistan. "
                                    "You write exhaustively detailed, commercially astute, investor-grade startup blueprints "
                                    "strictly formatted according to the 7 required sections."
                                ),
                            },
                            {
                                "role": "user",
                                "content": master_prompt,
                            },
                        ],
                        "stream": True,
                    }

                    # Exact parameters for openai/gpt-oss-120b as specified
                    if "openai" in candidate.lower() or "gpt" in candidate.lower():
                        create_params["temperature"] = 1
                        create_params["max_completion_tokens"] = 2048
                        create_params["top_p"] = 1
                        create_params["reasoning_effort"] = "medium"
                        create_params["stop"] = None
                    else:
                        create_params["temperature"] = 0.7
                        create_params["max_tokens"] = 4096

                    completion_stream = client.chat.completions.create(**create_params)
                    active_model_used = candidate
                    if candidate != selected_model_id:
                        fallback_notice = (
                            f"ℹ️ **Notice:** `{selected_model_id}` is not active on this Groq account. "
                            f"Automatically routed to **`{candidate}`**."
                        )
                    break
                except APIStatusError as api_err:
                    err_msg = str(api_err).lower()
                    if (
                        api_err.status_code in (400, 404)
                        or "model_decommissioned" in err_msg
                        or "model_not_found" in err_msg
                        or "does not exist" in err_msg
                        or "not have access" in err_msg
                    ):
                        continue
                    raise
                except Exception as ex:
                    err_msg = str(ex).lower()
                    if (
                        "model_decommissioned" in err_msg
                        or "model_not_found" in err_msg
                        or "does not exist" in err_msg
                        or "not have access" in err_msg
                    ):
                        continue
                    raise

            if not completion_stream:
                st.error("🚫 Could not connect to an active model on this Groq API key. Please check your Groq console.")
                st.stop()

            if fallback_notice:
                st.info(fallback_notice)

            # Stream response onto the page
            response_container = st.empty()
            full_content = ""

            for chunk in completion_stream:
                chunk_delta = chunk.choices[0].delta.content or ""
                full_content += chunk_delta
                response_container.markdown(full_content + " ▌")

            # Final render without cursor
            response_container.markdown(full_content)
            elapsed_time = round(time.time() - start_time, 2)

            # Save in session state for persistence across tab changes
            st.session_state["generated_plan"] = full_content
            st.session_state["plan_meta"] = {
                "problem": problem_input,
                "themes": selected_themes,
                "market": target_market,
                "model": business_model,
                "stage": venture_stage,
                "elapsed": elapsed_time,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "model_engine": active_model_used,
            }

            st.success(f"✅ **Plan generated successfully in {elapsed_time}s** using `{active_model_used}`.")

    except AuthenticationError as e:
        st.error(f"🔒 **Groq Authentication Error:** Invalid API Key provided. Please verify your key. Details: {e}")
    except RateLimitError as e:
        st.error(f"⏳ **Groq Rate Limit Exceeded:** You have hit the Groq API rate limit. Please wait a moment and retry. Details: {e}")
    except APIConnectionError as e:
        st.error(f"🌐 **Groq Network Error:** Failed to establish connection to Groq Cloud servers. Details: {e}")
    except APIStatusError as e:
        st.error(f"⚠️ **Groq Server Status Error ({e.status_code}):** {e.message}")
    except Exception as e:
        st.error(f"❌ **Unexpected Error during plan generation:** {str(e)}")


# ==============================================================================
# DISPLAY PERSISTED PLAN & ACTION TOOLS
# ==============================================================================
if "generated_plan" in st.session_state and not generate_clicked:
    plan_content = st.session_state["generated_plan"]
    meta = st.session_state.get("plan_meta", {})

    st.markdown("---")
    st.markdown("### 📋 Current Active Venture Blueprint")

    # Meta Tags Strip
    meta_cols = st.columns([3, 1])
    with meta_cols[0]:
        st.markdown(
            f"""
            <div style="margin-bottom: 16px;">
                <span class="badge-pill">📍 {meta.get('market', 'Target Market')}</span>
                <span class="badge-pill">💼 {meta.get('model', 'Business Model')}</span>
                <span class="badge-pill">🌱 {meta.get('stage', 'Stage')}</span>
                <span class="badge-pill">⚡ Generated in {meta.get('elapsed', '3.5')}s</span>
                <span class="badge-pill">🧠 {meta.get('model_engine', 'LLaMA')}</span>
                <span class="badge-pill">🕒 {meta.get('timestamp', '')}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with meta_cols[1]:
        # Extract title slug for file name
        title_match = re.search(r"## 1\. Startup Name.*?\n(?:- \*\*Suggested Startup Name:\*\*|\*\*Suggested Startup Name:\*\*|###)?\s*([A-Za-z0-9_-]+)", plan_content)
        startup_slug = title_match.group(1).strip() if title_match else "Venture_Forge"

        st.download_button(
            label="📥 Download Markdown Plan (.md)",
            data=plan_content,
            file_name=f"NIC_Venture_Plan_{startup_slug}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    # Render Document inside a styled container
    st.markdown(plan_content)

elif "generated_plan" in st.session_state and generate_clicked:
    # If just generated, show the download button
    plan_content = st.session_state["generated_plan"]
    title_match = re.search(r"## 1\. Startup Name.*?\n(?:- \*\*Suggested Startup Name:\*\*|\*\*Suggested Startup Name:\*\*|###)?\s*([A-Za-z0-9_-]+)", plan_content)
    startup_slug = title_match.group(1).strip() if title_match else "Venture_Forge"

    st.download_button(
        label="📥 Download Markdown Plan (.md)",
        data=plan_content,
        file_name=f"NIC_Venture_Plan_{startup_slug}.md",
        mime="text/markdown",
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
    </div>
    """,
    unsafe_allow_html=True,
)
