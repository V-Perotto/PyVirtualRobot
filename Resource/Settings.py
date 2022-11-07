from Library.Driver import Driver
from Library.Listener import Listener
from Library.Logger import Logger

import pytesseract


### DRIVER
# Driver Variables
TIMEOUT = 30
# Driver configuration
Driver = Driver()
DRIVER = Driver.set_driver()

### OCR
POPPLER = "C:/Program Files/poppler-0.68.0/bin/"
pytesseract = pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"