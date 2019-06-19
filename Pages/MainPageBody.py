from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_components.BasePage import BasePage


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
    akzii_block = (By.CSS_SELECTOR, 'div.action-items')
    top_prodazh = (By.CSS_SELECTOR, 'div#amasty-shopby-product-list')
    popular_categories = (By.CSS_SELECTOR, 'div.popular-categories-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-list.owl-carousel.owl-loaded.owl-drag')
    mosaica = (By.CSS_SELECTOR, 'div.mosaic-block-wrap')
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
        """
        Click on 'Все разделы' menu item,
        :return: True if main drop down menu is visible after clicking
        :return True, if element is visible, otherwise returns 'False'
         """
        self.click(self.confirm_location_btn, 'Confirm suggested loc btn')
        self.wait.until(EC.presence_of_element_located(self.all_menu_items)).click()
        return self.is_element_visible(self.left_side_menu, 'left side menu')

    def hover_menu_item_uhod(self):
        """
        Click on 'Все разделы' menu item, hovering "Uhod" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
        """
        self.click(self.confirm_location_btn, 'Confirm suggested loc btn')
        self.wait.until(EC.presence_of_element_located(self.all_menu_items)).click()
        self.hover_element(self.uhod_mi, '"Uhod" menu item')
        return self.is_element_visible(self.drop_down_menu_uhod, 'Uhod drop down')

    def hover_menu_item_parfum(self):
        """
        Click on 'Все разделы' menu item, hovering "Parfumerija" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
        """
        self.hover_element(self.parfumeria_mi, '"Parfumeruia" menu item')
        return self.is_element_visible(self.drop_down_menu_parfum, 'Parfumeriia drop down')

    def hover_menu_item_dlja_domy(self):
        """
        Click on 'Все разделы' menu item, hovering "Tovary dlja domy" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
        """
        self.hover_element(self.tovary_dlja_doma_mi, '"Dlia domu" menu item')
        return self.is_element_visible(self.drop_down_menu_dlja_domu, 'Dlia domu drop down')

    def hover_menu_item_himija(self):
        """
        Click on 'Все разделы' menu item, hovering "Himija" menu item,
        :return: True if drop down menu is visible, otherwise returns 'False'
        """
        self.hover_element(self.himija_mi, '"Himiia" menu item')
        return self.is_element_visible(self.drop_down_menu_himija, 'Himija drop down')

    def hover_menu_item_aksesuaru(self):
        """
        Click on 'Все разделы' menu item, hovering "Aksesuaru" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
        """
        self.hover_element(self.aksesuaru_mi, '"Aksesyaru" menu item')
        return self.is_element_visible(self.drop_down_menu_aksesuaru, 'Aksesyaru drop down')

    def hover_menu_item_kosmetika(self):
        """
        Click on 'Все разделы' menu item, hovering "Kosmetika dekoratyvna" menu item,
        :return: True if drop down menu is visible after hovering category, v
        """
        self.hover_element(self.kosmetika_dekorat_mi, '"Dekoratyvna kosmetyka" menu item')
        return self.is_element_visible(self.drop_down_menu_kosmetika, 'Dekoratyvna kosmetuka')

    def hover_menu_item_dlja_muzhchin(self):
        """
        Click on 'Все разделы' menu item, hovering "Tovary dlja muzchin" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
         """
        self.hover_element(self.dlja_muzchin_mi, '"Dlia muzhchin"menu item')
        return self.is_element_visible(self.drop_down_menu_dlja_muzchin, 'dlia muzhchin drop down')

    def hover_menu_item_dlja_ditej(self):
        """
        Click on 'Все разделы' menu item, hovering "Tovary dlja ditej" menu item,
        :return: True if drop down menu is visible after hovering category, otherwise returns 'False'
         """
        self.hover_element(self.dlja_ditej_mi, '"Dlia ditej" menu item')
        return self.is_element_visible(self.drop_down_dlja_ditej, 'Dlia ditej drop down')

    def is_slider_visible(self):
        """
        Check if the banner is visible,
        :return: True if the slider is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.slider, 'Slider')

    def is_side_banner_visible(self):
        """
        Check if the side banner is visible,
        :return: True if the side banner is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.side_banner, 'Side banner')

    def is_timer_visible(self):
        """
        Check if the timer in the "Tovar dnja" banner is visible,
        :return: True if the timer is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.timer, 'Timer')

    def is_akzii_block_visible(self):
        """ Checking if the "Akzii" block is visible,
        :return: True if the block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.akzii_block, 'Block "Aktsii"')

    def is_top_prodazh_visible(self):
        """
        Check if the "Top prodazh" block is visible,
        :return: True if the "Top prodazh" block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.top_prodazh, 'Block "Top prodazh"')

    def is_popular_categories_visible(self):
        """
        Check if the "Popular categories" block is visible,
        :return: True if the "Popular categories" block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.popular_categories, 'Block "Popular categories"')

    def is_brands_block_visible(self):
        """
        Check if the "Brands" block is visible,
        :return: True if the "Brands" block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.brands_block, 'Block "Brands"')

    def is_mozaika_block_visible(self):
        """
        Check if the "Mozaika" block is visible,
        :return: True if the "Brands" block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.mosaica, 'Block "Mozaika"')

    def is_blog_visible(self):
        """
        Check if the "Blog" block is visible,
        :return: True if the "Blog" block is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.blog, 'Block "Blog"')

    def click_all_promotion_btn(self):
        """
        Click "Vse Akzii" button, check if button is visible,
        :return: object of page
        """
        return self.wait.until(EC.visibility_of_element_located(self.vsi_akzii_btn)).click()

    def click_all_brands_btn(self):
        """
        Click "All brands" button, check if button is visible,
        :return: object of page
        """
        return self.wait.until(EC.visibility_of_element_located(self.all_brands_btn)).click()

    def open_blog(self):
        """
        Click "Go to blog" button, check if button is visible,
        :return: object of page
        """
        return self.wait.until(EC.visibility_of_element_located(self.go_to_blog_btn)).click()

    def get_slider_photo_src(self):
        """ Get the photo src to verify that photos are changing,
        :return: photo src
        """
        slider_image = self.wait.until(EC.presence_of_element_located(self.base_slider_img))
        image_src = slider_image.get_attribute('src')
        return image_src

    def click_scroll_btn(self):
        """
        Click right scroll button on the slider to switch image,
        :return: object of page
        """
        return self.click(self.slider_scroll_btn, 'Scroll button')

    def get_brand_img_src(self):
        """
        Get the photo src in the "Brands" block to verify that photos are changing,
        :return: photo src"""
        brand_image_1st = self.wait.until(EC.presence_of_element_located(self.brand_base_img))
        img_src = brand_image_1st.get_attribute('src')
        return img_src

    def get_next_brand_img_src(self):
        """
        Get the next photo src in the "Brands" block after clicking scroll btn
        to verify that photos are changing,
        :return: photo src """
        brand_image_3rd = self.wait.until(EC.presence_of_element_located(self.brand_img_3))
        img_src = brand_image_3rd.get_attribute('src')
        return img_src

    def click_brands_scroll_btn(self):
        """
        Click right scroll button on the slider to switch image,
        :return: object of page
        """
        self.wait.until(EC.visibility_of_any_elements_located(self.slider_scroll_btn))[2].click()
        return self