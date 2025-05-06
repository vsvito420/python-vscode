# Test-Verzeichnis

Dieses Verzeichnis enthält die Tests für dein Projekt. Hier findest du eine kurze Anleitung zum Testen deines Python-Codes mit pytest.

## Struktur

Die Teststruktur sollte die Struktur deines Quellcodes widerspiegeln:

```
tests/
├── __init__.py                 # Macht das Verzeichnis zu einem Python-Paket
├── test_example.py             # Einfacher Beispieltest
├── test_example_module.py      # Tests für src/example_module.py
└── package/                    # Tests für Unterpaket (entspricht src/package/)
    ├── __init__.py
    ├── test_module1.py         # Tests für src/package/module1.py
    └── test_module2.py         # Tests für src/package/module2.py
```

## Bewährte Praktiken für Tests

1. **Namenskonventionen**:
   - Testmodule sollten mit `test_` beginnen und nach dem getesteten Modul benannt sein
   - Testfunktionen und -methoden sollten mit `test_` beginnen und beschreiben, was getestet wird
   - Testklassen sollten mit `Test` beginnen und nach der getesteten Klasse benannt sein

2. **pytest verwenden**:
   - [pytest](https://docs.pytest.org/) ist das empfohlene Test-Framework für Python
   - Es bietet eine einfache Syntax, aussagekräftige Berichte und viele Plugins

3. **AAA-Prinzip** (Arrange-Act-Assert):
   - **Arrange**: Testdaten und -umgebung vorbereiten
   - **Act**: Zu testende Funktion oder Methode aufrufen
   - **Assert**: Überprüfen, ob das Ergebnis den Erwartungen entspricht

4. **Testabdeckung**:
   - Strebe eine hohe Testabdeckung an (mehr als 80%)
   - Teste sowohl den "Happy Path" als auch Fehlerszenarien
   - Nutze das `pytest-cov`-Plugin, um die Testabdeckung zu messen

5. **Fixtures und Mocks**:
   - Verwende Fixtures für wiederverwendbare Testvorbereitungen
   - Verwende Mocks für externe Abhängigkeiten (z.B. APIs, Datenbanken)

## Beispiel-Test

Das `test_example_module.py` dient als Vorlage für deine eigenen Tests. Es zeigt:

1. Wie man einfache Funktionstests schreibt
2. Wie man Klassentests strukturiert
3. Wie man das AAA-Prinzip anwendet
4. Wie man verschiedene Aspekte eines Moduls testet

## Tests ausführen

```bash
# Alle Tests ausführen
pytest

# Mit Testabdeckung
pytest --cov=src

# Einzelnen Test ausführen
pytest tests/test_example_module.py

# Spezifische Testfunktion oder -klasse ausführen
pytest tests/test_example_module.py::test_beispiel_funktion
pytest tests/test_example_module.py::TestBeispielKlasse

# Mit ausführlicher Ausgabe
pytest -v
```

## Weitere Ressourcen

- [pytest-Dokumentation](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/) - Testabdeckung messen
- [pytest-Fixtures](https://docs.pytest.org/en/stable/fixture.html) - Testvorbereitungen wiederverwendbar machen
- [pytest-Mock](https://pytest-mock.readthedocs.io/) - Mocking in pytest