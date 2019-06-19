import time

from selenium.webdriver.common.by import By

from base_components.BaseTest import BaseTest

from Pages.MainPageBody import Body


class TestBody(BaseTest):

    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')


    def setup(self):
        super(TestBody, self).setup()
        self.driver.get(self.base_url)

    def test_main_drop_down_menu(self):
        """
        Click on 'Все разделы' menu item, checking the presence of the side drop down menu
        :return True, if element is present, otherwise returns 'False'
        """
        main_page = Body()
        assert main_page.is_main_drop_down_menu_present(), 'The side drop down menu is absent'

    def test_hover_menu_categories(self):
        """
        Click on 'Все разделы' menu item, hovering each menu category,
        checking if the drop down menu is visible,
        :return True, if elements are visible, otherwise returns 'False'
        """
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
        assert main_page.hover_menu_item_dlja_muzhchin() is True, \
            'The drop down menu is not visible after hovering "Dlja muzhchin" menu item'
        assert main_page.hover_menu_item_dlja_ditej() is True, \
            'The drop down menu is not visible after hovering "Tovary dlja ditej" menu item'

    def test_visibility_of_all_blocks(self):
        """
        Check if the banner, side banner, "Akzii", "Top prodazh", "Nabory", "Popular categories",
        "Brands" blocks are present and visible
        :return True, if element is present, otherwise returns 'False
        """
        main_page = Body()
        assert main_page.is_side_banner_visible(), 'Side banner is not visible or absent'
        assert main_page.is_slider_visible(), 'The slider is not visible'
        assert main_page.is_timer_visible(), 'The timer is not visible or absent'
        assert main_page.is_akzii_block_visible(), 'Block "Akzii" is not visible or absent'
        assert main_page.is_top_prodazh_visible(), 'Block "Top prodazh" is not visible or absent'
        assert main_page.is_popular_categories_visible(), 'Block "Popular categories" is not visible or absent'
        assert main_page.is_brands_block_visible(), 'Block "Brands" is not visible'
        assert main_page.is_mozaika_block_visible(), 'Block "Mosaica" is not visible or absent'
        assert main_page.is_blog_visible(), 'Blog is not visible or absent'

    def test_buttons_in_blocks(self):
        """
        Click "All promotions" btn, "All brands", "Go to blog" buttons, get pages current Urls to verify
        that new page is opened
        :return True, if page url coincides with expected, otherwise returns 'False"""
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
        """
        Check if  the slider is present. Click right scroll button on the slider to switch image.
        Get the photo src to verify that photos are changing
        :return True, if photos src are different, otherwise returns 'False
        """
        main_page = Body()
        for i in range(4):
            photo_src = main_page.get_slider_photo_src()
            main_page.click_scroll_btn()
            assert photo_src != main_page.get_slider_photo_src(), \
                'Photo src is the same, photos in the slider are not changing '

    def test_changing_brands_photos(self):
        """
        Check if the "Brands" block is visible. Click right scroll button in the banner to switch image.
        Get the photo src to verify that photos are changing
        :return True, if photos src are different, otherwise returns 'False
        """
        main_page = Body()
        assert main_page.is_brands_block_visible(), 'Block "Brands" is not visible'
        main_page.click_brands_scroll_btn()
        time.sleep(2)
        assert main_page.get_brand_img_src() != main_page.get_next_brand_img_src(), \
            'Photo src is the same, brands images are not changing'