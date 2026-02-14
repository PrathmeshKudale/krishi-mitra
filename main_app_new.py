"""
🌱 Krishi Mitra - Modern Main Application
Refactored with modular architecture and modern UI
"""

import streamlit as st
from styles_new import get_custom_css
from components import language_selector, modern_footer
from translations import get_text
from features import (
    render_home_page,
    render_ai_assistant_page,
    render_crop_diagnosis_page,
    render_crop_knowledge_page,
    render_community_page,
    render_schemes_page,
    render_products_page
)


def run_main_app(user: dict):
    """
    Run main application with all features using modular architecture.
    
    Args:
        user: User dictionary with user information
    """
    # Inject Modern CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Get or initialize selected language
    selected_lang = st.session_state.get('selected_language', 'en')
    
    # ============================================================================
    # SIDEBAR NAVIGATION
    # ============================================================================
    st.sidebar.markdown(f"## 🌱 Krishi Mitra")
    st.sidebar.markdown("*Your Intelligent Farming Companion*")
    st.sidebar.markdown("---")
    
    # Navigation options with translated labels
    page_options = [
        get_text('home', selected_lang),
        get_text('ai_assistant', selected_lang),
        get_text('crop_diagnosis', selected_lang),
        get_text('crop_knowledge', selected_lang),
        get_text('community', selected_lang),
        get_text('schemes', selected_lang),
        get_text('products', selected_lang)
    ]
    
    # Page selection
    page = st.sidebar.radio(
        get_text('select_feature', selected_lang),
        options=page_options,
        label_visibility="collapsed"
    )
    
    # Language selector in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌐 Language / भाषा")
    
    def on_language_change(lang):
        st.session_state['selected_language'] = lang
        st.rerun()
    
    selected_lang = language_selector(
        current_lang=selected_lang,
        on_change=on_language_change,
        label=""
    )
    
    st.sidebar.markdown("---")
    
    # User info in sidebar
    st.sidebar.markdown("### 👤 User")
    st.sidebar.markdown(f"**{user['farmer_name']}**")
    st.sidebar.markdown(f"📍 {user['location']}")
    
    # ============================================================================
    # PAGE ROUTING
    # ============================================================================
    
    if page == get_text('home', selected_lang):
        render_home_page(user, selected_lang)
    
    elif page == get_text('ai_assistant', selected_lang):
        render_ai_assistant_page(user, selected_lang)
    
    elif page == get_text('crop_diagnosis', selected_lang):
        render_crop_diagnosis_page(user, selected_lang)
    
    elif page == get_text('crop_knowledge', selected_lang):
        render_crop_knowledge_page(user, selected_lang)
    
    elif page == get_text('community', selected_lang):
        render_community_page(user, selected_lang)
    
    elif page == get_text('schemes', selected_lang):
        render_schemes_page(user, selected_lang)
    
    elif page == get_text('products', selected_lang):
        render_products_page(user, selected_lang)


__all__ = ['run_main_app']
