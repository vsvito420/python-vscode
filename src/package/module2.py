"""Beispielmodul zur Datenspeicherung.

Dieses Modul enthält Funktionen zum Speichern von Daten.
"""

import json
import csv
from typing import Dict, List, Any, Optional
from pathlib import Path


def speichere_ergebnis(daten: List[Dict[str, Any]], 
                       dateiname: str, 
                       format: str = "json") -> Path:
    """Speichert verarbeitete Daten in einer Datei.

    Args:
        daten: Eine Liste von Dictionaries mit verarbeiteten Daten
        dateiname: Der Name der Datei (ohne Erweiterung)
        format: Das Format, in dem die Daten gespeichert werden sollen
               (unterstützt: "json", "csv")

    Returns:
        Path-Objekt der gespeicherten Datei

    Beispiel:
        >>> daten = [{"name": "TEST", "wert": 10}]
        >>> speichere_ergebnis(daten, "ausgabe", "json")
        PosixPath('ausgabe.json')
    """
    # Stellen sicher, dass das Format gültig ist
    if format.lower() not in ["json", "csv"]:
        raise ValueError(f"Nicht unterstütztes Format: {format}. Verwende 'json' oder 'csv'.")
    
    # Dateipfad bestimmen
    datei_erweiterung = f".{format.lower()}"
    if not dateiname.endswith(datei_erweiterung):
        dateiname = f"{dateiname}{datei_erweiterung}"
    
    dateipfad = Path(dateiname)
    
    # Daten speichern
    if format.lower() == "json":
        _speichere_json(daten, dateipfad)
    elif format.lower() == "csv":
        _speichere_csv(daten, dateipfad)
    
    return dateipfad


def lade_daten(dateipfad: str) -> List[Dict[str, Any]]:
    """Lädt Daten aus einer JSON- oder CSV-Datei.

    Args:
        dateipfad: Pfad zur Datei (muss .json oder .csv sein)

    Returns:
        Liste von Dictionaries mit den geladenen Daten

    Raises:
        ValueError: Wenn das Dateiformat nicht unterstützt wird
        FileNotFoundError: Wenn die Datei nicht existiert
    """
    pfad = Path(dateipfad)
    
    if not pfad.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {pfad}")
    
    if pfad.suffix.lower() == ".json":
        return _lade_json(pfad)
    elif pfad.suffix.lower() == ".csv":
        return _lade_csv(pfad)
    else:
        raise ValueError(
            f"Nicht unterstütztes Dateiformat: {pfad.suffix}. "
            "Verwende .json oder .csv"
        )


def _speichere_json(daten: List[Dict[str, Any]], dateipfad: Path) -> None:
    """Hilfsfunktion zum Speichern von Daten als JSON."""
    with open(dateipfad, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)


def _speichere_csv(daten: List[Dict[str, Any]], dateipfad: Path) -> None:
    """Hilfsfunktion zum Speichern von Daten als CSV."""
    if not daten:
        # Leere CSV-Datei erstellen
        with open(dateipfad, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([])  # Schreibe leere Zeile
        return
    
    # Bestimme die Spalten aus dem ersten Datensatz
    felder = list(daten[0].keys())
    
    with open(dateipfad, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=felder)
        writer.writeheader()
        writer.writerows(daten)


def _lade_json(dateipfad: Path) -> List[Dict[str, Any]]:
    """Hilfsfunktion zum Laden von Daten aus einer JSON-Datei."""
    with open(dateipfad, 'r', encoding='utf-8') as f:
        return json.load(f)


def _lade_csv(dateipfad: Path) -> List[Dict[str, Any]]:
    """Hilfsfunktion zum Laden von Daten aus einer CSV-Datei."""
    with open(dateipfad, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == "__main__":
    # Beispiel zur Verwendung
    test_daten = [
        {"name": "PRODUKT1", "wert": 200, "status": "verarbeitet"},
        {"name": "PRODUKT2", "wert": 400, "status": "verarbeitet"},
        {"name": "PRODUKT3", "wert": 300, "status": "verarbeitet"}
    ]
    
    # Daten in verschiedenen Formaten speichern
    json_pfad = speichere_ergebnis(test_daten, "beispiel_ausgabe", "json")
    csv_pfad = speichere_ergebnis(test_daten, "beispiel_ausgabe", "csv")
    
    print(f"Daten wurden in {json_pfad} und {csv_pfad} gespeichert.")
    
    # Daten wieder laden
    json_daten = lade_daten(str(json_pfad))
    print(f"Aus JSON geladene Daten: {json_daten}")