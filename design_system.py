"""
Modern Design System for Krishi Mitra
Inspired by Linear, Stripe, and Apple design principles
"""

# ============================================================================
# DESIGN TOKENS - The foundation of our design system
# ============================================================================

COLORS = {
    # Primary Colors - Nature-inspired greens
    "primary": {
        "50": "#ECFDF5",
        "100": "#D1FAE5",
        "200": "#A7F3D0",
        "300": "#6EE7B7",
        "400": "#34D399",
        "500": "#10B981",  # Primary brand color
        "600": "#059669",
        "700": "#047857",
        "800": "#065F46",
        "900": "#064E3B",
    },
    
    # Semantic Colors
    "success": {
        "light": "#D1FAE5",
        "DEFAULT": "#10B981",
        "dark": "#047857",
    },
    "warning": {
        "light": "#FEF3C7",
        "DEFAULT": "#F59E0B",
        "dark": "#B45309",
    },
    "error": {
        "light": "#FEE2E2",
        "DEFAULT": "#EF4444",
        "dark": "#B91C1C",
    },
    "info": {
        "light": "#DBEAFE",
        "DEFAULT": "#3B82F6",
        "dark": "#1D4ED8",
    },
    
    # Neutral Colors - Modern gray scale
    "gray": {
        "50": "#F9FAFB",
        "100": "#F3F4F6",
        "200": "#E5E7EB",
        "300": "#D1D5DB",
        "400": "#9CA3AF",
        "500": "#6B7280",
        "600": "#4B5563",
        "700": "#374151",
        "800": "#1F2937",
        "900": "#111827",
    },
    
    # Dark Mode Colors
    "dark": {
        "bg": "#0F172A",       # Deep blue-gray
        "bgSecondary": "#1E293B",
        "card": "#1E293B",
        "border": "#334155",
        "text": "#F1F5F9",
        "textSecondary": "#94A3B8",
    },
    
    # Light Mode Colors
    "light": {
        "bg": "#FFFFFF",
        "bgSecondary": "#F9FAFB",
        "card": "#FFFFFF",
        "border": "#E5E7EB",
        "text": "#111827",
        "textSecondary": "#6B7280",
    },
    
    # Accent Colors
    "accent": {
        "primary": "#10B981",
        "secondary": "#6366F1",
        "tertiary": "#F59E0B",
    },
}

# Typography Scale - Modern and readable
TYPOGRAPHY = {
    "fontFamily": {
        "primary": '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        "secondary": '"Poppins", "Inter", sans-serif',
    },
    "fontSize": {
        "xs": "0.75rem",    # 12px
        "sm": "0.875rem",   # 14px
        "base": "1rem",     # 16px
        "lg": "1.125rem",   # 18px
        "xl": "1.25rem",    # 20px
        "2xl": "1.5rem",    # 24px
        "3xl": "1.875rem",  # 30px
        "4xl": "2.25rem",   # 36px
        "5xl": "3rem",      # 48px
    },
    "fontWeight": {
        "normal": 400,
        "medium": 500,
        "semibold": 600,
        "bold": 700,
    },
    "lineHeight": {
        "tight": 1.25,
        "normal": 1.5,
        "relaxed": 1.75,
    },
}

# Spacing System - Consistent 4px base unit
SPACING = {
    "0": "0",
    "1": "0.25rem",   # 4px
    "2": "0.5rem",    # 8px
    "3": "0.75rem",   # 12px
    "4": "1rem",      # 16px
    "5": "1.25rem",   # 20px
    "6": "1.5rem",    # 24px
    "8": "2rem",      # 32px
    "10": "2.5rem",   # 40px
    "12": "3rem",     # 48px
    "16": "4rem",     # 64px
}

# Border Radius - Modern, subtle curves
BORDER_RADIUS = {
    "none": "0",
    "sm": "0.375rem",   # 6px
    "base": "0.5rem",   # 8px
    "md": "0.75rem",    # 12px
    "lg": "1rem",       # 16px
    "xl": "1.5rem",     # 24px
    "full": "9999px",
}

# Shadows - Subtle, layered shadows for depth
SHADOWS = {
    "none": "none",
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "base": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
    "2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
}

# Transitions - Smooth, performant animations
TRANSITIONS = {
    "fast": "150ms cubic-bezier(0.4, 0, 0.2, 1)",
    "base": "200ms cubic-bezier(0.4, 0, 0.2, 1)",
    "slow": "300ms cubic-bezier(0.4, 0, 0.2, 1)",
    "bounce": "500ms cubic-bezier(0.68, -0.55, 0.265, 1.55)",
}

# Breakpoints - Responsive design
BREAKPOINTS = {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px",
}

# Z-index Scale - Layer management
Z_INDEX = {
    "dropdown": 1000,
    "sticky": 1020,
    "fixed": 1030,
    "modalBackdrop": 1040,
    "modal": 1050,
    "popover": 1060,
    "tooltip": 1070,
}

# ============================================================================
# CSS GENERATOR FUNCTIONS
# ============================================================================

