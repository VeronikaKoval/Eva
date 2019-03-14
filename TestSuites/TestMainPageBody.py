import time

from TestSuites.BaseTest import BaseTest

from Pages.MainPageBody import Body


class TestBody(BaseTest):


    def setup(self):
        super(TestBody, self).setup()
        self.driver.get(self.base_url)

    def test_main_drop_down_menu(self):
        """ Clicking on 'Все разделы' menu item, checking the presence of the side drop down menu"""
        main_page = Body()
        assert main_page.is_main_drop_down_menu_present() is True, 'The side drop down menu is absent'

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
        # assert main_page.is_akzii_block_visible is True, 'Block "Akzii" is not visible or absent'
        # # self.driver.execute_script("window.scrollTo(0, 2300)")
        assert main_page.is_top_prodazh_visible is True, 'Block "Top prodazh" is not visible or absent'
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
        self.driver.execute_script("window.history.go(-1)")
        main_page.click_all_brands_btn()
        assert 'brands' in main_page.get_page_url(), 'URL doesnt match "brands"'
        self.driver.execute_script("window.history.go(-1)")
        main_page.open_blog()
        assert main_page.get_page_url() == 'https://evaportal.com.ua/', 'URL doesnt match "evaportal.com.ua" '

    def test_changing_slider_photos(self):
        """ Checking if  the slider is present. Clicking right scroll button on the slider to switch image.
        Getting the photo src to verify that photos are changing, :return: photo src"""
        main_page = Body()
        for i in range(4):
            photo_src = main_page.get_slider_photo_src()
            main_page.click_scroll_btn()
            assert photo_src != main_page.get_slider_photo_src(), \
                'Photo src is the same, photos in the slider are not changing '

    def test_changing_brands_photos(self):
        """ """
        main_page = Body()
        assert main_page.is_brands_block_visible() is True, 'Block "Brands" is not visible'
        # for i in range(2):
        #     img_src = main_page.get_brand_img_src()
        #     main_page.click_brands_scroll_btn()
        #     print(img_src)
            # assert img_src != main_page.get_brand_img_src(), \
            #     'Photo src is the same, photos in the "Brands" block are not changing '
        main_page.click_brands_scroll_btn()
        time.sleep(2)
        assert main_page.get_brand_img_src() != main_page.get_next_brand_img_src(), \
            'Photo src is the same, brands images are not changing'
