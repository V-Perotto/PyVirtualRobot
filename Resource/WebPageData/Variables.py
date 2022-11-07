import os
from pathlib import Path

ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
CURDIR = os.getcwd() # Path(os.path.dirname(os.path.abspath(__file__)))

driver_path = os.path.join(ROOT, 'drivers/geckodriver.exe')
url = "https://prenotami.esteri.it/Home?ReturnUrl=%2fServices"
data_it = os.path.join(ROOT, 'data/data.json')
comprovantes = os.path.join(ROOT, 'output')