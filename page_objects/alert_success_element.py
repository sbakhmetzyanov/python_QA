import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    ALERT_SUCCESS = By.CSS_SELECTOR, ".alert-success"
    CLOSE_BTN = By.CSS_SELECTOR, "#alert .btn-close"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.ALERT_SUCCESS))
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Check text in success alert when adding product to cart")
    def check_alert_success_text(self):
        self.logger.info("Check text in success alert when adding product to cart")
        assert "Success: You have added" in self.alert.text, \
            "The alert text is incorrect"
        return self

    @allure.step("Click on the close alert button")
    def close_alert(self):
        self.logger.info("Click on the close alert button")
        self.browser.find_element(*self.CLOSE_BTN).click()
        return self

    @allure.step("Check text in success alert when product changes")
    def check_alert_success_modified_product(self):
        self.logger.info("Check text in success alert when product changes")
        assert "Success: You have modified products!" in self.alert.text, \
            "The alert text is incorrect"
        return self
