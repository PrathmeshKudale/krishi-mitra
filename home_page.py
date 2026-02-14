"""
Home Page Feature
Dashboard and platform overview
"""

import streamlit as st
from database import get_all_posts, get_all_products
from config import SUPPORTED_LANGUAGES
from components import (
    modern_card, stat_card, modern_header, modern_footer,
    empty_state
)
from translations import get_text


def render_home_page(user: dict, lang: str = 'en'):
    """
    Render the home page with dashboard and overview.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    modern_header(
        get_text('home', lang),
        f"{get_text('welcome', lang)}, {user['farmer_name']}!",
        "🌱"
    )
    
    st.markdown("---")
    
    # User Guide Section
    st.subheader(get_text('user_guide', lang))
    st.markdown(f"**{get_text('how_to_use', lang)}**")
    
    guide_steps = [
        get_text('feature_1', lang),
        get_text('feature_2', lang),
        get_text('feature_3', lang),
        get_text('feature_4', lang),
        get_text('feature_5', lang),
        get_text('feature_6', lang),
    ]
    
    for idx, step in enumerate(guide_steps, 1):
        st.markdown(f"{idx}. {step}")
    
    st.markdown("---")
    
    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        modern_card(
            title=get_text('ai_assistant', lang).split(' ')[1],
            content=get_text('ask_question', lang),
            icon="🤖",
            key="feature_ai"
        )
    
    with col2:
        modern_card(
            title=get_text('crop_diagnosis', lang).split(' ')[1],
            content=get_text('upload_image', lang),
            icon="📷",
            key="feature_diagnosis"
        )
    
    with col3:
        modern_card(
            title=get_text('community', lang).split(' ')[1],
            content=get_text('share_experience', lang),
            icon="👥",
            key="feature_community"
        )
    
    st.markdown("---")
    
    # Platform Statistics
    st.subheader(get_text('platform_overview', lang))
    
    col1, col2, col3 = st.columns(3)
    
    try:
        posts = get_all_posts(limit=1000)
        products = get_all_products(limit=1000)
        
        with col1:
            stat_card(
                label=get_text('community', lang).split(' ')[1],
                value=len(posts),
                icon="👥",
                color="primary"
            )
        
        with col2:
            stat_card(
                label=get_text('products', lang).split(' ')[1],
                value=len(products),
                icon="🛒",
                color="secondary"
            )
        
        with col3:
            stat_card(
                label=get_text('language', lang),
                value=len(SUPPORTED_LANGUAGES),
                icon="🌐",
                color="accent"
            )
    
    except Exception as e:
        error_alert(f"Error loading statistics: {str(e)}")
    
    st.markdown("---")
    
    # Footer
    modern_footer()


__all__ = ['render_home_page']