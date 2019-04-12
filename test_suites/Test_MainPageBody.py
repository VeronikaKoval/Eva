import time

from selenium.webdriver.common.by import By

from base_components.BaseTest import BaseTest

from Pages.MainPageBody import Body


class TestBody(BaseTest):

    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')


    def setup(self):
        super(TestBody, self).setup()
        self.driver.get(self.base_url)

    # @pytest.mark.usefixtures("get_cookies")
    def test_main_drop_down_menu(self):
        """ Clicking on 'Все разделы' menu item, checking the presence of the side drop down menu"""
        main_page = Body()
        assert main_page.is_main_drop_down_menu_present() is True, 'The side drop down menu is absent'


    # @pytest.fixture()
    # def get_cookies_NEW(self):
    #     """ """
        # from singleton import Singleton
        # self.driver = Singleton.get_webdriver()
        #
        # # request.cls.driver.get('https://eva.ua/')
        # # from Pages.BasePage import BasePage
        # self.driver.click(self.confirm_location_btn, 'Confirm suggested loc btn')
        # cookies_list = self.driver.get_cookies()
        # print(cookies_list)
        # cookies_dict = {}
        # for cookie in cookies_list:
        #     cookies_dict[cookie['name']] = cookie['value']
        #     print(len(cookies_dict))
        #
        #     # def add_cookies(self):
        #     cookie = {'name': '', 'value': ''}
        #     self.driver.add_cookie(cookie)
        #     print(len(cookie))
        # return self.driver.add_cookie({'name': '', 'value': '', 'domain': ''})

    # @pytest.mark.usefixtures("get_cookies_NEW")
    def test_hover_menu_categories(self):
        """ Clicking on 'Все разделы' menu item, hovering each menu category,
         checking if the drop down menu is visible"""
        main_page = Body()
        assert main_page.hover_menu_item_uhod() is True, \
            'The drop down menu is not visible after hovering "Uhod" menu item'
        assert main_page.hover_menu_item_parfum() is True, \
            'The drop down menu is not visible after hovering "Parfumeria" menu item'
        assert main_page.hover_menu_item_dlja_domy() is True, \
            'The drop down menu is not visible after hovering "Tovary dlja domu" menu item'
        assert main_page.hover_menu_item_himija() is True, \
            'The drop down menu is not visible after hovering "Himija" menu item'
        assert main_page.hover_menu_item_kosmetika() is True, \
            'The drop down menu is not visible after hovering "Kosmetika dekoratuvna" menu item'
        assert main_page.hover_menu_item_dlja_muzchin() is True, \
            'The drop down menu is not visible after hovering "Dlja muzhchin" menu item'
        assert main_page.hover_menu_item_dlja_ditej() is True, \
            'The drop down menu is not visible after hovering "Tovary dlja ditej" menu item'

    def test_visibility_of_all_blocks(self):
        """ Checking if the banner. side banner, "Akzii", "Top prodazh", "Nabory", "Popular categories",
        "Brands"  blocks are present and visible """
        main_page = Body()
        assert main_page.is_side_banner_visible() is True, 'Side banner is not visible or absent'
        assert main_page.is_slider_visible() is True, 'The slider is not visible'
        assert main_page.is_timer_visible() is True, 'The timer is not visible or absent'
        assert main_page.is_akzii_block_visible() is True, 'Block "Akzii" is not visible or absent'
        assert main_page.is_top_prodazh_visible() is True, 'Block "Top prodazh" is not visible or absent'
        assert main_page.is_popular_categories_visible() is True, 'Block "Popular categories" is not visible or absent'
        assert main_page.is_brands_block_visible() is True, 'Block "Brands" is not visible'
        assert main_page.is_mozaika_block_visible() is True, 'Block "Mosaica" is not visible or absent'
        assert main_page.is_blog_visible() is True, 'Blog is not visible or absent'

    def test_buttons_in_blocks(self):
        """ Clicking "All promotions" btn, "All brands", "Go to blog" buttons, get pages current Urls to verify
        that new page is opened"""
        main_page = Body()
        main_page.click_all_promotion_btn()
        assert 'promotion' in main_page.get_page_url(), 'URL is different and doesnt match "promotion" '
        self.go_back_to_previous_tab()
        main_page.click_all_brands_btn()
        assert 'brands' in main_page.get_page_url(), 'URL doesnt match "brands"'
        self.go_back_to_previous_tab()
        main_page.open_blog()
        assert main_page.get_page_url() == 'https://evaportal.com.ua/', 'URL doesnt match "evaportal.com.ua" '

    def test_changing_slider_photos(self):
        """ Checking if  the slider is present. Clicking right scroll button on the slider to switch image.
        Getting the photo src to verify that photos are changing"""
        main_page = Body()
        for i in range(4):
            photo_src = main_page.get_slider_photo_src()
            main_page.click_scroll_btn()
            assert photo_src != main_page.get_slider_photo_src(), \
                'Photo src is the same, photos in the slider are not changing '

    def test_changing_brands_photos(self):
        """ Checking if the "Brands" block is visible. Clicking right scroll button in the banner to switch image.
        Getting the photo src to verify that photos are changing"""
        main_page = Body()
        assert main_page.is_brands_block_visible() is True, 'Block "Brands" is not visible'
        main_page.click_brands_scroll_btn()
        time.sleep(2)
        assert main_page.get_brand_img_src() != main_page.get_next_brand_img_src(), \
            'Photo src is the same, brands images are not changing'
