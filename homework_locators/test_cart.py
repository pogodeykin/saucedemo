from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart_and_check_details(browser):
    wait = WebDriverWait(browser, 10)


    browser.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))


    product = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='inventory-item']")
        )
    )

    expected_name = product.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-name']"
    ).text.strip()

    expected_price = product.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-price']"
    ).text.strip()


    product.find_element(By.TAG_NAME, "button").click()


    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))


    cart_item = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='inventory-item']")
        )
    )

    actual_name = cart_item.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-name']"
    ).text.strip()

    actual_price = cart_item.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-price']"
    ).text.strip()

    assert actual_name == expected_name, (
        f"Название не совпадает: ожидалось {expected_name!r}, "
        f"получено {actual_name!r}"
    )
    assert actual_price == expected_price, (
        f"Стоимость не совпадает: ожидалось {expected_price!r}, "
        f"получено {actual_price!r}"
    )