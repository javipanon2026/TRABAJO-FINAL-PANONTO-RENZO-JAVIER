# TP Final - EcoTech Solutions

Proyecto organizado en tres ejercicios prácticos de Python y Django.

## Requisitos
- Python 3.10 o superior
- pip

## Instalación
Desde la carpeta `ejercicio_3`:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

## Ejercicio 1
```bash
python ejercicio_1/sensores.py
```

## Ejercicio 2
```bash
python ejercicio_2/inventario.py
```
El catálogo se guarda en `ejercicio_2/catalogo_ecotech.json`.

## Ejercicio 3: pruebas y Django
Desde `ejercicio_3`:

```bash
python manage.py test
python manage.py runserver
```

Abrir http://127.0.0.1:8000/sustentabilidad/

## Subir a GitHub
1. Crear un repositorio público en GitHub.
2. Descomprimir esta carpeta.
3. Abrir una terminal dentro de `TP_FINAL_ECOTECH`.
4. Ejecutar:

```bash
git init
git add .
git commit -m "Entrega TP final EcoTech Solutions"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
```

Reemplazar la URL por la del repositorio propio. No subir la carpeta `venv`.
