"""Tests für das example_module."""

import pytest
from src.example_module import beispiel_funktion, BeispielKlasse


def test_beispiel_funktion():
    """Testet die beispiel_funktion."""
    # Arrange
    test_input = "hallo"
    expected = "HALLO"

    # Act
    result = beispiel_funktion(test_input)

    # Assert
    assert result == expected


class TestBeispielKlasse:
    """Tests für die BeispielKlasse."""

    def test_initialisierung(self):
        """Testet die Initialisierung der Klasse."""
        # Arrange & Act
        instanz = BeispielKlasse("Test")

        # Assert
        assert instanz.name == "Test"
        assert instanz.werte == []

    def test_initialisierung_mit_werten(self):
        """Testet die Initialisierung mit vordefinierten Werten."""
        # Arrange
        test_werte = [1, 2, 3]

        # Act
        instanz = BeispielKlasse("Test", test_werte)

        # Assert
        assert instanz.werte == test_werte

    def test_hinzufuegen(self):
        """Testet die hinzufuegen Methode."""
        # Arrange
        instanz = BeispielKlasse("Test")

        # Act
        instanz.hinzufuegen(42)

        # Assert
        assert 42 in instanz.werte
        assert len(instanz.werte) == 1

    def test_anzahl_property(self):
        """Testet das anzahl Property."""
        # Arrange
        instanz = BeispielKlasse("Test", [1, 2, 3, 4])

        # Act & Assert
        assert instanz.anzahl == 4

    def test_as_dict(self):
        """Testet die as_dict Methode."""
        # Arrange
        instanz = BeispielKlasse("Test", [1, 2])

        # Act
        result = instanz.as_dict()

        # Assert
        assert isinstance(result, dict)
        assert result["name"] == "Test"
        assert result["werte"] == [1, 2]
        assert result["anzahl"] == 2


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])