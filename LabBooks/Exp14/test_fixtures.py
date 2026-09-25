"""
Experiment 14: PyTest Fixtures and configtest.py
Module: Unit Test Frameworks - PyTest
Student: Nilanjana Pal
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginWithFixtures:
    """Tests using driver fixture from conftest.py"""

    def test_page_title(self, driver):
        """Each test gets its own fresh browser instance"""
        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Swag Labs"
        print(f"\n  [test] Page Title: {driver.title}")

    def test_login_form_elements(self, sauce_demo_driver):
        """Using pre-navigated SauceDemo fixture"""
        assert sauce_demo_driver.find_element(By.ID, "user-name").is_displayed()
        assert sauce_demo_driver.find_element(By.ID, "password").is_displayed()
        assert sauce_demo_driver.find_element(By.ID, "login-button").is_displayed()
        print("\n  [test] All login form elements displayed")

    def test_valid_login(self, sauce_demo_driver):
        """Test valid login scenario"""
        sauce_demo_driver.find_element(By.ID, "user-name").send_keys("standard_user")
        sauce_demo_driver.find_element(By.ID, "password").send_keys("secret_sauce")
        sauce_demo_driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(sauce_demo_driver, 10)
        wait.until(EC.url_contains("/inventory.html"))
        
        assert "/inventory.html" in sauce_demo_driver.current_url
        print(f"\n  [test] URL after login: {sauce_demo_driver.current_url}")

    def test_invalid_login(self, sauce_demo_driver):
        """Test invalid login scenario"""
        sauce_demo_driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        sauce_demo_driver.find_element(By.ID, "password").send_keys("wrong_pass")
        sauce_demo_driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(sauce_demo_driver, 10)
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container")))
        
        assert error.is_displayed()
        print(f"\n  [test] Error message displayed: {error.text}")


class TestInventoryWithFixtures:
    """Tests using logged_in_driver fixture"""

    def test_inventory_page_title(self, logged_in_driver):
        """Verify inventory page load after auto-login fixture"""
        assert "/inventory.html" in logged_in_driver.current_url
        print(f"\n  [test] On inventory page: {logged_in_driver.current_url}")

    def test_inventory_items_count(self, logged_in_driver):
        """Count items on inventory page"""
        items = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) == 6
        print(f"\n  [test] Found {len(items)} items on page")

    def test_add_to_cart(self, logged_in_driver):
        """Test adding item to cart"""
        add_btn = logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_btn.click()

        wait = WebDriverWait(logged_in_driver, 5)
        badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        
        assert badge.text == "1"
        print(f"\n  [test] Cart badge updated to: {badge.text}")


class TestDataDrivenWithFixtures:
    """Data-driven tests using PyTest Parametrize"""

    @pytest.mark.parametrize("user_key, expected_success", [
        ("valid_user", True),
        ("locked_user", False),
        ("problem_user", True),
    ])
    def test_data_driven_login(self, driver, test_data, user_key, expected_success):
        """Parameterized test running separate cases for each test credential"""
        credentials = test_data[user_key]
        
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(credentials["username"])
        driver.find_element(By.ID, "password").send_keys(credentials["password"])
        driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(driver, 5)

        if expected_success:
            wait.until(EC.url_contains("/inventory.html"))
            assert "/inventory.html" in driver.current_url
            print(f"\n  [{user_key}] Login successful as expected")
        else:
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container")))
            assert error.is_displayed()
            print(f"\n  [{user_key}] Correctly rejected with error: {error.text}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])