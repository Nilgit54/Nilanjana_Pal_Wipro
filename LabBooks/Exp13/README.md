# Experiment 13: PyTest Introduction and Installation

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **PyTest Introduction and Installation** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- PyTest installation and structure
- Naming conventions
- Test functions/classes
- Plain `assert` statements

## Requirements

- Python 3.10+
- pytest
- Selenium 4.x
- Google Chrome
- ChromeDriver/WebDriver support

### Install Packages

```bash
pip install selenium pytest
```

## How It Works

The script demonstrates PyTest naming conventions, test functions, test classes and Python `assert` statements. Google, SauceDemo and Bing checks are collected and executed by PyTest.

## How to Run

**Python file:** `pytestintro.py`

```bash
python pytestintro.py
```

## Source Code

The following code is taken from the supplied experiment source.

```python
Experiment 13: PyTest Introduction and Installation
Module: Unit Test Frameworks - PyTest
Student: Nilanjana Pal

Covers:
- Introduction to PyTest
- Installing PyTest
- Naming Conventions
- Test Files, Test Methods, Assertions
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ============================================
# PYTEST NAMING CONVENTIONS:
# - Test files: test_*.py
# - Test functions: test_*()
# - Test classes: Test*
# - Test methods: test_*()
# - Assertions: assert statement (no self.assert*)
# ============================================


def test_page_title_google():
    """Test Google page title - no class needed"""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
        assert driver.current_url.startswith("https://")
    finally:
        driver.quit()


def test_page_url_google():
    """Test Google page URL"""
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com")
        assert "google" in driver.current_url.lower()
    finally:
        driver.quit()


class TestSauceDemoPytest:
    """Test class for SauceDemo using PyTest"""

    def test_saucedemo_page_title(self):
        """Test SauceDemo page title"""
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument("--remote-allow-origins=*")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        try:
            driver.get("https://www.saucedemo.com/")
            assert driver.title == "Swag Labs"
        finally:
            driver.quit()

    def test_saucedemo_login_form_exists(self):
        """Test login form elements exist"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        try:
            driver.get("https://www.saucedemo.com/")
            assert driver.find_element(By.ID, "user-name").is_displayed()
            assert driver.find_element(By.ID, "password").is_displayed()
            assert driver.find_element(By.ID, "login-button").is_displayed()
        finally:
            driver.quit()

    def test_saucedemo_login_success(self):
        """Test successful login"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        try:
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            time.sleep(2)
            assert "/inventory.html" in driver.current_url
        finally:
            driver.quit()

    def test_saucedemo_login_page_elements_count(self):
        """Test number of inputs on login page"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        try:
            driver.get("https://www.saucedemo.com/")
            inputs = driver.find_elements(By.TAG_NAME, "input")
            assert len(inputs) >= 3
        finally:
            driver.quit()


class TestBingPytest:
    """Additional test class for variety"""

    def test_bing_title(self):
        """Test Bing page title"""
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.bing.com")
            assert "Bing" in driver.title
        finally:
            driver.quit()

    def test_bing_url(self):
        """Test Bing URL"""
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.bing.com")
            assert "bing" in driver.current_url.lower()
        finally:
            driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

## Recorded Output

```text
collected 8 items                                                                                                                            

pytestintro.py::test_page_title_google PASSED                                                                                          [ 12%]
pytestintro.py::test_page_url_google PASSED                                                                                            [ 25%]
pytestintro.py::TestSauceDemoPytest::test_saucedemo_page_title PASSED                                                                  [ 37%]
pytestintro.py::TestSauceDemoPytest::test_saucedemo_login_form_exists PASSED                                                           [ 50%]
pytestintro.py::TestSauceDemoPytest::test_saucedemo_login_success PASSED                                                               [ 62%]
pytestintro.py::TestSauceDemoPytest::test_saucedemo_login_page_elements_count PASSED                                                   [ 75%]
pytestintro.py::TestBingPytest::test_bing_title PASSED                                                                                 [ 87%]
pytestintro.py::TestBingPytest::test_bing_url PASSED                                                                                   [100%]


"""
configtest.py - Shared PyTest Fixtures
Module: Unit Test Frameworks - PyTest
Student: Nilanjana Pal

Covers:
- Modular driver initialization and teardown via yield
- Tiered fixture scopes (function, class, session)
- Automatic authentication and navigation fixtures
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================
# BROWSER FIXTURES
# ============================================

@pytest.fixture(scope="function")
def driver():
    """Create and destroy a Chrome driver instance for each test function."""
    print("\n  [fixture] Initializing Chrome browser...")
    options = Options()
    # options.add_argument("--headless")  # Enable for headless CI/CD runs
    
    _driver = webdriver.Chrome(options=options)
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    
    yield _driver
    
    print("  [fixture] Teardown: Closing browser instance...")
    _driver.quit()


@pytest.fixture(scope="class")
def class_driver():
    """Create and destroy a single browser instance shared across an entire test class."""
    print("\n  [class fixture] Initializing shared Chrome browser...")
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    
    yield _driver
    
    print("  [class fixture] Teardown: Closing shared browser...")
    _driver.quit()


# ============================================
# APPLICATION-SPECIFIC FIXTURES
# ============================================

@pytest.fixture(scope="function")
def sauce_demo_driver(driver):
    """Pre-navigate driver to the SauceDemo landing page."""
    driver.get("https://www.saucedemo.com/")
    return driver


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Provide a pre-authenticated driver on the SauceDemo inventory dashboard."""
    driver.get("https://www.saucedemo.com/")
    
    # Explicit wait for login elements to be interactive
    wait = WebDriverWait(driver, 10)
    user_field = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    
    user_field.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Wait until login succeeds and inventory page is visible
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    return driver


# ============================================
# DATA FIXTURES
# ============================================

@pytest.fixture(scope="session")
def test_data():
    """Session-scoped test data dictionary."""
    return {
        "valid_user": {"username": "standard_user", "password": "secret_sauce"},
        "locked_user": {"username": "locked_out_user", "password": "secret_sauce"},
        "problem_user": {"username": "problem_user", "password": "secret_sauce"},
    }


    """
```

## What Is Happening

The browser is initialized, the specified Selenium actions are performed, and the test framework checks the expected conditions. The recorded output shows the result of the supplied run.


## Expected Result

The experiment should complete with the tests passing as shown in the recorded output. Execution time and browser-specific details may vary by environment.

## Notes

- Google Chrome must be installed.
- Selenium must be able to start ChromeDriver.
- Internet access is required for the web pages used by these experiments.
- Keep the required supporting files in the expected project structure.
