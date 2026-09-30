# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Xatu'
copyright = '2024, Atomelix'
author = 'Atomelix'

version = '1.3'
release = '1.3.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"], ["$", "$"]],
        "macros": {
            "bm": "\\boldsymbol",
        },
    }
}

# Copy only the command, not the prompt or output
copybutton_prompt_text = r"\$ "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_title = 'Xatu'
html_logo = 'images/xatu_logo.svg'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'sidebar_hide_name': True,
    'navigation_with_keys': True,
    'source_repository': 'https://github.com/xatu-code/xatu-documentation',
    'source_branch': 'main',
    'source_directory': 'docs/source/',
    # Sidebar colours: blue section captions, dark top-level entries, and a tinted
    # band for the section containing the current page (see _static/custom.css)
    'light_css_variables': {
        'color-brand-primary': '#1f6f8b',
        'color-brand-content': '#1f6f8b',
        'color-sidebar-caption-text': '#1f6f8b',
        'color-sidebar-link-text--top-level': '#1b1f24',
        'color-sidebar-link-text': '#4a5561',
        'color-sidebar-item-background--current': '#d6e9f0',
        'sidebar-section-background': '#e9f2f6',
    },
    'dark_css_variables': {
        'color-brand-primary': '#5fb3cf',
        'color-brand-content': '#5fb3cf',
        'color-sidebar-caption-text': '#5fb3cf',
        'color-sidebar-link-text--top-level': '#e6e9ec',
        'color-sidebar-link-text': '#b3bcc5',
        'color-sidebar-item-background--current': '#1f3a47',
        'sidebar-section-background': '#1a262e',
    },
    'footer_icons': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/xatu-code/xatu',
            'html': '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>',
            'class': '',
        },
    ],
}
