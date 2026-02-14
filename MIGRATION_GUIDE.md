🌱 Krishi Mitra - Modern Frontend Migration Guide

📋 Overview

This guide will help you migrate from the legacy codebase to the new modern, modular architecture. The new system is production-ready, maintainable, and follows industry best practices.

🎯 What's Changed?

Architecture Improvements

Before:

- Monolithic main_app.py (1600+ lines)

- Mixed business logic and UI code

- Hard-to-maintain translation system

- Basic CSS without design system

After:

- Modular architecture with clear separation of concerns

- Reusable component library

- Dedicated translation module

- Comprehensive design system with CSS variables

- Feature-based modular structure

📁 New File Structure

workspace/
├── design_system.py          # Design tokens and CSS variables
├── styles_new.py             # Modern styling system
├── components.py             # Reusable UI components
├── translations.py           # Multi-language support
├── main_app_new.py           # Refactored main app (NEW)
├── features/                 # Feature modules (NEW)
│   ├── __init__.py
│   ├── home_page.py
│   ├── ai_assistant.py
│   ├── crop_diagnosis.py
│   ├── crop_knowledge.py
│   ├── community.py
│   ├── schemes.py
│   └── products.py
├── app.py                    # Login page (keep as is)
├── ai_service.py             # AI service (keep as is)
├── database.py               # Database operations (keep as is)
├── config.py                 # Configuration (keep as is)
├── utils.py                  # Utility functions (keep as is)
└── [other existing files...]

🚀 Migration Steps

Step 1: Backup Your Current Code

# Create backup directory
mkdir backup_old

# Backup main files
cp main_app.py backup_old/
cp styles.py backup_old/

Step 2: Update app.py to Use New Main App

Change the import in app.py:

Before:

from main_app import run_main_app

After:

from main_app_new import run_main_app

Step 3: Test the Application

Run the application:

streamlit run app.py

Step 4: Verify All Features

Test each feature:

- ✅ Home Dashboard

- ✅ AI Assistant

- ✅ Crop Diagnosis

- ✅ Crop Knowledge

- ✅ Community

- ✅ Government Schemes

- ✅ Organic Products

- ✅ Multi-language support (all 7 languages)

🎨 Design System Features

Color Palette

- Primary: Nature-inspired greens (#10B981)

- Secondary: Indigo (#6366F1)

- Accent: Amber (#F59E0B)

- Semantic: Success, Warning, Error, Info colors

Typography

- Font Family: Inter (primary), Poppins (secondary)

- Scale: 12px to 48px

- Weights: 400, 500, 600, 700

Spacing System

- 4px base unit

- Consistent margins and padding

- Responsive breakpoints

Shadows & Effects

- Subtle, layered shadows

- Smooth transitions (150ms-300ms)

- Hover effects and micro-interactions

🧩 Component Library

Available Components

modern_card()

Interactive card with icon, title, and content.

modern_card(
    title="Card Title",
    content="Card description",
    icon="🎯",
    on_click=callback_function
)

stat_card()

Statistics display with gradient background.

stat_card(
    label="Total Users",
    value=150,
    icon="👥",
    color="primary"  # primary, secondary, accent
)

product_card()

Product listing card with all details.

product_card(
    product={
        'product_name': 'Organic Tomatoes',
        'farmer_name': 'John Doe',
        'quantity': '50 kg',
        'location': 'Pune',
        'phone_number': '9876543210'
    },
    lang='en'
)

empty_state()

Empty state with optional CTA.

empty_state(
    message="No data found",
    icon="📭",
    action_text="Create New",
    on_action=callback_function
)

chat_message()

Modern chat message display.

chat_message(
    role="assistant",
    content="AI response here",
    language="English"
)

modern_form()

Form builder with multiple field types.

form_data = modern_form(
    fields=[
        {
            'name': 'name',
            'label': 'Name',
            'type': 'text',
            'placeholder': 'Enter name'
        }
    ],
    submit_button_text="Submit",
    on_submit=handle_form
)

🌍 Translation System

Using Translations

from translations import get_text

# Get translated text
translated_text = get_text('welcome', 'mr')

Adding New Translations

Edit translations.py:

TRANSLATIONS = {
    'en': {
        'new_key': 'English text'
    },
    'mr': {
        'new_key': 'मराठी टेक्स्ट'
    }
}

🎨 Custom Styling

Using Design Tokens

from design_system import get_color, COLORS

# Get color value
primary_color = get_color('primary', '500')

Custom CSS Variables

All CSS variables are available in styles_new.py:

- --color-primary-*

- --spacing-*

- --radius-*

- --shadow-*

- --transition-*

📱 Responsive Design

Breakpoints

- Mobile: < 640px

- Tablet: 640px - 1024px

- Desktop: > 1024px

Testing

Test on different screen sizes:

# Chrome DevTools
# 1. Open DevTools (F12)
# 2. Click device toolbar (Ctrl+Shift+M)
# 3. Test different device presets

♿ Accessibility Features

ARIA Labels

All interactive elements have proper ARIA labels.

Keyboard Navigation

- Tab through all elements

- Enter/Space to activate

- Escape to close modals

Color Contrast

WCAG AA compliant (4.5:1 ratio)

Screen Reader Support

Semantic HTML with proper landmarks

🚀 Performance Optimizations

Lazy Loading

Images and components load on demand.

Memoization

Expensive computations are cached.

Code Splitting

Features loaded only when needed.

🐛 Troubleshooting

Issue: Styles Not Loading

Solution: Clear browser cache and restart Streamlit.

Issue: Translation Missing

Solution: Add missing key to translations.py.

Issue: Component Not Working

Solution: Check component import and parameters.

📚 Additional Resources

Design System

- See design_system.py for full token reference

- See styles_new.py for CSS implementation

Components

- See components.py for all available components

- Each component has docstring with usage examples

Features

- See features/ directory for feature implementations

- Each feature is a separate, importable module

🎓 Best Practices

Code Organization

- Keep features in features/ directory

- Use reusable components from components.py

- Follow naming conventions

- Add docstrings to all functions

Styling

- Use design tokens, not hardcoded values

- Follow spacing system

- Use semantic colors

- Test in both light and dark modes

Performance

- Lazy load heavy components

- Optimize images

- Cache expensive operations

- Minimize re-renders

✅ Pre-Deployment Checklist

-  All features working correctly

-  Multi-language support tested

-  Responsive design verified

-  Accessibility tested

-  Performance optimized

-  No console errors

-  All translations complete

-  Dark mode working (if implemented)

🎉 Success!

Your Krishi Mitra application is now modern, maintainable, and production-ready!

Key Achievements

✅ Modular architecture ✅ Reusable components ✅ Design system implementation ✅ Improved UX/UI ✅ Better accessibility ✅ Performance optimized ✅ Production-ready code

Next Steps

- Deploy to production

- Monitor performance

- Gather user feedback

- Iterate and improve

📞 Support

If you encounter any issues:

- Check this migration guide

- Review component documentation

- Test in isolation

- Check browser console for errors

Made with ❤️ for Indian Farmers © 2026 Krishi Mitra
