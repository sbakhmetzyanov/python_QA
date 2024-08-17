import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogDesktopsPage(BasePage):
    PATH = "/en-gb/catalog/desktops"
    TITLE = By.CSS_SELECTOR, "head title"
    HEADER = By.CSS_SELECTOR, "#content h2"
    MENU_ITEM = By.CLASS_NAME, "list-group-item"
    PRODUCT_ITEM = By.CLASS_NAME, "product-thumb"
    BUTTON_LIST = By.ID, "button-list"
    LIST_VIEW = By.CLASS_NAME, "product-list"
    PRODUCT_PRICE_NEW = By.CLASS_NAME, "price-new"
    PRODUCT_PRICE_TAX = By.CLASS_NAME, "price-tax"

    @allure.step("Open the Desktops catalog page")
    def open_catalog_desktops_page(self):
        self.logger.info("Open the Desktops catalog page")
        self.open_page(self.PATH)
        return self

    @allure.step("Check display of the Desktops title")
    def check_desktops_title(self):
        self.logger.info("Check display of the Desktops title")
        self.check_title_text("Desktops")
        return self

    @allure.step("Check display of the Desktops header")
    def check_desktops_header(self):
        self.logger.info("Check display of the Desktops header")
        assert self.get_element(self.HEADER).text == "Desktops", \
            "The title of the Desktops section is incorrect"
        return self

    @allure.step("Check the count of items in the menu")
    def check_count_of_menu_items(self):
        self.logger.info("Check the count of items in the menu")
        menu_list = self.get_elements(self.MENU_ITEM)
        assert len(menu_list) == 10, \
            "The number of items in the menu is not correct"
        return self

    @allure.step("Click on a menu item")
    def click_menu_item(self, index):
        self.logger.info("Click on a menu item")
        self.get_elements(self.MENU_ITEM)[index].click()
        return self

    @allure.step("Check the count of products in the section")
    def check_count_of_product_items(self):
        self.logger.info("Check the count of products in the section")
        product_list = self.get_elements(self.PRODUCT_ITEM)
        assert len(product_list) == 1, \
            "Incorrect number of products in the section"
        return self

    @allure.step("Activate product list view")
    def activate_list_view(self):
        self.logger.info("Activate product list view")
        self.click(self.BUTTON_LIST)
        return self

    @allure.step("Check product list display")
    def check_list_view(self):
        self.logger.info("Check product list display")
        assert self.get_element(self.LIST_VIEW), \
            "The list view does not work"
        return self

    @allure.step("Check display of price and tax in Euro")
    def check_prices_in_euro(self):
        self.logger.info("Check display of price and tax in Euro")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "€" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "The price in euros is displayed incorrectly"
            assert "€" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "The price tax in euros is displayed incorrectly"
        return self

    @allure.step("Check display of price and tax in Pound")
    def check_prices_in_pound(self):
        self.logger.info("Check display of price and tax in Pound")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "£" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "The price in pounds is displayed incorrectly"
            assert "£" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "The price tax in pounds is displayed incorrectly"
        return self

    @allure.step("Check display of price and tax in Dollar")
    def check_prices_in_dollar(self):
        self.logger.info("Check display of price and tax in Dollar")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "$" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "The price in dollars is displayed incorrectly"
            assert "$" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "The price tax in dollars is displayed incorrectly"
        return self
