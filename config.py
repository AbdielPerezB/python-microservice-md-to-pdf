from dotenv import load_dotenv
import os

load_dotenv()

STAGE= os.getenv('STAGE')
WKHTMLTOPDF_PATH= os.getenv('WKHTMLTOPDF_PATH')