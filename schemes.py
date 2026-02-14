"""
Government Schemes Feature
Information about agricultural government schemes
"""

import streamlit as st
from components import (
    modern_header, modern_footer, scheme_card,
    info_alert, success_alert, error_alert, empty_state
)
from translations import get_text
from ai_service import get_ai_service


def render_schemes_page(user: dict, lang: str = 'en'):
    """
    Render the government schemes page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    ai_service = get_ai_service()
    
    modern_header(
        get_text('schemes', lang),
        icon="🏛️"
    )
    
    # Scheme search
    col1, col2 = st.columns([2, 1])
    
    with col1:
        scheme_query = st.text_input(
            get_text('ask_scheme', lang),
            placeholder="e.g., PM-KISAN, Soil Health Card, KCC...",
            help="Enter scheme name or keyword"
        )
    
    with col2:
        search_btn = st.button(
            get_text('search', lang),
            type="primary",
            use_container_width=True
        )
    
    # Search and display scheme info
    if search_btn and scheme_query:
        with st.spinner("🏛️ Fetching scheme information..."):
            try:
                info = ai_service.get_government_scheme_info(scheme_query, lang)
                
                st.markdown("---")
                
                # Display scheme info with modern styling
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #FEF3C7, #FDE68A);
                    border: 1px solid #FCD34D;
                    border-radius: 1rem;
                    padding: 2rem;
                    line-height: 1.7;
                ">
                    <h2 style="color: #B45309; margin-bottom: 1rem;">
                        📋 {scheme_query.upper()}
                    </h2>
                    {info}
                </div>
                """, unsafe_allow_html=True)
                
                success_alert("✨ Scheme information retrieved!")
            
            except Exception as e:
                error_alert(f"Error fetching scheme info: {str(e)}")
    
    st.markdown("---")
    
    # Popular Schemes
    st.subheader(get_text('popular_schemes', lang))
    
    schemes = [
        ("PM-KISAN", "Pradhan Mantri Kisan Samman Nidhi"),
        ("Soil Health Card", "Free soil testing"),
        ("KCC", "Kisan Credit Card"),
        ("PMFBY", "Crop Insurance"),
        ("MIDH", "Horticulture Mission"),
        ("NMOOP", "Oilseeds Mission")
    ]
    
    cols = st.columns(3)
    for idx, (short_name, full_name) in enumerate(schemes):
        with cols[idx % 3]:
            scheme_card(
                short_name=short_name,
                full_name=full_name,
                key=f"scheme_{idx}"
            )
            
            if st.button(f"🔍 {short_name}", key=f"search_{idx}"):
                st.session_state.scheme_query = short_name
                st.rerun()
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_schemes_page']