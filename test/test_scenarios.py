import random


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_login_and_logout_to_admin_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(browser, 2).until(EC.url_contains("/administration/index.php?route=common/dashboard&user_token"),
                                    message="Didn't login to admin page")
    WebDriverWait(browser, 1).until(EC.title_is("Dashboard"),
                                    message="Didn't login to admin page")
    browser.find_element(By.ID, "nav-logout").click()
    WebDriverWait(browser, 2).until(EC.url_contains("/administration/index.php?route=common/login"),
                                    message="Didn't logout to admin page")
    WebDriverWait(browser, 1).until(EC.title_is("Administration"),
                                    message="Didn't login to admin page")


def test_add_to_cart_random_product(browser):
    cart_btn = browser.find_element(By.CSS_SELECTOR, "a[title='Shopping Cart']")
    product_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    i = random.randint(1, len(product_items))
    target_btn = browser.find_element(By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) button[type='submit']:nth-child(1)")
    AC(browser).move_to_element(target_btn).click(target_btn).perform()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#alert div"), "Success"),
        message="Quantity product in button not change"
    )
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#alert .btn-close"))).click()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#header-cart button[type='button']"), "1 item"),
        message="The quantity of products in the cart button does not change."
    )
    AC(browser).move_to_element(cart_btn).click(cart_btn).perform()
    WebDriverWait(browser, 2).until(EC.url_to_be(browser.url + "/en-gb?route=checkout/cart"),
                                    message="The redirect to the cart page was not completed.")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#shopping-cart tr")), message="Корзина пустая"
    )


def test_main_page_switch_currencies(browser):
    product_items = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "product-thumb"))
    )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(1)").click()
    for i in range(1, len(product_items)+1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "€"),
            message="Incorrect price in euros"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(2)").click()
    for i in range(1, len(product_items)+1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "£"),
            message="Incorrect price in pounds"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(3)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "$"),
            message="Incorrect price in dollars"
        )


def test_catalog_page_switch_currencies(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    product_items = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "product-thumb")))
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(1)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "€"),
            message="Incorrect price in euros"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(2)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "£"),
            message="Incorrect price in pounds"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(3)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "$"),
            message="Incorrect price in dollars"
        )
