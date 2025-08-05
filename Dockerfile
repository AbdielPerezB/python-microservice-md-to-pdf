# Usa la imagen oficial de Python con la misma versión que usas localmente
FROM python:3.12.11-slim-bookworm

# Instala las dependencias del sistema (incluyendo wkhtmltopdf)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wkhtmltopdf \
    xvfb \
    fonts-liberation \
    fonts-dejavu \
    libssl-dev \
    libxrender-dev \
    libx11-dev \
    libxext-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    fontconfig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configuración alternativa para wkhtmltopdf en entornos headless
RUN echo '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf "$@"' > /usr/bin/wkhtmltopdf.sh && \
    chmod a+x /usr/bin/wkhtmltopdf.sh

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto que usa FastAPI (por defecto 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["fastapi", "run", "main.py"]