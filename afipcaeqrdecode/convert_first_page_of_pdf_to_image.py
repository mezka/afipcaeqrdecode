import fitz
import numpy as np

def convert_first_page_of_pdf_to_image(filepath):
    with fitz.open(filepath) as pdf_file:
        first_page = pdf_file[0]
        pixmap = first_page.get_pixmap(
            matrix=fitz.Matrix(200 / 72, 200 / 72),
            colorspace=fitz.csRGB,
            alpha=False,
        )

    return np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(pixmap.height, pixmap.width, pixmap.n)
