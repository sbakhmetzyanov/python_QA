import allure
from page_objects.main_page import MainPage
from page_objects.top_menu_element import TopMenu


@allure.feature("Main page")
@allure.title("Checking currencies in the drop-down list on the main page")
def test_main_page_currency(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .check_currency_list()


@allure.feature("Main page")
@allure.title("Checking the notification in the empty shopping cart on the main page")
def test_main_page_empty_cart_text(browser):
    MainPage(browser) \
        .click_cart_dropdown() \
        .check_empty_cart_dropdown_text()


@allure.feature("Main page")
@allure.title("Checking the number of banners in the upper carousel on the main page")
def test_main_page_carousel_0(browser):
    MainPage(browser) \
        .check_carousel_items(0)


@allure.feature("Main page")
@allure.title("Checking the display of buttons in the product profile on the main page")
def test_main_page_product_buttons(browser):
    MainPage(browser) \
        .check_product_buttons()


@allure.feature("Main page")
@allure.title("Checking the number of banners in the lower carousel on the main page")
def test_main_page_carousel_1(browser):
    MainPage(browser) \
        .check_carousel_items(1)
