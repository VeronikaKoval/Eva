import time

from TestSuites.BaseTest import BaseTest
from Pages.ProductPage import List


class TestProductPage(BaseTest):

    def setup(self):
        super(TestProductPage, self).setup()
        self.driver.get(self.base_url+'024-273-293/sredstva-problemnoj-kozhi/')

    def test_country_filter(self):
        """ Opening "Средства для проблемной кожи" page,checking checkbox "Франция" in "Страна производства" filter,
         getting checkbox attribute to verify that checkbox is checked """
        products_list = List()
        products_list.apply_filter_country()
        assert products_list.get_country_filter_attr() is True, 'The checkbox "Франция" is unchecked'

    def test_cancellation_of_filter(self):
        """ Checking checkbox "Франция" in "Страна производства" filter, unchecking it,
        verifying that page current URL doesn't have filter's url"""
        products_list = List()
        products_list.apply_filter_country()
        time.sleep(2)
        products_list.apply_filter_country()
        assert 'filter/strana_proizvodstva-73217/' not in products_list.get_page_url(), 'URL is different'

    def test_name_filter(self):
        """ Opening "Средства для проблемной кожи" page, scrolling down name filter, clicking on "Nivea" checkbox,
        checking the checkbox status to verify that checkbox is checked """
        product_list = List()
        product_list.apply_filter_name()
        assert product_list.get_name_filter_attr() is True, 'The checkbox "Nivea" is unchecked'

    def test_sort_price_desc(self):
        """ Opening the sorting drop down, clicking sorting from expensive to cheap,
        check page current URL to verifying that page URL is changed """
        product_list = List()
        product_list.apply_sort_price_decs()
        assert '/?product_list_order=price' in product_list.get_page_url(), 'URL is different'

    def test_sort_asc(self):
        """ Opening the sorting drop down, clicking sorting from cheap to expensive,
        check page current URL to verifying that page URL is changed """
        product_list = List()
        product_list.apply_sort_price_asc()
        assert 'price&product_list_dir=asc' in product_list.get_page_url(), 'URL is different'

    def test_manual_price_filter(self):
        """ Scrolling page to manual price filter, applying manual filter for sorting products by price,
        get price value from the price box to verify that price box contains chosen price """
        product_list = List()
        product_list. apply_manual_price_filter()
        assert '102' in product_list.get_text_from_price_box(), 'The price is different'
