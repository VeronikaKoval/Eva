from selenium import webdriver


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/ve.koval/Downloads\chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()

    def teardowm(self):
        self.driver.close()
