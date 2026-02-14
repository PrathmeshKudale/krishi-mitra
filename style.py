"""
Modern GitHub-inspired styling system for Krishi Mitra
Features: Light/dark theme support, responsive design, premium UI components
"""

import streamlit as st

def load_css():
    """Load all custom CSS styles"""
    return """
    <style>
        /* ===== CSS Variables ===== */
        :root {
            /* GitHub Light Theme */
            --gh-bg-primary: #ffffff;
            --gh-bg-secondary: #f6f8fa;
            --gh-bg-tertiary: #eaeef2;
            --gh-text-primary: #24292f;
            --gh-text-secondary: #57606a;
            --gh-text-tertiary: #6e7781;
            --gh-border-primary: #d0d7de;
            --gh-border-secondary: #d8dee4;
            --gh-accent: #2da44e;
            --gh-accent-light: #e6f7e6;
            --gh-accent-dark: #1a7f37;
            --gh-danger: #cf222e;
            --gh-warning: #bf8700;
            --gh-success: #1a7f37;
            --gh-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            --gh-shadow-hover: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
            --gh-transition: all 0.2s cubic-bezier(0.3, 0, 0.5, 1);
            --gh-radius-sm: 4px;
            --gh-radius-md: 6px;
            --gh-radius-lg: 8px;
            --gh-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        }

        /* GitHub Dark Theme */
        .dark-theme {
            --gh-bg-primary: #0d1117;
            --gh-bg-secondary: #161b22;
            --gh-bg-tertiary: #21262d;
            --gh-text-primary: #c9d1d9;
            --gh-text-secondary: #8b949e;
            --gh-text-tertiary: #6e7681;
            --gh-border-primary: #30363d;
            --gh-border-secondary: #21262d;
            --gh-accent: #238636;
            --gh-accent-light: #1f6f2f;
            --gh-accent-dark: #2ea043;
            --gh-danger: #f85149;
            --gh-warning: #d29922;
            --gh-success: #3fb950;
        }

        /* ===== Global Styles ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--gh-font-family);
            background-color: var(--gh-bg-primary);
            color: var(--gh-text-primary);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .stApp {
            background-color: var(--gh-bg-primary);
        }

        /* ===== Typography ===== */
        h1, h2, h3, h4, h5, h6 {
            color: var(--gh-text-primary);
            font-weight: 600;
            margin-bottom: 1rem;
        }

        h1 {
            font-size: 2rem;
            border-bottom: 1px solid var(--gh-border-primary);
            padding-bottom: 0.5rem;
        }

        h2 {
            font-size: 1.5rem;
        }

        h3 {
            font-size: 1.25rem;
        }

        p {
            color: var(--gh-text-secondary);
            margin-bottom: 1rem;
        }

        a {
            color: var(--gh-accent);
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* ===== Navigation Bar (GitHub-style) ===== */
        .gh-header {
            background-color: var(--gh-bg-secondary);
            border-bottom: 1px solid var(--gh-border-primary);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }

        .gh-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1400px;
            margin: 0 auto;
        }

        .gh-nav-left {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }

        .gh-nav-logo {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--gh-text-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .gh-nav-links {
            display: flex;
            gap: 1rem;
        }

        .gh-nav-link {
            padding: 0.5rem 1rem;
            border-radius: var(--gh-radius-md);
            color: var(--gh-text-secondary);
            font-size: 0.9rem;
            font-weight: 500;
            transition: var(--gh-transition);
            cursor: pointer;
        }

        .gh-nav-link:hover {
            color: var(--gh-text-primary);
            background-color: var(--gh-bg-tertiary);
            text-decoration: none;
        }

        .gh-nav-link.active {
            color: var(--gh-text-primary);
            font-weight: 600;
            background-color: var(--gh-bg-tertiary);
        }

        .gh-nav-right {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        /* ===== Cards (GitHub Repository-style) ===== */
        .gh-card {
            background-color: var(--gh-bg-primary);
            border: 1px solid var(--gh-border-primary);
            border-radius: var(--gh-radius-md);
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: var(--gh-transition);
        }

        .gh-card:hover {
            border-color: var(--gh-accent);
            box-shadow: var(--gh-shadow-hover);
        }

        .gh-card-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1rem;
        }

        .gh-card-icon {
            font-size: 1.5rem;
            color: var(--gh-accent);
        }

        .gh-card-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--gh-text-primary);
        }

        .gh-card-meta {
            font-size: 0.85rem;
            color: var(--gh-text-tertiary);
            display: flex;
            gap: 1rem;
            margin-top: 0.5rem;
        }

        /* ===== Buttons (GitHub-style) ===== */
        .gh-btn, .stButton > button {
            background-color: var(--gh-bg-secondary);
            border: 1px solid var(--gh-border-primary);
            border-radius: var(--gh-radius-md);
            color: var(--gh-text-primary);
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
            font-weight: 500;
            line-height: 1.2;
            cursor: pointer;
            transition: var(--gh-transition);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .gh-btn:hover, .stButton > button:hover {
            background-color: var(--gh-bg-tertiary);
            border-color: var(--gh-border-secondary);
            transform: translateY(-1px);
        }

        .gh-btn-primary, .stButton > button[type="primary"] {
            background-color: var(--gh-accent);
            border-color: var(--gh-accent-dark);
            color: white;
        }

        .gh-btn-primary:hover, .stButton > button[type="primary"]:hover {
            background-color: var(--gh-accent-dark);
            border-color: var(--gh-accent-dark);
        }

        .gh-btn-danger {
            background-color: var(--gh-danger);
            border-color: var(--gh-danger);
            color: white;
        }

        /* ===== Inputs (GitHub-style) ===== */
        .gh-input, .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            background-color: var(--gh-bg-primary);
            border: 1px solid var(--gh-border-primary);
            border-radius: var(--gh-radius-md);
            color: var(--gh-text-primary);
            padding: 0.5rem 0.75rem;
            font-size: 0.9rem;
            width: 100%;
            transition: var(--gh-transition);
        }

        .gh-input:focus, .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: var(--gh-accent);
            outline: none;
            box-shadow: 0 0 0 3px rgba(45, 164, 78, 0.1);
        }

        .gh-input-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--gh-text-secondary);
            margin-bottom: 0.25rem;
        }

        /* ===== Tabs (GitHub-style) ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background-color: transparent;
            border-bottom: 1px solid var(--gh-border-primary);
            padding: 0;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--gh-text-secondary);
            background: transparent;
            border: none;
            border-bottom: 2px solid transparent;
        }

        .stTabs [aria-selected="true"] {
            color: var(--gh-accent);
            border-bottom-color: var(--gh-accent);
            background: transparent;
        }

        /* ===== Metrics (GitHub-style) ===== */
        .gh-metric {
            background-color: var(--gh-bg-secondary);
            border: 1px solid var(--gh-border-primary);
            border-radius: var(--gh-radius-md);
            padding: 1rem;
            text-align: center;
        }

        .gh-metric-value {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--gh-text-primary);
        }

        .gh-metric-label {
            font-size: 0.85rem;
            color: var(--gh-text-tertiary);
            margin-top: 0.25rem;
        }

        /* ===== Badges ===== */
        .gh-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.2rem 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            line-height: 1;
            border-radius: 2rem;
            background-color: var(--gh-accent-light);
            color: var(--gh-accent-dark);
            border: 1px solid var(--gh-accent);
        }

        .gh-badge-success {
            background-color: var(--gh-success);
            color: white;
            border-color: var(--gh-success);
        }

        .gh-badge-warning {
            background-color: var(--gh-warning);
            color: white;
            border-color: var(--gh-warning);
        }

        .gh-badge-danger {
            background-color: var(--gh-danger);
            color: white;
            border-color: var(--gh-danger);
        }

        /* ===== Alerts ===== */
        .gh-alert {
            padding: 1rem;
            border-radius: var(--gh-radius-md);
            border: 1px solid var(--gh-border-primary);
            background-color: var(--gh-bg-secondary);
            margin-bottom: 1rem;
        }

        .gh-alert-success {
            background-color: rgba(45, 164, 78, 0.1);
            border-color: var(--gh-accent);
            color: var(--gh-accent);
        }

        .gh-alert-error {
            background-color: rgba(207, 34, 46, 0.1);
            border-color: var(--gh-danger);
            color: var(--gh-danger);
        }

        /* ===== Loading Skeletons ===== */
        @keyframes gh-shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }

        .gh-skeleton {
            background: linear-gradient(90deg, 
                var(--gh-bg-secondary) 25%, 
                var(--gh-bg-tertiary) 50%, 
                var(--gh-bg-secondary) 75%);
            background-size: 1000px 100%;
            animation: gh-shimmer 2s infinite;
            border-radius: var(--gh-radius-md);
            height: 1rem;
            margin-bottom: 0.5rem;
        }

        /* ===== Grid Layout ===== */
        .gh-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }

        /* ===== Footer ===== */
        .gh-footer {
            background-color: var(--gh-bg-secondary);
            border-top: 1px solid var(--gh-border-primary);
            padding: 2rem;
            text-align: center;
            margin-top: 3rem;
        }

        .gh-footer-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 1rem;
            align-items: center;
        }

        .gh-footer-links {
            display: flex;
            gap: 2rem;
            justify-content: center;
        }

        .gh-footer-link {
            color: var(--gh-text-secondary);
            font-size: 0.9rem;
        }

        /* ===== Responsive Design ===== */
        @media (max-width: 768px) {
            .gh-nav {
                flex-direction: column;
                gap: 1rem;
            }

            .gh-nav-links {
                flex-wrap: wrap;
                justify-content: center;
            }

            .gh-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 1.5rem;
            }
        }

        @media (max-width: 480px) {
            .gh-header {
                padding: 1rem;
            }

            .gh-nav-left {
                flex-direction: column;
                gap: 0.5rem;
            }

            .gh-card {
                padding: 1rem;
            }
        }

        /* ===== Utility Classes ===== */
        .text-center { text-align: center; }
        .text-right { text-align: right; }
        .mt-1 { margin-top: 0.5rem; }
        .mt-2 { margin-top: 1rem; }
        .mt-3 { margin-top: 1.5rem; }
        .mb-1 { margin-bottom: 0.5rem; }
        .mb-2 { margin-bottom: 1rem; }
        .mb-3 { margin-bottom: 1.5rem; }
        .p-1 { padding: 0.5rem; }
        .p-2 { padding: 1rem; }
        .p-3 { padding: 1.5rem; }
        .flex { display: flex; }
        .flex-col { flex-direction: column; }
        .items-center { align-items: center; }
        .justify-between { justify-content: space-between; }
        .gap-1 { gap: 0.5rem; }
        .gap-2 { gap: 1rem; }
        .gap-3 { gap: 1.5rem; }

        /* ===== Streamlit Overrides ===== */
        div[data-testid="stSidebar"] {
            background-color: var(--gh-bg-secondary);
            border-right: 1px solid var(--gh-border-primary);
        }

        div[data-testid="stSidebar"] .sidebar-content {
            background-color: var(--gh-bg-secondary);
        }

        .stProgress > div > div > div > div {
            background-color: var(--gh-accent);
        }

        .stSpinner > div {
            border-color: var(--gh-accent);
        }

        hr {
            border-color: var(--gh-border-primary);
        }

        code {
            background-color: var(--gh-bg-tertiary);
            color: var(--gh-text-primary);
            border-radius: var(--gh-radius-sm);
            padding: 0.2rem 0.4rem;
        }

        /* ===== Animations ===== */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-in {
            animation: fadeIn 0.3s ease-out;
        }

        /* ===== Custom Scrollbar ===== */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--gh-bg-secondary);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--gh-border-primary);
            border-radius: var(--gh-radius-md);
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--gh-text-tertiary);
        }

        /* ===== Print Styles ===== */
        @media print {
            .gh-header, .gh-footer, .stButton {
                display: none;
            }
        }
    </style>
    """

