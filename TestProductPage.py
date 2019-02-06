from BaseTest import BaseTest
from ProductPage import List


class TestProductPage(BaseTest):

    def setup(self):
        super(TestProductPage, self).setup()
        self.driver.get(self.base_url+'024-273-293/sredstva-problemnoj-kozhi/')

    def test_country_filters(self):
        """ Applying filters: county, """
        products_list = List()
        assert products_list.apply_filter_country() is True

    def test_cancellation_of_filter(self):
        """ Cancellation of the filter country"""
        products_list = List()
        assert products_list.cancel_filter_country() is True

    def test_name_filter(self):
        """ Apllying filter by name "Nivea" and verifying that checkbox status is checked """
        product_list = List()
        assert product_list.apply_filter_name() is True

    def test_sort_price_desc(self):
        """ Applying sorting be price from expensive to cheap and verifying that page URL is changed"""
        product_list = List()
        assert '/?product_list_order=price' in product_list.apply_sort_price_decs()

    def test_sort_asc(self):
        """ Applying sorting be price from cheap to expensive and verifying that page URL is changed"""
        product_list = List()
        assert 'price&product_list_dir=asc' in product_list.apply_sort_price_asc()

    def test_manual_price_filter(self):
        """ Applying manual filter for sorting products by price and verifying that price box contains chosen price"""
        product_list = List()
        assert '102' in product_list.apply_manual_price_filter()
