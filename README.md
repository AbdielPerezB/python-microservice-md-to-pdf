## Instrucciones de instalación No Docker
1. Instalar wkhtmltopdf    
   - `apt-get install wkhtmltopdf`
2. Crear un entorno cirtual: 
   - `python -m venv .venv`
   - Acceder al entorno virtual: `source .venv/bin/activate`
3. Instalar las dependencias dentro del entorno virtual:
   - `pip install -r requirements.txt`
4. INiciar FastAPI.
   - Para producción: `fastapi run main.py`
   - Para desarrollo. `fastapi dev main.py`

## Instrucciones de instalación Docker
1. Ejecutar: `docker compose up -d`

## Instrucciones de uso:
La aplicación expone el puero 8000

Docoumentación del API disponible en `localhost:8000/docs`

