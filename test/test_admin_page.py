
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page_header(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".card-header i")), message="Missing img title")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "card-header"), "Please enter your login details."),
        message="Title incorrect")


def test_admin_page_username_input(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "label[for='input-username']"), "Username"),
        message="Incorrect inputname Username")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".mb-3:nth-child(1) .input-group-text i")), message="Missing img Username")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.ID, "input-username")), message="Missing input Username")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element_attribute(
        (By.ID, "input-username"), "placeholder", "Username"),
        message="Incorrect placeholder Username")


def test_admin_page_password_input(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "label[for='input-password']"), "Password"),
        message="Incorrect inputname Password")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".mb-3:nth-child(2) .input-group-text i")), message="Missing img Password")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.ID, "input-password")), message="Missing input Password")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element_attribute(
        (By.ID, "input-password"), "placeholder", "Password"),
        message="Incorrect placeholder Password")


def test_admin_page_login_button(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")), message="Missing button Login")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "button[type='submit']"), "Login"),
        message="Button name Login incorrect")


def test_admin_page_alert(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "alert-dismissible"), "No match for Username and/or Password."),
        message="Incorrect alert text")
