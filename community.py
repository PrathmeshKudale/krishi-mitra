"""
Farmer Community Feature
Social platform for farmers to share experiences
"""

import streamlit as st
import os
from components import (
    modern_header, modern_footer, loading_skeleton,
    info_alert, success_alert, error_alert, empty_state
)
from translations import get_text
from database import get_all_posts, create_post
from utils import validate_image, validate_video, save_uploaded_file, format_datetime
from config import IMAGES_DIR, VIDEOS_DIR


def render_community_page(user: dict, lang: str = 'en'):
    """
    Render the farmer community page.
    
    Args:
        user: User dictionary
        lang: Language code
    """
    modern_header(
        get_text('community', lang),
        icon="👥"
    )
    
    # Tabs for viewing and creating posts
    tab1, tab2 = st.tabs([
        get_text('view_posts', lang),
        get_text('create_post', lang)
    ])
    
    # View Posts Tab
    with tab1:
        st.subheader(get_text('view_posts', lang))
        
        try:
            posts = get_all_posts(limit=20)
            
            if not posts:
                empty_state(
                    "No posts yet! Be the first to share.",
                    icon="📝",
                    action_text="Create a Post"
                )
            else:
                for post in posts:
                    with st.container():
                        # Modern post card
                        st.markdown(f"""
                        <div style="
                            background: var(--card-bg);
                            border: 1px solid var(--border-color);
                            border-radius: 1rem;
                            padding: 1.5rem;
                            margin-bottom: 1.5rem;
                            box-shadow: var(--shadow-sm);
                        ">
                            <h4 style="margin-bottom: 0.5rem;">👤 {post['farmer_name']}</h4>
                            <p style="margin-bottom: 0.5rem;">{post['content']}</p>
                            <small style="color: var(--text-secondary);">🕐 {format_datetime(post['created_at'])}</small>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Display attached image
                        if post['image_path'] and os.path.exists(post['image_path']):
                            st.image(post['image_path'], use_column_width=True)
                        
                        # Display attached video
                        if post['video_path'] and os.path.exists(post['video_path']):
                            st.video(post['video_path'])
                        
                        st.markdown("---")
        
        except Exception as e:
            error_alert(f"Error loading posts: {str(e)}")
    
    # Create Post Tab
    with tab2:
        st.subheader(get_text('create_post', lang))
        
        with st.form("post_form"):
            farmer_name = st.text_input(
                get_text('your_name', lang),
                value=user['farmer_name']
            )
            
            content = st.text_area(
                get_text('share_experience', lang),
                placeholder="Share your experience, ask questions, or help others...",
                height=150
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                image_file = st.file_uploader(
                    get_text('attach_photo', lang),
                    type=['jpg', 'jpeg', 'png']
                )
            
            with col2:
                video_file = st.file_uploader(
                    get_text('attach_video', lang),
                    type=['mp4']
                )
            
            submitted = st.form_submit_button(
                get_text('post', lang),
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                if not content:
                    error_alert("Please enter some content!")
                else:
                    try:
                        # Handle image upload
                        image_path = None
                        if image_file:
                            is_valid, msg = validate_image(image_file)
                            if not is_valid:
                                error_alert(f"Image error: {msg}")
                                st.stop()
                            image_path = save_uploaded_file(image_file, IMAGES_DIR)
                        
                        # Handle video upload
                        video_path = None
                        if video_file:
                            is_valid, msg = validate_video(video_file)
                            if not is_valid:
                                error_alert(f"Video error: {msg}")
                                st.stop()
                            video_path = save_uploaded_file(video_file, VIDEOS_DIR)
                        
                        # Create post
                        post_id = create_post(farmer_name, content, image_path, video_path)
                        
                        success_alert("✨ Posted successfully!")
                        st.balloons()
                        st.rerun()
                    
                    except Exception as e:
                        error_alert(f"Error creating post: {str(e)}")
    
    st.markdown("---")
    modern_footer()


__all__ = ['render_community_page']