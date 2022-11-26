import os
from pathlib import Path
from Resource.Library.Driver import driver
from Resource.Library.Listener import Listener
from Resource.Library.Logger import Logger
# import pytesseract

### Dir Paths
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
CURDIR = os.getcwd() # Path(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, 'Resource/Output')
INPUT_PATH = os.path.join(ROOT, 'Resource/Input')
SCREENSHOT_PATH = os.path.join(ROOT, 'Resource/Screenshot')

### Modules - OCR
# POPPLER = os.path.join(ROOT, "OCR/Poppler/bin/")
# pytesseract = pytesseract.pytesseract.tesseract_cmd = os.path.join(ROOT, "Tesseract/tesseract.exe")

### Modules - Browser
DRIVER = driver.set_driver(driver_path=os.path.join(ROOT, 'Browsers/BrowserName/browserdriver.exe'))
CHROMEDRIVER = driver.set_driver(driver_path=os.path.join(ROOT, 'Browsers/BrowserName/browserdriver.exe'))
GECKODRIVER = driver.set_driver(driver_path=os.path.join(ROOT, 'Browsers/BrowserName/browserdriver.exe'))

### Resource - Library

