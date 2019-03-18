import os

from selenium import webdriver

import time

import webdrivers


class Singleton(object):
    _instance = None

    @classmethod
    def get_webdriver(cls):
        if not cls._instance:
            cls._instance = Singleton()
            cls._driver = cls._instance._driver
        return cls._driver

    def __init__(self):
        webdrivers_path = os.path.dirname(webdrivers.__file__)
        drivers_path = os.path.join(webdrivers_path, "chromedriver.exe")
        self._driver = webdriver.Chrome(executable_path=drivers_path)
        self._driver.set_page_load_timeout(60)

    @classmethod
    def close_driver(cls):
        cls._driver.close()
        cls._driver.quit()
        cls._instance = None
