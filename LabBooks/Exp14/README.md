# Experiment 14: PyTest Fixtures and conftest.py

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **PyTest Fixtures and conftest.py** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- Function/class/session fixtures
- Application-specific fixtures
- Automatic login
- Parameterized data-driven testing

## Requirements

- Python 3.10+
- pytest
- Selenium 4.x
- Google Chrome
- ChromeDriver/WebDriver support
- configtest.py fixture file

### Install Packages

```bash
pip install selenium pytest
```

## How It Works

PyTest fixtures provide browser setup/teardown, SauceDemo navigation, automatic login and reusable test data. Parameterization executes separate login cases.

## How to Run

**Python file:** `test_fixtures.py`

```bash
pytest test_fixtures.py -v -s
```

### Important: Run `test_fixtures.py`

For Experiment 14, run the **`test_fixtures.py`** file using PyTest:

```bash
pytest test_fixtures.py -v -s
```

- `-v` displays detailed test names and results.
- `-s` displays the `print()` output from fixtures and tests.

The fixture definitions from `configtest.py` should be available in the expected PyTest fixture setup.

## Source Code

The following code is taken from the supplied experiment source.

```python


# TEST FILE: test_fixtures.py

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
```

## Recorded Output

```text
collected 10 items                                                                                                                           

test_fixtures.py::TestLoginWithFixtures::test_page_title 
  [fixture] Initializing Chrome browser...

  [test] Page Title: Swag Labs
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestLoginWithFixtures::test_login_form_elements 
  [fixture] Initializing Chrome browser...

  [test] All login form elements displayed
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestLoginWithFixtures::test_valid_login 
  [fixture] Initializing Chrome browser...

  [test] URL after login: https://www.saucedemo.com/inventory.html
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestLoginWithFixtures::test_invalid_login 
  [fixture] Initializing Chrome browser...

  [test] Error message displayed: Epic sadface: Username and password do not match any user in this service
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestInventoryWithFixtures::test_inventory_page_title 
  [fixture] Initializing Chrome browser...

  [test] On inventory page: https://www.saucedemo.com/inventory.html
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestInventoryWithFixtures::test_inventory_items_count 
  [fixture] Initializing Chrome browser...

  [test] Found 6 items on page
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestInventoryWithFixtures::test_add_to_cart 
  [fixture] Initializing Chrome browser...

  [test] Cart badge updated to: 1
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestDataDrivenWithFixtures::test_data_driven_login[valid_user-True] 
  [fixture] Initializing Chrome browser...

  [valid_user] Login successful as expected
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestDataDrivenWithFixtures::test_data_driven_login[locked_user-False] 
  [fixture] Initializing Chrome browser...

  [locked_user] Correctly rejected with error: Epic sadface: Sorry, this user has been locked out.
PASSED  [fixture] Teardown: Closing browser instance...

test_fixtures.py::TestDataDrivenWithFixtures::test_data_driven_login[problem_user-True] 
  [fixture] Initializing Chrome browser...

  [problem_user] Login successful as expected
PASSED  [fixture] Teardown: Closing browser instance...
```

## What Is Happening

The browser is initialized, the specified Selenium actions are performed, and the test framework checks the expected conditions. The recorded output shows the result of the supplied run.

### Fixture Flow

1. `driver` creates a fresh Chrome instance for each test.
2. `sauce_demo_driver` opens SauceDemo.
3. `logged_in_driver` performs the login and waits for the inventory page.
4. `test_data` supplies reusable credentials.
5. `pytest.mark.parametrize` runs multiple login scenarios.

## Expected Result

The experiment should complete with the tests passing as shown in the recorded output. Execution time and browser-specific details may vary by environment.

## Notes

- Google Chrome must be installed.
- Selenium must be able to start ChromeDriver.
- Internet access is required for the web pages used by these experiments.
- Keep the required supporting files in the expected project structure.
