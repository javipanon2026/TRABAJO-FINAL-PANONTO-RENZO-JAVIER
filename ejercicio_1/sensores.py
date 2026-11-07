"""Ejercicio 1: sanitización y análisis estadístico de sensores."""

def limpiar_registro_sensor(registro_raw):
    """Devuelve una copia normalizada de un registro crudo de sensor."""
    if not isinstance(registro_raw, dict):
        raise TypeError("El registro del sensor debe ser un diccionario.")

    sensor_id = str(registro_raw.get("sensor_id") or "SENSOR-SIN-ID").strip()
    ubicacion = str(registro_raw.get("ubicacion") or "").strip() or "Ubicación no especificada"

    temperatura_raw = registro_raw.get("temperatura")
    if temperatura_raw is None:
        raise ValueError("El registro no contiene temperatura.")

    # Acepta valores como 24.5, "24.5C", " 24,5 °C ".
    temperatura_texto = str(temperatura_raw).strip().upper()
    temperatura_texto = temperatura_texto.replace("°", "").replace("C", "").strip()
    temperatura_texto = temperatura_texto.replace(",", ".")
    try:
        temperatura = float(temperatura_texto)
    except ValueError as exc:
        raise ValueError(f"Temperatura inválida: {temperatura_raw!r}") from exc

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Retorna (IDs que superan el umbral, promedio global)."""
    sensores = list(lista_sensores_limpios)
    if not sensores:
        return ([], 0.0)

    alertas = [
        sensor["sensor_id"]
        for sensor in sensores
        if sensor["temperatura"] > float(umbral_temperatura)
    ]
    promedio = sum(float(s["temperatura"]) for s in sensores) / len(sensores)
    return (alertas, promedio)


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31 °C", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR-003 ", "temperatura": "27,2 C", "ubicacion": ""},
    ]

    sensores_limpios = [limpiar_registro_sensor(r) for r in registros_crudos]
    alertas, promedio = generar_resumen_sensores(sensores_limpios, 28)

    print("=== REPORTE DE SENSORES - ECOTECH SOLUTIONS ===")
    print(f"Sensores procesados: {len(sensores_limpios)}")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Sensores que superan 28 °C: {', '.join(alertas) if alertas else 'Ninguno'}")
