from unittest import TestCase
import os
from afipcaeqrdecode.get_cae_metadata import get_cae_metadata

class TestAfipCaeExtractAndDecode(TestCase):

    def test_extract_images_from_pdf_afip_invoice_and_decode(self):

        filenames_and_expected_metadatas = [
            ('2000005044986390.pdf', '{"ver":1,"fecha":"2023-02-10","cuit":30710145764,"ptoVta":4,"tipoCmp":1,"nroCmp":25399,"importe":2460,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73064176949471}'),
            ('2000006916821032.pdf', '{"ver":"1","fecha":"2023-11-18","cuit":30715327712,"ptoVta":7,"tipoCmp":1,"nroCmp":34748,"importe":"13649.43","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":"73462509910160"}'),
            ('2000006891852836.pdf', '{"ver":1,"cuit":33715334319,"ptoVta":20,"tipoCmp":1,"nroCmp":2083,"importe":13964.48,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73469264415216}'),
            ('2000006883967990.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":20340710062,"ptoVta":3,"tipoCmp":1,"nroCmp":438,"importe":18900.0,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73462259065050}'),
            ('2000006882418578.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":30715087738,"ptoVta":11,"tipoCmp":1,"nroCmp":1323,"importe":48899,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73468933099867}'),
            ('2000006835929544.pdf', '{"ver":1,"fecha":"2023-11-08","cuit":33590366329,"ptoVta":8,"tipoCmp":1,"nroCmp":7284,"importe":14178,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73459374223824}'),
            ('2000006788971254.pdf', '{"ver":1,"fecha":"2023-10-31","cuit":20211152800,"ptoVta":8,"tipoCmp":1,"nroCmp":4273,"importe":622436.27,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73440405182735}'),
            ('2000006846229610.pdf', '{"ver":1,"fecha":"2023-11-09","cuit":30695068286,"ptoVta":6,"tipoCmp":1,"nroCmp":118954,"importe":105978,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73456468252481}'),
            ('2000007385626396.pdf', '{"ver":1,"fecha":"2024-01-16","cuit":27309910171,"ptoVta":2,"tipoCmp":1,"nroCmp":449,"importe":48999,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74031190633651}'),
            ('2000006916821032.pdf', '{"ver":"1","fecha":"2023-11-18","cuit":30715327712,"ptoVta":7,"tipoCmp":1,"nroCmp":34748,"importe":"13649.43","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":"73462509910160"}'),
            ('2000007393886976.pdf', '{"ver":"1","fecha":"2024-01-17","cuit":30711129010,"ptoVta":7,"tipoCmp":1,"nroCmp":13389,"importe":"11439.99","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30709875821,"tipoCodAut":"E","codAut":"74030275879829"}'),
            ('2000006795586342.pdf', '{"ver":1,"fecha":"2023-11-14","cuit":20255531507,"ptoVta":3,"tipoCmp":1,"nroCmp":153,"importe":7040,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73467095369503}'),
            ('2000006966087902.pdf', '{"ver":"1","fecha":"2023-11-23","cuit":33717172189,"ptoVta":7,"tipoCmp":1,"nroCmp":5769,"importe":"10793.96","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":"73479124346527"}'),
            ('2000007367139794.pdf', '{"ver":1,"fecha":"2024-01-19","cuit":20310491099,"ptoVta":3,"tipoCmp":1,"nroCmp":7870,"importe":90324,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74039567808771}'),
            ('2000007319906440.pdf', '{"ver":1,"fecha":"2024-01-06","cuit":30712185488,"ptoVta":10,"tipoCmp":1,"nroCmp":2011,"importe":46811,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74028375391660}'),
            ('2000006788971254.pdf', '{"ver":1,"fecha":"2023-10-31","cuit":20211152800,"ptoVta":8,"tipoCmp":1,"nroCmp":4273,"importe":622436.27,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73440405182735}'),
            ('2000007305642262.pdf', '{"ver":1,"fecha":"2024-01-22","cuit":20275937011,"ptoVta":6,"tipoCmp":1,"nroCmp":3178,"importe":26000,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74041807350949}'),
            ('2000007305110094.pdf', '{"ver":1,"fecha":"2024-01-05","cuit":27236420197,"ptoVta":6,"tipoCmp":1,"nroCmp":5156,"importe":29100,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74017998767721}'),
            ('2000007387715912.pdf', '{"ver":1,"fecha":"2024-01-17","cuit":30717423484,"ptoVta":3,"tipoCmp":1,"nroCmp":2799,"importe":254016,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74034335589877}'),
            ('2000006835929544.pdf', '{"ver":1,"fecha":"2023-11-08","cuit":33590366329,"ptoVta":8,"tipoCmp":1,"nroCmp":7284,"importe":14178,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73459374223824}'),
            ('2000006891852836.pdf', '{"ver":1,"cuit":33715334319,"ptoVta":20,"tipoCmp":1,"nroCmp":2083,"importe":13964.48,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73469264415216}'),
            ('2000006882418578.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":30715087738,"ptoVta":11,"tipoCmp":1,"nroCmp":1323,"importe":48899,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73468933099867}'),
            ('2000006883967990.pdf', '{"ver":1,"fecha":"2023-11-13","cuit":20340710062,"ptoVta":3,"tipoCmp":1,"nroCmp":438,"importe":18900.0,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73462259065050}'),
            ('2000006891282390.pdf', '{"ver":1,"fecha":"2023-11-22","cuit":20114671259,"ptoVta":3,"tipoCmp":1,"nroCmp":3621,"importe":24000.0,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73479897694310}'),
            ('2000006796541102.pdf', '{"ver":"1","fecha":"2023-11-02","cuit":30715294415,"ptoVta":3,"tipoCmp":1,"nroCmp":1035,"importe":"10999.98","moneda":"PES","ctz":"1.00","tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":"73445678645164"}'),
            ('2000006896654198.pdf', '{"ver":1,"fecha":"2023-11-15","cuit":30713852704,"ptoVta":2,"tipoCmp":1,"nroCmp":8198,"importe":42500.0,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73464126584619}'),
            ('2000006846332512.pdf', '{"ver":1,"fecha":"2023-11-22","cuit":30711905452,"ptoVta":7,"tipoCmp":1,"nroCmp":3184,"importe":19293.78,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73472876582332}'),
            ('2000006795586344.pdf', '{"ver":1,"fecha":"2023-11-14","cuit":20255531507,"ptoVta":3,"tipoCmp":1,"nroCmp":153,"importe":7040,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73467095369503}'),
            ('2000007359945828.pdf', '{"ver":1,"fecha":"2024-01-12","cuit":30655921644,"ptoVta":8,"tipoCmp":1,"nroCmp":59501,"importe":37200,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74024750501331}'),
            ('2000006846229610.pdf', '{"ver":1,"fecha":"2023-11-09","cuit":30695068286,"ptoVta":6,"tipoCmp":1,"nroCmp":118954,"importe":105978,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73456468252481}'),
            ('2000007387102104.pdf', '{"ver":1,"fecha":"2024-01-16","cuit":30715821296,"ptoVta":4,"tipoCmp":1,"nroCmp":17699,"importe":53688.18,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":74036242343989}'),
            ('2000007360153112.pdf', '{"ver":1,"fecha":"2024-01-12","cuit":30716059274,"ptoVta":8,"tipoCmp":1,"nroCmp":2327,"importe":87870,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30709875821,"tipoCodAut":"E","codAut":74024737929199}'),
            ('2000006782171352.pdf', '{"ver":1,"fecha":"2023-10-31","cuit":30615304944,"ptoVta":2,"tipoCmp":1,"nroCmp":23625,"importe":12750.0,"moneda":"PES","ctz":1.0,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73444426082354}'),
            ('2000006976837030.pdf', '{"ver":1,"fecha":"2023-11-25","cuit":23317835019,"ptoVta":8,"tipoCmp":1,"nroCmp":6491,"importe":32474.0,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73479309901795}'),
            ('2000006831197192.pdf', '{"ver":1,"fecha":"2023-11-07","cuit":30708910003,"ptoVta":107,"tipoCmp":1,"nroCmp":305,"importe":125602.4,"moneda":"PES","ctz":1.0,"tipoDocRec":8}'),
            ('2000007387345660.pdf', '{"ver":1,"fecha":"2024-01-16","cuit":27126668150,"ptoVta":10,"tipoCmp":1,"nroCmp":1708,"importe":51556.21,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30709875821,"tipoCodAut":"E","codAut":74030185745545}'),
            ('2000006831202610.pdf', '{"ver":1,"fecha":"2023-11-07","cuit":30708910003,"ptoVta":107,"tipoCmp":1,"nroCmp":307,"importe":125602.4,"moneda":"PES","ctz":1.0,"tipoDocRec":8}'),
            ('2000006966100266.pdf', '{"ver":1,"fecha":"2023-11-24","cuit":30715138707,"ptoVta":13,"tipoCmp":1,"nroCmp":4780,"importe":24000,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73477140754576}'),
            ('2000006831202602.pdf', '{"ver":1,"fecha":"2023-11-07","cuit":30708910003,"ptoVta":107,"tipoCmp":1,"nroCmp":306,"importe":125602.4,"moneda":"PES","ctz":1.0,"tipoDocRec":8}'),
            ('2000006896618636.pdf', '{"ver":1,"fecha":"2023-11-20","cuit":30710804245,"ptoVta":11,"tipoCmp":1,"nroCmp":22049,"importe":14810.24,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73475683560421}'),
            ('2000006976835534.pdf', '{"ver":1,"fecha":"2023-11-25","cuit":23317835019,"ptoVta":8,"tipoCmp":1,"nroCmp":6490,"importe":32474.0,"moneda":"PES","ctz":1,"tipoDocRec":80,"nroDocRec":30717336905,"tipoCodAut":"E","codAut":73479309859589}'),
            ('2000007302947382.pdf', None)
        ]

        for filename, expected_metadata in filenames_and_expected_metadatas:
            decoded_cae = get_cae_metadata(os.path.join(os.path.dirname(__file__), 'sample_files', filename))
            self.assertEqual(decoded_cae, expected_metadata)
