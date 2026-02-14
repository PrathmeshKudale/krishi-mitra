"""
Crop Disease Diagnosis Feature
AI-powered crop disease detection from images
"""

import streamlit as st
from PIL import Image
from components import (
    modern_header, modern_footer, loading_skeleton,
    info_alert, success_alert, error_alert, empty_state
)
from translations import get_text
from ai_service import get_ai_service
from utils import validate_image, compress_image


def render_crop_diagnosis_page(user: dict, lang: str = 'en'):
    """
    Render the crop diagnosis page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    ai_service = get_ai_service()
    
    modern_header(
        get_text('crop_diagnosis', lang),
        icon="📷"
    )
    
    info_alert("Upload a clear photo of your crop for AI-powered disease detection")
    
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(get_text('upload_image', lang))
        
        uploaded_file = st.file_uploader(
            "Choose image",
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear, well-lit photo of the affected crop"
        )
        
        additional_context = st.text_area(
            "Additional info (optional)",
            placeholder="Describe symptoms, when you noticed them, etc.",
            help="Add any relevant details to improve accuracy"
        )
        
        analyze_btn = st.button(
            get_text('analyze', lang),
            type="primary",
            use_container_width=True
        )
    
    with col2:
        st.subheader(get_text('preview', lang))
        
        if uploaded_file:
            is_valid, msg = validate_image(uploaded_file)
            
            if is_valid:
                try:
                    image = Image.open(uploaded_file)
                    st.image(image, use_column_width=True, caption="Uploaded image")
                except Exception as e:
                    error_alert(f"Error displaying image: {str(e)}")
            else:
                error_alert(msg)
        else:
            empty_state(
                "No image uploaded yet",
                icon="📷",
                action_text="Upload an image to get started"
            )
    
    # Process analysis
    if analyze_btn and uploaded_file:
        is_valid, msg = validate_image(uploaded_file)
        
        if not is_valid:
            error_alert(msg)
        else:
            # Show loading state
            with st.spinner("🔬 Analyzing crop image..."):
                loading_skeleton("30px", 4)
                
                try:
                    # Compress image for AI processing
                    compressed_image = compress_image(uploaded_file)
                    
                    if compressed_image:
                        # Get AI analysis
                        analysis = ai_service.analyze_crop_image(
                            compressed_image,
                            additional_context,
                            lang
                        )
                        
                        st.markdown("---")
                        st.subheader(get_text('analysis_report', lang))
                        
                        # Display analysis with formatted styling
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
                            border: 1px solid #A7F3D0;
                            border-radius: 1rem;
                            padding: 2rem;
                            line-height: 1.6;
                        ">
                            {analysis}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        success_alert("✨ Analysis complete!")
                    else:
                        error_alert("Failed to process image. Please try again.")
                
                except Exception as e:
                    error_alert(f"Analysis error: {str(e)}")
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_crop_diagnosis_page']