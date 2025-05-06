"""Sphinx-Konfigurationsdatei.

Diese Datei konfiguriert Sphinx für die automatische Dokumentationsgenerierung.
"""

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# Füge das Projektverzeichnis zum Pfad hinzu
sys.path.insert(0, str(Path(__file__).parents[2].resolve()))

# -- Projektinformationen -----------------------------------------------------
project = 'Python-Template'
copyright = '2025, Dein Name'
author = 'Dein Name'
release = '0.1.0'

# -- Allgemeine Konfiguration -------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Automatische API-Dokumentation
    'sphinx.ext.viewcode',       # "Quellcode anzeigen"-Links
    'sphinx.ext.napoleon',       # Google-Style Docstrings
    'sphinx.ext.intersphinx',    # Verweise auf andere Dokumentationen
    'sphinx_rtd_theme',          # ReadTheDocs-Theme
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'de'  # Deutsch als Standardsprache

# -- Optionen für HTML-Ausgabe ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Konfiguration für Napoleon (Google-Style Docstrings) ---------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True

# -- Intersphinx-Konfiguration ------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
}