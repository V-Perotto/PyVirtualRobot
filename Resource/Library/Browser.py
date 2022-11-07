import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.variables import driver_path

class Browser():

    def open_browser(self, url: str ="https://www.google.com"):
        driver.get(url)

    def close_browser(self):
        driver.close()

    def click_element(self, locator: str):
        element = driver.find_element_by_xpath(locator)
        element.click()

    def input_text(self, locator: str, text):
        element = driver.find_element_by_xpath(locator)
        element.send_keys(text)

    def screenshot(self, locator: str, filename: str):
        with open(filename, 'wb') as file:
            file.write(driver.find_element_by_xpath(locator).screenshot_as_png)
        return filename

    def wait_until_element_is_visible(self, locator: str, timeout: int =TIMEOUT):
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def wait_until_element_is_not_visible(self, locator: str, timeout: int =TIMEOUT):
        try:
            WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def get_text(self, locator: str):
        return driver.find_element_by_xpath(locator).text

    def clear(self, locator: str):
        driver.find_element_by_xpath(locator).clear()

    def get_value(self, locator: str, value: str):
        return driver.find_element_by_xpath(locator).get_attribute(value)

    def count_itens(self, bag: str):
        count_of_tags = len(driver.find_elements(by=By.XPATH, value=bag))
        return count_of_tags

    def choose_file(self, locator: str, file: str):
        try:
            upload_file = driver.find_element_by_xpath(locator)
            upload_file.sendKeys(file)
            return True
        except:
            return False 
        # driver.findElement(By.id("terms")).click()
        # driver.findElement(By.name("send")).click()

    def select_checkbox(self, locator: str):
        try:
            checked = driver.find_element_by_xpath(locator).get_attribute('checked')
            if not checked:
                driver.find_element_by_xpath(locator).click()
            if checked:
                return True
            return True
        except:
            return False