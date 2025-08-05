import markdown
import pdfkit
import asyncio
from pathlib import Path
# from functools import partial
#ajustes default
AJUSTES_PDF_DEFAULT = {
        "page-size": "letter",
        "margin-top": "1.5cm",
        "margin-right": "0.1cm",
        "margin-bottom": "2.5cm",
        "margin-left": "0.1cm",
        "encoding": "UTF-8",
        "enable-local-file-access": ""
    }
class SavePdfWkhtmltopdf:

    def __init__(self, css: str = None, ajustes_pagina_pdf = None):
        self.config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf') #for_linux_only
        self.ajustes_pagina_pdf = AJUSTES_PDF_DEFAULT if not ajustes_pagina_pdf else ajustes_pagina_pdf
        self.story = ""
        self.css = css if css else str(Path(__file__).parent / "styles.css")
        #async features
        self.loop = asyncio.get_event_loop()

    def add_title(self, title: str, encabezado: str):
        self.story = self.story + f'<p class="encabezado"><b>{encabezado}</b></p>'
        self.story = self.story + f'<h2 class="tittle">{title}</h2>'

    def add_subtitle(self, subtitle: str):
        self.story = self.story + f'<h3 class="sub-tittle">{subtitle}</h3>'

    def add_content(self, content: str, is_markdown: bool = True):
        if is_markdown:
            self.story = self.story + markdown.markdown(content)
        else:
            self.story = self.story + f"<p>{content}</p>"

    def save_pdf(self, path_file_with_name_and_extension: str) -> None:
        try:
            pdfkit.from_string(
                self.story,
                path_file_with_name_and_extension,
                css=self.css,
                options=self.ajustes_pagina_pdf,
                configuration=self.config
            )
            self.story = ""
        except Exception as e:
            raise RuntimeError(f"Error generating PDF: {e}") from e


