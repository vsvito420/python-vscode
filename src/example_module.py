"""Ein Beispielmodul zur Demonstration guter Python-Praktiken.

Dieses Modul dient als Beispiel für:
1. Dokumentation mit Docstrings (PEP 257)
2. Typisierung mit Typehints (PEP 484)
3. Funktionale Strukturierung
4. Modulare Organisation
"""

from typing import List, Dict, Optional


def beispiel_funktion(parameter: str) -> str:
    """Nimmt einen String und gibt ihn in Großbuchstaben zurück.

    Args:
        parameter: Der zu konvertierende String

    Returns:
        Der konvertierte String in Großbuchstaben

    Beispiel:
        >>> beispiel_funktion("hallo")
        'HALLO'
    """
    return parameter.upper()


class BeispielKlasse:
    """Eine Beispielklasse zur Demonstration von Klassen in Python.

    Diese Klasse zeigt:
    - Initialisierung mit __init__
    - Methoden mit Typehints
    - Properties
    - Docstrings gemäß PEP 257

    Attributes:
        name: Name der Instanz
        werte: Liste von Werten
    """

    def __init__(self, name: str, werte: Optional[List[int]] = None):
        """Initialisiert eine neue BeispielKlasse.

        Args:
            name: Name der Instanz
            werte: Optional Liste von Werten, standardmäßig leere Liste
        """
        self.name = name
        self.werte = werte or []

    def hinzufuegen(self, wert: int) -> None:
        """Fügt einen Wert zur Liste hinzu.

        Args:
            wert: Der hinzuzufügende Wert
        """
        self.werte.append(wert)

    @property
    def anzahl(self) -> int:
        """Gibt die Anzahl der Werte zurück.

        Returns:
            Anzahl der gespeicherten Werte
        """
        return len(self.werte)

    def as_dict(self) -> Dict[str, object]:
        """Konvertiert die Instanz in ein Dictionary.

        Returns:
            Ein Dictionary mit den Attributen der Instanz
        """
        return {
            "name": self.name,
            "werte": self.werte,
            "anzahl": self.anzahl
        }


if __name__ == "__main__":
    # Demonstration der Verwendung
    print(beispiel_funktion("hallo welt"))

    # Demonstration der Klasse
    beispiel = BeispielKlasse("Mein Beispiel")
    beispiel.hinzufuegen(1)
    beispiel.hinzufuegen(2)
    beispiel.hinzufuegen(3)

    print(f"Anzahl: {beispiel.anzahl}")
    print(f"Als Dictionary: {beispiel.as_dict()}")