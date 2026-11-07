"""Demostración del catálogo y persistencia JSON del Ejercicio 2."""

from pathlib import Path
from productos import (
    PanelSolar,
    StockInvalidoError,
    GestorInventario,
)


if __name__ == "__main__":
    paneles = [
        PanelSolar("EcoPanel 450", "EcoTech", 185000, 12, 450, 21.5),
        PanelSolar("EcoPanel 550", "SolarVerde", 220000, 8, 550, 22.8),
    ]

    print("=== VALIDACIÓN DE STOCK ===")
    try:
        paneles[0].stock = -5
    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    ruta = Path(__file__).with_name("catalogo_ecotech.json")
    GestorInventario.guardar_catalogo_json(paneles, ruta)
    print(f"Catálogo exportado correctamente en: {ruta}")
    for panel in paneles:
        print(panel.ficha_tecnica())
