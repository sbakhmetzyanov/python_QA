import allure
from page_objects.admin_page import AdminPage
from page_objects.alert_danger_element import AlertDangerElement


@allure.feature("Admin page")
@allure.title("Checking the header in the authorization card of the admin panel")
def test_admin_page_header(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_header()


@allure.feature("Admin page")
@allure.title("Checking the username field in the authorization card of the admin panel")
def test_admin_page_username_input(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_input_label(0) \
        .check_input_icon(0) \
        .check_input_placeholder(0)


@allure.feature("Admin page")
@allure.title("Checking the user's password field in the authorization card of the admin panel")
def test_admin_page_password_input(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_input_label(1) \
        .check_input_icon(1) \
        .check_input_placeholder(1)


@allure.feature("Admin page")
@allure.title("Checking the login button in the authorization card of the admin panel")
def test_admin_page_login_button(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_login_button()


@allure.feature("Admin page")
@allure.title("Checking the alert for blank fields in the authorization card of the admin panel")
def test_admin_page_alert(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .submit_login_button()
    AlertDangerElement(browser).check_alert_danger_text()
