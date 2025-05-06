# Quellcode-Verzeichnis

Dieses Verzeichnis enthält den Quellcode deines Projekts. Hier findest du eine kurze Anleitung zur Organisation deines Python-Codes.

## Struktur

Eine gute Codestruktur ist wichtig für die Wartbarkeit deines Projekts. Hier ist ein Vorschlag:

```
src/
├── __init__.py             # Macht das Verzeichnis zu einem Python-Paket
├── example_module.py       # Ein Beispielmodul mit Funktionen und Klassen
├── main.py                 # Einstiegspunkt für deine Anwendung (optional)
└── package/                # Ein Unterpaket für verwandte Funktionalität
    ├── __init__.py
    ├── module1.py
    └── module2.py
```

## Bewährte Praktiken

1. **Module vs. Pakete**: 
   - Ein **Modul** ist eine einzelne Python-Datei (z.B. `example_module.py`)
   - Ein **Paket** ist ein Verzeichnis mit einer `__init__.py`-Datei, das Module und weitere Pakete enthalten kann

2. **Namenskonventionen**:
   - Benutze aussagekräftige Namen für Module und Pakete
   - Verwende Kleinbuchstaben und Unterstriche für Modul- und Paketnamen (z.B. `data_processing`)
   - Verwende CamelCase für Klassennamen (z.B. `DataProcessor`)
   - Verwende Kleinbuchstaben und Unterstriche für Funktionen und Methoden (z.B. `process_data`)

3. **Imports**:
   - Importiere Module absolut von der Projektbasis (z.B. `from src.package import module1`)
   - Vermeide sternförmige Imports (`from module import *`)

4. **Dokumentation**:
   - Versehe jedes Modul, jede Klasse und jede Funktion mit einem Docstring
   - Sieh dir `example_module.py` für ein Beispiel an

5. **Typannotationen**:
   - Verwende Typannotationen, um den Code besser lesbar und wartbar zu machen
   - Beispiel: `def process_data(input_data: List[str]) -> Dict[str, int]:`

## Beispiel-Modul

Das `example_module.py` dient als Vorlage für deine eigenen Module. Es zeigt:

1. Wie man Docstrings schreibt
2. Wie man Typannotationen verwendet
3. Wie man Klassen und Funktionen strukturiert
4. Wie man Code testen kann (siehe `tests/test_example_module.py`)

## Weitere Ressourcen

- [PEP 8 Style Guide](https://peps.python.org/pep-0008/) - Offizieller Python-Styleguide
- [PEP 257 Docstring Conventions](https://peps.python.org/pep-0257/) - Konventionen für Docstrings
- [Python-Typannotationen](https://docs.python.org/3/library/typing.html) - Dokumentation zu Typannotationen