[Github Link for PyPI](https://github.com/mezka/afip_invoice_extract_qr_cae_and_decode) | [PyPI python package](https://pypi.org/project/afipcaeqrdecode/)

# AFIP invoice pdf qr CAE extract and decode

This is a python package that uses [pyzbar](https://pypi.org/project/pyzbar/) to extract QR codes from PDF files and decodes them in order to automate extraction of relevant invoice metadata like:

- Invoice date
- CUIT of invoice creator
- AFIP electronic invoice point of sale (Punto de venta)
- Invoice number
- Amount
- Currency
- CUIT of inovoice recipient

And other less important properties.

## Example Usage

Using the included sample files for demonstration (and ran from repository root using included sample file):

```
from afipcaeqrdecode import extract_images_from_pdf_afip_invoice_and_decode

invoice_metadata = extract_images_from_pdf_afip_invoice_and_decode('./tests/sample_files/2000005044986390.pdf')
```

Here, invoice metadata will evaluate to:

```
{
    "ver":1,
    "fecha":"2023-02-10",
    "cuit":30710145764,
    "ptoVta":4,
    "tipoCmp":1,
    "nroCmp":25399,
    "importe":2460,
    "moneda":"PES",
    "ctz":1,
    "tipoDocRec":80,
    "nroDocRec":30717336905,
    "tipoCodAut":"E",
    "codAut":73064176949471
}
```

## System Dependencies and their installation

This package depends on [pyzbar](https://pypi.org/project/pyzbar/), which in turn depends on the open source [ZBar library](https://zbar.sourceforge.net/)

Check your OS documentation on what package to install to get ZBar working with pyzbar.

On Linux (Ubuntu 22.04):

`sudo apt-get install libzbar0`


On Mac OS X:

`brew install zbar`

## Installation using pip

After installing system dependencies, you can install using the [PyPI python package](https://pypi.org/project/afipcaeqrdecode/)

`pip install afipcaeqrdecode`

## How does it work

It scans every image of the PDF invoice and then matches it with the format of the URL link that an AFIP CAE QR typically returns, if it matches it decodes it using `jwt.utils.base64url_decode`

## WARNING

This is an experimental package, DO NOT USE IT IN PRODUCTION.

It is barely even tested, i'm sharing it so I can actually import it as a PyPI package in another project that consumes it.

## Credits

Facundo Mainere for helping with JWT decode
Author: Emiliano Mesquita

## License

GNU GPLv3

