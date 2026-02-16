"""
🌾 Krishi Mitra - FastAPI Login Server
Beautiful HTML login page
"""

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import hashlib
import jwt
from datetime import datetime, timedelta
import os

app = FastAPI(title="Krishi Mitra Login")
templates = Jinja2Templates(directory="templates")

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
DB_PATH = "krishi_mitra.db"

def create_templates():
    """Create HTML template."""
    os.makedirs("templates", exist_ok=True)
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Krishi Mitra - Login</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        
        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container { width: 100%; max-width: 400px; }
        
        .logo-section {
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }
        
        .logo-emoji {
            font-size: 64px;
            margin-bottom: 10px;
            display: block;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .logo-title { font-size: 28px; font-weight: 700; margin-bottom: 5px; }
        .logo-subtitle { font-size: 14px; opacity: 0.9; }
        
        .card {
            background: white;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }
        
        .tabs {
            display: flex;
            background: #f3f4f6;
            border-radius: 12px;
            padding: 4px;
            margin-bottom: 24px;
        }
        
        .tab {
            flex: 1;
            padding: 12px;
            text-align: center;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s;
            border: none;
            background: transparent;
        }
        
        .tab.active { background: #667eea; color: white; }
        
        .form { display: none; }
        .form.active { display: block; }
        
        .input-group { margin-bottom: 16px; }
        
        .input-group input {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e5e7eb;
            border-radius: 12px;
            font-size: 15px;
            transition: all 0.3s;
            background: #f9fafb;
        }
        
        .input-group input:focus {
            outline: none;
            border-color: #667eea;
            background: white;
        }
        
        .forgot-password {
            text-align: right;
            margin: -8px 0 16px 0;
        }
        
        .forgot-password a {
            color: #667eea;
            font-size: 13px;
            text-decoration: none;
        }
        
        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .features {
            display: flex;
            justify-content: space-between;
            margin-top: 24px;
            padding-top: 24px;
            border-top: 1px solid #e5e7eb;
        }
        
        .feature { text-align: center; }
        .feature-icon { font-size: 24px; margin-bottom: 4px; }
        .feature-name { font-size: 11px; color: #6b7280; font-weight: 500; }
        
        .footer {
            text-align: center;
            margin-top: 20px;
            color: rgba(255,255,255,0.8);
            font-size: 12px;
        }
        
        .alert {
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 16px;
            font-size: 14px;
        }
        
        .alert-error { background: #fee2e2; color: #dc2626; border: 1px solid #fecaca; }
        .alert-success { background: #d1fae5; color: #059669; border: 1px solid #a7f3d0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo-section">
            <span class="logo-emoji">🌾</span>
            <h1 class="logo-title">Krishi Mitra</h1>
            <p class="logo-subtitle">Smart Farming Solutions</p>
        </div>
        
        <div class="card">
            {% if error %}
            <div class="alert alert-error">{{ error }}</div>
            {% endif %}
            
            {% if success %}
            <div class="alert alert-success">{{ success }}</div>
            {% endif %}
            
            <div class="tabs">
                <button class="tab active" onclick="showTab('login')">Sign In</button>
                <button class="tab" onclick="showTab('register')">Create Account</button>
            </div>
            
            <form id="loginForm" class="form active" action="/login" method="post">
                <div class="input-group">
                    <input type="text" name="mobile_email" placeholder="Mobile Number or Email" required>
                </div>
                <div class="input-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <div class="forgot-password">
                    <a href="#">Forgot password?</a>
                </div>
                <button type="submit" class="btn">Sign In →</button>
            </form>
            
            <form id="registerForm" class="form" action="/register" method="post">
                <div class="input-group">
                    <input type="text" name="farmer_name" placeholder="Full Name" required>
                </div>
                <div class="input-group">
                    <input type="text" name="mobile_email" placeholder="Mobile Number" required>
                </div>
                <div class="input-group">
                    <input type="text" name="location" placeholder="Village / District" required>
                </div>
                <div class="input-group">
                    <input type="password" name="password" placeholder="Create Password" required>
                </div>
                <button type="submit" class="btn">Create Account →</button>
            </form>
            
            <div class="features">
                <div class="feature">
                    <div class="feature-icon">🤖</div>
                    <div class="feature-name">AI Help</div>
                </div>
                <div class="feature">
                    <div class="feature-icon">📸</div>
                    <div class="feature-name">Scan</div>
                </div>
                <div class="feature">
                    <div class="feature-icon">👥</div>
                    <div class="feature-name">Community</div>
                </div>
                <div class="feature">
                    <div class="feature-icon">🏛️</div>
                    <div class="feature-name">Schemes</div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            Made with ❤️ for Indian Farmers • 2026
        </div>
    </div>
    
    <script>
        function showTab(tabName) {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            event.target.classList.add('active');
            document.querySelectorAll('.form').forEach(form => form.classList.remove('active'));
            document.getElementById(tabName + 'Form').classList.add('active');
        }
    </script>
</body>
</html>"""
    
    with open("templates/login.html", "w") as f:
        f.write(html_content)

create_templates()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_user(mobile_email, password):
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cursor = conn.cursor()
        password_hash = hash_password(password)
        cursor.execute('''
            SELECT id, farmer_name, location FROM users 
            WHERE mobile_email = ? AND password_hash = ?
        ''', (mobile_email, password_hash))
        user = cursor.fetchone()
        conn.close()
        if user:
            return {'id': user[0], 'mobile_email': mobile_email, 'farmer_name': user[1], 'location': user[2]}
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def register_user_db(mobile_email, password, farmer_name, location):
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

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request, error: str = None, success: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "error": error, "success": success})

@app.post("/login")
async def login(mobile_email: str = Form(...), password: str = Form(...)):
    user = verify_user(mobile_email, password)
    if user:
        # Redirect to Streamlit app with user info in URL
        streamlit_url = os.getenv("STREAMLIT_URL", "https://your-streamlit-app.streamlit.app")
        params = f"?logged_in=true&name={user['farmer_name']}&location={user['location']}&email={user['mobile_email']}"
        return RedirectResponse(url=streamlit_url + params, status_code=302)
    else:
        return RedirectResponse(url="/?error=Invalid+credentials", status_code=302)

@app.post("/register")
async def register(farmer_name: str = Form(...), mobile_email: str = Form(...), location: str = Form(...), password: str = Form(...)):
    success, msg = register_user_db(mobile_email, password, farmer_name, location)
    if success:
        return RedirectResponse(url="/?success=Account+created+Please+sign+in", status_code=302)
    else:
        return RedirectResponse(url=f"/?error={msg.replace(' ', '+')}", status_code=302)

@app.get("/health")
async def health():
    return {"status": "ok"}
