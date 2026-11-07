from django.shortcuts import render
from .algoritmos import obtener_metricas_consumo

# Datos de ejemplo. En una aplicación real podrían provenir de una base de datos.
REGISTROS_CONSUMO = [
    {"planta": "Planta Norte", "consumo_kwh": 1250},
    {"planta": "Planta Sur", "consumo_kwh": 980},
    {"planta": "Planta Norte", "consumo_kwh": 350},
    {"planta": "Planta Este", "consumo_kwh": 1475},
]


def vista_panel_sustentabilidad(request):
    metricas = obtener_metricas_consumo(REGISTROS_CONSUMO)
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "mayor_consumo_kwh": metricas["mayor_consumo_kwh"],
        "consumos_por_planta": metricas["consumos_por_planta"],
    }
    return render(request, "sustentabilidad/panel.html", contexto)
