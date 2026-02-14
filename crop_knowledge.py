"""
Crop Knowledge Feature
Comprehensive crop information and lifecycle details
"""

import streamlit as st
from components import (
    modern_header, modern_footer, loading_skeleton,
    info_alert, success_alert, error_alert, empty_state
)
from translations import get_text
from ai_service import get_ai_service


def render_crop_knowledge_page(user: dict, lang: str = 'en'):
    """
    Render the crop knowledge page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    ai_service = get_ai_service()
    
    modern_header(
        get_text('crop_knowledge', lang),
        icon="📚"
    )
    
    info_alert("Enter a crop name to get comprehensive information about its lifecycle, care, and best practices")
    
    # Crop name input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        crop_name = st.text_input(
            get_text('enter_crop', lang),
            placeholder="e.g., Wheat, Rice, Cotton, Tomato...",
            help="Enter the common name of the crop"
        )
    
    with col2:
        generate_btn = st.button(
            get_text('generate', lang),
            type="primary",
            use_container_width=True
        )
    
    # Display crop knowledge
    if generate_btn and crop_name:
        # Show loading state
        with st.spinner("🌱 Generating crop knowledge..."):
            loading_skeleton("25px", 5)
            
            try:
                # Get crop knowledge from AI
                knowledge = ai_service.generate_crop_knowledge(crop_name, lang)
                
                st.markdown("---")
                
                # Display knowledge with modern styling
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #F0F9FF, #E0F2FE);
                    border: 1px solid #BAE6FD;
                    border-radius: 1rem;
                    padding: 2rem;
                    line-height: 1.7;
                ">
                    <h2 style="color: #0369A1; margin-bottom: 1rem;">
                        🌾 {crop_name.title()} - Complete Guide
                    </h2>
                    {knowledge}
                </div>
                """, unsafe_allow_html=True)
                
                success_alert(f"✨ Successfully generated knowledge for {crop_name.title()}!")
            
            except Exception as e:
                error_alert(f"Error generating knowledge: {str(e)}")
    
    elif not crop_name:
        empty_state(
            "No crop selected yet",
            icon="🌱",
            action_text="Enter a crop name to get started"
        )
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_crop_knowledge_page']