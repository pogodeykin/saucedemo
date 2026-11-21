from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def find_and_report(browser, by, locator):
    try:
        element = browser.find_element(by, locator)
        print(f"Найден: By={by}, локатор={locator}")
        return element
    except NoSuchElementException:
        print(f"Не найден: By={by}, локатор={locator}")
        return None


def test_saucedemo_locators(browser):
    browser.get("https://www.saucedemo.com/")

    find_and_report(browser, By.ID, "user-name")
    find_and_report(browser, By.NAME, "user-name")
    find_and_report(browser, By.CLASS_NAME, "form_input")
    find_and_report(browser, By.TAG_NAME, "input")

    find_and_report(browser, By.XPATH, "//input[@id='user-name']")
    find_and_report(browser, By.XPATH, "//div[text()='Swag Labs']")
    find_and_report(
        browser,
        By.XPATH,
        "//input[contains(@placeholder, 'Username')]"
    )
    find_and_report(
        browser,
        By.XPATH,
        "//div[contains(text(), 'Swag Labs')]"
    )


    find_and_report(
        browser,
        By.XPATH,
        "//input[@id='user-name']/ancestor::div[1]"
    )
    find_and_report(
        browser,
        By.XPATH,
        "//div[@class='login_container']/descendant::input"
    )
    find_and_report(
        browser,
        By.XPATH,
        "//input[@id='user-name']/following::input[@id='password']"
    )
    find_and_report(
        browser,
        By.XPATH,
        "//input[@id='user-name']/parent::*"
    )
    find_and_report(
        browser,
        By.XPATH,
        "//input[@id='password']/preceding::input[@id='user-name']"
    )

    find_and_report(
        browser,
        By.XPATH,
        "//input[@name='user-name' and @type='text']"
    )

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    WebDriverWait(browser, 10).until(
        EC.url_contains("inventory.html")
    )

    find_and_report(browser, By.LINK_TEXT, "Twitter")
    find_and_report(browser, By.PARTIAL_LINK_TEXT, "Twitt")

    find_and_report(browser, By.CSS_SELECTOR, ".inventory_list")
    find_and_report(browser, By.CSS_SELECTOR, ".btn.btn_primary")
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        ".inventory_item .inventory_item_name"
    )
    find_and_report(browser, By.CSS_SELECTOR, "#shopping_cart_container")
    find_and_report(browser, By.CSS_SELECTOR, "div")
    find_and_report(browser, By.CSS_SELECTOR, "div.inventory_item")
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[data-test='inventory-item']"
    )
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[class~='inventory_item']"
    )
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[data-test|='inventory']"
    )
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[data-test^='inventory']"
    )
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[data-test$='item']"
    )
    find_and_report(
        browser,
        By.CSS_SELECTOR,
        "[data-test*='inventory']"
    )