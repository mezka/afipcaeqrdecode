from unittest import TestCase
import os
from afip_invoice_extract_qr_cae_and_decode.afip_invoice_extract_qr_cae_and_decode import extract_images_from_pdf_afip_invoice_and_decode

class TestAfipCaeExtractAndDecode(TestCase):

    def setUp(self):
        self.test_pdf_filepath = os.path.join(os.path.dirname(__file__), 'sample_files', '2000005044986390.pdf')

    def test_extract_images_from_pdf_afip_invoice_and_decode(self):
        result = extract_images_from_pdf_afip_invoice_and_decode(self.test_pdf_filepath)
        self.assertIn('{"ver":1,"fecha":"2023-02-10","cuit":30710145764,"ptoVta":4,"tipoCmp":1,"nroCmp":25399,"importe":2460,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73064176949471}', result)
