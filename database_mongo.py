"""
MongoDB Database operations for Krishi Mitra
"""

import os
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import streamlit as st

def get_mongo_client():
    """Get MongoDB client from Streamlit secrets or env variable."""
    try:
        # Try Streamlit secrets first
        mongo_uri = st.secrets["MONGO_URI"]
    except:
        # Fallback to environment variable
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            st.error("⚠️ MONGO_URI not found! Please add it to Streamlit Secrets.")
            st.stop()
    
    client = MongoClient(mongo_uri)
    return client

def get_db():
    """Get database object."""
    client = get_mongo_client()
    db = client["krishi_mitra"]  # Database name
    return db, client

# =============================================================================
# USERS COLLECTION
# =============================================================================

def create_user_mongo(mobile_email, password_hash, farmer_name, location):
    """Create new user in MongoDB."""
    db, client = get_db()
    try:
        users = db["users"]
        
        # Check if user exists
        if users.find_one({"mobile_email": mobile_email}):
            return False, "User already exists!"
        
        user_doc = {
            "mobile_email": mobile_email,
            "password_hash": password_hash,
            "farmer_name": farmer_name,
            "location": location,
            "created_at": datetime.now()
        }
        
        result = users.insert_one(user_doc)
        return True, str(result.inserted_id)
    except Exception as e:
        return False, str(e)
    finally:
        client.close()

def verify_user_mongo(mobile_email, password_hash):
    """Verify user login from MongoDB."""
    db, client = get_db()
    try:
        users = db["users"]
        user = users.find_one({
            "mobile_email": mobile_email,
            "password_hash": password_hash
        })
        
        if user:
            return True, {
                "id": str(user["_id"]),
                "mobile_email": user["mobile_email"],
                "farmer_name": user["farmer_name"],
                "location": user["location"]
            }
        else:
            return False, "Invalid credentials!"
    except Exception as e:
        return False, str(e)
    finally:
        client.close()

# =============================================================================
# COMMUNITY POSTS COLLECTION
# =============================================================================

def create_post_mongo(farmer_name, content, image_path=None, video_path=None):
    """Create new community post in MongoDB."""
    db, client = get_db()
    try:
        posts = db["community_posts"]
        
        post_doc = {
            "farmer_name": farmer_name,
            "content": content,
            "image_path": image_path,
            "video_path": video_path,
            "created_at": datetime.now()
        }
        
        result = posts.insert_one(post_doc)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error creating post: {e}")
        return None
    finally:
        client.close()

def get_all_posts_mongo(limit=50):
    """Get all community posts from MongoDB."""
    db, client = get_db()
    try:
        posts = db["community_posts"]
        all_posts = list(posts.find().sort("created_at", -1).limit(limit))
        
        # Convert ObjectId to string for JSON serialization
        for post in all_posts:
            post["_id"] = str(post["_id"])
            post["id"] = post["_id"]
        
        return all_posts
    except Exception as e:
        print(f"Error getting posts: {e}")
        return []
    finally:
        client.close()

# =============================================================================
# ORGANIC PRODUCTS COLLECTION
# =============================================================================

def add_product_mongo(farmer_name, product_name, quantity, location, phone_number):
    """Add new organic product to MongoDB."""
    db, client = get_db()
    try:
        products = db["organic_products"]
        
        product_doc = {
            "farmer_name": farmer_name,
            "product_name": product_name,
            "quantity": quantity,
            "location": location,
            "phone_number": phone_number,
            "created_at": datetime.now()
        }
        
        result = products.insert_one(product_doc)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error adding product: {e}")
        return None
    finally:
        client.close()

def get_all_products_mongo(limit=100):
    """Get all organic products from MongoDB."""
    db, client = get_db()
    try:
        products = db["organic_products"]
        all_products = list(products.find().sort("created_at", -1).limit(limit))
        
        # Convert ObjectId to string
        for product in all_products:
            product["_id"] = str(product["_id"])
            product["id"] = product["_id"]
        
        return all_products
    except Exception as e:
        print(f"Error getting products: {e}")
        return []
    finally:
        client.close()

def search_products_mongo(search_term):
    """Search products in MongoDB."""
    db, client = get_db()
    try:
        products = db["organic_products"]
        
        # Create text search query
        query = {
            "$or": [
                {"product_name": {"$regex": search_term, "$options": "i"}},
                {"location": {"$regex": search_term, "$options": "i"}},
                {"farmer_name": {"$regex": search_term, "$options": "i"}}
            ]
        }
        
        results = list(products.find(query).sort("created_at", -1))
        
        for product in results:
            product["_id"] = str(product["_id"])
            product["id"] = product["_id"]
        
        return results
    except Exception as e:
        print(f"Error searching products: {e}")
        return []
    finally:
        client.close()
