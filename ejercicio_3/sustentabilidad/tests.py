import unittest
from django.test import SimpleTestCase, Client
from .algoritmos import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_nominal(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(200, 0.5), 100.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


class TestMetricasConsumo(unittest.TestCase):
    def test_total_y_planta_de_mayor_consumo(self):
        registros = [
            {"planta": "Norte", "consumo_kwh": 100},
            {"planta": "Sur", "consumo_kwh": 200},
            {"planta": "Norte", "consumo_kwh": 50},
        ]
        resultado = obtener_metricas_consumo(registros)
        self.assertAlmostEqual(resultado["total_emisiones"], 140.0)
        self.assertEqual(resultado["planta_mayor_consumo"], "Sur")
        self.assertEqual(resultado["mayor_consumo_kwh"], 200.0)

    def test_lista_vacia(self):
        resultado = obtener_metricas_consumo([])
        self.assertEqual(resultado["total_emisiones"], 0.0)
        self.assertEqual(resultado["planta_mayor_consumo"], "Sin datos")


class TestVistaPanel(SimpleTestCase):
    def test_panel_responde_correctamente(self):
        respuesta = Client().get("/sustentabilidad/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Panel de sustentabilidad")
