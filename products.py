"""
Organic Products Feature
Marketplace for buying and selling organic products
"""

import streamlit as st
from components import (
    product_card, modern_header, modern_footer,
    info_alert, success_alert, error_alert, empty_state
)
from translations import get_text
from database import get_all_products, search_products, add_product


def render_products_page(user: dict, lang: str = 'en'):
    """
    Render the organic products page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    modern_header(
        get_text('products', lang),
        icon="🛒"
    )
    
    # Tabs for browsing and listing products
    tab1, tab2 = st.tabs([
        get_text('browse_products', lang),
        get_text('list_product', lang)
    ])
    
    # Browse Products Tab
    with tab1:
        st.subheader(get_text('browse_products', lang))
        
        # Search functionality
        search_term = st.text_input(
            get_text('search', lang),
            placeholder="Search by product name, location, or farmer...",
            help="Enter keywords to search products"
        )
        
        st.markdown("---")
        
        try:
            if search_term:
                products = search_products(search_term)
            else:
                products = get_all_products(limit=50)
            
            if not products:
                empty_state(
                    "No products found",
                    icon="📦",
                    action_text="List a Product"
                )
            else:
                info_alert(f"Found {len(products)} product(s)")
                
                cols = st.columns(2)
                for idx, product in enumerate(products):
                    with cols[idx % 2]:
                        product_card(product, lang)
        
        except Exception as e:
            error_alert(f"Error loading products: {str(e)}")
    
    # List Product Tab
    with tab2:
        st.subheader(get_text('list_product', lang))
        
        with st.form("product_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                farmer_name = st.text_input(
                    get_text('your_name', lang),
                    value=user['farmer_name']
                )
                
                product_name = st.text_input(
                    get_text('product_name', lang),
                    placeholder="e.g., Organic Tomatoes"
                )
                
                quantity = st.text_input(
                    get_text('quantity', lang),
                    placeholder="e.g., 50 kg"
                )
            
            with col2:
                location = st.text_input(
                    get_text('location', lang),
                    value=user['location']
                )
                
                phone = st.text_input(
                    get_text('phone', lang),
                    value=user['mobile_email']
                )
            
            submitted = st.form_submit_button(
                get_text('list', lang),
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                if not all([farmer_name, product_name, quantity, location, phone]):
                    error_alert("Please fill all fields!")
                elif len(phone) < 10:
                    error_alert("Invalid phone number! Must be at least 10 digits.")
                else:
                    try:
                        product_id = add_product(
                            farmer_name,
                            product_name,
                            quantity,
                            location,
                            phone
                        )
                        
                        success_alert("✨ Product listed successfully!")
                        st.balloons()
                        st.rerun()
                    
                    except Exception as e:
                        error_alert(f"Error listing product: {str(e)}")
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_products_page']