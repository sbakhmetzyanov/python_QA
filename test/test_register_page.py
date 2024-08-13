import allure
from page_objects.register_page import RegisterPage


@allure.feature("Registration page")
@allure.title("Checking the number of items in the side menu of the registration page")
def test_register_page_menu_items(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_right_column_menu_items()


@allure.feature("Registration page")
@allure.title("Checking the headers in the field sets of the registration page")
def test_register_page_fieldset_titles(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_fieldset_titles()


@allure.feature("Registration page")
@allure.title("Checking the activation of the subscription checkbox on the registration page")
def test_register_page_subscribe_checkbox(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .click_newsletter_checkbox() \
        .check_active_newsletter_checkbox()


@allure.feature("Registration page")
@allure.title("Checking the link to the login page on the registration page")
def test_register_page_go_to_login_page(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_text_to_login_page() \
        .click_link_to_login_page() \
        .wait_url("/en-gb?route=account/login")


@allure.feature("Registration page")
@allure.title("Validation check in the password field on the registration page")
def test_register_page_fill_invalid_password(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .enter_invalid_password() \
        .click_submit_button() \
        .check_password_validation()
