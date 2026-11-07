"""Ejercicio 2: dominio del catálogo de dispositivos ecológicos."""

import json
from abc import ABC, abstractmethod


class StockInvalidoError(Exception):
    """Se produce cuando se intenta asignar un stock negativo."""


class DispositivoEcológico(ABC):
    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = float(precio)
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("El stock debe ser un número entero.")
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")
        self.__stock = valor

    @abstractmethod
    def ficha_tecnica(self):
        """Devuelve la descripción comercial del dispositivo."""

    def a_diccionario(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock,
            "ficha_tecnica": self.ficha_tecnica(),
        }


class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, marca, precio, stock, potencia_w, eficiencia):
        super().__init__(nombre, marca, precio, stock)
        self.potencia_w = int(potencia_w)
        self.eficiencia = float(eficiencia)

    def ficha_tecnica(self):
        return (
            f"{self.nombre}: panel solar {self.potencia_w} W, "
            f"eficiencia del {self.eficiencia:.1f}%. "
            f"Marca: {self.marca}."
        )

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos.update({
            "potencia_w": self.potencia_w,
            "eficiencia": self.eficiencia,
        })
        return datos


class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        """Serializa los dispositivos y guarda un archivo JSON legible."""
        catalogo = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, ensure_ascii=False, indent=4)
        return ruta_archivo