def init_theme():
    """Initialize theme based on session state"""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    
    # Apply theme class to body
    if st.session_state.dark_mode:
        st.markdown('<script>document.body.classList.add("dark-theme");</script>', unsafe_allow_html=True)

def theme_toggle():
    """Render theme toggle button"""
    icon = "🌙" if not st.session_state.dark_mode else "☀️"
    if st.button(icon, key="theme_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

def gh_header(title="Krishi Mitra", show_theme_toggle=True):
    """Render GitHub-style header"""
    with st.container():
        st.markdown(f'''
        <div class="gh-header">
            <div class="gh-nav">
                <div class="gh-nav-left">
                    <div class="gh-nav-logo">
                        <span>🌾</span>
                        <span>{title}</span>
                    </div>
                    <div class="gh-nav-links">
                        <a class="gh-nav-link active">Home</a>
                        <a class="gh-nav-link">Assistant</a>
                        <a class="gh-nav-link">Diagnosis</a>
                        <a class="gh-nav-link">Community</a>
                    </div>
                </div>
                <div class="gh-nav-right">
                    {f'<button class="gh-btn" onclick="toggleTheme()">{"🌙" if not st.session_state.dark_mode else "☀️"}</button>' if show_theme_toggle else ''}
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

def gh_card(content, title=None, icon=None, meta=None):
    """Render GitHub-style card"""
    meta_html = f'<div class="gh-card-meta">{meta}</div>' if meta else ''
    title_html = f'<div class="gh-card-header"><span class="gh-card-icon">{icon}</span><span class="gh-card-title">{title}</span></div>' if title else ''
    
    st.markdown(f'''
    <div class="gh-card">
        {title_html}
        <div>{content}</div>
        {meta_html}
    </div>
    ''', unsafe_allow_html=True)

def gh_metric(value, label, delta=None):
    """Render GitHub-style metric"""
    delta_html = f'<div style="font-size:0.8rem; color:{ "var(--gh-success)" if delta and delta>0 else "var(--gh-danger)" };">{delta}</div>' if delta else ''
    st.markdown(f'''
    <div class="gh-metric">
        <div class="gh-metric-value">{value}</div>
        <div class="gh-metric-label">{label}</div>
        {delta_html}
    </div>
    ''', unsafe_allow_html=True)

def gh_alert(message, type="info"):
    """Render GitHub-style alert"""
    type_class = f"gh-alert-{type}" if type in ["success", "error", "warning"] else ""
    st.markdown(f'<div class="gh-alert {type_class}">{message}</div>', unsafe_allow_html=True)

def gh_badge(text, type="default"):
    """Render GitHub-style badge"""
    type_class = f"gh-badge-{type}" if type in ["success", "warning", "danger"] else ""
    st.markdown(f'<span class="gh-badge {type_class}">{text}</span>', unsafe_allow_html=True)

def gh_skeleton(lines=3):
    """Render GitHub-style loading skeleton"""
    for _ in range(lines):
        st.markdown('<div class="gh-skeleton"></div>', unsafe_allow_html=True)

def gh_footer():
    """Render GitHub-style footer"""
    st.markdown('''
    <div class="gh-footer">
        <div class="gh-footer-content">
            <div>🌾 Krishi Mitra</div>
            <div class="gh-footer-links">
                <a class="gh-footer-link" href="#">About</a>
                <a class="gh-footer-link" href="#">Privacy</a>
                <a class="gh-footer-link" href="#">Terms</a>
                <a class="gh-footer-link" href="#">Contact</a>
            </div>
            <div style="color: var(--gh-text-tertiary); font-size: 0.8rem;">
                © 2026 Krishi Mitra. All rights reserved.
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

def gh_grid(items, cols=3):
    """Render GitHub-style grid"""
    html = '<div class="gh-grid">'
    for item in items:
        html += f'<div class="gh-card">{item}</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
