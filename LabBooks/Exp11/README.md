# Experiment 11: Unittest SetUp/TearDown, Assert Methods and Test Suite

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **Unittest SetUp/TearDown, Assert Methods and Test Suite** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- `setUp()` and `tearDown()`
- Common unittest assert methods
- Login validation
- Custom and all-tests suites

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

Two unittest classes demonstrate assertion methods and login validation. The program builds a custom `TestSuite` and an all-tests suite, then runs both.

## How to Run

**Python file:** `unittestasserts.py`

```bash
python unittestasserts.py
```

## Source Code

The following code is taken from the supplied experiment source.

```python
Experiment 11: Unittest SetUp/TearDown, Assert Methods, Test Suite
Module: Unit Test Frameworks - Unittest
Student: Nilanjana Pal

Covers:
- Class Level SetUp and TearDown
- All Assert Methods
- Creating and running Test Suites
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class TestAssertMethods(unittest.TestCase):
    """Demonstrate all unittest assert methods"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.quit()

    def test_assertEqual(self):
        """assertEqual - checks if two values are equal"""
        self.assertEqual(self.driver.title, "Swag Labs")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        print("  assertEqual: Title matches expected value")

    def test_assertNotEqual(self):
        """assertNotEqual - checks if two values are NOT equal"""
        self.assertNotEqual(self.driver.title, "Google")
        self.assertNotEqual(self.driver.current_url, "https://www.google.com/")
        print("  assertNotEqual: Title differs from Google")

    def test_assertTrue(self):
        """assertTrue - checks if condition is True"""
        username = self.driver.find_element(By.ID, "user-name")
        self.assertTrue(username.is_displayed())
        self.assertTrue(username.is_enabled())
        print("  assertTrue: Element is displayed and enabled")

    def test_assertFalse(self):
        """assertFalse - checks if condition is False"""
        self.driver.find_element(By.ID, "user-name").send_keys("test")
        # Error text should NOT be present before clicking login
        element = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        self.assertFalse("Username and password do not match" in element.text)
        print("  assertFalse: No error message text before login attempt")

    def test_assertIn(self):
        """assertIn - checks if value is in collection"""
        self.assertIn("saucedemo", self.driver.current_url)
        self.assertIn("Swag Labs", self.driver.title)
        print("  assertIn: URL contains expected string")

    def test_assertIsNotNone(self):
        """assertIsNotNone - checks if value is not None"""
        element = self.driver.find_element(By.ID, "user-name")
        self.assertIsNotNone(element)
        self.assertIsNotNone(element.get_attribute("id"))
        self.assertIsNotNone(element.get_attribute("type"))
        print("  assertIsNotNone: Element and attributes are not None")

    def test_assertRaises(self):
        """assertRaises - checks if exception is raised"""
        with self.assertRaises(Exception):
            self.driver.find_element(By.ID, "non_existent_element_xyz")
        print("  assertRaises: NoSuchElementException raised as expected")


class TestLoginValidation(unittest.TestCase):
    """Test login validations using assert methods"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        """Test valid credentials"""
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        self.assertIn("/inventory.html", self.driver.current_url)

    def test_invalid_credentials_show_error(self):
        """Test invalid credentials show error"""
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_pass")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        error = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        self.assertTrue(error.is_displayed())
        self.assertIn("Username and password do not match", error.text)

    def test_empty_credentials_show_error(self):
        """Test empty credentials show error"""
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        error = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        self.assertTrue(error.is_displayed())


def create_test_suite():
    """Create a custom test suite"""
    suite = unittest.TestSuite()

    # Add specific tests
    suite.addTest(TestAssertMethods("test_assertEqual"))
    suite.addTest(TestAssertMethods("test_assertNotEqual"))
    suite.addTest(TestAssertMethods("test_assertTrue"))
    suite.addTest(TestAssertMethods("test_assertFalse"))
    suite.addTest(TestAssertMethods("test_assertIn"))
    suite.addTest(TestAssertMethods("test_assertIsNotNone"))
    suite.addTest(TestAssertMethods("test_assertRaises"))
    suite.addTest(TestLoginValidation("test_valid_login"))
    suite.addTest(TestLoginValidation("test_invalid_credentials_show_error"))

    return suite


def create_all_tests_suite():
    """Create suite with ALL tests using loadTestsFromTestCase"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestAssertMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestLoginValidation))

    return suite


if __name__ == "__main__":
    print("=" * 60)
    print("Running Custom Test Suite")
    print("=" * 60)
    runner = unittest.TextTestRunner(verbosity=2)
    suite = create_test_suite()
    runner.run(suite)

    print("\n" + "=" * 60)
    print("Running ALL Tests via TestSuite")
    print("=" * 60)
    runner = unittest.TextTestRunner(verbosity=2)
    all_suite = create_all_tests_suite()
    runner.run(all_suite)
```

