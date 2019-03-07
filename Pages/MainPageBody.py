import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Body(BasePage):

    # Locators

    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')

    left_side_menu = (By.CSS_SELECTOR, 'ul.left-menu.js-left-menu')
    all_menu_items = (By.CSS_SELECTOR, 'span.top-level-a')
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

    drop_down_menu_uhod = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu.width-banner.mansorny')
    drop_down_menu_parfum = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="380"]')
    drop_down_menu_dlja_domu = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="817"]')
    # drop_down_menu_himija = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="380"]')
    drop_down_menu_aksesuaru = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="444"]')
    drop_down_menu_kosmetika = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="416"]')
    # drop_down_menu_dlja_muzchin = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="380"]')
    drop_down_dlja_ditej = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="391"]')

    product_block = (By.CSS_SELECTOR, 'div.block-product-tabs')
    linejka_tovarov = (By.CSS_SELECTOR, 'div.new-banners-wrap')
    naboru_block = (By.CSS_SELECTOR, 'div.collecting-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-wrap')

    slider = (By.CSS_SELECTOR, 'div.hp-promo-slider.hp-promo-slider-adaptive')
    base_slider_image = (By.CSS_SELECTOR, '#maincontent > div.columns > div.column.main > div.block-hp-promo-slider \
     > div > div.owl-stage-outer > div > div.owl-item.active > div > a > picture > img')
    slider_scroll_btn = (By.CSS_SELECTOR, 'button.owl-next')

    # more_akzijnuch_tovariv_btn = (By.CSS_SELECTOR, 'a[href="https://eva.ua/promotion/"}') #LOCATOR IS NOT UNOQUE
    more_akzijnuch_tovariv_btn = (By.CSS_SELECTOR, 'div.block-more-btn > a.more-btn')

    # Actions

    def is_main_drop_down_menu_present(self):
        """ Clicking on 'Все разделы' menu item,
         :return: True if main drop down menu is visible after clicking"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.all_menu_items)).click()
        return self.is_element_visible(self.left_side_menu)

    def hover_menu_item_uhod(self):
        """ Clicking on 'Все разделы' menu item, hovering "Uhod" menu item,
        :return: True if drop down menu is visible after hovering category"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.all_menu_items)).click()
        self.hover_element(self.uhod_mi)
        return self.is_element_visible(self.drop_down_menu_uhod)

    def hover_menu_item_parfum(self):
        """ Clicking on 'Все разделы' menu item, hovering "Parfumerija" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.parfumeria_mi)
        return self.is_element_visible(self.drop_down_menu_parfum)

    def hover_menu_item_dlja_domy(self):
        """ Clicking on 'Все разделы' menu item, hovering "Tovary dlja domy" menu item,
        :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.tovary_dlja_doma_mi)
        return self.is_element_visible(self.drop_down_menu_dlja_domu)

    # def hover_menu_item_himija(self):
    #  """ Clicking on 'Все разделы' menu item, hovering "Himija" menu item,
    #      :return: True if drop down menu is visible after hovering category"""
    #     self.hover_element(self.himija_mi)
    #     return self.is_element_visible(self.drop_down_menu_himija)

    def hover_menu_item_aksesuaru(self):
        """ Clicking on 'Все разделы' menu item, hovering "Aksesuaru" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.aksesuaru_mi)
        return self.is_element_visible(self.drop_down_menu_aksesuaru)

    def hover_menu_item_kosmetika(self):
        """ Clicking on 'Все разделы' menu item, hovering "Kosmetika dekoratyvna" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.kosmetika_dekorat_mi)
        return self.is_element_visible(self.drop_down_menu_kosmetika)

    # def hover_menu_item_dlja_muzchin(self):
    #     """ Clicking on 'Все разделы' menu item, hovering "Tovary dlja muzchin" menu item,
    #      :return: True if drop down menu is visible after hovering category"""
    #     self.hover_element(self.dlja_muzchin_mi)
    #     return self.is_element_visible(self.drop_down_menu_dlja_muzchin)

    def hover_menu_item_dlja_ditej(self):
        """ Clicking on 'Все разделы' menu item, hovering "Tovary dlja ditej" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.dlja_ditej_mi)
        return self.is_element_visible(self.drop_down_dlja_ditej)

    def is_pokupajte_vigodno_visible(self):
        """ Checking is product block present, :return: True if the section is visible"""
        return self.is_element_visible(self.product_block)

    def is_linejka_tovarov_visible(self):
        """ Checking presence of the block "Linejka tovarov", :return: True if the section is visible"""
        return self.is_element_visible(self.linejka_tovarov)

    def is_nabory_visible(self):
        """ Checking presence of the "Nabory" block, :return: True if the section is visible"""
        return self.is_element_visible(self.naboru_block)

    def is_brands_block_visible(self):
        """ Checking presence of the "Brands" block, :return: True if the section is visible"""
        return self.is_element_visible(self.brands_block)

    def is_slider_visible(self):
        """ Checking is slider present, :return: True if the slider is visible"""
        return self.is_element_visible(self.slider)

    def get_slider_photo_src(self):
        """ Getting the photo src to verify that photos are changing, :return: photo src"""
        slider_image = self.wait.until(EC.visibility_of_element_located(self.base_slider_image))
        image_src = slider_image.get_attribute('src')
        return image_src

    def click_scroll_btn(self):
        """ Clicking right scroll button on the slider to switch image"""
        self.click(self.slider_scroll_btn)
        return self

    def is_more_btn_visible(self):
        """ Checking if the "More promotions" btn is visible in the Product block,
        :return: True if the section is visible """
        return self.is_element_visible(self.more_akzijnuch_tovariv_btn)

    def click_more_btn(self):
        """ Clicking "More promotions" btn in the Product block"""
        return self.wait.until(EC.visibility_of_element_located(self.more_akzijnuch_tovariv_btn)).click()

