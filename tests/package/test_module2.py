"""Tests für das src.package.module2 Modul."""

import json
import pytest
import tempfile
import os
from pathlib import Path
from src.package.module2 import speichere_ergebnis, lade_daten


@pytest.fixture
def beispiel_daten():
    """Fixture für Testdaten."""
    return [
        {"name": "PRODUKT1", "wert": 200, "status": "verarbeitet"},
        {"name": "PRODUKT2", "wert": 400, "status": "verarbeitet"}
    ]


@pytest.fixture
def temp_verzeichnis():
    """Fixture für ein temporäres Verzeichnis."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Merke aktuelles Verzeichnis
        alter_pfad = os.getcwd()
        # Wechsle in das temporäre Verzeichnis
        os.chdir(tempdir)
        # Übergebe das temporäre Verzeichnis
        yield Path(tempdir)
        # Wechsle zurück zum ursprünglichen Verzeichnis
        os.chdir(alter_pfad)


def test_speichere_ergebnis_json(beispiel_daten, temp_verzeichnis):
    """Testet das Speichern von Daten als JSON."""
    # Arrange
    dateiname = "test_daten"
    
    # Act
    pfad = speichere_ergebnis(beispiel_daten, dateiname, "json")
    
    # Assert
    assert pfad.exists()
    assert pfad.name == "test_daten.json"
    
    # Überprüfe Inhalt
    with open(pfad, 'r', encoding='utf-8') as f:
        geladen = json.load(f)
        assert geladen == beispiel_daten


def test_speichere_ergebnis_csv(beispiel_daten, temp_verzeichnis):
    """Testet das Speichern von Daten als CSV."""
    # Arrange
    dateiname = "test_daten"
    
    # Act
    pfad = speichere_ergebnis(beispiel_daten, dateiname, "csv")
    
    # Assert
    assert pfad.exists()
    assert pfad.name == "test_daten.csv"
    
    # Inhalt überprüfen (einfacher Test)
    with open(pfad, 'r', encoding='utf-8') as f:
        inhalt = f.read()
        # CSV-Header und Werte überprüfen
        assert "name,wert,status" in inhalt
        assert "PRODUKT1,200,verarbeitet" in inhalt.replace(" ", "")


def test_lade_daten_json(beispiel_daten, temp_verzeichnis):
    """Testet das Laden von Daten aus einer JSON-Datei."""
    # Arrange - Daten speichern
    pfad = speichere_ergebnis(beispiel_daten, "test_laden", "json")
    
    # Act
    geladen = lade_daten(str(pfad))
    
    # Assert
    assert geladen == beispiel_daten


def test_lade_daten_csv(beispiel_daten, temp_verzeichnis):
    """Testet das Laden von Daten aus einer CSV-Datei."""
    # Arrange - Daten speichern
    pfad = speichere_ergebnis(beispiel_daten, "test_laden", "csv")
    
    # Act
    geladen = lade_daten(str(pfad))
    
    # Assert
    assert len(geladen) == len(beispiel_daten)
    # CSV-Dateien speichern Zahlen als Strings
    for original, geladen_item in zip(beispiel_daten, geladen):
        assert geladen_item["name"] == original["name"]
        assert geladen_item["status"] == original["status"]


def test_lade_daten_datei_nicht_gefunden():
    """Testet das Verhalten, wenn die zu ladende Datei nicht existiert."""
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        lade_daten("nicht_existierende_datei.json")


def test_lade_daten_ungültiges_format():
    """Testet das Verhalten bei ungültigem Dateiformat."""
    # Arrange - Temporäre Datei mit falscher Endung erstellen
    with tempfile.NamedTemporaryFile(suffix=".txt") as temp:
        # Act & Assert
        with pytest.raises(ValueError):
            lade_daten(temp.name)


def test_speichere_ergebnis_ungültiges_format(beispiel_daten, temp_verzeichnis):
    """Testet das Verhalten bei ungültigem Ausgabeformat."""
    # Act & Assert
    with pytest.raises(ValueError):
        speichere_ergebnis(beispiel_daten, "test", "ungültig")


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])