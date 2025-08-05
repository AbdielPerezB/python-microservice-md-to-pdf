from src.modules.pdf.pdfClass import SavePdfWkhtmltopdf
from pathlib import Path
from uuid import uuid4
import os



class AppService:

    def __init__(self):
        self.pdfClass = SavePdfWkhtmltopdf()

    def generate_pdf(self, textInMd: str, title: str, encabezado: str) -> str:
        """
        Devuelve el path del pdf generado con el texto en formato md
        """

        #Guardamos el contenido
        self.pdfClass.add_title(title, encabezado)
        self.pdfClass.add_content(textInMd)

        ##creamos la carpet temporal
        temporalFolder = Path(__file__).parents[1] / 'filesTemp'
        temporalFolder.mkdir(parents=True, exist_ok=True)

        path_file_with_name_and_extension = str(temporalFolder / f'{uuid4()}.pdf')

        #Guardamos el pdf
        self.pdfClass.save_pdf(path_file_with_name_and_extension)

        return path_file_with_name_and_extension



