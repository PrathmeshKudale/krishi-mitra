"""
🌾 Krishi Mitra - Intelligent Farming Support Application
Main Entry Point with Login System
Supports both SQLite (local) and MongoDB (cloud)
"""

import streamlit as st
import sqlite3
import hashlib
from datetime import datetime
import os

# Must be first
st.set_page_config(
    page_title="Krishi Mitra - Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# DATABASE SWITCH - Easy toggle between SQLite and MongoDB
# =============================================================================
USE_MONGODB = True  # Set to False for SQLite, True for MongoDB

if USE_MONGODB:
    # Use MongoDB (Production - Streamlit Cloud)
    from database_mongo import (
        create_user_mongo as create_user,
        verify_user_mongo as verify_user,
        create_post_mongo as create_post,
        get_all_posts_mongo as get_all_posts,
        add_product_mongo as add_product,
        get_all_products_mongo as get_all_products,
        search_products_mongo as search_products
    )
else:
    # Use SQLite (Local testing)
    from database import (
        create_user, verify_user, create_post,
        get_all_posts, add_product, get_all_products, search_products
    )

# Database setup for users (SQLite fallback)
DB_PATH = "krishi_mitra.db"

def init_user_db():
    """Initialize user database (SQLite fallback)."""
    if not USE_MONGODB:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mobile_email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                farmer_name TEXT,
                location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()

def hash_password(password):
    """Hash password for security."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user_local(mobile_email, password, farmer_name, location):
    """Register new user (SQLite)."""
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        
        cursor.execute('''
            INSERT INTO users (mobile_email, password_hash, farmer_name, location)
            VALUES (?, ?, ?, ?)
        ''', (mobile_email, password_hash, farmer_name, location))
        
        conn.commit()
        conn.close()
        return True, "Registration successful!"
    except sqlite3.IntegrityError:
        return False, "Mobile number or Email already registered!"
    except Exception as e:
        return False, f"Error: {str(e)}"

def login_user_local(mobile_email, password):
    """Verify login credentials (SQLite)."""
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        
        cursor.execute('''
            SELECT * FROM users 
            WHERE mobile_email = ? AND password_hash = ?
        ''', (mobile_email, password_hash))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return True, user
        else:
            return False, "Invalid credentials!"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Initialize database (only for SQLite)
if not USE_MONGODB:
    init_user_db()

# =============================================================================
# SESSION STATE
# =============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "show_register" not in st.session_state:
    st.session_state.show_register = False

# =============================================================================
# CUSTOM CSS
# =============================================================================
st.markdown("""
<style>
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        background-color: #F1F8E9;
        border-radius: 15px;
        border: 2px solid #4CAF50;
        margin-top: 50px;
    }
    .login-header {
        text-align: center;
        color: #2E7D32;
        font-size: 2rem;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
    }
    .welcome-banner {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #4CAF50;
    }
    .db-badge {
        position: fixed;
        top: 10px;
        right: 10px;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        z-index: 999;
    }
    .db-mongo {
        background-color: #4CAF50;
        color: white;
    }
    .db-sqlite {
        background-color: #FF9800;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# DATABASE BADGE (Show which database is active)
# =============================================================================
if USE_MONGODB:
    st.markdown('<div class="db-badge db-mongo">🍃 MongoDB</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="db-badge db-sqlite">🗄️ SQLite</div>', unsafe_allow_html=True)

# =============================================================================
# LOGIN PAGE
# =============================================================================
def show_login():
    st.markdown('<div class="login-header">🌾 Krishi Mitra</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; margin-bottom:30px;">Your Intelligent Farming Companion</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        if not st.session_state.show_register:
            # LOGIN FORM
            st.subheader("🔐 Login")
            
            mobile_email = st.text_input(
                "Mobile Number or Email",
                placeholder="Enter mobile or email",
                key="login_mobile"
            )
            
            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter password",
                key="login_pass"
            )
            
            if st.button("Login", type="primary"):
                if mobile_email and password:
                    if USE_MONGODB:
                        success, result = verify_user(mobile_email, hash_password(password))
                    else:
                        success, result = login_user_local(mobile_email, password)
                    
                    if success:
                        st.session_state.logged_in = True
                        if USE_MONGODB:
                            st.session_state.user = result
                        else:
                            st.session_state.user = {
                                "id": result[0],
                                "mobile_email": result[1],
                                "farmer_name": result[3],
                                "location": result[4]
                            }
                        st.rerun()
                    else:
                        st.error(result)
                else:
                    st.warning("Please fill all fields!")
            
            st.markdown("---")
            st.markdown("New farmer?")
            if st.button("Create Account", key="switch_to_register"):
                st.session_state.show_register = True
                st.rerun()
        
        else:
            # REGISTER FORM
            st.subheader("📝 Register")
            
            farmer_name = st.text_input("Your Full Name", placeholder="Enter your name")
            mobile_email = st.text_input(
                "Mobile Number or Email", 
                placeholder="Enter mobile or email (this will be your username)"
            )
            location = st.text_input("Your Village/Location", placeholder="Enter your location")
            password = st.text_input("Create Password", type="password", placeholder="Min 6 characters")
            confirm_password = st.text_input("Confirm Password", type="password")
            
            if st.button("Register", type="primary"):
                if not all([farmer_name, mobile_email, location, password]):
                    st.warning("Please fill all fields!")
                elif len(password) < 6:
                    st.warning("Password must be at least 6 characters!")
                elif password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    if USE_MONGODB:
                        success, message = create_user(mobile_email, password, farmer_name, location)
                    else:
                        success, message = register_user_local(mobile_email, password, farmer_name, location)
                    
                    if success:
                        st.success(message)
                        st.info("Please login now!")
                        st.session_state.show_register = False
                        st.rerun()
                    else:
                        st.error(message)
            
            st.markdown("---")
            st.markdown("Already have account?")
            if st.button("Back to Login", key="switch_to_login"):
                st.session_state.show_register = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# LOGOUT FUNCTION
# =============================================================================
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.rerun()

# =============================================================================
# MAIN APP ROUTING
# =============================================================================
if not st.session_state.logged_in:
    show_login()
else:
    # Show welcome banner
    st.markdown(f"""
    <div class="welcome-banner">
        <h4>👋 Welcome, {st.session_state.user['farmer_name']}!</h4>
        <p>📍 {st.session_state.user['location']} | 📱 {st.session_state.user['mobile_email']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Logout button in top right
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🚪 Logout"):
            logout()
    
    st.markdown("---")
    
    # Import and run main app
    from main_app import run_main_app
    run_main_app(st.session_state.user)
    
