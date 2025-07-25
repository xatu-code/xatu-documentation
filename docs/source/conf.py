# Configuration file for the Sphinx documentation builder.

# -* Project information

project = 'Xatu'
copyright = '2024, Atomelix'
author = 'Atomelix'

release = '1.0'
version = '1.3.1'

# -* General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"], ["$", "$"]],
        "macros": {
            "bm": "\\boldsymbol"
        }
    }
}

html_static_path = ['_static']
html_logo = "images/xatu_logo.svg"   # path relative to conf.py

def setup(app):
    app.add_css_file('custom.css')


intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -* Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -* Options for EPUB output
epub_show_urls = 'footnote'
