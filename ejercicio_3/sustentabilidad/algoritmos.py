"""Funciones de cálculo y procesamiento de métricas ambientales."""

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula emisiones en kg de CO2 equivalente."""
    consumo = float(consumo_kwh)
    factor = float(factor_emision)
    if consumo < 0:
        raise ValueError("El consumo eléctrico no puede ser negativo.")
    if factor < 0:
        raise ValueError("El factor de emisión no puede ser negativo.")
    return consumo * factor


def obtener_metricas_consumo(registros):
    """
    Recibe registros con las claves 'planta' y 'consumo_kwh'.
    Retorna emisiones totales y nombre/consumo de la planta de mayor consumo.
    """
    total_emisiones = 0.0
    consumos_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo = float(registro["consumo_kwh"])
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        consumos_por_planta[planta] = consumos_por_planta.get(planta, 0.0) + consumo

    if consumos_por_planta:
        planta_mayor = max(consumos_por_planta, key=consumos_por_planta.get)
        mayor_consumo = consumos_por_planta[planta_mayor]
    else:
        planta_mayor = "Sin datos"
        mayor_consumo = 0.0

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor,
        "mayor_consumo_kwh": mayor_consumo,
        "consumos_por_planta": consumos_por_planta,
    }
