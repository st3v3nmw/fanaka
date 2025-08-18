# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

html_title = full_title = project = 'Fanaka'
copyright = '2025 Daniele Procida and contributors, licensed under CC BY-SA 4.0'
author = 'Daniele Procida and contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx', 'sphinxcontrib.spelling']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env', 'readme.rst']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "top_of_page_buttons": ["edit"],
    "source_repository": "https://github.com/evildmp/fanaka/",
    "source_branch": "main",
}

html_static_path = ['_static']
html_css_files = ["fanaka.css"
]

intersphinx_mapping = {'vurt': ('https://vurt.eu', None)}

spelling_lang = tokenizer_lang = "en_GB"

locale_dirs = ['translations/']
gettext_compact = False
