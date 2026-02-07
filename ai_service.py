"""
Google Gemini AI Service for Krishi Mitra
Handles all AI interactions with automatic language detection and response
"""

import google.generativeai as genai
from PIL import Image
import streamlit as st
from config import get_gemini_api_key, GEMINI_MODEL_TEXT, GEMINI_MODEL_VISION

class KrishiAI:
    def __init__(self):
        """Initialize Gemini AI with API key."""
        api_key = get_gemini_api_key()
        genai.configure(api_key=api_key)
        self.text_model = genai.GenerativeModel(GEMINI_MODEL_TEXT)
        self.vision_model = genai.GenerativeModel(GEMINI_MODEL_VISION)
    
    def detect_language(self, text):
        """
        Detect language of input text using Gemini.
        Returns language code.
        """
        prompt = f"""
        Detect the language of the following text and respond with ONLY the ISO 639-1 language code.
        Supported codes: mr (Marathi), hi (Hindi), en (English), gu (Gujarati), ta (Tamil), te (Telugu), kn (Kannada).
        If uncertain, default to 'en'.
        
        Text: "{text}"
        
        Respond with only the 2-letter code (e.g., 'hi', 'en', 'mr').
        """
        
        try:
            response = self.text_model.generate_content(prompt)
            lang_code = response.text.strip().lower()[:2]
            valid_codes = ['mr', 'hi', 'en', 'gu', 'ta', 'te', 'kn']
            return lang_code if lang_code in valid_codes else 'en'
        except:
            return 'en'
    
    def get_farming_response(self, query, language='en'):
        """
        Get AI response for farming-related questions.
        Automatically responds in the detected language.
        """
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        system_prompt = f"""
        You are Krishi Mitra, an expert agricultural advisor with deep knowledge of Indian farming.
        You provide practical, detailed, and context-aware farming advice.
        
        CRITICAL: Respond ONLY in {lang_name} language.
        Use natural, farmer-friendly language appropriate for rural Indian farmers.
        
        Guidelines:
        - Be specific and actionable
        - Include local/regional context when relevant
        - Provide step-by-step instructions when applicable
        - Mention approximate quantities, timings, and costs in INR when relevant
        - Include both traditional and modern farming techniques
        - Warn about common mistakes
        
        Farmer's Question: {query}
        """
        
        try:
            response = self.text_model.generate_content(system_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def analyze_crop_image(self, image, farmer_query="", language='en'):
        """
        Comprehensive crop analysis from image using Gemini Vision.
        Returns detailed agricultural intelligence.
        """
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        analysis_prompt = f"""
        You are an expert agricultural scientist and crop doctor. Analyze this crop image comprehensively.
        
        CRITICAL: Provide your entire response in {lang_name} language only.
        
        Provide detailed analysis in this exact structure:
        
        🌱 **Crop Identification**
        - Crop name (English and local name)
        - Growth stage visible
        - Variety (if identifiable)
        
        🔍 **Health Assessment**
        - Overall health status (Healthy/Mild issue/Severe issue)
        - Specific diseases detected (if any)
        - Pest infestation signs (if any)
        - Nutrient deficiencies visible (if any)
        
        🦠 **Disease/Pest Details** (if applicable)
        - Name of disease/pest
        - Symptoms observed
        - Severity level
        - Spread risk
        
        🌾 **Soil Requirements**
        - Ideal soil type
        - pH requirements
        - Soil preparation tips
        
        💧 **Water Requirements**
        - Irrigation frequency
        - Water quantity per acre
        - Best irrigation methods
        - Drainage requirements
        
        🌤️ **Climate & Weather Needs**
        - Ideal temperature range
        - Humidity requirements
        - Seasonal suitability
        - Weather warnings
        
        📈 **Growth Stages**
        - Current stage details
        - Next stages timeline
        - Critical care periods
        
        🧪 **Nutrient Requirements**
        - NPK requirements
        - Micronutrients needed
        - Organic fertilizer options
        - Chemical fertilizer schedule
        
        🛡️ **Disease Prevention**
        - Preventive measures
        - Organic treatments
        - Chemical treatments (if severe)
        - Early warning signs
        
        ✅ **Best Practices**
        - Sowing/planting tips
        - Weeding schedule
        - Pruning/training methods
        - Harvest indicators
        
        ❌ **Common Mistakes to Avoid**
        - Critical errors farmers make
        - Timing mistakes
        - Over/under application risks
        
        Additional farmer context: {farmer_query if farmer_query else "None provided"}
        """
        
        try:
            response = self.vision_model.generate_content([analysis_prompt, image])
            return response.text
        except Exception as e:
            return f"Error analyzing image: {str(e)}"
    
    def generate_crop_knowledge(self, crop_name, language='en'):
        """
        Generate comprehensive crop lifecycle information.
        """
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        prompt = f"""
        You are an agricultural expert. Generate comprehensive knowledge base for: {crop_name}
        
        CRITICAL: Respond entirely in {lang_name} language.
        
        Structure:
        
        🌾 **Crop Overview**
        - Botanical name and family
        - Local/regional names
        - Origin and history
        
        ⏱️ **Complete Lifecycle**
        - Germination to harvest duration
        - Stage-wise breakdown (days for each stage)
        - Critical growth phases
        
        📅 **Seasonal Calendar**
        - Best sowing months for different regions of India
        - Rabi/Kharif/Zaid suitability
        - Climate zone recommendations
        
        🌱 **Input Requirements (Per Acre)**
        - Seeds: quantity, variety recommendations, cost
        - Fertilizers: organic and chemical options with quantities
        - Pesticides/Herbicides: preventive and curative
        - Water: total requirement, irrigation schedule
        - Labor: estimated man-days
        
        💰 **Economics**
        - Total investment per acre (approximate INR)
        - Expected yield per acre
        - Market price trends
        - Profit estimation
        
        ⚠️ **Yield Impact Factors**
        - Positive factors (best practices)
        - Negative factors (risks)
        - Weather dependencies
        - Market risks
        
        🏆 **Success Tips**
        - High-yield variety recommendations
        - Government support available
        - Export potential
        - Value-addition opportunities
        """
        
        try:
            response = self.text_model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating crop knowledge: {str(e)}"
    
    def get_government_scheme_info(self, query, language='en'):
        """
        Provide information about Indian government farming schemes.
        """
        language_names = {
            'mr': 'Marathi', 'hi': 'Hindi', 'en': 'English',
            'gu': 'Gujarati', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada'
        }
        lang_name = language_names.get(language, 'English')
        
        prompt = f"""
        You are a government scheme expert for Indian agriculture.
        Provide accurate, up-to-date information about government farming schemes.
        
        CRITICAL: Respond in {lang_name} language.
        
        Query: {query}
        
        Provide information in this structure:
        
        📋 **Scheme Overview**
        - Full scheme name
        - Launch year (if known)
        - Implementing department
        
        🎯 **Objectives**
        - Main goals of the scheme
        - Target beneficiaries
        
        ✅ **Eligibility Criteria**
        - Who can apply
        - Land requirements (if any)
        - Income limits (if any)
        - Category reservations (SC/ST/OBC/General)
        
        💵 **Benefits**
        - Subsidy amount/percentage
        - Financial assistance details
        - Non-financial benefits
        
        📝 **Application Process**
        - Where to apply (online/offline)
        - Required documents
        - Step-by-step procedure
        - Application deadlines (if any)
        
        📞 **Contact Information**
        - Helpline numbers
        - Website links
        - Local office contacts
        
        ⚠️ **Important Notes**
        - Common rejection reasons
        - Renewal process (if applicable)
        - Recent updates/changes
        """
        
        try:
            response = self.text_model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error fetching scheme info: {str(e)}"

# Singleton instance
@st.cache_resource
def get_ai_service():
    """Get or create AI service singleton."""
    return KrishiAI()
      
