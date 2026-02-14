"""
AI Farming Assistant Feature
Chat-based AI assistance for farming questions
"""

import streamlit as st
from components import (
    chat_message, loading_skeleton, modern_header, modern_footer,
    info_alert, success_alert, error_alert
)
from translations import get_text, get_supported_languages
from ai_service import get_ai_service


def render_ai_assistant_page(user: dict, lang: str = 'en'):
    """
    Render the AI farming assistant page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    ai_service = get_ai_service()
    
    modern_header(
        get_text('ai_assistant', lang),
        icon="🤖"
    )
    
    # Language indicator
    info_alert(
        f"🌐 {get_text('language', lang)}: **{get_supported_languages().get(lang, 'English')}**"
    )
    st.markdown(get_text('ask_question', lang))
    
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for idx, message in enumerate(st.session_state.chat_history):
        chat_message(
            role=message["role"],
            content=message["content"],
            language=message.get("language"),
            key=f"chat_{idx}"
        )
    
    # Chat input
    user_query = st.chat_input(get_text('type_here', lang))
    
    if user_query:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_query
        })
        
        # Display user message
        chat_message(role="user", content=user_query)
        
        # Show loading state
        with st.spinner("🤖 Thinking..."):
            loading_skeleton("20px", 3)
            
            try:
                # Get AI response
                response = ai_service.get_farming_response(user_query, lang)
                
                # Add assistant response to history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response,
                    "language": lang
                })
                
                # Display assistant response
                chat_message(
                    role="assistant",
                    content=response,
                    language=lang
                )
                
                success_alert("✨ Response generated successfully!")
            
            except Exception as e:
                error_alert(f"Error: {str(e)}")
    
    st.markdown("---")
    
    # Quick Questions
    st.subheader(get_text('quick_questions', lang))
    
    quick_questions = {
        'en': [
            "How to control aphids?",
            "Best fertilizer for rice",
            "Organic pest control",
            "Water management"
        ],
        'mr': [
            "अ‍ॅफिड्स कसे नियंत्रित करावे?",
            "भातासाठी सर्वोत्तम खत",
            "सेंद्रिय किटक नियंत्रण",
            "पाणी व्यवस्थापन"
        ],
        'hi': [
            "एफिड्स को कैसे नियंत्रित करें?",
            "चावल के लिए उर्वरक",
            "जैविक कीट नियंत्रण",
            "जल प्रबंधन"
        ]
    }
    
    questions = quick_questions.get(lang, quick_questions['en'])
    
    cols = st.columns(len(questions))
    for idx, question in enumerate(questions):
        with cols[idx]:
            if st.button(question[:15] + "...", key=f"quick_{idx}"):
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": question
                })
                st.rerun()
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_ai_assistant_page']