import os.path, os

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
from config import WKHTMLTOPDF_PATH
from src.service import AppService



#Dto para la función de recibir texto en md y guardarlo en pdf
class PdfRequest(BaseModel):
    textInMd: str
    title: str
    header: str
    
#Instancia del service
appService = AppService()

#Elementos de FastAPi
app = FastAPI(
    title="Microservicio md a pdf",
    summary= "Microservicio que recibe un texto en formato md y lo devuelve en un pdf",
    # description="Esta API contiene las interfaces para las funcioanlidade de Checklist",
)

@app.get("/status", name="Status API", summary='Retorna ok si el API esta en funcionamiento')
def read_root():
    return {
        "status": "pk",
    }

@app.post(
    path="/generate-pdf",
    name="Checklist",
    response_class=FileResponse,
    summary='Recibe un texto en formato md y lo guarda en un pdf'
    )
async def mdToPdf(request: PdfRequest):

    ##obtenemos el pdf
    pathPdf = appService.generate_pdf(request.textInMd, request.title, request.header)

    #Verificamos que si exista el pdf
    if not os.path.exists(pathPdf):
        raise HTTPException(status_code=500, detail=f"Error generating PDF. ")


    # leemos el contenido del pdf
    with open(pathPdf, 'rb') as pdfFile:
        pdf_content = pdfFile.read()

    # removemos el archivo temporal
    os.remove(pathPdf)

    return Response(
        content=pdf_content,
        media_type='application/pdf',
        headers={"Content-Disposition": f"attachment; filename=Response-ia.pdf"}
    )