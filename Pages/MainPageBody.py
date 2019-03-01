from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Body(BasePage):


    # Locators
    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')

    left_side_menu = (By.CSS_SELECTOR, 'ul.left-menu.js-left-menu')
    menu_item = (By.CSS_SELECTOR, 'span.top-level-a')
    uhod_mi = (By.CSS_SELECTOR, 'a[href$="uhod-soboj/"]')
    parfumeria_mi = (By.CSS_SELECTOR, 'a[href$="parfjumerija/"]')
    tovary_dlja_doma_mi = (By.CSS_SELECTOR, 'a[href$="tovary-dlja-doma/"]')
    himija_mi = (By.CSS_SELECTOR, 'a[href$="bytovaja-himija/"]')
    aksesuaru_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/235/aksessuary/"')
    kosmetika_dekorat_mi = (By.CSS_SELECTOR, 'a[href$="kosmetika-dekorativnaja/"]')
    dlja_muzchin_mi = (By.CSS_SELECTOR, 'a[href$="dlja-muzhchin/"]')
    odezda_mi = (By.CSS_SELECTOR, 'a[href$="odezhda-obuv-aksessuary/"]')
    bizhuterija_mi = (By.CSS_SELECTOR, 'a[href$="bizhuterija/"]')
    dlja_ditej_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/12536/dlja-detej/"]')
    drop_down_menu = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu.width-banner.mansorny')

    product_block = (By.CSS_SELECTOR, 'div.block-product-tabs')
    linejka_tovarov = (By.CSS_SELECTOR, 'div.new-banners-wrap')
    naboru_block = (By.CSS_SELECTOR, 'div.collecting-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-wrap')



    # Actions
    def is_main_drop_down_menu_present(self):
        """ Clicking on 'Все разделы' menu item, checking the presence of the side drop down menu """
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        return self.is_element_present(self.left_side_menu)

    # def hover_menu_items(self):
    #     """ Hovering over menu items from left side menu and che checking drop down menu"""
    #     self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
    #     time.sleep(2)
    #     self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
    #     time.sleep(2)
    #     self.hover_element(self.uhod_mi)
    #     self.hover_element(self.parfumeria_mi)
    #     self.hover_element(self.tovary_dlja_doma_mi)
    #     self.hover_element(self.himija_mi)
    #     self.hover_element(self.aksesuaru_mi)
    #     self.hover_element(self.kosmetika_dekorat_mi)
    #     self.hover_element(self.dlja_muzchin_mi)
    #     self.hover_element(self.odezda_mi)
    #     self.hover_element(self.bizhuterija_mi)
    #     self.hover_element(self.dlja_ditej_mi)
    #     try:
    #         self.wait.until(EC.presence_of_element_located(self.drop_down_menu))
    #         return True
    #     except:
    #         return False

    def is_pokupajte_vigodno_visible(self):
        """ Checking is product block present"""
        return self.is_element_visible(self.product_block)

    def is_linejka_tovarov_visible(self):
        """ Checking presence of the block "Linejka tovarov" """
        return self.is_element_visible(self.linejka_tovarov)

    def is_nabory_visible(self):
        """ Checking presence of the "Nabory" block"""
        return self.is_element_visible(self.naboru_block)

    def is_brands_block_visible(self):
        """ Checking presence of the "Brands" block """
        return self.is_element_visible(self.brands_block)




