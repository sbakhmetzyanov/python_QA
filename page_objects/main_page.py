import random
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from page_objects.base_page import BasePage


class MainPage(BasePage):
    CART_DD = By.ID, "header-cart"
    CART_DD_TEXT = By.CSS_SELECTOR, "#header-cart li"
    CAROUSEL = By.CLASS_NAME, "carousel.slide"
    CAROUSEL_ITEM = By.CLASS_NAME, "carousel-item"
    PRODUCT_ITEM = By.CLASS_NAME, "product-thumb"
    PRODUCT_BTN = By.CSS_SELECTOR, "button[type='submit']"
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, ".product-thumb h4 a"
    ADD_TO_CART_BTN = By.CSS_SELECTOR, "button[type='submit']:nth-of-type(1)"
    PRODUCT_PRICE_NEW = By.CLASS_NAME, "price-new"
    PRODUCT_PRICE_TAX = By.CLASS_NAME, "price-tax"

    @allure.step("Click on Cart dropdown")
    def click_cart_dropdown(self):
        self.logger.info("Click on Cart dropdown")
        self.click(self.CART_DD)
        return self

    @allure.step("Check the text in the dropdown of an empty cart")
    def check_empty_cart_dropdown_text(self):
        self.logger.info("Check the text in the dropdown of an empty cart")
        assert self.get_element(self.CART_DD_TEXT).text == "Your shopping cart is empty!", \
            "Incorrect text with an empty shopping cart"
        return self

    @allure.step("Check the number of banners in the carousel")
    def check_carousel_items(self, index):
        self.logger.info("Check the number of banners in the carousel")
        carousel_list = self.get_invisible_elements(self.CAROUSEL)
        if index == 0:
            carousel_items = carousel_list[0].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 2, "The number of elements in carousel_0 is not equal to 2"
        elif index == 1:
            carousel_items = carousel_list[1].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 3, "The number of elements in carousel_1 is not equal to 3"
        return self

    @allure.step("Check the number of buttons on product cards")
    def check_product_buttons(self):
        self.logger.info("Check the number of buttons on product cards")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            product_buttons = product_items[i].find_elements(*self.PRODUCT_BTN)
            assert len(product_buttons) == 3, f"КThe number of buttons on the {i} product card is not equal to 3"

    @allure.step("Click on the recommended product card")
    def click_featured_product(self, index=0):
        self.logger.info("Click on the recommended product card")
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()
        return self

    @allure.step("Add a random product to cart")
    def add_to_cart_random_product(self):
        self.logger.info("Add a random product to cart")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        i = random.randint(1, len(product_items))
        target_btn = self.get_element((By.CSS_SELECTOR,
                                       f"div.col.mb-3:nth-child({i}) button[type='submit']:nth-child(1)"))
        AC(self.browser).move_to_element(target_btn).click(target_btn).perform()
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
