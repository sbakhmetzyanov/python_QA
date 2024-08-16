import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/administration"
    CARD = By.CLASS_NAME, "card"
    HEADER = By.CLASS_NAME, "card-header"
    HEADER_ICON = By.CSS_SELECTOR, ".card-header i"
    INPUT = By.CSS_SELECTOR, ".mb-3 input"
    INPUT_LABEL = By.CSS_SELECTOR, ".mb-3 label"
    INPUT_ICON = By.CSS_SELECTOR, ".mb-3 i"
    LOGIN_BTN = By.CSS_SELECTOR, "button[type='submit']"
    LOGIN_INPUT = By.ID, "input-username"
    PASS_INPUT = By.ID, "input-password"
    LOGOUT_BTN = By.ID, "nav-logout"


    @allure.step("Open admin page")
    def open_admin_page(self):
        self.logger.info("Open admin page")
        self.open_page(self.PATH)
        return self

    @allure.step("Wait for the login card element in the admin page")
    def wait_card(self):
        self.logger.info("Wait for the login card element in the admin page")
        self.get_element(self.CARD)
        return self

    @allure.step("Check header display")
    def check_header(self):
        self.logger.info("Check header display")
        self.get_element(self.HEADER_ICON)
        assert self.get_element(self.HEADER).text == "Please enter your login details.", \
            "The title text is incorrect"

    @allure.step("Check label of Username input")
    def check_input_label(self, index=0):
        if index == 0:
            self.logger.info("Check label of Username input")
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Username", \
                "Invalid field signature Username"
        else:
            self.logger.info("Check label of Password input")
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Password", \
                "Invalid field signature Password"
        return self

    @allure.step("Check icon of Username input")
    def check_input_icon(self, index=0):
        if index == 0:
            self.logger.info("Check icon of Username input")
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Miss icon of input Username"
        else:
            self.logger.info("Check icon of Password input")
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Miss icon of input Password"
        return self

    @allure.step("Check placeholder of Username input")
    def check_input_placeholder(self, index=0):
        if index == 0:
            self.logger.info("Check placeholder of Username input")
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Username", \
                "incorrect placeholder input Username"
        else:
            self.logger.info("Check placeholder of Password input")
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Password", \
                "incorrect placeholder input Password"

    @allure.step("Check the display of the Login button")
    def check_login_button(self):
        self.logger.info("Check the display of the Login button")
        assert self.get_element(self.LOGIN_BTN).text == "Login", \
            "Name Login's button  incorrect"
        return self

    @allure.step("Click on the Login button")
    def submit_login_button(self):
        self.logger.info("Click on the Login button")
        self.click(self.LOGIN_BTN)
        return self

    @allure.step("Login to the admin panel")
    def login(self):
        self.logger.info("Login to the admin panel")
        self.input_value(self.LOGIN_INPUT, "user")
        self.input_value(self.PASS_INPUT, "bitnami")
        self.click(self.LOGIN_BTN)
        return self


    @allure.step("Check login success")
    def wait_logged_in(self):
        self.logger.info("Check login success")
        self.wait_url("/administration/index.php?route=common/dashboard&user_token")
        self.check_title_text("Dashboard")
        return self


    @allure.step("Logout in admin panel")
    def logout(self):
        self.logger.info("Logout from the admin panel")
        self.click(self.LOGOUT_BTN)
        return self

    @allure.step("Check success logout")
    def wait_logged_out(self):
        self.logger.info("Check logout success")
        self.wait_url("/administration/index.php?route=common/login")
        self.check_title_text("Administration")
        return self
