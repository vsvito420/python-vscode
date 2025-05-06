# Python-Template

Dieses Template bietet eine grundlegende Struktur für Python-Projekte mit integrierten Tools für Code-Qualität, Tests und CI/CD.

## Features

- **Code-Formatierung:** [Black](https://github.com/psf/black) und [isort](https://github.com/PyCQA/isort) konfiguriert über `pyproject.toml`.
- **Linting:** [Flake8](https://github.com/PyCQA/flake8) konfiguriert über `pyproject.toml`.
- **Tests:** [pytest](https://docs.pytest.org/) konfiguriert über `pyproject.toml`.
- **Pre-commit Hooks:** Automatische Code-Formatierung und Linting vor jedem Commit mit [pre-commit](https://pre-commit.com/).
- **CI/CD:** Beispiel-Workflow mit [GitHub Actions](https://github.com/features/actions) für Code-Prüfungen und Tests.
- **VS Code Integration:** Einstellungen für die nahtlose Nutzung der Tools in VS Code.

## Erste Schritte

1.  Klone dieses Repository.
2.  Installiere [Poetry](https://python-poetry.org/docs/#installation).
3.  Installiere die Abhängigkeiten:
    ```bash
    poetry install
    ```
4.  Installiere die pre-commit Hooks:
    ```bash
    pre-commit install
    ```

## Nutzung der Tools

- **Formatierung (Black & isort):**
    ```bash
    poetry run black .
    poetry run isort .
    ```
- **Linting (Flake8):**
    ```bash
    poetry run flake8
    ```
- **Tests (pytest):**
    ```bash
    poetry run pytest
    ```

Diese Befehle werden auch automatisch ausgeführt, wenn du einen Commit erstellst (dank pre-commit) und in der CI/CD-Pipeline (dank GitHub Actions).

## Projektstruktur

Eine empfohlene Projektstruktur:

```
.
├── .github/workflows/ci.yml  # GitHub Actions Workflow
├── .vscode/settings.json     # VS Code Einstellungen
├── .pre-commit-config.yaml   # Pre-commit Konfiguration
├── pyproject.toml            # Projekt- und Tool-Konfiguration (Poetry)
├── README.md                 # Diese Datei
└── src/                      # Dein Quellcode
    └── __init__.py
└── tests/                    # Deine Tests
    └── __init__.py
    └── test_example.py       # Beispiel Test
