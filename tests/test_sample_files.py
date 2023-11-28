from unittest import TestCase
import os
from afipcaeqrdecode.get_cae_metadata import get_cae_metadata

class TestAfipCaeExtractAndDecode(TestCase):

    def test_extract_images_from_pdf_afip_invoice_and_decode(self):

        filenames_and_expected_metadatas = [
            ('2000005044986390.pdf', '{"ver":1,"fecha":"2023-02-10","cuit":30710145764,"ptoVta":4,"tipoCmp":1,"nroCmp":25399,"importe":2460,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73064176949471}'),
            ('2000006916821032.pdf', '{"ver":"1","fecha":"2023-11-18","cuit":30715327712,"ptoVta":7,"tipoCmp":1,"nroCmp":34748,"importe":"13649.43","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":"73462509910160"}'),
            ('2000006891852836.pdf', '{"ver":1,"cuit":33715334319,"ptoVta":20,"tipoCmp":1,"nroCmp":2083,"importe":13964.48,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73469264415216}'),
            ('2000006883967990.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":20340710062,"ptoVta":3,"tipoCmp":1,"nroCmp":438,"importe":18900.00,"moneda":"PES","ctz":1.0000,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73462259065050}'),
            ('2000006882418578.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":30715087738,"ptoVta":11,"tipoCmp":1,"nroCmp":1323,"importe":48899,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73468933099867}'),
            ('2000006835929544.pdf', '{"ver":1,"fecha":"2023-11-08","cuit":33590366329,"ptoVta":8,"tipoCmp":1,"nroCmp":7284,"importe":14178,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73459374223824}')
        ]

        for filename, expected_metadata in filenames_and_expected_metadatas:
            decoded_cae = get_cae_metadata(os.path.join(os.path.dirname(__file__), 'sample_files', filename))
            self.assertIn(decoded_cae, expected_metadata)
