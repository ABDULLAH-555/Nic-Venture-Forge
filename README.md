# 🚀 NIC Venture Forge

> **An Investor-Grade Generative AI Startup Plan Generator for the National Incubation Center (NIC)**  
> *Developed by Abdullah Khalid Khan | Designed for National Incubation Center*

[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Groq LPU](https://img.shields.io/badge/Groq-LLaMA%203.3%2070B-F05A28?style=for-the-badge&logo=fastapi&logoColor=white)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-0D5C46?style=for-the-badge)](LICENSE)

---

## 📌 Executive Overview

**NIC Venture Forge** is a production-grade Generative AI accelerator tool engineered specifically for the **National Incubation Center (NIC)** ecosystem in Pakistan (Islamabad, Karachi, Lahore, Peshawar, Quetta).

Aspiring student entrepreneurs and early-stage founders often have powerful, authentic grassroots insights—such as agricultural post-harvest spoilage in Punjab, informal retail khata debt in Karachi, or rural maternal healthcare gaps in KP—but lack the venture design vocabulary to frame them into venture-capital-ready propositions.

NIC Venture Forge bridges this gap. By leveraging the **Groq LPU™ Inference Engine** running **LLaMA 3.3 70B Versatile**, the application turns high-level problem statements, sector tags, and tech angles into an exhaustive, 7-part investor-grade startup blueprint in under 5 seconds.

---

## 🏛️ Key Features

- **Native Multi-Page Streamlit Routing:** Clean separation between the Brand Landing Page (`app.py`) and the Interactive Venture Forge (`pages/1_🚀_Idea_Generator.py`).
- **NIC Pakistan Visual Identity:** Custom CSS design system inspired by the National Incubation Center branding (deep emerald green `#0D5C46`, tech mint `#10B981`, slate typography, and modern responsive cards).
- **Sub-5-Second Inference via Groq LPU:** Leverages Groq's high-throughput Language Processing Units running Meta's flagship `llama-3.3-70b-versatile` model.
- **Production Secrets Architecture:** Strict adherence to zero-hardcoded-credentials. Securely reads `st.secrets["GROQ_API_KEY"]` with graceful UI telemetry and error handling.
- **7-Part Investor-Grade Blueprint:**
  1. **Startup Name & Punchy Tagline** (Brand architecture and positioning)
  2. **Executive Summary & Core Insight** (Unfair advantage, "Why Now?", TAM/SAM/SOM)
  3. **Target Customer & Problem Persona** (Quantified pain points, willingness to pay)
  4. **Minimum Viable Product (MVP) Scope** (6-week roadmap from sprint 1 to beta launch)
  5. **Monetization & Business Model** (Pricing, unit economics, CAC, ARPU, LTV:CAC)
  6. **90-Day Go-To-Market (GTM) Strategy** (Guerilla distribution, pilot partnerships)
  7. **60-Second NIC Elevator Pitch Deck Script** (Demo Day script formatted for judges)
- **One-Click Markdown Export:** Download the generated strategy document as a clean `.md` file for immediate use in pitch decks and grant proposals.
- **Pre-Engineered Cohort Presets:** 1-click preset buttons (AgriTech Punjab, FinTech Retail, HealthTech Voice) for immediate evaluation without typing.

---

## 📂 Repository File Structure

```text
nic-venture-forge/
├── .streamlit/
│   ├── config.toml           # NIC brand theme colors and server settings
│   └── secrets.toml          # Local secrets (Groq API key) - Ignored by Git
├── pages/
│   └── 1_🚀_Idea_Generator.py # Interactive idea generator & Groq API runner
├── .gitignore                # Protects secrets.toml from being committed
├── app.py                    # Landing page with NIC hero, value cards & routing
├── requirements.txt          # Pinned, tested production dependencies
└── README.md                 # Complete system documentation
```

---

## 🛠️ Local Installation & Setup

Follow these steps to run NIC Venture Forge on your local machine:

### 1. Prerequisites
- Python 3.9, 3.10, 3.11, or 3.12 installed.
- A free Groq Cloud API Key (obtainable at [console.groq.com/keys](https://console.groq.com/keys)).

### 2. Clone or Navigate to the Workspace
```bash
git clone <your-repository-url>
cd nic-venture-forge
```

### 3. Create and Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Your Local Secrets
Create or edit the `.streamlit/secrets.toml` file in the project root:
```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
```
> ⚠️ **Security Warning:** The `.gitignore` file is pre-configured to ensure `.streamlit/secrets.toml` is never committed to GitHub. Never share or push your live API keys!

### 6. Launch the Application
```bash
streamlit run app.py
```
The application will launch automatically in your default browser at `http://localhost:8501`.

---

## ☁️ Streamlit Community Cloud Deployment Guide

Deploying NIC Venture Forge to Streamlit Community Cloud is straightforward and secure:

### Step 1: Push Code to GitHub
1. Initialize Git (if not already done) and push to a private or public GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "feat: complete production release of NIC Venture Forge"
   git branch -M main
   git remote add origin https://github.com/<your-username>/nic-venture-forge.git
   git push -u origin main
   ```
2. Verify on GitHub that `.streamlit/secrets.toml` is **NOT** present in the repository (safeguarded by `.gitignore`).

### Step 2: Deploy on Streamlit Cloud
1. Navigate to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **"Create app"** (or **"New app"**).
3. Select your repository: `<your-username>/nic-venture-forge`.
4. Set the **Main file path** to: `app.py`.
5. Click **"Advanced settings..."** before deploying.

### Step 3: Configure Cloud Secrets
In the **Secrets** text area within Advanced Settings, paste your production Groq API key:
```toml
GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
```
6. Click **Save** and then **Deploy!**

Your live, production-grade application will be live at `https://<your-app-name>.streamlit.app` with fully encrypted secrets.

---

## 🧠 Master Prompt & Architecture

NIC Venture Forge uses a specialized system prompt calibrated to the **National Incubation Center Selection Rubric**:

```
Role: Chief Accelerator Director & Managing Partner, National Incubation Center (NIC)
Model: llama-3.3-70b-versatile
Inference: Groq LPUs (~280 tokens/sec)
Structure: Strict 7-Section Investor Blueprint
```

### Exception & Fail-Safe Architecture
- `groq.AuthenticationError`: Detects invalid keys and renders intuitive troubleshooting guidance.
- `groq.RateLimitError`: Warns the user gracefully with cool-down recommendations.
- `groq.APIConnectionError`: Catches network dropouts with retry advice.
- `model_not_found (404)` Auto-Failover: If `llama-3.3-70b-versatile` is restricted or unprovisioned on a specific Groq account tier, the system automatically routes to high-availability `llama-3.1-8b-instant` without crashing.
- Missing Key Telemetry: Side-panel status indicator shows connection state and provides a session-level override input for live evaluation.

---

## 👨‍💻 Developer & Attribution

- **Lead Engineer:** Abdullah Khalid Khan
- **Client Organization:** National Incubation Center (NIC)
- **Engine:** Groq LPU™ Cloud + Meta LLaMA 3.3 70B Versatile
- **Framework:** Streamlit (Python 3)

---

*NIC Venture Forge &bull; Developed by Abdullah Khalid Khan | Designed for National Incubation Center*
