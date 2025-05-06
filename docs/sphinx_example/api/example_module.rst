Example Module
=============

.. automodule:: src.example_module
   :members:
   :undoc-members:
   :show-inheritance:

Übersicht
--------

Dieses Modul dient als Beispiel für:

1. Dokumentation mit Docstrings (PEP 257)
2. Typisierung mit Typehints (PEP 484)
3. Funktionale Strukturierung
4. Modulare Organisation

Beispielfunktion
--------------

Die :func:`beispiel_funktion` dient als einfaches Beispiel für eine gut dokumentierte Funktion.

.. code-block:: python

   from src.example_module import beispiel_funktion
   
   ergebnis = beispiel_funktion("hallo welt")
   print(ergebnis)  # Ausgabe: "HALLO WELT"

Klassenbeispiel
-------------

Die :class:`BeispielKlasse` zeigt, wie man Klassen strukturiert und dokumentiert.

.. code-block:: python

   from src.example_module import BeispielKlasse
   
   beispiel = BeispielKlasse("Mein Beispiel")
   beispiel.hinzufuegen(42)
   print(f"Anzahl: {beispiel.anzahl}")