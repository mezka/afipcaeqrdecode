from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='afipcaeqrdecode',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'Pillow==10.1.0',
        'PyJWT==2.8.0',
        'PyMuPDF==1.23.6',
        'PyMuPDFb==1.23.6',
        'pyzbar==0.1.9'
    ],
    description='Package to decode and extract invoice metadata from an AFIP CAE qr code link',
    author='Emiliano Mesquita',
    license='GPLv3',
    long_description=long_description,
    long_description_content_type='text/markdown'
)