from selenium.webdriver.common.by import By

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
        # assert main_page.hover_menu_item_himija() is True, ''
        assert main_page.hover_menu_item_kosmetika() is True, \
            'The drop down menu is not visible after hovering "Kosmetika dekoratuvna" menu item'
        # assert main_page.hover_menu_item_dlja_muzchin() is True, ''
        assert main_page.hover_menu_item_dlja_ditej() is True, \
            'The drop down menu is not visible after hovering "Tovary dlja ditej" menu item'


    def test_presence_of_presence_of_all_blocks(self):
        """ Checking if the "Product block", "Linejka tovarov", "Nabory", "Brands" are present """
        main_page = Body()
        assert main_page.is_pokupajte_vigodno_visible() is True,\
            'The block "Pokupajte vigodno" is not visible or absent'
        assert main_page.is_linejka_tovarov_visible() is True, \
            'The block "Linejka tovarov" is not visible or absent'
        assert main_page.is_nabory_visible() is True, \
            'The block "Nabory" is not visible or absent'
        assert main_page.is_brands_block_visible() is True, \
            'The block "Brands" is not visible or absent' ## ПЕРЕПИСАТИ ВІДПОВІДНО ДО ОНОВЛЕНЬ

    def test_changing_slider_photos(self):
        """ Checking if  the slider is present. Clicking right scroll button on the slider to switch image.
        Getting the photo src to verify that photos are changing, :return: photo src"""
        main_page = Body()
        assert main_page.is_slider_visible() is True, 'The slider is not visible'
        for i in range(7):
            photo_src = main_page.get_slider_photo_src()
            main_page.click_scroll_btn()
            assert photo_src != main_page.get_slider_photo_src(), \
                'Photo src is the same, photos in the slider are not changing ' ## ПЕРЕПИСАТИ

    def test_is_more_btn_visible(self):
        """ """
        main_page = Body()
        self.driver.execute_script("window.scrollTo(0, 620)")
        assert main_page.is_more_btn_visible() is True, \
            'More button is not visible or absent'
        main_page.click_more_btn()
        assert 'https://eva.ua/promotion/' in main_page.get_page_url(), \
            'The page "Promotion" is not opened or the URL is different' ## ПЕРЕПИСАТИ
