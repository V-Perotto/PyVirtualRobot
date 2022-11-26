import os
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resource.Settings import DRIVER, TIMEOUT, ROOT

class Browser():
    
    def __init__(self) -> None:
        pass

    def open_browser(self, url: str ="https://www.google.com"):
        DRIVER.get(url)

    def close_browser(self):
        DRIVER.close()

    def click_element(self, locator: str):
        """
        Args:
            locator (str): Click element using XPath.
        """
        DRIVER.find_element_by_xpath(locator).click()

    def input_text(self, locator: str, text):
        element = DRIVER.find_element_by_xpath(locator)
        element.send_keys(text)

    def screenshot(self, locator: str, filename: str = os.path.join(f"{ROOT}/")):
        """
            Take a Screenshot of a page in selected Driver and save filename as PNG.
        """
        try:
            with open(filename, 'wb') as file:
                file.write(DRIVER.find_element_by_xpath(locator).screenshot_as_png)
            return filename
        except Exception as e:
            raise e

    def wait_until_element_is_visible(self, locator: str, timeout: int = TIMEOUT):
        try:
            WebDriverWait(DRIVER, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def wait_until_element_is_not_visible(self, locator: str, timeout: int = TIMEOUT):
        try:
            WebDriverWait(DRIVER, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def get_text(self, locator: str):
        return DRIVER.find_element_by_xpath(locator).text

    def clear(self, locator: str):
        try:
            DRIVER.find_element_by_xpath(locator).clear()
            return True
        except:
            return False

    def get_value(self, locator: str, value: str):
        return DRIVER.find_element_by_xpath(locator).get_attribute(value)

    def count_itens(self, bag: str):
        count_of_tags = len(DRIVER.find_elements(by=By.XPATH, value=bag))
        return count_of_tags

    def choose_file(self, locator: str, file: str):
        try:
            upload_file = DRIVER.find_element_by_xpath(locator)
            upload_file.sendKeys(file)
            return True
        except:
            return False 

    def select_checkbox(self, locator: str):
        try:
            checked = DRIVER.find_element_by_xpath(locator).get_attribute('checked')
            if not checked:
                DRIVER.find_element_by_xpath(locator).click()
            if checked:
                return True
            return True
        except:
            return False
        
browser = Browser()