import os

from selenium import webdriver

import webdrivers


class Driver:
    _instance = None

    @classmethod
    def get_webdriver(cls):
        if not cls._instance:
            cls._instance = Driver()
            cls._driver = cls._instance._driver
        return cls._driver

    def __init__(self):
        webdrivers_path = os.path.dirname(webdrivers.__file__)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        drivers_path = os.path.join(webdrivers_path, "chromedriver.exe")
        self._driver = webdriver.Chrome(executable_path=drivers_path, options=options)
        self._driver.set_page_load_timeout(60)


    @classmethod
    def close_driver(cls):
        cls._driver.close()
        cls._driver.quit()
        cls._instance = None
