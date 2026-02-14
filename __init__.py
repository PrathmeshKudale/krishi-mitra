"""
Features Package for Krishi Mitra
Modular feature implementations
"""

from .home_page import render_home_page
from .ai_assistant import render_ai_assistant_page
from .crop_diagnosis import render_crop_diagnosis_page
from .crop_knowledge import render_crop_knowledge_page
from .community import render_community_page
from .schemes import render_schemes_page
from .products import render_products_page

__all__ = [
    'render_home_page',
    'render_ai_assistant_page',
    'render_crop_diagnosis_page',
    'render_crop_knowledge_page',
    'render_community_page',
    'render_schemes_page',
    'render_products_page',
]