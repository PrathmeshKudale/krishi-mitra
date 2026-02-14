"""
Modern Styling System for Krishi Mitra
Production-ready, accessible, and responsive design
Inspired by Linear, Stripe, and Apple design principles
"""

def get_custom_css():
    """
    Generate comprehensive CSS for modern, production-ready UI.
    Includes: Design system, components, animations, dark mode, and responsiveness.
    """
    return """
    <style>
        /* ========================================
           1. DESIGN SYSTEM & CSS VARIABLES
           ======================================== */
        :root {
            /* Primary Colors - Nature-inspired greens */
            --color-primary-50: #ECFDF5;
            --color-primary-100: #D1FAE5;
            --color-primary-200: #A7F3D0;
            --color-primary-300: #6EE7B7;
            --color-primary-400: #34D399;
            --color-primary-500: #10B981;
            --color-primary-600: #059669;
            --color-primary-700: #047857;
            --color-primary-800: #065F46;
            --color-primary-900: #064E3B;
            
            /* Semantic Colors */
            --color-success: #10B981;
            --color-warning: #F59E0B;
            --color-error: #EF4444;
            --color-info: #3B82F6;
            
            /* Neutral Colors */
            --color-gray-50: #F9FAFB;
            --color-gray-100: #F3F4F6;
            --color-gray-200: #E5E7EB;
            --color-gray-300: #D1D5DB;
            --color-gray-400: #9CA3AF;
            --color-gray-500: #6B7280;
            --color-gray-600: #4B5563;
            --color-gray-700: #374151;
            --color-gray-800: #1F2937;
            --color-gray-900: #111827;
            
            /* Light Mode */
            --bg-primary: #FFFFFF;
            --bg-secondary: #F9FAFB;
            --bg-tertiary: #F3F4F6;
            --text-primary: #111827;
            --text-secondary: #6B7280;
            --border-color: #E5E7EB;
            --card-bg: #FFFFFF;
            
            /* Shadows */
            --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            
            /* Border Radius */
            --radius-sm: 0.375rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            --radius-xl: 1rem;
            --radius-2xl: 1.5rem;
            --radius-full: 9999px;
            
            /* Spacing */
            --spacing-1: 0.25rem;
            --spacing-2: 0.5rem;
            --spacing-3: 0.75rem;
            --spacing-4: 1rem;
            --spacing-5: 1.25rem;
            --spacing-6: 1.5rem;
            --spacing-8: 2rem;
            --spacing-10: 2.5rem;
            --spacing-12: 3rem;
            
            /* Transitions */
            --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
            --transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1);
            --transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* ========================================
           2. DARK MODE SUPPORT
           ======================================== */
        [data-theme="dark"] {
            --bg-primary: #0F172A;
            --bg-secondary: #1E293B;
            --bg-tertiary: #334155;
            --text-primary: #F1F5F9;
            --text-secondary: #94A3B8;
            --border-color: #334155;
            --card-bg: #1E293B;
            --color-gray-50: #1E293B;
            --color-gray-100: #334155;
            --color-gray-200: #475569;
            --color-gray-300: #64748B;
            --color-gray-800: #F1F5F9;
        }
        
        /* ========================================
           3. GLOBAL RESET & BASE STYLES
           ======================================== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: var(--text-primary);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        /* Main Container */
        .stApp {
            background-color: var(--bg-secondary);
            background-image: radial-gradient(circle at 1px 1px, rgba(16, 185, 129, 0.05) 1px, transparent 0);
            background-size: 40px 40px;
        }
        
        /* ========================================
           4. TYPOGRAPHY
           ======================================== */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: var(--spacing-4);
        }
        
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.02em;
        }
        
        h2 {
            font-size: 2rem;
            line-height: 1.3;
        }
        
        h3 {
            font-size: 1.5rem;
            line-height: 1.4;
        }
        
        h4 {
            font-size: 1.25rem;
            font-weight: 600;
        }
        
        p {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: var(--spacing-4);
        }
        
        /* ========================================
           5. SIDEBAR MODERNIZATION
           ======================================== */
        [data-testid="stSidebar"] {
            background: var(--bg-primary);
            border-right: 1px solid var(--border-color);
            padding: var(--spacing-6);
        }
        
        [data-testid="stSidebar"] h2 {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--color-primary-500), var(--color-primary-600));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: var(--spacing-2);
        }
        
        /* ========================================
           6. MODERN CARDS
           ======================================== */
        .modern-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--spacing-6);
            box-shadow: var(--shadow-sm);
            transition: all var(--transition-base);
        }
        
        .modern-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateY(-4px);
            border-color: var(--color-primary-300);
        }
        
        .feature-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: var(--spacing-8);
            box-shadow: var(--shadow-sm);
            transition: all var(--transition-base);
            height: 100%;
        }
        
        .feature-card:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-8px);
            border-color: var(--color-primary-400);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: var(--spacing-4);
            display: inline-block;
            padding: var(--spacing-4);
            background: linear-gradient(135deg, var(--color-primary-100), var(--color-primary-200));
            border-radius: var(--radius-xl);
        }
        
        .feature-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: var(--spacing-3);
        }
        
        .feature-desc {
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }
        
        /* ========================================
           7. MODERN BUTTONS
           ======================================== */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, var(--color-primary-500), var(--color-primary-600));
            color: white;
            border: none;
            border-radius: var(--radius-md);
            padding: var(--spacing-3) var(--spacing-6);
            font-weight: 600;
            font-size: 1rem;
            transition: all var(--transition-base);
            box-shadow: var(--shadow-md);
        }
        
        div.stButton > button:first-child:hover {
            background: linear-gradient(135deg, var(--color-primary-600), var(--color-primary-700));
            box-shadow: var(--shadow-lg);
            transform: translateY(-2px);
        }
        
        div.stButton > button:first-child:active {
            transform: translateY(0);
        }
        
        /* Secondary Button */
        .btn-secondary {
            background: var(--bg-primary);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: var(--spacing-3) var(--spacing-6);
            font-weight: 600;
            transition: all var(--transition-base);
        }
        
        .btn-secondary:hover {
            background: var(--bg-secondary);
            border-color: var(--color-primary-400);
        }
        
        /* ========================================
           8. MODERN INPUTS & FORMS
           ======================================== */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            background: var(--bg-primary);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: var(--spacing-3) var(--spacing-4);
            font-size: 1rem;
            transition: all var(--transition-fast);
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus {
            border-color: var(--color-primary-500);
            box-shadow: 0 0 0 4px var(--color-primary-100);
            outline: none;
        }
        
        /* ========================================
           9. PRODUCT CARDS
           ======================================== */
        .product-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--spacing-6);
            position: relative;
            overflow: hidden;
            transition: all var(--transition-base);
        }
        
        .product-card:hover {
            box-shadow: var(--shadow-lg);
            border-color: var(--color-primary-300);
            transform: translateY(-4px);
        }
        
        .product-badge {
            position: absolute;
            top: var(--spacing-4);
            right: var(--spacing-4);
            background: linear-gradient(135deg, var(--color-primary-500), var(--color-primary-600));
            color: white;
            padding: var(--spacing-2) var(--spacing-3);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* ========================================
           10. SCHEME CARDS
           ======================================== */
        .scheme-card {
            background: linear-gradient(135deg, var(--color-primary-50), var(--color-primary-100));
            border: 1px solid var(--color-primary-200);
            border-radius: var(--radius-lg);
            padding: var(--spacing-6);
            transition: all var(--transition-base);
            height: 100%;
        }
        
        .scheme-card:hover {
            background: linear-gradient(135deg, var(--color-primary-100), var(--color-primary-200));
            transform: translateY(-4px);
        }
        
        /* ========================================
           11. MODERN FOOTER
           ======================================== */
        .main-footer {
            text-align: center;
            background: linear-gradient(135deg, var(--color-primary-50), var(--color-primary-100));
            padding: var(--spacing-10);
            border-radius: var(--radius-2xl);
            margin-top: var(--spacing-10);
            border: 1px solid var(--color-primary-200);
        }
        
        [data-theme="dark"] .main-footer {
            background: linear-gradient(135deg, var(--color-primary-900), var(--color-primary-800));
            border-color: var(--color-primary-700);
        }
        
        .footer-icon {
            font-size: 3rem;
            margin-bottom: var(--spacing-4);
            display: block;
        }
        
        /* ========================================
           12. CHAT INTERFACE
           ======================================== */
        .stChatMessage {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--spacing-4);
            margin: var(--spacing-4) 0;
            box-shadow: var(--shadow-sm);
        }
        
        .stChatMessage[data-testid="chat-message-assistant"] {
            background: linear-gradient(135deg, var(--color-primary-50), var(--color-primary-100));
            border-color: var(--color-primary-200);
        }
        
        /* ========================================
           13. LOADING STATES
           ======================================== */
        .loading-skeleton {
            background: linear-gradient(90deg, var(--bg-secondary) 25%, var(--bg-tertiary) 50%, var(--bg-secondary) 75%);
            background-size: 200% 100%;
            animation: skeleton-loading 1.5s infinite;
            border-radius: var(--radius-md);
        }
        
        @keyframes skeleton-loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
        
        /* ========================================
           14. EMPTY STATES
           ======================================== */
        .empty-state {
            text-align: center;
            padding: var(--spacing-12);
            color: var(--text-secondary);
        }
        
        .empty-state-icon {
            font-size: 4rem;
            margin-bottom: var(--spacing-6);
            opacity: 0.5;
        }
        
        /* ========================================
           15. RESPONSIVE DESIGN
           ======================================== */
        @media (max-width: 768px) {
            h1 { font-size: 2rem; }
            h2 { font-size: 1.75rem; }
            h3 { font-size: 1.25rem; }
            
            .feature-card {
                padding: var(--spacing-6);
            }
            
            .main-footer {
                padding: var(--spacing-8);
                margin-top: var(--spacing-8);
            }
        }
        
        @media (max-width: 640px) {
            h1 { font-size: 1.75rem; }
            h2 { font-size: 1.5rem; }
            
            .feature-card,
            .product-card {
                padding: var(--spacing-4);
            }
        }
        
        /* ========================================
           16. ACCESSIBILITY
           ======================================== */
        *:focus {
            outline: 2px solid var(--color-primary-500);
            outline-offset: 2px;
        }
        
        /* Ensure high contrast */
        a {
            color: var(--color-primary-600);
            text-decoration: none;
            font-weight: 500;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        /* ========================================
           17. ANIMATIONS
           ======================================== */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.5s ease-out;
        }
        
        .animate-slide-in {
            animation: slideIn 0.3s ease-out;
        }
        
        /* ========================================
           18. UTILITY CLASSES
           ======================================== */
        .text-center { text-align: center; }
        .text-left { text-align: left; }
        .text-right { text-align: right; }
        
        .mt-2 { margin-top: var(--spacing-2); }
        .mt-4 { margin-top: var(--spacing-4); }
        .mt-6 { margin-top: var(--spacing-6); }
        .mt-8 { margin-top: var(--spacing-8); }
        
        .mb-2 { margin-bottom: var(--spacing-2); }
        .mb-4 { margin-bottom: var(--spacing-4); }
        .mb-6 { margin-bottom: var(--spacing-6); }
        
        .p-4 { padding: var(--spacing-4); }
        .p-6 { padding: var(--spacing-6); }
        .p-8 { padding: var(--spacing-8); }
        
        /* Language Badge */
        .lang-badge {
            display: inline-block;
            padding: var(--spacing-2) var(--spacing-3);
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: var(--radius-full);
            color: white;
            background: linear-gradient(135deg, var(--color-primary-500), var(--color-primary-600));
        }
        
        /* Remove Streamlit default elements */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }
    </style>
    """
