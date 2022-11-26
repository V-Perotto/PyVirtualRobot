from selenium import webdriver

class Driver():

    def __init__(self) -> None:
        pass

    def __chromedriver(self, driver_path: str):
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("useAutomationExtension", False)
        options = options.add_experimental_option("excludeSwitches",["enable-automation"])
        return webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    def __geckodriver(self, driver_path: str):
        options = webdriver.FirefoxOptions()
        # options.add_experimental_option("useAutomationExtension", False)
        options = options.add_experimental_option("excludeSwitches",["enable-automation"])
        return webdriver.Firefox(executable_path=driver_path, finally_options=options)

    def set_driver(self, driver_path: str):
        """
        Args:
            driver_path (str, Required): Driver Directory.

        Returns:
            webdriver: Returns driver about choosed Browser (Ex.: chromedriver/geckodriver). 
        """
        try:
            if "chrome" in driver_path.lower():
                return self.__chromedriver(driver_path)
            if "gecko" in driver_path.lower() or "firefox" in driver_path.lower():
                return self.__geckodriver(driver_path)
        except Exception as e:
            raise e     # "Driver não foi especificado."
            # logging.critical "Navegador não encontrado"

driver = Driver()