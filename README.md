## About it
This microservice obtains a text in markdown format, saves it in a pdf and returns the file

## No Docker Installation Instructions
1. Install wkhtmltopdf    
   - `apt-get install wkhtmltopdf`
2. Create a virtual environment: 
   - `python3 -m venv .venv`
   - Access to the virtual environment: `source .venv/bin/activate`
3. Install all dependencies whithin the virtual environment:
   - `pip install -r requirements.txt`
4. Start FastAPI.
   - For production mode: `fastapi run main.py`
   - For dev mode. `fastapi dev main.py`

## Docker Installation Instructions
1. Execute: `docker compose up -d`

## Usage instructions:
You can access microservice at `localhost:8000` in your web browser

API docs: `localhost:8000/docs`

