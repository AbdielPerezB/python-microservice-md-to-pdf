import os.path, os

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
    title="Microservice md a pdf",
    summary= "Microservice that gets a text in markdown format and returns it in a pdf",
)

#CORS
origins = [
    "*" #Permitimos todos
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status", name="Status API", summary='Returns ok if app is ok')
def read_root():
    return {
        "status": "ok",
    }

@app.post(
    path="/generate-pdf",
    name="Pdf generator",
    response_class=FileResponse,
    summary='Receives a text in markdown format and generates a pdf file'
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
        headers={"Content-Disposition": "attachment; filename=md_in_pdf.pdf"}
    )