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
    drop_down_menu_himija = (By.CSS_SELECTOR, 'body > div.page-wrapper > div > div > nav > ul >'
         ' li.top-level.js-show-shadow.first-colapse.parent > ul > li.level-0.nav-4.level-top.parent > ul')
    # drop_down_menu_himija = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="380"]')
    drop_down_menu_aksesuaru = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="444"]')
    drop_down_menu_kosmetika = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="416"]')
    drop_down_menu_dlja_muzchin = (By.CSS_SELECTOR, 'body > div.page-wrapper > div > div > nav > ul > '
                'li.top-level.js-show-shadow.first-colapse.parent > ul > li.level-0.nav-7.level-top.parent > ul')
    #(By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="380"]')
    drop_down_dlja_ditej = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu[data-height="391"]')

    slider = (By.CSS_SELECTOR, 'div.action-banners-slider-block')
    side_banner = (By.CSS_SELECTOR, 'div.side-banners')
    akzii_block =  (By.CSS_SELECTOR, '#maincontent > div.columns > div:nth-child(2)')
    # (By.CSS_SELECTOR, 'div.action-items') #(By.CSS_SELECTOR, 'div.action-banners-wrap')
    top_prodazh = (By.CSS_SELECTOR, 'div#amasty-shopby-product-list') #(By.XPATH, '//*[@id="maincontent"]/div[2]/div[4]') #(By.CSS_SELECTOR, 'div.best-selling-wrap')
    popular_categories = (By.CSS_SELECTOR, 'div.popular-categories-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-list.owl-carousel.owl-loaded.owl-drag')
    mosaica = (By.CSS_SELECTOR, 'div.mosaic-block')
    blog = (By.CSS_SELECTOR, 'div.blog-wrap')

    vsi_akzii_btn = (By.CSS_SELECTOR, 'div.all-action-url > a[href="https://eva.ua/promotion/"]')
    all_brands_btn = (By.CSS_SELECTOR, 'div.more-brands-link > a[href="https://eva.ua/brands/"]')
    go_to_blog_btn = (By.CSS_SELECTOR, 'a[href="http://evaportal.com.ua/"]')

    base_slider_img = (By.CSS_SELECTOR, '#maincontent > div.columns > div:nth-child(1) > div > div > '
    'div.action-banners-slider-block > div.banners-slider-block.owl-loaded.owl-drag.owl-carousel.loaded > '
    'div.owl-stage-outer > div > div.owl-item.active > div > a > picture > img')
    slider_scroll_btn = (By.CSS_SELECTOR, 'button.owl-next')

    brand_base_img = (By.CSS_SELECTOR, '#maincontent > div.columns > div:nth-child(6) > '
    'div > div.brands-list.owl-carousel.owl-loaded.owl-drag > div.owl-stage-outer > div > div > div > a > div > picture > img')
    brand_img_3 = (By.CSS_SELECTOR, '#maincontent > div.columns > div:nth-child(6) > div > div.brands-list.owl-carousel.owl-loaded.owl-drag > '
                        'div.owl-stage-outer > div > div:nth-child(3) > div > a > div > picture > img')
    brand_scroll_btn = (By.CSS_SELECTOR, 'button.owl-next')

    timer = (By.CSS_SELECTOR, 'div.timer_block')

    recovery_pass_succ_msg = (By.CSS_SELECTOR,'div.message-success.success.message')

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

    def hover_menu_item_himija(self):
        """ Clicking on 'Все разделы' menu item, hovering "Himija" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.himija_mi)
        return self.is_element_visible(self.drop_down_menu_himija)

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

    def hover_menu_item_dlja_muzchin(self):
        """ Clicking on 'Все разделы' menu item, hovering "Tovary dlja muzchin" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.dlja_muzchin_mi)
        return self.is_element_visible(self.drop_down_menu_dlja_muzchin)

    def hover_menu_item_dlja_ditej(self):
        """ Clicking on 'Все разделы' menu item, hovering "Tovary dlja ditej" menu item,
         :return: True if drop down menu is visible after hovering category"""
        self.hover_element(self.dlja_ditej_mi)
        return self.is_element_visible(self.drop_down_dlja_ditej)

    def is_slider_visible(self):
        """ Checking if the banner is visible,
        :return: True if the slider is visible"""
        return self.is_element_visible(self.slider)

    def is_side_banner_visible(self):
        """ Checking if the side banner is visible,
        :return: True if the side banner is visible"""
        return self.is_element_visible(self.side_banner)

    def is_timer_visible(self):
        """ Checking if the timer in the "Tovar dnja" banner is visible,
        :return: True if the timer is visible"""
        return self.is_element_visible(self.timer)

    def is_akzii_block_visible(self):
        """ Checking if the "Akzii" block is visible,
        :return: True if the block is visible """
        return self.is_element_visible(self.akzii_block)

    def is_top_prodazh_visible(self):
        """ Checking if the "Top prodazh" block is visible,
        :return: True if the "Top prodazh" block is visible"""
        return self.is_element_visible(self.top_prodazh)

    def is_popular_categories_visible(self):
        """ Checking if the "Popular categories" block is visible,
        :return: True if the "Popular categories" block is visible"""
        return self.is_element_visible(self.popular_categories)

    def is_brands_block_visible(self):
        """ Checking if the "Brands" block is visible,
        :return: True if the "Brands" block is visible"""
        return self.is_element_visible(self.brands_block)

    def is_mozaika_block_visible(self):
        """ Checking if the "Mozaika" block is visible,
        :return: True if the "Brands" block is visible"""
        return self.is_element_visible(self.mosaica)

    def is_blog_visible(self):
        """ Checking if the "Blog" block is visible,
        :return: True if the "Blog" block is visible """
        return self.is_element_visible(self.blog)

    def click_all_promotion_btn(self):
        """ Clicking "Vse Akzii" button, check if button is visible,
        :return: object of page"""
        return self.wait.until(EC.visibility_of_element_located(self.vsi_akzii_btn)).click()

    def click_all_brands_btn(self):
        """ Clicking "All brands" button, check if button is visible,
        :return: object of page"""
        return self.wait.until(EC.visibility_of_element_located(self.all_brands_btn)).click()

    def open_blog(self):
        """ Clicking "Go to blog" button, check if button is visible,
        :return: object of page"""
        return self.wait.until(EC.visibility_of_element_located(self.go_to_blog_btn)).click()

    def get_slider_photo_src(self):
        """ Getting the photo src to verify that photos are changing,
        :return: photo src"""
        slider_image = self.wait.until(EC.presence_of_element_located(self.base_slider_img))
        image_src = slider_image.get_attribute('src')
        return image_src

    def click_scroll_btn(self):
        """ Clicking right scroll button on the slider to switch image,
        :return: object of page """
        return self.click(self.slider_scroll_btn)

    def get_brand_img_src(self):
        """ Getting the photo src in the "Brands" block to verify that photos are changing,
        :return: photo src"""
        brand_image_1st = self.wait.until(EC.presence_of_element_located(self.brand_base_img))
        img_src = brand_image_1st.get_attribute('src')
        return img_src

    def get_next_brand_img_src(self):
        """ Getting the next photo src in the "Brands" block after clicking scroll btn
        to verify that photos are changing,
        :return: photo src """
        brand_image_3rd = self.wait.until(EC.presence_of_element_located(self.brand_img_3))
        img_src = brand_image_3rd.get_attribute('src')
        return img_src

    def click_brands_scroll_btn(self):
        """ Clicking right scroll button on the slider to switch image,
        :return: object of page"""
        # self.click(self.brand_scroll_btn)
        # self.wait.until(EC.element_to_be_clickable(self.brand_scroll_btn)).click()
        self.wait.until(EC.visibility_of_any_elements_located(self.slider_scroll_btn))[2].click()
        return self

    def get_recovery_success_msg_text(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering valid email,
        clicking "Получить новый пароль" btn",
        :return: recovery success msg text"""
        return self.wait.until(EC.visibility_of_element_located(self.recovery_pass_succ_msg)).text

