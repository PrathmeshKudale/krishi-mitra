"""
🌾 Krishi Mitra - Main Application Features
Multi-language UI support - NO VOICE for smooth performance
✨ ENHANCED: Full 3D / Glassmorphism / Depth UI
"""

import streamlit as st
from PIL import Image
from datetime import datetime
import os

from config import APP_NAME, APP_TAGLINE, SUPPORTED_LANGUAGES, IMAGES_DIR, VIDEOS_DIR
from database import create_post, get_all_posts, add_product, get_all_products, search_products
from ai_service import get_ai_service
from utils import (
    validate_image, validate_video, compress_image,
    save_uploaded_file, get_language_name, format_datetime
)

# Initialize AI Service
ai_service = get_ai_service()

# Create upload directories
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

# =============================================================================
# TRANSLATIONS - All UI text in different languages
# =============================================================================

TRANSLATIONS = {
    'en': {
        'home': '🏠 Home',
        'ai_assistant': '💬 AI Farming Assistant',
        'crop_diagnosis': '📸 Crop Diagnosis',
        'crop_knowledge': '📚 Crop Knowledge',
        'community': '👥 Farmer Community',
        'schemes': '🏛️ Government Schemes',
        'products': '🥬 Organic Products',
        'welcome': 'Welcome',
        'ask_question': 'Ask any farming-related question in your language',
        'type_here': 'Type your question here...',
        'quick_questions': '💡 Quick Questions',
        'upload_image': '📤 Upload Image',
        'analyze': '🔍 Analyze Crop',
        'preview': '🖼️ Preview',
        'analysis_report': '📋 Analysis Report',
        'enter_crop': 'Enter Crop Name',
        'generate': '📖 Generate Knowledge',
        'view_posts': '📰 View Posts',
        'create_post': '➕ Create Post',
        'your_name': 'Your Name',
        'share_experience': 'Share your experience or question',
        'attach_photo': 'Attach Photo (Optional)',
        'attach_video': 'Attach Video (Optional)',
        'post': 'Post to Community',
        'ask_scheme': 'Ask about any scheme',
        'popular_schemes': '📋 Popular Schemes',
        'browse_products': '🛒 Browse Products',
        'list_product': '➕ List Your Product',
        'product_name': 'Product Name',
        'quantity': 'Quantity',
        'location': 'Location/Village',
        'phone': 'Phone Number',
        'list': 'List Product',
        'search': '🔍 Search',
        'logout': '🚪 Logout',
        'language': 'Language',
        'select_feature': 'Select Feature',
        'user_guide': '📖 User Guide',
        'how_to_use': 'How to use this app:',
        'feature_1': '💬 AI Assistant - Ask any farming question',
        'feature_2': '📸 Crop Diagnosis - Upload photo to detect diseases',
        'feature_3': '📚 Crop Knowledge - Get complete crop information',
        'feature_4': '👥 Community - Share with other farmers',
        'feature_5': '🏛️ Schemes - Learn about government schemes',
        'feature_6': '🥬 Products - Buy/Sell organic products',
        'platform_overview': '📊 Platform Overview',
        'made_with_love': 'Made with ❤️ for our Annadata',
        'copyright': '© 2026 Krishi Mitra. Empowering Indian Farmers.',
        'tagline': 'Your Intelligent Farming Companion'
    },
    'mr': {
        'home': '🏠 मुख्यपृष्ठ',
        'ai_assistant': '💬 कृषी सहाय्यक',
        'crop_diagnosis': '📸 पिक निदान',
        'crop_knowledge': '📚 पिक माहिती',
        'community': '👥 शेतकरी समुदाय',
        'schemes': '🏛️ सरकारी योजना',
        'products': '🥬 सेंद्रिय उत्पादने',
        'welcome': 'स्वागत आहे',
        'ask_question': 'तुमच्या भाषेत कोणत्याही शेतीसंबंधित प्रश्न विचारा',
        'type_here': 'तुमचा प्रश्न येथे टाइप करा...',
        'quick_questions': '💡 जलद प्रश्न',
        'upload_image': '📤 प्रतिमा अपलोड करा',
        'analyze': '🔍 विश्लेषण करा',
        'preview': '🖼️ पूर्वावलोकन',
        'analysis_report': '📋 विश्लेषण अहवाल',
        'enter_crop': 'पिकाचे नाव टाका',
        'generate': '📖 माहिती मिळवा',
        'view_posts': '📰 पोस्ट पहा',
        'create_post': '➕ नवीन पोस्ट',
        'your_name': 'तुमचे नाव',
        'share_experience': 'तुमचा अनुभव किंवा प्रश्न शेअर करा',
        'attach_photo': 'फोटो जोडा (ऐच्छिक)',
        'attach_video': 'व्हिडिओ जोडा (ऐच्छिक)',
        'post': 'समुदायात पोस्ट करा',
        'ask_scheme': 'कोणत्याही योजनेबद्दल विचारा',
        'popular_schemes': '📋 लोकप्रिय योजना',
        'browse_products': '🛒 उत्पादने पहा',
        'list_product': '➕ तुमचे उत्पादन विका',
        'product_name': 'उत्पादनाचे नाव',
        'quantity': 'प्रमाण',
        'location': 'गाव/ठिकाण',
        'phone': 'फोन नंबर',
        'list': 'यादीत टाका',
        'search': '🔍 शोधा',
        'logout': '🚪 बाहेर पडा',
        'language': 'भाषा',
        'select_feature': 'वैशिष्ट्य निवडा',
        'user_guide': '📖 वापरकर्ता मार्गदर्शक',
        'how_to_use': 'अ‍ॅप कसे वापरावे:',
        'feature_1': '💬 AI सहाय्यक - कोणत्याही प्रश्न विचारा',
        'feature_2': '📸 पिक निदान - रोग शोधण्यासाठी फोटो अपलोड करा',
        'feature_3': '📚 पिक माहिती - संपूर्ण माहिती मिळवा',
        'feature_4': '👥 समुदाय - इतर शेतकऱ्यांसोबत शेअर करा',
        'feature_5': '🏛️ योजना - सरकारी योजना जाणून घ्या',
        'feature_6': '🥬 उत्पादने - सेंद्रिय उत्पादने खरेदी/विक्री करा',
        'platform_overview': '📊 प्लॅटफॉर्म सिंहावलोकन',
        'made_with_love': 'आमच्या अन्नदात्यांसाठी ❤️ ने बनवले',
        'copyright': '© २०२६ कृषी मित्र. शेतकऱ्यांना सशक्त बनवणे.',
        'tagline': 'तुमचे बुद्धिमान शेती सहाय्यक'
    },
    'hi': {
        'home': '🏠 होम',
        'ai_assistant': '💬 कृषि सहायक',
        'crop_diagnosis': '📸 फसल निदान',
        'crop_knowledge': '📚 फसल जानकारी',
        'community': '👥 किसान समुदाय',
        'schemes': '🏛️ सरकारी योजनाएं',
        'products': '🥬 जैविक उत्पाद',
        'welcome': 'स्वागत है',
        'ask_question': 'अपनी भाषा में कोई भी कृषि संबंधित प्रश्न पूछें',
        'type_here': 'अपना प्रश्न यहां टाइप करें...',
        'quick_questions': '💡 त्वरित प्रश्न',
        'upload_image': '📤 छवि अपलोड करें',
        'analyze': '🔍 विश्लेषण करें',
        'preview': '🖼️ पूर्वावलोकन',
        'analysis_report': '📋 विश्लेषण रिपोर्ट',
        'enter_crop': 'फसल का नाम दर्ज करें',
        'generate': '📖 जानकारी प्राप्त करें',
        'view_posts': '📰 पोस्ट देखें',
        'create_post': '➕ नई पोस्ट',
        'your_name': 'आपका नाम',
        'share_experience': 'अपना अनुभव या प्रश्न साझा करें',
        'attach_photo': 'फोटो जोड़ें (वैकल्पिक)',
        'attach_video': 'वीडियो जोड़ें (वैकल्पिक)',
        'post': 'समुदाय में पोस्ट करें',
        'ask_scheme': 'किसी भी योजना के बारे में पूछें',
        'popular_schemes': '📋 लोकप्रिय योजनाएं',
        'browse_products': '🛒 उत्पाद देखें',
        'list_product': '➕ अपना उत्पाद बेचें',
        'product_name': 'उत्पाद का नाम',
        'quantity': 'मात्रा',
        'location': 'गांव/स्थान',
        'phone': 'फोन नंबर',
        'list': 'सूचीबद्ध करें',
        'search': '🔍 खोजें',
        'logout': '🚪 लॉगआउट',
        'language': 'भाषा',
        'select_feature': 'सुविधा चुनें',
        'user_guide': '📖 उपयोगकर्ता गाइड',
        'how_to_use': 'ऐप का उपयोग कैसे करें:',
        'feature_1': '💬 AI सहायक - कोई भी प्रश्न पूछें',
        'feature_2': '📸 फसल निदान - रोग का पता लगाने के लिए फोटो अपलोड करें',
        'feature_3': '📚 फसल जानकारी - पूरी जानकारी प्राप्त करें',
        'feature_4': '👥 समुदाय - अन्य किसानों के साथ साझा करें',
        'feature_5': '🏛️ योजनाएं - सरकारी योजनाओं के बारे में जानें',
        'feature_6': '🥬 उत्पाद - जैविक उत्पाद खरीदें/बेचें',
        'platform_overview': '📊 प्लेटफॉर्म अवलोकन',
        'made_with_love': 'हमारे अन्नदाताओं के लिए ❤️ से बनाया गया',
        'copyright': '© २०२६ कृषि मित्र. किसानों को सशक्त बनाना.',
        'tagline': 'आपका बुद्धिमान कृषि सहायक'
    },
    'gu': {
        'home': '🏠 હોમ',
        'ai_assistant': '💬 કૃષિ સહાયક',
        'crop_diagnosis': '📸 પાક નિદાન',
        'crop_knowledge': '📚 પાક માહિતી',
        'community': '👥 ખેડૂત સમુદાય',
        'schemes': '🏛️ સરકારી યોજનાઓ',
        'products': '🥬 જૈવિક ઉત્પાદનો',
        'welcome': 'સ્વાગત છે',
        'ask_question': 'તમારી ભાષામાં કોઈપણ ખેતી સંબંધિત પ્રશ્ન પૂછો',
        'type_here': 'તમારો પ્રશ્ન અહીં ટાઈપ કરો...',
        'quick_questions': '💡 ઝડપી પ્રશ્નો',
        'upload_image': '📤 છબી અપલોડ કરો',
        'analyze': '🔍 વિશ્લેષણ કરો',
        'preview': '🖼️ પૂર્વાવલોકન',
        'analysis_report': '📋 વિશ્લેષણ અહેવાલ',
        'enter_crop': 'પાકનું નામ દાખલ કરો',
        'generate': '📖 માહિતી મેળવો',
        'view_posts': '📰 પોસ્ટ જુઓ',
        'create_post': '➕ નવી પોસ્ટ',
        'your_name': 'તમારું નામ',
        'share_experience': 'તમારો અનુભવ અથવા પ્રશ્ન શેર કરો',
        'attach_photo': 'ફોટો જોડો (વૈકલ્પિક)',
        'attach_video': 'વીડિયો જોડો (વૈકલ્પિક)',
        'post': 'સમુદાયમાં પોસ્ટ કરો',
        'ask_scheme': 'કોઈપણ યોજના વિશે પૂછો',
        'popular_schemes': '📋 લોકપ્રિય યોજનાઓ',
        'browse_products': '🛒 ઉત્પાદનો જુઓ',
        'list_product': '➕ તમારું ઉત્પાદન વેચો',
        'product_name': 'ઉત્પાદનનું નામ',
        'quantity': 'જથ્થો',
        'location': 'ગામ/સ્થાન',
        'phone': 'ફોન નંબર',
        'list': 'યાદીમાં મૂકો',
        'search': '🔍 શોધો',
        'logout': '🚪 લોગઆઉટ',
        'language': 'ભાષા',
        'select_feature': 'સુવિધા પસંદ કરો',
        'user_guide': '📖 વપરાશકર્તા માર્ગદર્શિકા',
        'how_to_use': 'એપ્લિકેશનનો ઉપયોગ કેવી રીતે કરવો:',
        'feature_1': '💬 AI સહાયક - કોઈપણ પ્રશ્ન પૂછો',
        'feature_2': '📸 પાક નિદાન - રોગ શોધવા માટે ફોટો અપલોડ કરો',
        'feature_3': '📚 પાક માહિતી - સંપૂર્ણ માહિતી મેળવો',
        'feature_4': '👥 સમુદાય - અન્ય ખેડૂતો સાથે શેર કરો',
        'feature_5': '🏛️ યોજનાઓ - સરકારી યોજનાઓ વિશે જાણો',
        'feature_6': '🥬 ઉત્પાદનો - જૈવિક ઉત્પાદનો ખરીદો/વેચો',
        'platform_overview': '📊 પ્લેટફોર્મ અવલોકન',
        'made_with_love': 'અમારા અન્નદાતા માટે ❤️ થી બનાવેલ',
        'copyright': '© ૨૦૨૬ કૃષિ મિત્ર. ખેડૂતોને સશક્ત બનાવવા.',
        'tagline': 'તમારું બુદ્ધિશાળી કૃષિ સહાયક'
    },
    'ta': {
        'home': '🏠 முகப்பு',
        'ai_assistant': '💬 விவசாய உதவியாளர்',
        'crop_diagnosis': '📸 பயிர் கண்டறிதல்',
        'crop_knowledge': '📚 பயிர் தகவல்',
        'community': '👥 விவசாயி சமூகம்',
        'schemes': '🏛️ அரசு திட்டங்கள்',
        'products': '🥬 இயற்கை பொருட்கள்',
        'welcome': 'வரவேற்கிறோம்',
        'ask_question': 'உங்கள் மொழியில் எந்த விவசாய தொடர்பான கேள்வியும் கேளுங்கள்',
        'type_here': 'உங்கள் கேள்வியை இங்கே தட்டச்சு செய்க...',
        'quick_questions': '💡 விரைவான கேள்விகள்',
        'upload_image': '📤 படத்தை பதிவேற்றவும்',
        'analyze': '🔍 பகுப்பாய்வு செய்யவும்',
        'preview': '🖼️ முன்னோட்டம்',
        'analysis_report': '📋 பகுப்பாய்வு அறிக்கை',
        'enter_crop': 'பயிரின் பெயரை உள்ளிடவும்',
        'generate': '📖 தகவலைப் பெறுங்கள்',
        'view_posts': '📰 பதிவுகளைக் காண்க',
        'create_post': '➕ புதிய பதிவு',
        'your_name': 'உங்கள் பெயர்',
        'share_experience': 'உங்கள் அனுபவம் அல்லது கேள்வியைப் பகிரவும்',
        'attach_photo': 'புகைப்படத்தை இணைக்கவும் (விரும்பினால்)',
        'attach_video': 'வீடியோவை இணைக்கவும் (விரும்பினால்)',
        'post': 'சமூகத்தில் பதிவு செய்யவும்',
        'ask_scheme': 'எந்த திட்டம் பற்றியும் கேளுங்கள்',
        'popular_schemes': '📋 பிரபலமான திட்டங்கள்',
        'browse_products': '🛒 பொருட்களைக் காண்க',
        'list_product': '➕ உங்கள் பொருளை விற்கவும்',
        'product_name': 'பொருளின் பெயர்',
        'quantity': 'அளவு',
        'location': 'கிராமம்/இடம்',
        'phone': 'தொலைபேசி எண்',
        'list': 'பட்டியலிடுங்கள்',
        'search': '🔍 தேடுங்கள்',
        'logout': '🚪 வெளியேறு',
        'language': 'மொழி',
        'select_feature': 'அம்சத்தைத் தேர்வு செய்க',
        'user_guide': '📖 பயனர் வழிகாட்டி',
        'how_to_use': 'பயன்பாட்டை எவ்வாறு பயன்படுத்துவது:',
        'feature_1': '💬 AI உதவியாளர் - எந்த கேள்வியும் கேளுங்கள்',
        'feature_2': '📸 பயிர் கண்டறிதல் - நோயைக் கண்டறிய புகைப்படத்தை பதிவேற்றவும்',
        'feature_3': '📚 பயிர் தகவல் - முழு தகவல் பெறுங்கள்',
        'feature_4': '👥 சமூகம் - பிற விவசாயிகளுடன் பகிர்ந்து கொள்ளுங்கள்',
        'feature_5': '🏛️ திட்டங்கள் - அரசு திட்டங்கள் பற்றி அறிந்து கொள்ளுங்கள்',
        'feature_6': '🥬 பொருட்கள் - இயற்கை பொருட்களை வாங்க/விற்க',
        'platform_overview': '📊 தள கண்ணோட்டம்',
        'made_with_love': 'எங்கள் அன்னதாதாக்களுக்காக ❤️ உடன் உருவாக்கப்பட்டது',
        'copyright': '© २०२६ கிருஷி மித்ரா. விவசாயிகளை வலுப்படுத்துதல்.',
        'tagline': 'உங்கள் புத்திசாலி விவசாய உதவியாளர்'
    },
    'te': {
        'home': '🏠 హోమ్',
        'ai_assistant': '💬 వ్యవసాయ సహాయకుడు',
        'crop_diagnosis': '📸 పంట నిర్ధారణ',
        'crop_knowledge': '📚 పంట సమాచారం',
        'community': '👥 రైతు సమాజం',
        'schemes': '🏛️ ప్రభుత్వ పథకాలు',
        'products': '🥬 సేంద్రీయ ఉత్పత్తులు',
        'welcome': 'స్వాగతం',
        'ask_question': 'మీ భాషలో ఏదైనా వ్యవసాయ సంబంధిత ప్రశ్న అడగండి',
        'type_here': 'మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...',
        'quick_questions': '💡 త్వరిత ప్రశ్నలు',
        'upload_image': '📤 చిత్రాన్ని అప్‌లోడ్ చేయండి',
        'analyze': '🔍 విశ్లేషణ చేయండి',
        'preview': '🖼️ మునుజూపు',
        'analysis_report': '📋 విశ్లేషణ నివేదిక',
        'enter_crop': 'పంట పేరును నమోదు చేయండి',
        'generate': '📖 సమాచారం పొందండి',
        'view_posts': '📰 పోస్ట్‌లను చూడండి',
        'create_post': '➕ కొత్త పోస్ట్',
        'your_name': 'మీ పేరు',
        'share_experience': 'మీ అనుభవం లేదా ప్రశ్నను పంచుకోండి',
        'attach_photo': 'ఫోటోను జోడించండి (ఐచ్ఛికం)',
        'attach_video': 'వీడియోను జోడించండి (ఐచ్ఛికం)',
        'post': 'సమాజంలో పోస్ట్ చేయండి',
        'ask_scheme': 'ఏదైనా పథకం గురించి అడగండి',
        'popular_schemes': '📋 ప్రజాదరణ పొందిన పథకాలు',
        'browse_products': '🛒 ఉత్పత్తులను చూడండి',
        'list_product': '➕ మీ ఉత్పత్తిని అమ్మండి',
        'product_name': 'ఉత్పత్తి పేరు',
        'quantity': 'పరిమాణం',
        'location': 'గ్రామం/స్థలం',
        'phone': 'ఫోన్ నంబర్',
        'list': 'జాబితాలో చేర్చండి',
        'search': '🔍 వెతకండి',
        'logout': '🚪 లాగౌట్',
        'language': 'భాష',
        'select_feature': 'ఫీచర్ ఎంచుకోండి',
        'user_guide': '📖 వినియోగదారు గైడ్',
        'how_to_use': 'అప్లికేషన్‌ను ఎలా ఉపయోగించాలి:',
        'feature_1': '💬 AI సహాయకుడు - ఏదైనా ప్రశ్న అడగండి',
        'feature_2': '📸 పంట నిర్ధారణ - వ్యాధులను గుర్తించడానికి ఫోటో అప్‌లోడ్ చేయండి',
        'feature_3': '📚 పంట సమాచారం - పూర్తి సమాచారం పొందండి',
        'feature_4': '👥 సమాజం - ఇతర రైతులతో పంచుకోండి',
        'feature_5': '🏛️ పథకాలు - ప్రభుత్వ పథకాల గురించి తెలుసుకోండి',
        'feature_6': '🥬 ఉత్పత్తులు - సేంద్రీయ ఉత్పత్తులను కొనుగోలు/అమ్మండి',
        'platform_overview': '📊 ప్లాట్‌ఫారమ్ అవలోకనం',
        'made_with_love': 'మా అన్నదాతల కోసం ❤️ తో తయారు చేయబడింది',
        'copyright': '© २०२६ కృషి మిత్ర. రైతులను సశక్తీకరించడం.',
        'tagline': 'మీ తెలివైన వ్యవసాయ సహాయకుడు'
    },
    'kn': {
        'home': '🏠 ಮುಖಪುಟ',
        'ai_assistant': '💬 ಕೃಷಿ ಸಹಾಯಕ',
        'crop_diagnosis': '📸 ಬೆಳೆ ನಿದಾನ',
        'crop_knowledge': '📚 ಬೆಳೆ ಮಾಹಿತಿ',
        'community': '👥 ರೈತರ ಸಮುದಾಯ',
        'schemes': '🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು',
        'products': '🥬 ಸಾವಯವ ಉತ್ಪನ್ನಗಳು',
        'welcome': 'ಸ್ವಾಗತ',
        'ask_question': 'ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಯಾವುದೇ ಕೃಷಿ ಸಂಬಂಧಿತ ಪ್ರಶ್ನೆ ಕೇಳಿ',
        'type_here': 'ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಇಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ...',
        'quick_questions': '💡 ತ್ವರಿತ ಪ್ರಶ್ನೆಗಳು',
        'upload_image': '📤 ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ',
        'analyze': '🔍 ವಿಶ್ಲೇಷಣೆ ಮಾಡಿ',
        'preview': '🖼️ ಮುನ್ನೋಟ',
        'analysis_report': '📋 ವಿಶ್ಲೇಷಣೆ ವರದಿ',
        'enter_crop': 'ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ',
        'generate': '📖 ಮಾಹಿತಿ ಪಡೆಯಿರಿ',
        'view_posts': '📰 ಪೋಸ್ಟ್‌ಗಳನ್ನು ವೀಕ್ಷಿಸಿ',
        'create_post': '➕ ಹೊಸ ಪೋಸ್ಟ್',
        'your_name': 'ನಿಮ್ಮ ಹೆಸರು',
        'share_experience': 'ನಿಮ್ಮ ಅನುಭವ ಅಥವಾ ಪ್ರಶ್ನೆಯನ್ನು ಹಂಚಿಕೊಳ್ಳಿ',
        'attach_photo': 'ಫೋಟೋವನ್ನು ಲಗತ್ತಿಸಿ (ಐಚ್ಛಿಕ)',
        'attach_video': 'ವೀಡಿಯೊವನ್ನು ಲಗತ್ತಿಸಿ (ಐಚ್ಛಿಕ)',
        'post': 'ಸಮುದಾಯದಲ್ಲಿ ಪೋಸ್ಟ್ ಮಾಡಿ',
        'ask_scheme': 'ಯಾವುದೇ ಯೋಜನೆಯ ಬಗ್ಗೆ ಕೇಳಿ',
        'popular_schemes': '📋 ಜನಪ್ರಿಯ ಯೋಜನೆಗಳು',
        'browse_products': '🛒 ಉತ್ಪನ್ನಗಳನ್ನು ವೀಕ್ಷಿಸಿ',
        'list_product': '➕ ನಿಮ್ಮ ಉತ್ಪನ್ನವನ್ನು ಮಾರಾಟ ಮಾಡಿ',
        'product_name': 'ಉತ್ಪನ್ನದ ಹೆಸರು',
        'quantity': 'ಪ್ರಮಾಣ',
        'location': 'ಗ್ರಾಮ/ಸ್ಥಳ',
        'phone': 'ಫೋನ್ ಸಂಖ್ಯೆ',
        'list': 'ಪಟ್ಟಿ ಮಾಡಿ',
        'search': '🔍 ಹುಡುಕಿ',
        'logout': '🚪 ಲಾಗ್ ಔಟ್',
        'language': 'ಭಾಷೆ',
        'select_feature': 'ವೈಶಿಷ್ಟ್ಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ',
        'user_guide': '📖 ಬಳಕೆದಾರ ಮಾರ್ಗದರ್ಶಿ',
        'how_to_use': 'ಅಪ್ಲಿಕೇಶನ್ ಹೇಗೆ ಬಳಸುವುದು:',
        'feature_1': '💬 AI ಸಹಾಯಕ - ಯಾವುದೇ ಪ್ರಶ್ನೆ ಕೇಳಿ',
        'feature_2': '📸 ಬೆಳೆ ನಿದಾನ - ರೋಗಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ',
        'feature_3': '📚 ಬೆಳೆ ಮಾಹಿತಿ - ಸಂಪೂರ್ಣ ಮಾಹಿತಿ ಪಡೆಯಿರಿ',
        'feature_4': '👥 ಸಮುದಾಯ - ಇತರ ರೈತರೊಂದಿಗೆ ಹಂಚಿಕೊಳ್ಳಿ',
        'feature_5': '🏛️ ಯೋಜನೆಗಳು - ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ',
        'feature_6': '🥬 ಉತ್ಪನ್ನಗಳು - ಸಾವಯವ ಉತ್ಪನ್ನಗಳನ್ನು ಖರೀದಿಸಿ/ಮಾರಾಟ ಮಾಡಿ',
        'platform_overview': '📊 ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಅವಲೋಕನ',
        'made_with_love': 'ನಮ್ಮ ಅನ್ನದಾತರಿಗಾಗಿ ❤️ ಯೊಂದಿಗೆ ತಯಾರಿಸಲಾಗಿದೆ',
        'copyright': '© २०२६ ಕೃಷಿ ಮಿತ್ರ. ರೈತರನ್ನು ಸಬಲೀಕರಣಗೊಳಿಸುವುದು.',
        'tagline': 'ನಿಮ್ಮ ಬುದ್ಧಿವಂತ ಕೃಷಿ ಸಹಾಯಕ'
    }
}


