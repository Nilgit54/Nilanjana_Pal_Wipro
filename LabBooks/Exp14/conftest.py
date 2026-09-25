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