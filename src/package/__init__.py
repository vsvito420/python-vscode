"""Beispiel-Unterpaket zur Demonstration der Paketstruktur.

Dieses Paket zeigt, wie man Python-Code in mehrere Module organisiert und
durch ein Paket zusammenfasst.
"""

from src.package.module1 import verarbeite_daten
from src.package.module2 import speichere_ergebnis

# Exponiere nur bestimmte Funktionen an der Paket-Ebene
__all__ = ["verarbeite_daten", "speichere_ergebnis"]