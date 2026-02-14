"""
Reusable UI Components for Krishi Mitra
Modern, accessible, and production-ready components
"""

import streamlit as st
from typing import Optional, Callable, List, Dict, Any


def modern_card(
    title: str,
    content: str,
    icon: str = "",
    on_click: Optional[Callable] = None,
    key: str = "card"
):
    """
    Render a modern, interactive card component.
    
    Args:
        title: Card title
        content: Card description/content
        icon: Emoji icon
        on_click: Optional callback function
        key: Unique key for the component
    """
    with st.container():
        st.markdown(f"""
        <div class="feature-card" style="cursor: pointer;">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{content}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if on_click:
            if st.button("", key=f"{key}_btn"):
                on_click()


def stat_card(
    label: str,
    value: int,
    icon: str = "",
    color: str = "primary"
):
    """
    Render a modern statistics card.
    
    Args:
        label: Stat label
        value: Stat value
        icon: Emoji icon
        color: Color theme (primary, secondary, accent)
    """
    color_map = {
        "primary": "linear-gradient(135deg, #10B981, #059669)",
        "secondary": "linear-gradient(135deg, #6366F1, #4F46E5)",
        "accent": "linear-gradient(135deg, #F59E0B, #D97706)",
    }
    
    background = color_map.get(color, color_map["primary"])
    
    st.markdown(f"""
    <div style="
        background: {background};
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    ">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 2rem; font-weight: 700;">{value}</div>
        <div style="font-size: 1rem; opacity: 0.9;">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def product_card(
    product: Dict[str, Any],
    lang: str = 'en'
):
    """
    Render a product listing card.
    
    Args:
        product: Product dictionary with details
        lang: Language code
    """
    from translations import get_text
    
    st.markdown(f"""
    <div class="product-card">
        <span class="product-badge">Organic</span>
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">🛒 {product['product_name']}</h3>
        <p><strong>Farmer:</strong> {product['farmer_name']}</p>
        <p><strong>{get_text('quantity', lang)}:</strong> {product['quantity']}</p>
        <p><strong>{get_text('location', lang)}:</strong> 📍 {product['location']}</p>
        <p><strong>{get_text('phone', lang)}:</strong> 📞 {product['phone_number']}</p>
    </div>
    """, unsafe_allow_html=True)


def scheme_card(
    short_name: str,
    full_name: str,
    on_click: Optional[Callable] = None,
    key: str = "scheme"
):
    """
    Render a government scheme card.
    
    Args:
        short_name: Scheme short name
        full_name: Scheme full description
        on_click: Optional callback
        key: Unique key
    """
    st.markdown(f"""
    <div class="scheme-card">
        <h4 style="font-size: 1.125rem; margin-bottom: 0.5rem;">{short_name}</h4>
        <p style="margin-bottom: 0;">{full_name}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if on_click:
        if st.button("", key=f"{key}_btn", help="Learn more"):
            on_click()


def empty_state(
    message: str,
    icon: str = "📭",
    action_text: Optional[str] = None,
    on_action: Optional[Callable] = None
):
    """
    Render an empty state component.
    
    Args:
        message: Empty state message
        icon: Emoji icon
        action_text: Optional CTA button text
        on_action: Optional callback for CTA
    """
    st.markdown(f"""
    <div class="empty-state">
        <div class="empty-state-icon">{icon}</div>
        <p style="font-size: 1.125rem; color: var(--text-secondary);">{message}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if action_text and on_action:
        if st.button(action_text):
            on_action()


def loading_skeleton(height: str = "100px", count: int = 1):
    """
    Render loading skeleton placeholders.
    
    Args:
        height: Height of each skeleton
        count: Number of skeletons to render
    """
    for _ in range(count):
        st.markdown(f"""
        <div class="loading-skeleton" style="height: {height}; margin-bottom: 1rem;"></div>
        """, unsafe_allow_html=True)


def chat_message(
    role: str,
    content: str,
    language: Optional[str] = None,
    timestamp: Optional[str] = None
):
    """
    Render a modern chat message.
    
    Args:
        role: 'user' or 'assistant'
        content: Message content
        language: Optional language indicator
        timestamp: Optional timestamp
    """
    icon = "👤" if role == "user" else "🤖"
    
    with st.chat_message(role):
        st.write(content)
        
        if language:
            from translations import get_text
            st.caption(f"{get_text('language', 'en')}: {language}")
        
        if timestamp:
            st.caption(f"⏰ {timestamp}")


def modern_form(
    fields: List[Dict[str, Any]],
    submit_button_text: str = "Submit",
    on_submit: Optional[Callable] = None
) -> Dict[str, Any]:
    """
    Render a modern form with multiple fields.
    
    Args:
        fields: List of field dictionaries with keys: name, label, type, placeholder, options
        submit_button_text: Submit button text
        on_submit: Callback function
    
    Returns:
        Dictionary of form values
    """
    form_data = {}
    
    with st.form("modern_form"):
        for field in fields:
            field_name = field.get("name")
            field_label = field.get("label")
            field_type = field.get("type", "text")
            placeholder = field.get("placeholder", "")
            options = field.get("options", [])
            default = field.get("default", "")
            
            if field_type == "text":
                form_data[field_name] = st.text_input(
                    field_label,
                    value=default,
                    placeholder=placeholder,
                    key=f"form_{field_name}"
                )
            elif field_type == "textarea":
                form_data[field_name] = st.text_area(
                    field_label,
                    value=default,
                    placeholder=placeholder,
                    key=f"form_{field_name}"
                )
            elif field_type == "select":
                form_data[field_name] = st.selectbox(
                    field_label,
                    options=options,
                    index=0 if not default else options.index(default) if default in options else 0,
                    key=f"form_{field_name}"
                )
            elif field_type == "file_uploader":
                form_data[field_name] = st.file_uploader(
                    field_label,
                    type=field.get("file_types", []),
                    key=f"form_{field_name}"
                )
        
        submitted = st.button(
            submit_button_text,
            type="primary",
            use_container_width=True
        )
        
        if submitted and on_submit:
            on_submit(form_data)
    
    return form_data if submitted else {}


def info_alert(message: str, icon: str = "ℹ️"):
    """
    Render an informational alert.
    
    Args:
        message: Alert message
        icon: Emoji icon
    """
    st.info(f"{icon} {message}")


def success_alert(message: str, icon: str = "✅"):
    """
    Render a success alert.
    
    Args:
        message: Success message
        icon: Emoji icon
    """
    st.success(f"{icon} {message}")


def warning_alert(message: str, icon: str = "⚠️"):
    """
    Render a warning alert.
    
    Args:
        message: Warning message
        icon: Emoji icon
    """
    st.warning(f"{icon} {message}")


def error_alert(message: str, icon: str = "❌"):
    """
    Render an error alert.
    
    Args:
        message: Error message
        icon: Emoji icon
    """
    st.error(f"{icon} {message}")


def language_selector(
    current_lang: str,
    on_change: Optional[Callable] = None,
    label: str = "🌐 Language / भाषा / भाषा"
):
    """
    Render a modern language selector dropdown.
    
    Args:
        current_lang: Current selected language code
        on_change: Callback when language changes
        label: Selector label
    """
    from translations import get_supported_languages
    
    languages = get_supported_languages()
    
    selected = st.selectbox(
        label,
        options=list(languages.keys()),
        format_func=lambda x: languages[x],
        index=list(languages.keys()).index(current_lang),
        key="language_selector"
    )
    
    if selected != current_lang and on_change:
        on_change(selected)
    
    return selected


def modern_header(
    title: str,
    subtitle: Optional[str] = None,
    icon: str = ""
):
    """
    Render a modern page header.
    
    Args:
        title: Page title
        subtitle: Optional subtitle
        icon: Optional icon
    """
    if icon:
        title = f"{icon} {title}"
    
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
    
    if subtitle:
        st.markdown(f"<h3 style='text-align: center;'>{subtitle}</h3>", unsafe_allow_html=True)


def modern_footer():
    """Render a modern footer component."""
    from translations import TRANSLATIONS
    
    # Get current language from session state
    lang = st.session_state.get('selected_language', 'en')
    ft = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    
    st.markdown("---")
    st.markdown("---")
    st.markdown(f"""
    <div class="main-footer">
        <div class="footer-icon">🌱</div>
        <div style="font-size: 1.25rem; font-weight: bold; color: var(--text-primary); margin-bottom: 0.5rem;">
            Krishi Mitra
        </div>
        <div style="font-size: 1rem; color: var(--color-primary-600); margin-bottom: 0.5rem;">
            {ft['tagline']}
        </div>
        <div style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1rem;">
            {ft['made_with_love']}
        </div>
        <div style="font-size: 0.8rem; color: var(--color-gray-500); border-top: 1px solid var(--color-primary-200); padding-top: 1rem;">
            {ft['copyright']}
        </div>
    </div>
    """, unsafe_allow_html=True)


__all__ = [
    'modern_card',
    'stat_card',
    'product_card',
    'scheme_card',
    'empty_state',
    'loading_skeleton',
    'chat_message',
    'modern_form',
    'info_alert',
    'success_alert',
    'warning_alert',
    'error_alert',
    'language_selector',
    'modern_header',
    'modern_footer',
]
