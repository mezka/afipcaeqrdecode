[PyPI package](https://pypi.org/project/afipcaeqrdecode/)

# AFIP invoice PDF QR CAE extract and decode

`afipcaeqrdecode` extracts AFIP CAE invoice metadata from PDF invoices. It renders the first page of the PDF, locates the AFIP QR code, decodes the QR payload, and returns the decoded metadata as a Python `dict`.

## Installation

This package depends on `qreader`, which depends on `pyzbar`, which depends on the system `zbar` library.

On Linux (Ubuntu 22.04):

`sudo apt-get install libzbar0`

On macOS:

`brew install zbar`

Then install the package:

`pip install afipcaeqrdecode`

## Quick Start

```python
from afipcaeqrdecode import get_cae_metadata

invoice_metadata = get_cae_metadata("./tests/sample_files/2000005044986390.pdf")
```

Example output:

```python
{
    "ver": 1,
    "fecha": "2023-02-10",
    "cuit": 30710145764,
    "ptoVta": 4,
    "tipoCmp": 1,
    "nroCmp": 25399,
    "importe": 2460,
    "moneda": "PES",
    "ctz": 1,
    "tipoDocRec": 80,
    "nroDocRec": 30717336905,
    "tipoCodAut": "E",
    "codAut": 73064176949471,
}
```

## Return Value

`get_cae_metadata(filepath, attempt_to_repair_json=True)` returns:

- a Python `dict` when AFIP QR metadata is decoded successfully
- `None` when no AFIP QR metadata can be extracted

The returned dictionary preserves the value types present in the decoded JSON payload. Some invoices encode numeric-looking values as JSON strings, and those values are preserved as strings.

## How It Works

The decoding flow has two stages:

1. Render the first page of the PDF with [PyMuPDF](https://pypi.org/project/PyMuPDF/) and run [qreader](https://pypi.org/project/qreader/) on the resulting image.
2. If that fails, extract embedded images from the first page and run `qreader` on those images as a fallback.

If the AFIP QR payload contains malformed JSON, [json-repair](https://pypi.org/project/json-repair/) is used by default to repair it before parsing.

## Why qreader instead of pyzbar

Earlier versions of this project used only [pyzbar](https://pypi.org/project/pyzbar/). Some real-world AFIP invoice QRs did not decode reliably with `pyzbar` alone.

`qreader` still uses `pyzbar` for decoding, but it first uses a trained QR detector and applies preprocessing strategies that improve decode rates on difficult images.

## Notes and Limitations

- On first run, `qreader` may download model weights before decoding.
- Some invoices omit fields such as `fecha` in the QR payload.
- This project is tested mainly with sample PDF integration tests in `tests/sample_files/`.
- This package is still experimental. Use it carefully in production workloads.

## Testing

Run the sample-based integration test suite with:

`python -m unittest tests.test_sample_files`

## License

GNU Lesser General Public License v3.0 or later (`LGPL-3.0-or-later`). See `LICENSE`.