def generate_root_variables():
    """Generate CSS custom properties for design tokens."""
    css_vars = []
    
    # Colors
    for color_name, color_values in COLORS.items():
        if isinstance(color_values, dict):
            for shade, value in color_values.items():
                css_vars.append(f"--color-{color_name}-{shade}: {value};")
    
    # Typography
    for type_name, value in TYPOGRAPHY.items():
        if isinstance(value, dict):
            for key, val in value.items():
                css_vars.append(f"--{type_name}-{key}: {val};")
    
    # Spacing
    for key, value in SPACING.items():
        css_vars.append(f"--spacing-{key}: {value};")
    
    # Border Radius
    for key, value in BORDER_RADIUS.items():
        css_vars.append(f"--radius-{key}: {value};")
    
    # Shadows
    for key, value in SHADOWS.items():
        css_vars.append(f"--shadow-{key}: {value};")
    
    # Transitions
    for key, value in TRANSITIONS.items():
        css_vars.append(f"--transition-{key}: {value};")
    
    return "\n    ".join(css_vars)


def get_color(variant, shade="500"):
    """Get color value from design system."""
    return COLORS.get(variant, {}).get(shade, "#000000")


# ============================================================================
# COMPONENT STYLES
# ============================================================================

CARD_STYLES = {
    "base": {
        "background": COLORS["light"]["card"],
        "border": f"1px solid {COLORS['gray']['200']}",
        "borderRadius": BORDER_RADIUS["lg"],
        "shadow": SHADOWS["base"],
        "padding": SPACING["6"],
    },
    "hover": {
        "shadow": SHADOWS["lg"],
        "transform": "translateY(-2px)",
    },
    "dark": {
        "background": COLORS["dark"]["card"],
        "border": f"1px solid {COLORS['dark']['border']}",
    },
}

BUTTON_STYLES = {
    "primary": {
        "background": f"linear-gradient(135deg, {COLORS['primary']['500']}, {COLORS['primary']['600']})",
        "color": "#FFFFFF",
        "borderRadius": BORDER_RADIUS["md"],
        "padding": f"{SPACING['3']} {SPACING['6']}",
        "fontWeight": TYPOGRAPHY["fontWeight"]["medium"],
        "transition": f"all {TRANSITIONS['base']}",
        "shadow": SHADOWS["base"],
        "hover": {
            "shadow": SHADOWS["md"],
            "transform": "translateY(-1px)",
        },
    },
    "secondary": {
        "background": COLORS["light"]["bg"],
        "color": COLORS["gray"]["700"],
        "border": f"1px solid {COLORS['gray']['300']}",
        "borderRadius": BORDER_RADIUS["md"],
        "padding": f"{SPACING['3']} {SPACING['6']}",
        "fontWeight": TYPOGRAPHY["fontWeight"]["medium"],
        "transition": f"all {TRANSITIONS['base']}",
        "hover": {
            "background": COLORS["gray"]["50"],
            "borderColor": COLORS["gray"]["400"],
        },
    },
}

INPUT_STYLES = {
    "base": {
        "border": f"1px solid {COLORS['gray']['300']}",
        "borderRadius": BORDER_RADIUS["md"],
        "padding": f"{SPACING['3']} {SPACING['4']}",
        "fontSize": TYPOGRAPHY["fontSize"]["base"],
        "transition": f"all {TRANSITIONS['fast']}",
        "focus": {
            "borderColor": COLORS["primary"]["500"],
            "boxShadow": f"0 0 0 3px {COLORS['primary']['100']}",
        },
    },
}

# ============================================================================
# UTILITY CLASSES
# ============================================================================

UTILITY_CLASSES = {
    "text": {
        "heading": f"font-{TYPOGRAPHY['fontWeight']['bold']} text-{TYPOGRAPHY['fontSize']['3xl']}",
        "subheading": f"font-{TYPOGRAPHY['fontWeight']['semibold']} text-{TYPOGRAPHY['fontSize']['xl']}",
        "body": f"font-{TYPOGRAPHY['fontWeight']['normal']} text-{TYPOGRAPHY['fontSize']['base']}",
        "caption": f"font-{TYPOGRAPHY['fontWeight']['normal']} text-{TYPOGRAPHY['fontSize']['sm']}",
    },
    "flex": {
        "center": "flex items-center justify-center",
        "between": "flex items-center justify-between",
        "start": "flex items-center justify-start",
        "end": "flex items-center justify-end",
    },
    "spacing": {
        "gap-2": f"gap: {SPACING['2']}",
        "gap-4": f"gap: {SPACING['4']}",
        "gap-6": f"gap: {SPACING['6']}",
        "gap-8": f"gap: {SPACING['8']}",
    },
}

# Export design system
__all__ = [
    "COLORS",
    "TYPOGRAPHY",
    "SPACING",
    "BORDER_RADIUS",
    "SHADOWS",
    "TRANSITIONS",
    "BREAKPOINTS",
    "Z_INDEX",
    "CARD_STYLES",
    "BUTTON_STYLES",
    "INPUT_STYLES",
    "generate_root_variables",
    "get_color",
]