## Recorded Output

```text
Running Custom Test Suite
============================================================
test_assertEqual (__main__.TestAssertMethods.test_assertEqual)
assertEqual - checks if two values are equal ...   assertEqual: Title matches expected value
ok
test_assertNotEqual (__main__.TestAssertMethods.test_assertNotEqual)
assertNotEqual - checks if two values are NOT equal ...   assertNotEqual: Title differs from Google
ok
test_assertTrue (__main__.TestAssertMethods.test_assertTrue)
assertTrue - checks if condition is True ...   assertTrue: Element is displayed and enabled
ok
test_assertFalse (__main__.TestAssertMethods.test_assertFalse)
assertFalse - checks if condition is False ...   assertFalse: No error message text before login attempt
ok
test_assertIn (__main__.TestAssertMethods.test_assertIn)
assertIn - checks if value is in collection ...   assertIn: URL contains expected string
ok
test_assertIsNotNone (__main__.TestAssertMethods.test_assertIsNotNone)
assertIsNotNone - checks if value is not None ...   assertIsNotNone: Element and attributes are not None
ok
test_assertRaises (__main__.TestAssertMethods.test_assertRaises)
assertRaises - checks if exception is raised ...   assertRaises: NoSuchElementException raised as expected
ok
test_valid_login (__main__.TestLoginValidation.test_valid_login)
Test valid credentials ... ok
test_invalid_credentials_show_error (__main__.TestLoginValidation.test_invalid_credentials_show_error)
Test invalid credentials show error ... ok

----------------------------------------------------------------------
Ran 9 tests in 44.123s

OK

============================================================
Running ALL Tests via TestSuite
============================================================
test_assertEqual (__main__.TestAssertMethods.test_assertEqual)
assertEqual - checks if two values are equal ...   assertEqual: Title matches expected value
ok
test_assertFalse (__main__.TestAssertMethods.test_assertFalse)
assertFalse - checks if condition is False ...   assertFalse: No error message text before login attempt
ok
test_assertIn (__main__.TestAssertMethods.test_assertIn)
assertIn - checks if value is in collection ...   assertIn: URL contains expected string
ok
test_assertIsNotNone (__main__.TestAssertMethods.test_assertIsNotNone)
assertIsNotNone - checks if value is not None ...   assertIsNotNone: Element and attributes are not None
ok
test_assertNotEqual (__main__.TestAssertMethods.test_assertNotEqual)
assertNotEqual - checks if two values are NOT equal ...   assertNotEqual: Title differs from Google
ok
test_assertRaises (__main__.TestAssertMethods.test_assertRaises)
assertRaises - checks if exception is raised ...   assertRaises: NoSuchElementException raised as expected
ok
test_assertTrue (__main__.TestAssertMethods.test_assertTrue)
assertTrue - checks if condition is True ...   assertTrue: Element is displayed and enabled
ok
test_empty_credentials_show_error (__main__.TestLoginValidation.test_empty_credentials_show_error)
Test empty credentials show error ... ok
test_invalid_credentials_show_error (__main__.TestLoginValidation.test_invalid_credentials_show_error)
Test invalid credentials show error ... ok
test_valid_login (__main__.TestLoginValidation.test_valid_login)
Test valid credentials ... ok

----------------------------------------------------------------------
Ran 10 tests in 48.796s

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
