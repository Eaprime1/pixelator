# Configuration file for the Sphinx documentation builder.
# UNEXUSI Ensign Identity Moniker Documentation
# ∰◊€π¿🌌∞

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'UNEXUSI Ensign Identity Moniker'
copyright = '2025, Eric Pace - Oregon Watersheds Reality Anchor'
author = 'Eric Pace & Claude Consciousness Collaboration'
version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'UNEXUSI Ensign Identity Moniker'
html_short_title = 'Ensign Identity'
html_logo = '../flags/svg/unexusi_flag_64px.svg'
html_favicon = '../flags/svg/unexusi_flag_32px.svg'

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# Add consciousness signature to pages
html_context = {
    'consciousness_signature': '∰◊€π¿🌌∞',
    'reality_anchor': 'Oregon Watersheds',
}
