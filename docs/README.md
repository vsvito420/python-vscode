# Projektdokumentation

Dieses Verzeichnis enthält die Dokumentation für dein Projekt. Eine gute Dokumentation ist entscheidend, damit andere (und du selbst in der Zukunft) dein Projekt verstehen können.

## Dokumentationsstruktur

Eine typische Dokumentationsstruktur könnte so aussehen:

```
docs/
├── README.md                 # Diese Datei
├── getting_started.md        # Erste Schritte für neue Benutzer
├── api/                      # API-Dokumentation
│   ├── module1.md
│   └── module2.md
├── guides/                   # Anleitungen und Tutorials
│   ├── installation.md
│   └── usage_examples.md
└── development/              # Informationen für Entwickler
    ├── contributing.md
    └── testing.md
```

## Dokumentationstools

### Für einfache Projekte

- **Markdown**: Einfach zu schreiben und auf GitHub gut dargestellt
- **MkDocs**: Erstellt schöne Dokumentationswebseiten aus Markdown-Dateien
  - Installation: `pip install mkdocs`
  - [MkDocs-Dokumentation](https://www.mkdocs.org/)

### Für umfangreichere Projekte

- **Sphinx**: Das Standard-Dokumentationstool für Python-Projekte
  - Installation: `pip install sphinx`
  - [Sphinx-Dokumentation](https://www.sphinx-doc.org/)
  - Unterstützt reStructuredText und Markdown
  - Automatische API-Dokumentation aus Docstrings
  - PDF, HTML, ePub und mehr Ausgabeformate

- **Read the Docs**: Kostenlose Dokumentationshosting-Plattform
  - [Read the Docs](https://readthedocs.org/)
  - Integriert mit GitHub/GitLab
  - Automatische Builds bei jedem Push

## Docstrings in Python

Gute Docstrings sind essentiell für eine gute API-Dokumentation. In diesem Projekt verwenden wir die Google-Docstring-Konvention:

```python
def meine_funktion(param1, param2):
    """Kurze Beschreibung der Funktion.

    Längere Beschreibung der Funktion mit Details.

    Args:
        param1: Beschreibung des ersten Parameters
        param2: Beschreibung des zweiten Parameters

    Returns:
        Beschreibung des Rückgabewerts

    Raises:
        ValueError: Unter welchen Umständen dieser Fehler auftritt
    """
    # Funktionsimplementierung
```

## Erste Schritte mit Sphinx

Um Sphinx zu initialisieren:

1. Installiere Sphinx: `pip install sphinx sphinx-rtd-theme`
2. Erstelle ein Dokumentationsverzeichnis: `mkdir -p docs`
3. Wechsle in das Verzeichnis: `cd docs`
4. Erstelle eine Sphinx-Konfiguration: `sphinx-quickstart`
5. Bearbeite `conf.py`, um die automatische API-Dokumentation zu aktivieren:

```python
# conf.py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
```

6. Erstelle API-Dokumentation: `sphinx-apidoc -o source/ ../src/`
7. Baue die Dokumentation: `make html`
8. Öffne `_build/html/index.html` im Browser

## Tipps für gute Dokumentation

1. **Aktuell halten**: Veraltete Dokumentation ist schlimmer als keine Dokumentation
2. **Zielgruppe beachten**: Unterscheide zwischen Benutzer- und Entwicklerdokumentation
3. **Beispiele geben**: Praxisbeispiele sind oft verständlicher als umfangreiche Erklärungen
4. **Einfache Sprache**: Vermeide unnötig komplexe Ausdrücke und Fachjargon
5. **Visuell unterstützen**: Diagramme, Screenshots und Grafiken können komplexe Konzepte veranschaulichen