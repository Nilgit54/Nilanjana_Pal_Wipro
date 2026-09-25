# Experiment 10: Unittest Introduction with Selenium

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **Unittest Introduction with Selenium** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- `unittest` TestCase
- `setUp()` and `tearDown()`
- Selenium assertions
- Five basic browser tests

## Requirements

- Python 3.10+
- Selenium 4.x
- Google Chrome
- ChromeDriver/WebDriver support

### Install Packages

```bash
pip install selenium
```

## How It Works

The script creates a `unittest.TestCase` class. `setUp()` opens and configures Chrome before each test, while `tearDown()` closes it. Five tests verify Google and SauceDemo behavior.

## How to Run

**Python file:** `unittestintro.py`

```bash
python unittestintro.py
```

## Source Code

The following code is taken from the supplied experiment source.

```python
Experiment 10: Unittest Introduction
Module: Unit Test Frameworks - Unittest
Student: Nilanjana Pal

Covers:
- Unittest Introduction
- First Test Case with Selenium
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSeleniumBasic(unittest.TestCase):
    """First test case using unittest framework"""

    def setUp(self):
        """Run before each test method"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        """Run after each test method"""
        self.driver.quit()

    def test_page_title_google(self):
        """Test to verify Google page title"""
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_page_url_google(self):
        """Test to verify Google page URL"""
        self.driver.get("https://www.google.com")
        self.assertTrue(self.driver.current_url.startswith("https://"))

    def test_saucedemo_page_title(self):
        """Test to verify SauceDemo page title"""
        self.driver.get("https://www.saucedemo.com/")
        self.assertEqual(self.driver.title, "Swag Labs")

    def test_saucedemo_login_form_exists(self):
        """Test to verify login form elements exist"""
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")
        self.assertTrue(username.is_displayed())
        self.assertTrue(password.is_displayed())
        self.assertTrue(login_btn.is_displayed())

    def test_saucedemo_login_success(self):
        """Test successful login on SauceDemo"""
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        self.assertIn("/inventory.html", self.driver.current_url)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Recorded Output

```text
test_page_title_google (__main__.TestSeleniumBasic.test_page_title_google)
Test to verify Google page title ... ok
test_page_url_google (__main__.TestSeleniumBasic.test_page_url_google)
Test to verify Google page URL ... ok
test_saucedemo_login_form_exists (__main__.TestSeleniumBasic.test_saucedemo_login_form_exists)
Test to verify login form elements exist ... ok
test_saucedemo_login_success (__main__.TestSeleniumBasic.test_saucedemo_login_success)
Test successful login on SauceDemo ... ok
test_saucedemo_page_title (__main__.TestSeleniumBasic.test_saucedemo_page_title)
Test to verify SauceDemo page title ... ok

----------------------------------------------------------------------
Ran 5 tests in 27.183s

OK
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
