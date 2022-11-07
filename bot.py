from math import radians
import time
import os
from Bot.Resource.Library.Browser import Browser
from config.variables import url, data_it, comprovantes, driver_path
from config.locators import locators as x
from Bot.Resource.Library.lib_json import lib_json

class Pepperoni:

    def consulado_italiano(self):
        try: 
            browser = Browser() 
            driver = browser.start_driver() # path
            browser.open_browser(driver, url=url)
            visible = browser.wait_until_element_is_visible(driver, x['input_email'], 10)
            if visible:
                UNPW = lib_json.read(self, data_it)
                browser.input_text(driver, x['input_email'], UNPW['UN'])
                browser.input_text(driver, x['input_pass'], UNPW['PW'])
                browser.click_element(driver, x['btn_submit'])
                time.sleep(1)
                visible = browser.wait_until_element_is_visible(driver, x['btn_reservar'], 10)
                if visible:
                    browser.click_element(driver, x['btn_reservar'])
                    visible = browser.wait_until_element_is_visible(driver, x['btn_cidadania_reserva'], 10)
                    if visible:
                        browser.click_element(driver, x['btn_cidadania_reserva'])
                        visible = browser.wait_until_element_is_visible(driver, x['btn_cidadania_reserva'], 10)
                        if visible:
                            browser.click_element(driver, x['btn_cidadania_reserva'])
                            # capturar arquivos, etc e etc, por nome e talz
                            # browser.choose_file(driver, x['btn_choose_file'], os.path.join(comprovantes, 'comprovante_victor.pdf'))
                            browser.click_element(x['box_privacy'])
                            print(driver.find_element_by_xpath(x['box_privacy']).get_attribute('checked'))
                            checked = browser.select_checkbox(driver, x['box_privacy'])
                            print(checked)
                            # if checked:
                            #     browser.click_element(driver, x['btn_avanti'])
        except:
            time.sleep(5)
            driver.quit()

pasta = Pepperoni()
pasta.consulado_italiano()