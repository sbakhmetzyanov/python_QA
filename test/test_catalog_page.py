import allure
from page_objects.catalog_desktops_page import CatalogDesktopsPage


@allure.feature("Catalog page")
@allure.title("Checking the header in the desktop catalog")
def test_catalog_page_desktops_header(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_header()


@allure.feature("Catalog page")
@allure.title("Checking the header in the desktop catalog")
def test_catalog_page_desktops_title(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_title()


@allure.feature("Catalog page")
@allure.title("Checking the number of menu items in the desktop catalog")
def test_catalog_page_desktops_menu_elements(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_count_of_menu_items()


@allure.feature("Catalog page")
@allure.title("Checking the number of Mac products in the desktop catalog")
def test_catalog_page_desktops_mac_quantity(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .click_menu_item(2) \
        .check_count_of_product_items()


@allure.feature("Catalog page")
@allure.title("Checking for switching the view to a list in the desktop catalog")
def test_catalog_page_desktops_select_list_view(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .activate_list_view() \
        .check_list_view()
