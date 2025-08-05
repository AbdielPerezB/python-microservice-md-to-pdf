import os.path
from pyexpat.errors import messages

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing_extensions import Literal, Annotated, List

from service import AppService


#Dto para la función de recibir texto en md y guardarlo en pdf
class PdfRequest(BaseModel):
    textInMd: str
    title: str

#Instancia del service
appService = AppService()

#Elementos de FastAPi
app = FastAPI(
    title="Microservicio md a pdf",
    summary= "Microservicio que recibe un texto en formato md y lo devuelve en un pdf",
    # description="Esta API contiene las interfaces para las funcioanlidade de Checklist",
)

@app.get("/status", name="Status API", summary='Retorna ok si el API esta en funcionamiento')
def read_root()->Literal["ok"]:
    return "ok"

@app.post(
    path="/generate-pdf",
    name="Checklist",
    response_class=FileResponse,
    summary='Recibe un texto en formato md y lo guarda en un pdf'
    )
async def mdToPdf(request: PdfRequest):

    ##obtenemos el pdf
    pathPdf = appService.generate_pdf(request.textInMd, request.title)

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