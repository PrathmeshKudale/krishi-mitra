"""
Google Gemini AI Service for Krishi Mitra
"""

import google.generativeai as genai
from PIL import Image
import streamlit as st
from config import get_gemini_api_key

class KrishiAI:
    def __init__(self):
        api_key = get_gemini_api_key()
        genai.configure(api_key=api_key)
        # Use the same model for both text and vision
        self.model = genai.GenerativeModel('gemini-1.0-pro')
    
    def detect_language(self, text):
        """Detect language of input text."""
        prompt = f"""
        Detect the language of the following text and respond with ONLY the ISO 639-1 language code.
        Supported codes: mr (Marathi), hi (Hindi), en (English), gu (Gujarati), ta (Tamil), te (Telugu), kn (Kannada).
        If uncertain, default to 'en'.
        
        Text: "{text}"
        
        Respond with only the 2-letter code.
        """
        
        try:
            response = self.model.generate_content(prompt)
            lang_code = response.text.strip().lower()[:2]
            valid_codes = ['mr', 'hi', 'en', 'gu', 'ta', 'te', 'kn']
            return lang_code if lang_code in valid_codes else 'en'
        except:
            return 'en'
    
    def get_farming_response(self, query, language='en'):
        """Get AI response for farming questions."""
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        system_prompt = f"""
        You are Krishi Mitra, an expert agricultural advisor for Indian farmers.
        Respond ONLY in {lang_name} language.
        
        Farmer's Question: {query}
        """
        
        try:
            response = self.model.generate_content(system_prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_crop_image(self, image, farmer_query="", language='en'):
        """Analyze crop image."""
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        prompt = f"""
        You are an agricultural expert. Analyze this crop image.
        Respond in {lang_name} language.
        
        Farmer's context: {farmer_query if farmer_query else "None"}
        
        Provide:
        1. Crop identification
        2. Health assessment
        3. Disease/Pest detection
        4. Treatment recommendations
        5. Care tips
        """
        
        try:
            # For vision, use the same model with image
            response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return f"Error analyzing image: {str(e)}"
    
    def generate_crop_knowledge(self, crop_name, language='en'):
        """Generate crop lifecycle information."""
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        prompt = f"""
        You are an agricultural expert. Provide complete information about {crop_name}.
        Respond entirely in {lang_name} language.
        
        Include:
        - Crop overview
        - Complete lifecycle
        - Seasonal calendar
        - Input requirements
        - Economics
        - Best practices
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_government_scheme_info(self, query, language='en'):
        """Provide government scheme information."""
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        prompt = f"""
        You are a government scheme expert for Indian agriculture.
        Respond in {lang_name} language.
        
        Query: {query}
        
        Provide:
        - Scheme overview
        - Eligibility criteria
        - Benefits
        - Application process
        - Contact information
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

# Singleton instance
@st.cache_resource
def get_ai_service():
    return KrishiAI()
        
