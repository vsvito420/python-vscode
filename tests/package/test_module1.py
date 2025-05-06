"""Tests für das src.package.module1 Modul."""

import pytest
from src.package.module1 import verarbeite_daten, filtere_daten


@pytest.fixture
def beispiel_daten():
    """Fixture für Testdaten."""
    return [
        {"name": "produkt1", "wert": 100, "verfügbar": True},
        {"name": "produkt2", "wert": 200, "verfügbar": False},
        {"name": "produkt3", "wert": 150, "verfügbar": True}
    ]


def test_verarbeite_daten(beispiel_daten):
    """Testet die verarbeite_daten Funktion."""
    # Act
    ergebnis = verarbeite_daten(beispiel_daten)
    
    # Assert
    assert len(ergebnis) == len(beispiel_daten)
    assert all("status" in datensatz for datensatz in ergebnis)
    assert all(datensatz["status"] == "verarbeitet" for datensatz in ergebnis)
    
    # Überprüfe Transformation (Name in Großbuchstaben, Wert verdoppelt)
    for original, verarbeitet in zip(beispiel_daten, ergebnis):
        assert verarbeitet["name"] == original["name"].upper()
        assert verarbeitet["wert"] == original["wert"] * 2


def test_filtere_daten(beispiel_daten):
    """Testet die filtere_daten Funktion."""
    # Act
    gefiltert_verfuegbar = filtere_daten(beispiel_daten, "verfügbar", True)
    gefiltert_wert = filtere_daten(beispiel_daten, "wert", 200)
    
    # Assert - Filtere nach Verfügbarkeit
    assert len(gefiltert_verfuegbar) == 2
    assert all(datensatz["verfügbar"] for datensatz in gefiltert_verfuegbar)
    
    # Assert - Filtere nach Wert
    assert len(gefiltert_wert) == 1
    assert gefiltert_wert[0]["name"] == "produkt2"


def test_filtere_daten_keine_treffer(beispiel_daten):
    """Testet den Fall, dass keine Datensätze dem Filter entsprechen."""
    # Act
    gefiltert = filtere_daten(beispiel_daten, "name", "nicht_vorhanden")
    
    # Assert
    assert gefiltert == []


def test_verarbeite_daten_leere_liste():
    """Testet das Verhalten mit einer leeren Liste."""
    # Arrange
    leere_liste = []
    
    # Act
    ergebnis = verarbeite_daten(leere_liste)
    
    # Assert
    assert ergebnis == []


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])