def get_text(key, lang='en'):
    """Get translated text for given key and language."""
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, TRANSLATIONS['en'][key])


# =============================================================================
# MAIN APP FUNCTION
# =============================================================================

def run_main_app(user):
    """Run main application with all features."""

    # Get selected language
    selected_lang = st.session_state.get('selected_language', 'en')

    # =========================================================================
    # ✨ ENHANCED 3D GLOBAL CSS — Glassmorphism + Depth + Perspective
    # =========================================================================
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=Nunito:wght@400;600;700;800;900&family=Playfair+Display:wght@700;900&display=swap');

    /* ── CSS Variables ─────────────────────────────────── */
    :root {
        --earth-dark:      #0d2210;
        --leaf-deep:       #1b5e20;
        --leaf-mid:        #388e3c;
        --leaf-bright:     #66bb6a;
        --leaf-neon:       #a5d6a7;
        --sun-gold:        #f9a825;
        --sun-warm:        #ffd54f;
        --sun-glow:        #ffe082;
        --soil-brown:      #6d4c41;
        --sky-blue:        #b3e5fc;
        --cream:           #faf7ef;
        --white:           #ffffff;

        /* 3D Depth shadows */
        --shadow-soft:     0 4px 20px rgba(27,94,32,0.12), 0 1px 4px rgba(0,0,0,0.06);
        --shadow-lift:     0 12px 48px rgba(27,94,32,0.22), 0 4px 12px rgba(0,0,0,0.10);
        --shadow-deep:     0 24px 64px rgba(13,34,16,0.35), 0 8px 24px rgba(0,0,0,0.15);
        --shadow-3d:       0 2px 0 rgba(255,255,255,0.5) inset,
                           0 -4px 0 rgba(0,0,0,0.15) inset,
                           0 8px 32px rgba(27,94,32,0.20);
        --shadow-gold:     0 8px 32px rgba(249,168,37,0.30), 0 2px 8px rgba(249,168,37,0.15);

        /* Glass */
        --glass-bg:        rgba(255,255,255,0.60);
        --glass-border:    rgba(255,255,255,0.80);
        --glass-blur:      blur(16px) saturate(1.6);

        /* Radius */
        --radius-card:     20px;
        --radius-btn:      50px;

        /* Perspective for 3D cards */
        --perspective:     1000px;
    }

    /* ── Global body ──────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    /* ── Animated 3D background ───────────────────────── */
    .stApp {
        background:
            radial-gradient(ellipse at 20% 10%, rgba(102,187,106,0.18) 0%, transparent 55%),
            radial-gradient(ellipse at 80% 90%, rgba(249,168,37,0.14) 0%, transparent 55%),
            radial-gradient(ellipse at 60% 40%, rgba(27,94,32,0.10) 0%, transparent 50%),
            linear-gradient(160deg, #dff0dc 0%, #f0faf0 35%, #fffef5 70%, #fff8e1 100%);
        min-height: 100vh;
    }

    /* Grain texture */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 0;
    }

    /* ── Floating orbs (background decoration) ────────── */
    .stApp::after {
        content: "";
        position: fixed;
        width: 600px; height: 600px;
        top: -200px; right: -200px;
        background: radial-gradient(circle, rgba(102,187,106,0.10) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        animation: orbDrift 18s ease-in-out infinite alternate;
        z-index: 0;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── KEYFRAMES ─────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    @keyframes orbDrift {
        from { transform: translate(0,0) scale(1); }
        to   { transform: translate(-80px, 60px) scale(1.2); }
    }
    @keyframes sway {
        0%,100% { transform: rotate(-6deg) scale(1); }
        50%      { transform: rotate(6deg)  scale(1.05); }
    }
    @keyframes fadeSlideDown {
        from { opacity:0; transform:translateY(-30px) rotateX(10deg); }
        to   { opacity:1; transform:translateY(0)     rotateX(0); }
    }
    @keyframes fadeSlideUp {
        from { opacity:0; transform:translateY(30px) rotateX(-8deg); }
        to   { opacity:1; transform:translateY(0)    rotateX(0); }
    }
    @keyframes growIn3D {
        from { opacity:0; transform:scale(0.88) rotateX(12deg); }
        to   { opacity:1; transform:scale(1)    rotateX(0); }
    }
    @keyframes shimmer {
        0%   { background-position: -300% center; }
        100% { background-position:  300% center; }
    }
    @keyframes float3D {
        0%,100% { transform: translateY(0)    rotateZ(0deg); }
        33%      { transform: translateY(-8px) rotateZ(2deg); }
        66%      { transform: translateY(-4px) rotateZ(-1deg); }
    }
    @keyframes pulseGlow {
        0%,100% { box-shadow: 0 0 0 0  rgba(102,187,106,0.50), var(--shadow-lift); }
        50%      { box-shadow: 0 0 0 12px rgba(102,187,106,0),  var(--shadow-lift); }
    }
    @keyframes goldPulse {
        0%,100% { box-shadow: var(--shadow-gold); }
        50%      { box-shadow: 0 16px 48px rgba(249,168,37,0.50), 0 4px 16px rgba(249,168,37,0.30); }
    }
    @keyframes borderRun {
        0%   { background-position:   0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position:   0% 50%; }
    }
    @keyframes slideRight {
        from { transform: translateX(0); }
        to   { transform: translateX(8px); }
    }
    @keyframes heroParticle {
        0%   { transform: translateY(0)    translateX(0)   scale(1);   opacity:0.6; }
        50%  { transform: translateY(-40px) translateX(15px) scale(1.3); opacity:0.9; }
        100% { transform: translateY(-80px) translateX(-5px) scale(0.8); opacity:0; }
    }
    @keyframes spin3D {
        from { transform: rotateY(0deg); }
        to   { transform: rotateY(360deg); }
    }

    /* ─────────────────────────────────────────────────── */
    /* ── SIDEBAR ───────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #0d2210 0%, #1b5e20 40%, #2e7d32 75%, #388e3c 100%) !important;
        border-right: none !important;
        box-shadow: 6px 0 40px rgba(0,0,0,0.35), 2px 0 8px rgba(0,0,0,0.15);
    }
    /* Inner light reflection */
    section[data-testid="stSidebar"]::after {
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 3px; height: 100%;
        background: linear-gradient(180deg, rgba(255,255,255,0.18) 0%, transparent 60%);
        pointer-events: none;
    }
    section[data-testid="stSidebar"] * {
        color: #e8f5e3 !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(6px);
        border-radius: 14px;
        padding: 11px 16px;
        margin: 5px 0;
        transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
        cursor: pointer;
        border: 1px solid rgba(255,255,255,0.10);
        display: block;
        box-shadow: 0 2px 8px rgba(0,0,0,0.12),
                    0 1px 0 rgba(255,255,255,0.08) inset;
    }
    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.17);
        transform: translateX(6px) scale(1.02);
        border-color: rgba(165,214,167,0.40);
        box-shadow: 0 4px 16px rgba(0,0,0,0.18), 4px 0 0 rgba(165,214,167,0.6);
    }
    section[data-testid="stSidebar"] .stSelectbox select,
    section[data-testid="stSidebar"] .stSelectbox > div {
        background: rgba(255,255,255,0.10) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.20) !important;
        backdrop-filter: blur(8px);
    }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.12) !important;
    }

    /* ── Sidebar brand ──────────────────────────────────── */
    .km-sidebar-brand {
        text-align: center;
        padding: 24px 10px 12px;
        animation: fadeSlideDown 0.8s cubic-bezier(.34,1.56,.64,1) both;
        position: relative;
    }
    .km-sidebar-brand::after {
        content: "";
        position: absolute;
        bottom: 0; left: 20%; right: 20%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(165,214,167,0.5), transparent);
    }
    .km-sidebar-brand .km-logo-anim {
        font-size: 52px;
        display: inline-block;
        animation: sway 3.5s ease-in-out infinite;
        filter: drop-shadow(0 6px 18px rgba(0,0,0,0.4)) drop-shadow(0 0 24px rgba(165,214,167,0.5));
    }
    .km-sidebar-brand h2 {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.55rem !important;
        background: linear-gradient(135deg, #ffd54f 0%, #f9a825 50%, #fff8e1 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        margin: 8px 0 3px !important;
        letter-spacing: 1.5px;
        text-shadow: none !important;
    }
    .km-sidebar-brand p {
        font-size: 0.73rem !important;
        color: #a5d6a7 !important;
        margin: 0 !important;
        letter-spacing: 0.5px;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── HERO BANNER — Full 3D ──────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-hero {
        background:
            linear-gradient(135deg, #0d2210 0%, #1b5e20 40%, #2e7d32 70%, #388e3c 100%);
        border-radius: 28px;
        padding: 56px 40px;
        text-align: center;
        margin-bottom: 36px;
        position: relative;
        overflow: hidden;
        animation: growIn3D 0.8s cubic-bezier(.34,1.56,.64,1) both;
        /* Multi-layer 3D shadow */
        box-shadow:
            0 2px 0 rgba(255,255,255,0.08) inset,
            0 -6px 0 rgba(0,0,0,0.20) inset,
            0 20px 60px rgba(13,34,16,0.50),
            0 8px 24px rgba(0,0,0,0.20),
            0 2px 8px rgba(0,0,0,0.10);
        transform-style: preserve-3d;
    }

    /* Bottom crop decoration */
    .km-hero::before {
        content: "🌾🌱🌻🌾🌱🌻🌾🌱🌻🌾🌱🌻";
        position: absolute;
        bottom: -14px; left: 0; right: 0;
        font-size: 2.2rem;
        opacity: 0.10;
        letter-spacing: 10px;
        white-space: nowrap;
        overflow: hidden;
        filter: blur(1px);
    }
    /* Top highlight edge */
    .km-hero::after {
        content: "";
        position: absolute;
        top: 0; left: 5%; right: 5%;
        height: 2px;
        background: linear-gradient(90deg,
            transparent 0%,
            rgba(255,255,255,0.35) 30%,
            rgba(255,213,79,0.60) 50%,
            rgba(255,255,255,0.35) 70%,
            transparent 100%);
        border-radius: 50%;
    }
    /* Glow orb inside hero */
    .km-hero-orb {
        position: absolute;
        width: 320px; height: 320px;
        top: -80px; left: 50%;
        transform: translateX(-50%);
        background: radial-gradient(circle, rgba(102,187,106,0.18) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        animation: orbDrift 10s ease-in-out infinite alternate;
    }
    .km-hero h1 {
        font-family: 'Playfair Display', serif !important;
        font-size: clamp(2.2rem, 5vw, 3.5rem) !important;
        background: linear-gradient(135deg, #ffd54f 0%, #f9a825 40%, #fff8e1 70%, #ffd54f 100%) !important;
        background-size: 200% auto !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        animation: shimmer 4s linear infinite !important;
        margin-bottom: 8px !important;
        position: relative;
        z-index: 1;
        /* 3D text depth */
        filter: drop-shadow(0 4px 16px rgba(249,168,37,0.40));
    }
    .km-hero h3 {
        color: #c8e6c9 !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin: 0 !important;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }

    /* ─────────────────────────────────────────────────── */
    /* ── FEATURE CARDS — 3D Glass ─────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-feature-card {
        background: var(--glass-bg);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border-radius: var(--radius-card);
        padding: 30px 24px;
        border: 1.5px solid var(--glass-border);
        box-shadow: var(--shadow-3d);
        transition: transform 0.35s cubic-bezier(.34,1.56,.64,1), box-shadow 0.35s;
        animation: fadeSlideUp 0.55s ease both;
        height: 100%;
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
        /* Bottom thickness illusion */
        outline: 1px solid rgba(255,255,255,0.40);
    }
    /* Shiny top edge */
    .km-feature-card::before {
        content: "";
        position: absolute;
        top: 0; left: 8%; right: 8%;
        height: 1.5px;
        background: linear-gradient(90deg,
            transparent, rgba(255,255,255,0.90), transparent);
        border-radius: 50%;
    }
    /* Accent bar */
    .km-feature-card::after {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, #388e3c, #66bb6a, #f9a825, #66bb6a, #388e3c);
        background-size: 200% auto;
        animation: borderRun 4s linear infinite;
        border-radius: 20px 20px 0 0;
    }
    .km-feature-card:hover {
        transform: translateY(-10px) rotateX(4deg) rotateY(-2deg) scale(1.02);
        box-shadow: var(--shadow-deep);
    }
    .km-feature-card .km-icon {
        font-size: 2.6rem;
        display: inline-block;
        animation: float3D 4s ease-in-out infinite;
        filter: drop-shadow(0 4px 12px rgba(0,0,0,0.20));
    }
    .km-feature-card h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.22rem;
        color: var(--leaf-deep);
        margin: 12px 0 8px;
    }
    .km-feature-card p {
        font-size: 0.88rem;
        color: #4a5568;
        margin: 0;
        line-height: 1.65;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── STATS / METRICS ────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    [data-testid="metric-container"] {
        background: var(--glass-bg) !important;
        backdrop-filter: var(--glass-blur) !important;
        -webkit-backdrop-filter: var(--glass-blur) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        border: 1.5px solid var(--glass-border) !important;
        box-shadow: var(--shadow-3d) !important;
        transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), box-shadow 0.3s !important;
        animation: growIn3D 0.6s ease both !important;
        position: relative;
        overflow: hidden;
    }
    [data-testid="metric-container"]::before {
        content: "";
        position: absolute;
        top: 0; left: 8%; right: 8%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
    }
    [data-testid="metric-container"]:hover {
        transform: translateY(-6px) rotateX(3deg) !important;
        box-shadow: var(--shadow-lift) !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--leaf-deep) !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    [data-testid="stMetricValue"] {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(135deg, #1b5e20, #388e3c, #66bb6a) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 2.4rem !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── BUTTONS — 3D Press Effect ──────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stButton > button {
        border-radius: var(--radius-btn) !important;
        font-family: 'Nunito', sans-serif !important;
        font-weight: 800 !important;
        transition: all 0.25s cubic-bezier(.34,1.56,.64,1) !important;
        border: none !important;
        letter-spacing: 0.3px;
        position: relative;
        overflow: hidden;
    }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid*="primary"] {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 40%, #43a047 80%, #66bb6a 100%) !important;
        color: white !important;
        /* 3D raised button look */
        box-shadow:
            0 1px 0 rgba(255,255,255,0.30) inset,
            0 -3px 0 rgba(0,0,0,0.25) inset,
            0 6px 24px rgba(27,94,32,0.40),
            0 2px 8px rgba(0,0,0,0.15) !important;
        animation: pulseGlow 3s infinite;
    }
    .stButton > button[kind="primary"]::after,
    .stButton > button[data-testid*="primary"]::after {
        content: "";
        position: absolute;
        top: 0; left: -100%;
        width: 60%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.22), transparent);
        transform: skewX(-20deg);
        transition: left 0.5s ease;
    }
    .stButton > button[kind="primary"]:hover::after,
    .stButton > button[data-testid*="primary"]:hover::after {
        left: 150%;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.04) !important;
        box-shadow:
            0 1px 0 rgba(255,255,255,0.30) inset,
            0 -3px 0 rgba(0,0,0,0.25) inset,
            0 12px 36px rgba(27,94,32,0.45),
            0 4px 12px rgba(0,0,0,0.18) !important;
    }
    .stButton > button:active {
        transform: translateY(2px) scale(0.97) !important;
        box-shadow:
            0 1px 0 rgba(0,0,0,0.10) inset,
            0 -1px 0 rgba(255,255,255,0.15) inset,
            0 2px 8px rgba(27,94,32,0.20) !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── INPUTS & SELECTS ──────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox select {
        border-radius: 14px !important;
        border: 2px solid rgba(102,187,106,0.40) !important;
        background: rgba(255,255,255,0.75) !important;
        backdrop-filter: blur(8px) !important;
        font-family: 'Nunito', sans-serif !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 2px 8px rgba(27,94,32,0.08),
                    0 1px 0 rgba(255,255,255,0.80) inset !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #66bb6a !important;
        box-shadow:
            0 0 0 3px rgba(102,187,106,0.22),
            0 4px 16px rgba(27,94,32,0.15),
            0 1px 0 rgba(255,255,255,0.80) inset !important;
        outline: none !important;
        background: rgba(255,255,255,0.95) !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── HEADERS ──────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
    }
    .stApp h2, .stApp h3 {
        color: var(--leaf-deep) !important;
    }
    .stApp h2, .stApp [data-testid="stHeader"] {
        background: linear-gradient(90deg,
            var(--leaf-deep) 0%,
            var(--leaf-mid)  30%,
            var(--leaf-bright) 55%,
            var(--sun-gold)  75%,
            var(--leaf-deep) 100%);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 5s linear infinite;
        filter: drop-shadow(0 2px 6px rgba(27,94,32,0.18));
    }

    /* ─────────────────────────────────────────────────── */
    /* ── COMMUNITY POST CARD ───────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-post-card {
        background: var(--glass-bg);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1.5px solid rgba(255,255,255,0.75);
        border-radius: var(--radius-card);
        padding: 24px 22px;
        margin-bottom: 20px;
        box-shadow: var(--shadow-3d);
        transition: transform 0.28s cubic-bezier(.34,1.56,.64,1), box-shadow 0.28s;
        animation: fadeSlideUp 0.45s ease both;
        position: relative;
        overflow: hidden;
    }
    .km-post-card::before {
        content: "";
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 5px;
        background: linear-gradient(180deg, #66bb6a, #f9a825, #66bb6a);
        background-size: 100% 200%;
        animation: borderRun 3s linear infinite;
        border-radius: 20px 0 0 20px;
    }
    .km-post-card::after {
        content: "";
        position: absolute;
        top: 0; left: 8%; right: 8%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
    }
    .km-post-card:hover {
        transform: translateY(-6px) rotateX(2deg);
        box-shadow: var(--shadow-lift);
    }
    .km-post-card h4 {
        font-family: 'Playfair Display', serif;
        color: var(--leaf-deep);
        margin: 0 0 10px;
        font-size: 1.08rem;
    }
    .km-post-card p  { color: #2d3748; margin: 0 0 8px; line-height: 1.6; }
    .km-post-card small { color: #718096; font-size: 0.8rem; }

    /* ─────────────────────────────────────────────────── */
    /* ── SCHEME CARDS ──────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-scheme-card {
        background: linear-gradient(135deg,
            rgba(240,249,240,0.90) 0%,
            rgba(232,245,233,0.85) 100%);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1.5px solid rgba(165,214,167,0.60);
        border-radius: 18px;
        padding: 22px 18px;
        text-align: center;
        transition: transform 0.30s cubic-bezier(.34,1.56,.64,1), box-shadow 0.30s;
        animation: growIn3D 0.5s ease both;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow:
            0 1px 0 rgba(255,255,255,0.90) inset,
            0 -3px 0 rgba(56,142,60,0.12) inset,
            0 6px 24px rgba(56,142,60,0.14);
    }
    .km-scheme-card::before {
        content: "";
        position: absolute;
        top: 0; left: 15%; right: 15%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.95), transparent);
    }
    .km-scheme-card:hover {
        transform: translateY(-8px) rotateX(5deg) scale(1.03);
        box-shadow:
            0 1px 0 rgba(255,255,255,0.90) inset,
            0 20px 48px rgba(56,142,60,0.22),
            0 8px 20px rgba(0,0,0,0.10);
    }
    .km-scheme-card h4 {
        font-family: 'Playfair Display', serif;
        color: var(--leaf-deep);
        font-size: 1.12rem;
        margin: 0 0 6px;
    }
    .km-scheme-card p {
        font-size: 0.82rem;
        color: #388e3c;
        margin: 0;
        font-weight: 600;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── PRODUCT CARDS ─────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-product-card {
        background: linear-gradient(135deg,
            rgba(255,253,231,0.92) 0%,
            rgba(255,248,225,0.88) 100%);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1.5px solid rgba(255,224,130,0.70);
        border-radius: var(--radius-card);
        padding: 24px 20px;
        margin-bottom: 20px;
        box-shadow:
            0 1px 0 rgba(255,255,255,0.95) inset,
            0 -3px 0 rgba(244,185,66,0.20) inset,
            0 8px 28px rgba(244,185,66,0.20),
            0 3px 8px rgba(0,0,0,0.07);
        transition: transform 0.30s cubic-bezier(.34,1.56,.64,1), box-shadow 0.30s;
        animation: fadeSlideUp 0.45s ease both;
        position: relative;
        overflow: hidden;
    }
    .km-product-card::before {
        content: "";
        position: absolute;
        top: 0; left: 8%; right: 8%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.95), transparent);
    }
    .km-product-card::after {
        content: "";
        position: absolute;
        top: 0; right: 0;
        width: 70px; height: 70px;
        background: radial-gradient(circle at top right,
            rgba(249,168,37,0.25) 0%, transparent 70%);
        border-radius: 0 20px 0 0;
    }
    .km-product-card:hover {
        transform: translateY(-8px) rotateX(3deg);
        box-shadow:
            0 1px 0 rgba(255,255,255,0.95) inset,
            0 -3px 0 rgba(244,185,66,0.25) inset,
            0 20px 48px rgba(244,185,66,0.32),
            0 8px 20px rgba(0,0,0,0.10);
        animation: goldPulse 2s infinite;
    }
    .km-product-card h3 {
        font-family: 'Playfair Display', serif;
        color: var(--soil-brown);
        margin: 0 0 12px;
        font-size: 1.18rem;
    }
    .km-product-card p {
        color: #5a4020;
        margin: 5px 0;
        font-size: 0.92rem;
        font-weight: 600;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── FOOTER ─────────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-footer {
        background: linear-gradient(135deg, #0d2210 0%, #1b5e20 50%, #2e7d32 100%);
        border-radius: 24px;
        padding: 36px;
        text-align: center;
        margin-top: 32px;
        box-shadow:
            0 2px 0 rgba(255,255,255,0.08) inset,
            0 -6px 0 rgba(0,0,0,0.18) inset,
            var(--shadow-deep);
        position: relative;
        overflow: hidden;
        animation: fadeSlideUp 0.7s ease both;
    }
    .km-footer::before {
        content: "🌾🌱🌾🌱🌾🌱🌾🌱🌾🌱🌾";
        position: absolute;
        top: -8px; left: 0; right: 0;
        font-size: 1.5rem;
        opacity: 0.12;
        letter-spacing: 12px;
        white-space: nowrap;
        overflow: hidden;
        filter: blur(0.5px);
    }
    .km-footer::after {
        content: "";
        position: absolute;
        top: 0; left: 5%; right: 5%;
        height: 2px;
        background: linear-gradient(90deg,
            transparent,
            rgba(255,213,79,0.50) 30%,
            rgba(255,255,255,0.30) 50%,
            rgba(255,213,79,0.50) 70%,
            transparent);
        border-radius: 50%;
    }
    .km-footer .km-footer-logo {
        font-size: 3rem;
        display: inline-block;
        animation: sway 3.5s ease-in-out infinite;
        filter: drop-shadow(0 6px 16px rgba(0,0,0,0.4)) drop-shadow(0 0 20px rgba(249,168,37,0.5));
    }
    .km-footer h3 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(135deg, #ffd54f, #f9a825, #fff8e1) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 1.5rem !important;
        margin: 10px 0 5px !important;
        filter: drop-shadow(0 2px 8px rgba(249,168,37,0.4));
    }
    .km-footer .km-tagline { color: #a5d6a7 !important; font-size: 0.95rem; margin: 0 0 6px; }
    .km-footer .km-love   { color: #c8e6c9 !important; font-size: 0.88rem; margin: 0 0 14px; }
    .km-footer .km-copy   {
        color: rgba(255,255,255,0.38) !important;
        font-size: 0.74rem;
        border-top: 1px solid rgba(255,255,255,0.10);
        padding-top: 12px;
        margin-top: 8px;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── TABS ───────────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(56,142,60,0.10);
        backdrop-filter: blur(8px);
        border-radius: 50px;
        padding: 5px;
        gap: 4px;
        box-shadow: 0 2px 12px rgba(27,94,32,0.10),
                    0 1px 0 rgba(255,255,255,0.60) inset;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 50px !important;
        font-weight: 800;
        font-family: 'Nunito', sans-serif;
        transition: all 0.25s cubic-bezier(.34,1.56,.64,1);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1b5e20, #43a047, #66bb6a) !important;
        color: white !important;
        box-shadow:
            0 1px 0 rgba(255,255,255,0.25) inset,
            0 -2px 0 rgba(0,0,0,0.15) inset,
            0 4px 16px rgba(27,94,32,0.30) !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── FILE UPLOADER ─────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stFileUploader {
        border: 2px dashed rgba(102,187,106,0.55) !important;
        border-radius: 18px !important;
        background: rgba(240,250,240,0.70) !important;
        backdrop-filter: blur(8px) !important;
        transition: all 0.25s ease;
        box-shadow: 0 2px 12px rgba(27,94,32,0.08);
    }
    .stFileUploader:hover {
        border-color: #66bb6a !important;
        background: rgba(232,245,233,0.85) !important;
        box-shadow: 0 4px 20px rgba(27,94,32,0.14);
        transform: scale(1.01);
    }

    /* ─────────────────────────────────────────────────── */
    /* ── CHAT MESSAGES ─────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    [data-testid="stChatMessage"] {
        background: var(--glass-bg) !important;
        backdrop-filter: var(--glass-blur) !important;
        -webkit-backdrop-filter: var(--glass-blur) !important;
        border-radius: 18px !important;
        border: 1.5px solid rgba(255,255,255,0.75) !important;
        box-shadow: var(--shadow-3d) !important;
        margin-bottom: 12px !important;
        animation: fadeSlideUp 0.35s ease both;
        transition: transform 0.2s ease !important;
    }
    [data-testid="stChatMessage"]:hover {
        transform: translateY(-2px) !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── ALERTS / INFO / SUCCESS ──────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stAlert {
        border-radius: 16px !important;
        border-left-width: 5px !important;
        font-family: 'Nunito', sans-serif !important;
        backdrop-filter: blur(8px) !important;
        background: rgba(255,255,255,0.80) !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── SPINNER ──────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .stSpinner > div {
        border-top-color: #66bb6a !important;
        border-width: 3px !important;
        filter: drop-shadow(0 0 8px rgba(102,187,106,0.6));
    }

    /* ─────────────────────────────────────────────────── */
    /* ── DIVIDER ──────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    hr {
        border: none !important;
        height: 1.5px !important;
        background: linear-gradient(90deg,
            transparent, rgba(102,187,106,0.35) 25%,
            rgba(249,168,37,0.25) 50%,
            rgba(102,187,106,0.35) 75%,
            transparent) !important;
        margin: 24px 0 !important;
    }

    /* ─────────────────────────────────────────────────── */
    /* ── SCROLLBAR ─────────────────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track {
        background: rgba(240,250,240,0.50);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #66bb6a, #f9a825);
        border-radius: 10px;
        box-shadow: 0 0 6px rgba(102,187,106,0.4);
    }

    /* ─────────────────────────────────────────────────── */
    /* ── USER GUIDE LIST ITEMS ─────────────────────────── */
    /* ─────────────────────────────────────────────────── */

    .km-guide-item {
        background: var(--glass-bg);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border-radius: 15px;
        padding: 15px 20px;
        margin-bottom: 10px;
        border: 1.5px solid rgba(255,255,255,0.75);
        box-shadow: var(--shadow-3d);
        font-size: 0.95rem;
        color: #1b3a1e;
        display: flex;
        align-items: center;
        gap: 12px;
        transition: transform 0.25s cubic-bezier(.34,1.56,.64,1), box-shadow 0.25s;
        animation: fadeSlideUp 0.4s ease both;
        position: relative;
        overflow: hidden;
    }
    .km-guide-item::before {
        content: "";
        position: absolute;
        top: 0; left: 8%; right: 8%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.90), transparent);
    }
    .km-guide-item:hover {
        transform: translateX(8px) translateY(-2px);
        box-shadow: var(--shadow-lift);
        border-color: rgba(102,187,106,0.40);
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================================================================
    # SIDEBAR NAVIGATION
    # =========================================================================
    st.sidebar.markdown("""
    <div class="km-sidebar-brand">
        <span class="km-logo-anim">🌾</span>
        <h2>Krishi Mitra</h2>
        <p>Your Intelligent Farming Companion</p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("---")

    # Navigation with translated labels
    page_options = [
        get_text('home', selected_lang),
        get_text('ai_assistant', selected_lang),
        get_text('crop_diagnosis', selected_lang),
        get_text('crop_knowledge', selected_lang),
        get_text('community', selected_lang),
        get_text('schemes', selected_lang),
        get_text('products', selected_lang)
    ]

    page = st.sidebar.radio(
        get_text('select_feature', selected_lang),
        options=page_options
    )

    # Language selector in sidebar
    st.sidebar.markdown(f"### 🌐 {get_text('language', selected_lang)}")
    lang_options = {
        'en': 'English',
        'mr': 'मराठी (Marathi)',
        'hi': 'हिन्दी (Hindi)',
        'gu': 'ગુજરાતી (Gujarati)',
        'ta': 'தமிழ் (Tamil)',
        'te': 'తెలుగు (Telugu)',
        'kn': 'ಕನ್ನಡ (Kannada)'
    }

    selected_lang_key = st.sidebar.selectbox(
        "Select Language / भाषा चुनें",
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=list(lang_options.keys()).index(selected_lang),
        key='language_selector'
    )

    # Update session state if language changed
    if selected_lang_key != selected_lang:
        st.session_state['selected_language'] = selected_lang_key
        st.rerun()

    st.sidebar.markdown("---")

    # =========================================================================
    # HOME PAGE
    # =========================================================================
    if page == get_text('home', selected_lang):
        st.markdown(f"""
        <div class="km-hero">
            <div class="km-hero-orb"></div>
            <h1>&#127806; Krishi Mitra</h1>
            <h3>{get_text("welcome", selected_lang)}, {user["farmer_name"]}! &#128591;</h3>
        </div>
        """, unsafe_allow_html=True)

        st.subheader(get_text('user_guide', selected_lang))
        st.markdown(
            f"<p style='color:#2e7d32;font-weight:800;margin-bottom:10px;font-size:1.02rem;'>"
            f"{get_text('how_to_use', selected_lang)}</p>",
            unsafe_allow_html=True
        )
        for i, key in enumerate(['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6'], 1):
            text = get_text(key, selected_lang)
            st.markdown(
                f'<div class="km-guide-item" style="animation-delay:{i * 0.08}s">'
                f'<span style="font-size:1.15rem;min-width:28px;text-align:center;'
                f'background:linear-gradient(135deg,#2e7d32,#66bb6a);'
                f'-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
                f'font-weight:900;">{i}.</span>{text}</div>',
                unsafe_allow_html=True
            )

        # Feature cards
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        cards = [
            ("🤖", get_text('ai_assistant', selected_lang).split(' ', 1)[-1], get_text('ask_question', selected_lang)),
            ("📸", get_text('crop_diagnosis', selected_lang).split(' ', 1)[-1], get_text('upload_image', selected_lang)),
            ("👥", get_text('community', selected_lang).split(' ', 1)[-1], get_text('share_experience', selected_lang)),
        ]
        for col, (icon, title, desc) in zip([col1, col2, col3], cards):
            with col:
                st.markdown(f"""
                <div class="km-feature-card">
                    <div class="km-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)

        # Stats
        st.markdown("---")
        st.subheader(get_text('platform_overview', selected_lang))

        col1, col2, col3 = st.columns(3)

        posts = get_all_posts(limit=1000)
        products = get_all_products(limit=1000)

        with col1:
            st.metric(get_text('community', selected_lang).split(' ')[1], len(posts))
        with col2:
            st.metric(get_text('products', selected_lang).split(' ')[1], len(products))
        with col3:
            st.metric(get_text('language', selected_lang), len(SUPPORTED_LANGUAGES))

        # Footer on home page
        st.markdown("---")
        ft = TRANSLATIONS.get(selected_lang, TRANSLATIONS['en'])
        st.markdown(f"""
        <div class="km-footer">
            <div class="km-footer-logo">&#127806;</div>
            <h3>Krishi Mitra</h3>
            <p class="km-tagline">{ft['tagline']}</p>
            <p class="km-love">{ft['made_with_love']}</p>
            <p class="km-copy">{ft['copyright']}</p>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================================
    # AI FARMING ASSISTANT - NO VOICE
    # =========================================================================
    elif page == get_text('ai_assistant', selected_lang):
        st.header(get_text('ai_assistant', selected_lang))

        st.markdown(f"🌐 {get_text('language', selected_lang)}: **{get_language_name(selected_lang)}**")
        st.markdown(get_text('ask_question', selected_lang))

        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display chat history - NO VOICE BUTTONS
        for idx, message in enumerate(st.session_state.chat_history):
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if "language" in message:
                    st.caption(f"{get_text('language', selected_lang)}: {get_language_name(message['language'])}")

        # Text input
        user_query = st.chat_input(get_text('type_here', selected_lang))

        if user_query:
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_query
            })

            with st.chat_message("user"):
                st.write(user_query)

            with st.spinner("🤖 Thinking..."):
                response = ai_service.get_farming_response(user_query, selected_lang)

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response,
                "language": selected_lang
            })

            with st.chat_message("assistant"):
                st.write(response)
                st.caption(f"{get_text('language', selected_lang)}: {get_language_name(selected_lang)}")

        # Quick questions
        st.markdown("---")
        st.subheader(get_text('quick_questions', selected_lang))

        quick_questions = {
            'en': ["How to control aphids?", "Best fertilizer for rice", "Organic pest control", "Water management"],
            'mr': ["अ‍ॅफिड्स कसे नियंत्रित करावे?", "भातासाठी सर्वोत्तम खत", "सेंद्रिय कीटक नियंत्रण", "पाणी व्यवस्थापन"],
            'hi': ["एफिड्स को कैसे नियंत्रित करें?", "चावल के लिए उर्वरक", "जैविक कीट नियंत्रण", "जल प्रबंधन"],
            'gu': ["એફિડ્સને કેવી રીતે નિયંત્રિત કરવા?", "ધાન્ય માટે ખાતર", "જૈવિક જીવાત નિયંત્રણ", "પાણીનું વ્યવસ્થાપન"],
            'ta': ["அஃபிட்களை கட்டுப்படுத்துவது?", "நெல்லுக்கு உரம்", "உயிரியல் பூச்சி கட்டுப்பாடு", "நீர் மேலாண்மை"],
            'te': ["ఎఫిడ్లను నియంత్రించడం?", "వరికి ఎరువు", "సేంద్రీయ పురుగు నియంత్రణ", "నీటి నిర్వహణ"],
            'kn': ["ಎಫಿಡ್‌ಗಳನ್ನು ನಿಯಂತ್ರಿಸುವುದು?", "ಭತ್ತಕ್ಕೆ ಗೊಬ್ಬರ", "ಸಾವಯವ ಕೀಟ ನಿಯಂತ್ರಣ", "ನೀರಿನ ವ್ಯವಸ್ಥಾಪನೆ"]
        }

        questions = quick_questions.get(selected_lang, quick_questions['en'])

        cols = st.columns(len(questions))
        for idx, question in enumerate(questions):
            with cols[idx]:
                if st.button(question[:15] + "...", key=f"quick_{idx}"):
                    st.session_state.chat_history.append({
                        "role": "user",
                        "content": question
                    })
                    st.rerun()

    # =========================================================================
    # CROP DIAGNOSIS - NO VOICE
    # =========================================================================
    elif page == get_text('crop_diagnosis', selected_lang):
        st.header(get_text('crop_diagnosis', selected_lang))

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader(get_text('upload_image', selected_lang))
            uploaded_file = st.file_uploader(
                "Choose image",
                type=['jpg', 'jpeg', 'png'],
                help="Upload clear photo"
            )

            additional_context = st.text_area(
                "Additional info (optional)",
                placeholder="Describe symptoms..."
            )

            analyze_btn = st.button(get_text('analyze', selected_lang), type="primary")

        with col2:
            st.subheader(get_text('preview', selected_lang))
            if uploaded_file:
                is_valid, msg = validate_image(uploaded_file)
                if is_valid:
                    image = Image.open(uploaded_file)
                    st.image(image, use_column_width=True)
                else:
                    st.error(msg)
            else:
                st.info("Image preview will appear here")

        if analyze_btn and uploaded_file:
            is_valid, msg = validate_image(uploaded_file)
            if not is_valid:
                st.error(msg)
            else:
                with st.spinner("🧠 Analyzing..."):
                    compressed_image = compress_image(uploaded_file)

                    if compressed_image:
                        analysis = ai_service.analyze_crop_image(
                            compressed_image,
                            additional_context,
                            selected_lang
                        )

                        st.markdown("---")
                        st.subheader(get_text('analysis_report', selected_lang))
                        st.markdown(analysis)
                    else:
                        st.error("Failed to process image")

    # =========================================================================
    # CROP KNOWLEDGE - NO VOICE
    # =========================================================================
    elif page == get_text('crop_knowledge', selected_lang):
        st.header(get_text('crop_knowledge', selected_lang))

        crop_name = st.text_input(
            get_text('enter_crop', selected_lang),
            placeholder="e.g., Wheat, Rice, Cotton..."
        )

        if st.button(get_text('generate', selected_lang), type="primary") and crop_name:
            with st.spinner("🌱 Generating..."):
                knowledge = ai_service.generate_crop_knowledge(crop_name, selected_lang)

                st.markdown("---")
                st.markdown(knowledge)

    # =========================================================================
    # FARMER COMMUNITY - NO VOICE
    # =========================================================================
    elif page == get_text('community', selected_lang):
        st.header(get_text('community', selected_lang))

        tab1, tab2 = st.tabs([get_text('view_posts', selected_lang), get_text('create_post', selected_lang)])

        with tab1:
            st.subheader(get_text('view_posts', selected_lang))

            posts = get_all_posts(limit=20)

            if not posts:
                st.info("No posts yet!")
            else:
                for post in posts:
                    with st.container():
                        st.markdown(f"""
                        <div class="km-post-card">
                            <h4>&#128100; {post['farmer_name']}</h4>
                            <p>{post['content']}</p>
                            <small>&#128336; {format_datetime(post['created_at'])}</small>
                        </div>
                        """, unsafe_allow_html=True)

                        if post['image_path'] and os.path.exists(post['image_path']):
                            st.image(post['image_path'], use_column_width=True)

                        if post['video_path'] and os.path.exists(post['video_path']):
                            st.video(post['video_path'])

                        st.markdown("---")

        with tab2:
            st.subheader(get_text('create_post', selected_lang))

            with st.form("post_form"):
                farmer_name = st.text_input(get_text('your_name', selected_lang), value=user['farmer_name'])
                content = st.text_area(
                    get_text('share_experience', selected_lang),
                    placeholder="Share your experience..."
                )

                col1, col2 = st.columns(2)
                with col1:
                    image_file = st.file_uploader(get_text('attach_photo', selected_lang), type=['jpg', 'jpeg', 'png'])
                with col2:
                    video_file = st.file_uploader(get_text('attach_video', selected_lang), type=['mp4'])

                submitted = st.form_submit_button(get_text('post', selected_lang), type="primary")

                if submitted:
                    if not content:
                        st.error("Please enter content!")
                    else:
                        image_path = None
                        video_path = None

                        if image_file:
                            is_valid, msg = validate_image(image_file)
                            if not is_valid:
                                st.error(f"Image error: {msg}")
                                st.stop()
                            image_path = save_uploaded_file(image_file, IMAGES_DIR)

                        if video_file:
                            is_valid, msg = validate_video(video_file)
                            if not is_valid:
                                st.error(f"Video error: {msg}")
                                st.stop()
                            video_path = save_uploaded_file(video_file, VIDEOS_DIR)

                        post_id = create_post(farmer_name, content, image_path, video_path)
                        st.success("Posted successfully!")
                        st.balloons()
                        st.rerun()

    # =========================================================================
    # GOVERNMENT SCHEMES - NO VOICE
    # =========================================================================
    elif page == get_text('schemes', selected_lang):
        st.header(get_text('schemes', selected_lang))

        scheme_query = st.text_input(
            get_text('ask_scheme', selected_lang),
            placeholder="e.g., PM-KISAN, Soil Health Card..."
        )

        if st.button(get_text('search', selected_lang), type="primary") and scheme_query:
            with st.spinner("🏛️ Fetching..."):
                info = ai_service.get_government_scheme_info(scheme_query, selected_lang)

                st.markdown("---")
                st.markdown(info)

        st.markdown("---")
        st.subheader(get_text('popular_schemes', selected_lang))

        schemes = [
            ("PM-KISAN", "Pradhan Mantri Kisan Samman Nidhi"),
            ("Soil Health Card", "Free soil testing"),
            ("KCC", "Kisan Credit Card"),
            ("PMFBY", "Crop Insurance"),
            ("MIDH", "Horticulture Mission"),
            ("NMOOP", "Oilseeds Mission")
        ]

        cols = st.columns(3)
        for idx, (short_name, full_name) in enumerate(schemes):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="km-scheme-card">
                    <h4>{short_name}</h4>
                    <p>{full_name}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"{get_text('search', selected_lang)} {short_name}", key=f"scheme_{idx}"):
                    st.session_state.scheme_query = short_name
                    st.rerun()

    # =========================================================================
    # ORGANIC PRODUCTS - NO VOICE
    # =========================================================================
    elif page == get_text('products', selected_lang):
        st.header(get_text('products', selected_lang))

        tab1, tab2 = st.tabs([get_text('browse_products', selected_lang), get_text('list_product', selected_lang)])

        with tab1:
            st.subheader(get_text('browse_products', selected_lang))

            search = st.text_input(get_text('search', selected_lang))

            if search:
                products = search_products(search)
            else:
                products = get_all_products(limit=50)

            if not products:
                st.info("No products listed yet!")
            else:
                cols = st.columns(2)
                for idx, product in enumerate(products):
                    with cols[idx % 2]:
                        st.markdown(f"""
                        <div class="km-product-card">
                            <h3>&#129388; {product['product_name']}</h3>
                            <p><strong>Farmer:</strong> {product['farmer_name']}</p>
                            <p><strong>{get_text('quantity', selected_lang)}:</strong> {product['quantity']}</p>
                            <p><strong>{get_text('location', selected_lang)}:</strong> &#128205; {product['location']}</p>
                            <p><strong>{get_text('phone', selected_lang)}:</strong> &#128222; {product['phone_number']}</p>
                        </div>
                        """, unsafe_allow_html=True)

        with tab2:
            st.subheader(get_text('list_product', selected_lang))

            with st.form("product_form"):
                col1, col2 = st.columns(2)

                with col1:
                    farmer_name = st.text_input(get_text('your_name', selected_lang), value=user['farmer_name'])
                    product_name = st.text_input(get_text('product_name', selected_lang), placeholder="e.g., Organic Tomatoes")
                    quantity = st.text_input(get_text('quantity', selected_lang), placeholder="e.g., 50 kg")

                with col2:
                    location = st.text_input(get_text('location', selected_lang), value=user['location'])
                    phone = st.text_input(get_text('phone', selected_lang), value=user['mobile_email'])

                submitted = st.form_submit_button(get_text('list', selected_lang), type="primary")

                if submitted:
                    if not all([farmer_name, product_name, quantity, location, phone]):
                        st.error("Please fill all fields!")
                    elif len(phone) < 10:
                        st.error("Invalid phone number!")
                    else:
                        product_id = add_product(farmer_name, product_name, quantity, location, phone)
                        st.success("Listed successfully!")
                        st.balloons()
                        st.rerun()

    # =========================================================================
    # FOOTER - All Languages, Copyright 2026
    # =========================================================================
    ft = TRANSLATIONS.get(selected_lang, TRANSLATIONS['en'])

    st.markdown("---")
    st.markdown(f"""
    <div class="km-footer">
        <div class="km-footer-logo">&#127806;</div>
        <h3>Krishi Mitra</h3>
        <p class="km-tagline">{ft['tagline']}</p>
        <p class="km-love">{ft['made_with_love']}</p>
        <p class="km-copy">{ft['copyright']}</p>
    </div>
    """, unsafe_allow_html=True)
