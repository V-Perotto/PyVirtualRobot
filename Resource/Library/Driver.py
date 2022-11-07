import imp
from selenium import webdriver
from configs.variables import CHROMEDRIVER_DIRECTORY

class Driver():

    def __chromedriver(self, driver_path):
        # driver_path = 'chromedriver.exe'
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("useAutomationExtension", False)
        options = options.add_experimental_option("excludeSwitches",["enable-automation"])
        return webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    def __geckodriver(self, driver_path):
        return -1

    def set_driver(self, name="chrome", driver_path=CHROMEDRIVER_DIRECTORY):
        if "chrome" in name.lower():
            return self.__chromedriver(driver_path)
        if "gecko" in name.lower() or "firefox" in name.lower():
            return self.__geckodriver(driver_path)
        else:
            # logging.critical "Navegador não encontrado"
            ...