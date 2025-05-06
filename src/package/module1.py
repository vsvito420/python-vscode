"""Beispielmodul zur Datenverarbeitung.

Dieses Modul enthält Funktionen zur Verarbeitung von Daten.
"""

from typing import Dict, List, Any, Union


def verarbeite_daten(daten: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Verarbeitet eine Liste von Datensätzen.

    Diese Funktion ist ein Beispiel für eine Datenverarbeitungsfunktion.
    Sie filtert Datensätze und transformiert die Werte.

    Args:
        daten: Eine Liste von Dictionaries mit Rohdaten

    Returns:
        Eine Liste von verarbeiteten Datensätzen

    Beispiel:
        >>> rohdaten = [{"name": "test", "wert": 5}, {"name": "abc", "wert": 10}]
        >>> verarbeite_daten(rohdaten)
        [{'name': 'TEST', 'wert': 10, 'status': 'verarbeitet'}, 
         {'name': 'ABC', 'wert': 20, 'status': 'verarbeitet'}]
    """
    ergebnis = []
    for datensatz in daten:
        # Kopiere Datensatz, um das Original nicht zu verändern
        verarbeitet = datensatz.copy()
        
        # Transformiere Werte
        if "name" in verarbeitet:
            verarbeitet["name"] = verarbeitet["name"].upper()
        
        if "wert" in verarbeitet:
            verarbeitet["wert"] = verarbeitet["wert"] * 2
        
        # Füge Status hinzu
        verarbeitet["status"] = "verarbeitet"
        
        ergebnis.append(verarbeitet)
    
    return ergebnis


def filtere_daten(daten: List[Dict[str, Any]], 
                 schluessel: str, 
                 wert: Union[str, int, float]) -> List[Dict[str, Any]]:
    """Filtert Datensätze nach einem bestimmten Schlüssel-Wert-Paar.

    Args:
        daten: Eine Liste von Dictionaries mit Daten
        schluessel: Der Schlüssel, nach dem gefiltert werden soll
        wert: Der Wert, nach dem gefiltert werden soll

    Returns:
        Eine Liste der gefilterten Datensätze

    Beispiel:
        >>> daten = [{"name": "test", "wert": 5}, {"name": "abc", "wert": 10}]
        >>> filtere_daten(daten, "wert", 5)
        [{'name': 'test', 'wert': 5}]
    """
    return [datensatz for datensatz in daten if datensatz.get(schluessel) == wert]


if __name__ == "__main__":
    # Beispiel zur Verwendung
    test_daten = [
        {"name": "produkt1", "wert": 100, "verfügbar": True},
        {"name": "produkt2", "wert": 200, "verfügbar": False},
        {"name": "produkt3", "wert": 150, "verfügbar": True}
    ]
    
    verarbeitete_daten = verarbeite_daten(test_daten)
    print("Verarbeitete Daten:", verarbeitete_daten)
    
    gefilterte_daten = filtere_daten(test_daten, "verfügbar", True)
    print("Gefilterte Daten:", gefilterte_daten)