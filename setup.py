from setuptools import setup, find_packages

setup(
    name='pidisplay',
    version='0.0.0',
    description='a display status server for Raspberry Pi',
    packages=find_packages(),
    install_requires=[
        'Adafruit_SSD1306'
    ],
)
