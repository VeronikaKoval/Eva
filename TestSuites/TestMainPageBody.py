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

        # def test_hovering_menu_item(self):
        #     """ Hovering main menu items"""
        #     main_page = Header()
        #     assert main_page.hover_menu_items() is True

    def test_presence_of_presence_of_all_blocks(self):
        """ Checking if the "Product block", "Linejka tovarov", "Nabory", "Brands" are present """
        main_page = Body()
        assert main_page.is_pokupajte_vigodno_visible() is True, 'The block is not visible or absent'
        assert main_page.is_linejka_tovarov_visible() is True, 'The block is not visible or absent'
        assert main_page.is_nabory_visible() is True, 'The block is not visible or absent'
        assert main_page.is_brands_block_visible() is True, 'The block is not visible or absent'

