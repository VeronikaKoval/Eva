from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class BasePopup(BasePage):

# Locators

    popup_locator = (By.CSS_SELECTOR, 'div.modal-content')

    def __init__(self):
        super(BasePopup, self).__init__()
        popup_window = self.wait.until(EC.visibility_of_any_elements_located(self.popup_locator))[0]
        self.wait = WebDriverWait(popup_window, self.wait_element_time)
