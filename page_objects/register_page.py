import allure
from selenium.webdriver.common.by import By
from faker import Faker
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    RC_MENU_ITEM = By.CLASS_NAME, "list-group-item"
    TITLE_PD = By.CSS_SELECTOR, "#account legend"
    TITLE_PASS = By.CSS_SELECTOR, "fieldset:nth-child(2) legend"
    TITLE_NL = By.CSS_SELECTOR, "fieldset:nth-child(3) legend"
    CBOX_NL = By.ID, "input-newsletter"
    LABEL_LOGIN_LINK = By.CSS_SELECTOR, "#content p"
    LOGIN_LINK = By.CSS_SELECTOR, "#content p a"
    PASS_INPUT = By.ID, "input-password"
    SUBMIT_BTN = By.CSS_SELECTOR, "button[type='submit']"
    PASS_VALID = By.ID, "error-password"
    FIRST_NAME_INPUT = By.ID, "input-firstname"
    LAST_NAME_INPUT = By.ID, "input-lastname"
    EMAIL_INPUT = By.ID, "input-email"
    CBOX_AGREEMENT = By.CSS_SELECTOR, "input[name='agree']"
    H1_SUCCESS_REG = By.CSS_SELECTOR, "#content h1"


    @allure.step("Open registration page")
    def open_register_page(self):
        self.logger.info("Open registration page")
        self.open_page(self.PATH)
        return self

    @allure.step("Check count of items in side menu")
    def check_right_column_menu_items(self):
        self.logger.info("Check count of items in side menu")
        menu_items = self.get_elements(self.RC_MENU_ITEM)
        assert len(menu_items) == 13, \
            "Incorrect number of items in the side menu"
        return self

    @allure.step("Check display of field set headers")
    def check_fieldset_titles(self):
        self.logger.info("Check display of field set headers")
        assert self.get_element(self.TITLE_PD).text == "Your Personal Details", \
            "The header of the personal information block is incorrect"
        assert self.get_element(self.TITLE_PASS).text == "Your Password", \
            "The password block header is incorrect"
        assert self.get_element(self.TITLE_NL).text == "Newsletter", \
            "The header of the mailing block is not correct"
        return self

    @allure.step("Click on the newsletter checkbox")
    def click_newsletter_checkbox(self):
        self.logger.info("Click on the newsletter checkbox")
        self.click(self.CBOX_NL)
        return self

    @allure.step("Check activation of the newsletter checkbox")
    def check_active_newsletter_checkbox(self):
        self.logger.info("Check activation of the newsletter checkbox")
        assert self.get_element(self.CBOX_NL).is_selected(), \
            "The checkbox was not activated after clicking"
        return self

    @allure.step("Check the text of the link to the login page")
    def check_text_to_login_page(self):
        self.logger.info("Check the text of the link to the login page")
        assert (self.get_element(self.LABEL_LOGIN_LINK).text ==
                "If you already have an account with us, please login at the login page."), \
            "incorrect text"
        return self

    @allure.step("Click on the link to the login page")
    def click_link_to_login_page(self):
        self.logger.info("Click on the link to the login page")
        self.click(self.LOGIN_LINK)
        return self

    @allure.step("Input invalid password '123' in the Password field")
    def enter_invalid_password(self):
        self.logger.info("Input invalid password '123' in the Password field")
        self.input_value(self.PASS_INPUT, "123")
        return self

    @allure.step("Click on the Submit button")
    def click_submit_button(self):
        self.logger.info("Click on the Submit button")
        self.click(self.SUBMIT_BTN)
        return self

    @allure.step("Check password validation text")
    def check_password_validation(self):
        self.logger.info("Check password validation text")
        assert self.get_element(self.PASS_VALID).text == "Password must be between 4 and 20 characters!", \
            "The password validation text is not correct"
        return self

    @allure.step("Fill in the personal details fields")
    def fill_your_personal_details_inputs(self):
        fake = Faker()
        f_name = fake.first_name()
        l_name = fake.last_name()
        email = fake.email()
        self.logger.info("Fill in the personal details fields")
        self.input_value(self.FIRST_NAME_INPUT, f_name)
        self.input_value(self.LAST_NAME_INPUT, l_name)
        self.input_value(self.EMAIL_INPUT, email)
        return self

    @allure.step("Input a valid password '123Smith' in the Password field")
    def enter_valid_password(self):
        self.logger.info("Input a valid password '123Smith' in the Password field")
        self.input_value(self.PASS_INPUT, "123Smith")
        return self

    @allure.step("Click on the agreement checkbox")
    def click_agreement_checkbox(self):
        self.logger.info("Click on the agreement checkbox")
        self.click(self.CBOX_AGREEMENT)
        return self

    @allure.step("Wait for successful registration")
    def wait_success_registration(self):
        self.logger.info("Wait for successful registration")
        self.wait_url("/en-gb?route=account/success&customer_token")
        self.check_title_text("Your Account Has Been Created!")
        assert self.get_element(self.H1_SUCCESS_REG).text == "Your Account Has Been Created!"
