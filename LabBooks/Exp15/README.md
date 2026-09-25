# Experiment 15: PyTest Integration with HTML Reporting

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **PyTest Integration with HTML Reporting** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- PyTest fixtures
- Login, inventory, cart and navigation tests
- `pytest-html`
- HTML report generation

## Requirements

- Python 3.10+
- pytest
- pytest-html
- Selenium 4.x
- Google Chrome
- ChromeDriver/WebDriver support

### Install Packages

```bash
pip install selenium pytest pytest-html
```

## How It Works

The tests use fixtures for browser setup and exercise login, inventory, cart and navigation behavior. PyTest HTML reporting creates a browser-viewable report after execution.

## How to Run

**Python file:** `pytesthtml.py`

```bash
pytest pytesthtml.py -v --html=reports/report.html --self-contained-html
```

### HTML Report Generation

After running the Python/PyTest command, the report is generated as:

```text
reports/report.html
```

Open this HTML file in a web browser to view the test results. The command uses `--self-contained-html` to create a self-contained report.

## Source Code

The following code is taken from the supplied experiment source.

```python
Experiment 15: PyTest Integration with HTML Reporting (Assignment 9)
Module: Unit Test Frameworks - PyTest
Student: Nilanjana Pal

Assignment 9: PyTest Integration with HTML Reporting
Covers:
- PyTest fixtures for driver initialization/teardown
- Generate HTML reports using pytest-html
- Run test suite and capture results

How to run:
    pytest pytesthtml.py -v --html=reports/report.html --self-contained-html
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime


# ============================================
# FIXTURES
# ============================================

@pytest.fixture(scope="function")
def driver():
    """Fixture: browser setup and teardown"""
    print("\n  [fixture] Opening browser...")
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    yield _driver
    print("  [fixture] Closing browser...")
    _driver.quit()


@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Fixture: Take screenshot on test failure"""
    yield driver
    if request.node.rep_call and request.node.rep_call.failed:
        print(f"\n  [fixture] Test FAILED - taking screenshot...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        filepath = os.path.join(screenshot_dir, f"FAIL_{test_name}_{timestamp}.png")
        driver.save_screenshot(filepath)
        print(f"  [fixture] Screenshot saved: {filepath}")


# ============================================
# TEST CLASS 1: Login Tests
# ============================================

class TestLoginWithHTMLReport:
    """Login test suite for HTML report"""

    def test_valid_login(self, driver):
        """Test successful login"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert "/inventory.html" in driver.current_url
        print(f"  [PASS] Login successful, URL: {driver.current_url}")

    def test_invalid_password(self, driver):
        """Test invalid password shows error"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        error = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        assert error.is_displayed()
        assert "Username and password do not match" in error.text
        print(f"  [PASS] Error displayed: {error.text[:50]}")

    def test_empty_credentials(self, driver):
        """Test empty credentials show error"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        error = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        assert error.is_displayed()
        print(f"  [PASS] Empty credentials error shown")

    def test_locked_out_user(self, driver):
        """Test locked out user shows error"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        error = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        assert error.is_displayed()
        print(f"  [PASS] Locked out error shown: {error.text[:50]}")


# ============================================
# TEST CLASS 2: Inventory Tests
# ============================================

class TestInventoryWithHTMLReport:
    """Inventory test suite for HTML report"""

    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        """Auto-login before each test in this class"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def test_inventory_page_loaded(self, driver):
        """Verify inventory page loaded"""
        assert "/inventory.html" in driver.current_url
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) > 0
        print(f"  [PASS] Inventory loaded with {len(items)} items")

    def test_add_item_to_cart(self, driver):
        """Test adding item to cart"""
        add_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_btn.click()
        time.sleep(1)
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"
        print(f"  [PASS] Item added, badge count: {badge.text}")

    def test_remove_item_from_cart(self, driver):
        """Test removing item from cart"""
        add_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_btn.click()
        time.sleep(1)
        remove_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_btn.click()
        time.sleep(1)
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0
        print(f"  [PASS] Item removed from cart")


# ============================================
# TEST CLASS 3: Navigation Tests
# ============================================

class TestNavigationWithHTMLReport:
    """Navigation test suite for HTML report"""

    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        """Auto-login before each test"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def test_navigate_to_cart(self, driver):
        """Test navigation to cart page"""
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart.click()
        time.sleep(1)
        assert "/cart.html" in driver.current_url
        print(f"  [PASS] Cart page loaded: {driver.current_url}")

    def test_navigate_to_cart_and_back(self, driver):
        """Test navigation back to inventory"""
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart.click()
        time.sleep(1)
        back = driver.find_element(By.ID, "continue-shopping")
        back.click()
        time.sleep(1)
        assert "/inventory.html" in driver.current_url
        print(f"  [PASS] Back to inventory: {driver.current_url}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/report.html", "--self-contained-html"])
```

## Recorded Output

```text
collected 9 items                                                                                                                            

pytesthtml.py::TestLoginWithHTMLReport::test_valid_login PASSED                                                                        [ 11%]
pytesthtml.py::TestLoginWithHTMLReport::test_invalid_password PASSED                                                                   [ 22%]
pytesthtml.py::TestLoginWithHTMLReport::test_empty_credentials PASSED                                                                  [ 33%]
pytesthtml.py::TestLoginWithHTMLReport::test_locked_out_user PASSED                                                                    [ 44%]
pytesthtml.py::TestInventoryWithHTMLReport::test_inventory_page_loaded PASSED                                                          [ 55%]
pytesthtml.py::TestInventoryWithHTMLReport::test_add_item_to_cart PASSED                                                               [ 66%]
pytesthtml.py::TestInventoryWithHTMLReport::test_remove_item_from_cart PASSED                                                          [ 77%]
pytesthtml.py::TestNavigationWithHTMLReport::test_navigate_to_cart PASSED                                                              [ 88%]
pytesthtml.py::TestNavigationWithHTMLReport::test_navigate_to_cart_and_back PASSED                                                     [100%]
```

## What Is Happening

The browser is initialized, the specified Selenium actions are performed, and the test framework checks the expected conditions. The recorded output shows the result of the supplied run.

### Reporting Flow

1. PyTest starts each browser through the fixture.
2. Login, inventory, cart and navigation tests execute.
3. PyTest collects the results.
4. `pytest-html` creates `reports/report.html`.
5. The HTML file can be opened in a browser for detailed results.

## Expected Result

The experiment should complete with the tests passing as shown in the recorded output. Execution time and browser-specific details may vary by environment.

## Notes

- Google Chrome must be installed.
- Selenium must be able to start ChromeDriver.
- Internet access is required for the web pages used by these experiments.
- Keep the required supporting files in the expected project structure.
