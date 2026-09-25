# Experiment 12: Data-Driven Automation with Unittest

**Module:** Unit Test Frameworks  
**Student:** Nilanjana Pal

## Overview

This experiment demonstrates **Data-Driven Automation with Unittest** using Selenium and the testing framework specified in the source material.

## What This Experiment Covers

- Data-driven testing
- JSON, CSV and Excel test data
- `openpyxl`
- Generated CSV/XLSX files

## Requirements

- Python 3.10+
- Selenium 4.x
- openpyxl
- Google Chrome
- ChromeDriver/WebDriver support

### Install Packages

```bash
pip install selenium openpyxl
```

## How It Works

The login workflow is tested using JSON, CSV and Excel data. The program creates `login_test_data.csv` and `login_test_data.xlsx`, reads them back, and validates each expected result.

## How to Run

**Python file:** `datadrivenunittest.py`

```bash
python datadrivenunittest.py
```

### Generated Files

When the Python file is run, it generates these files:

- `login_test_data.csv`
- `login_test_data.xlsx`

The CSV file is created and read with Python's `csv` module. The Excel workbook is created and read with `openpyxl`.

## Source Code

The following code is taken from the supplied experiment source.

```python
Experiment 12: Data-Driven Automation with Unittest (Assignment 8)
Module: Unit Test Frameworks - Unittest
Student: Nilanjana Pal

Assignment 8: Data-Driven Automation (DDT)
Tier: Unittest

Task: Build a login script that reads multiple test cases from an external source
(Excel file via pandas or JSON/CSV file) and asserts proper validation errors.
"""

import unittest
import json
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ============================================
# TEST DATA (simulating external file read)
# ============================================
def get_test_data_json():
    """Load test data from JSON file"""
    test_data = [
        {"username": "standard_user", "password": "secret_sauce", "expected": "success"},
        {"username": "locked_out_user", "password": "secret_sauce", "expected": "locked_out"},
        {"username": "wrong_user", "password": "wrong_pass", "expected": "error_message"},
        {"username": "", "password": "secret_sauce", "expected": "error_message"},
        {"username": "standard_user", "password": "", "expected": "error_message"},
        {"username": "", "password": "", "expected": "error_message"},
    ]
    return test_data


def get_test_data_csv():
    """Load test data from CSV"""
    test_data = []
    # Create CSV file for demonstration
    with open("login_test_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password", "expected"])
        writer.writerow(["standard_user", "secret_sauce", "success"])
        writer.writerow(["locked_out_user", "secret_sauce", "locked_out"])
        writer.writerow(["wrong_user", "wrong_pass", "error_message"])

    with open("login_test_data.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_data.append(row)
    return test_data


def get_test_data_excel():
    """Load test data from Excel using openpyxl"""
    from openpyxl import Workbook, load_workbook

    # Create Excel file
    wb = Workbook()
    sheet = wb.active
    sheet.title = "LoginTests"
    sheet.append(["username", "password", "expected"])
    sheet.append(["standard_user", "secret_sauce", "success"])
    sheet.append(["locked_out_user", "secret_sauce", "locked_out"])
    sheet.append(["problem_user", "secret_sauce", "success"])
    wb.save("login_test_data.xlsx")

    # Read back
    test_data = []
    wb = load_workbook("login_test_data.xlsx")
    sheet = wb.active
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_data.append(dict(zip(headers, row)))
    return test_data


class TestLoginDataDriven(unittest.TestCase):
    """Data-Driven Login Tests using Unittest"""

    def setUp(self):
        """Run before each test - fresh browser for clean state"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        """Run after each test - close browser"""
        self.driver.quit()

    def _do_login(self, username, password):
        """Helper method to perform login with proper waits"""
        wait = WebDriverWait(self.driver, 10)

        # Wait for page to be ready before interacting
        user_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        user_field.clear()
        user_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # Wait for the page to settle (either redirect or error message)
        try:
            wait.until(lambda d: "/inventory.html" in d.current_url or
                       self._get_error_message() != "")
        except Exception:
            pass

    def _get_error_message(self):
        """Helper to get error message text"""
        try:
            error_element = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
            return error_element.text if error_element.is_displayed() else ""
        except Exception:
            return ""

    # ---- Test with JSON data ----
    def test_login_json_data(self):
        """Test login using JSON test data"""
        test_cases = get_test_data_json()
        print(f"\nRunning {len(test_cases)} JSON test cases")

        for i, tc in enumerate(test_cases):
            with self.subTest(i=i, username=tc["username"]):
                self.driver.get("https://www.saucedemo.com/")
                self._do_login(tc["username"], tc["password"])

                if tc["expected"] == "success":
                    self.assertIn("/inventory.html", self.driver.current_url,
                                  f"Login should succeed for {tc['username']}")
                elif tc["expected"] == "locked_out":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Locked out error should appear for {tc['username']}")
                elif tc["expected"] == "error_message":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Error message should appear for {tc['username']}")

                print(f"  [PASS] {tc['username']} - {tc['expected']}")
                self.driver.get("https://www.saucedemo.com/")

    # ---- Test with CSV data ----
    def test_login_csv_data(self):
        """Test login using CSV test data"""
        test_cases = get_test_data_csv()
        print(f"\nRunning {len(test_cases)} CSV test cases")

        for i, tc in enumerate(test_cases):
            with self.subTest(i=i, username=tc["username"]):
                self.driver.get("https://www.saucedemo.com/")
                self._do_login(tc["username"], tc["password"])

                if tc["expected"] == "success":
                    self.assertIn("/inventory.html", self.driver.current_url,
                                  f"Login should succeed for {tc['username']}")
                elif tc["expected"] == "locked_out":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Locked out error should appear for {tc['username']}")
                elif tc["expected"] == "error_message":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Error message should appear for {tc['username']}")

                print(f"  [PASS] {tc['username']} - {tc['expected']}")
                self.driver.get("https://www.saucedemo.com/")

    # ---- Test with Excel data ----
    def test_login_excel_data(self):
        """Test login using Excel test data"""
        test_cases = get_test_data_excel()
        print(f"\nRunning {len(test_cases)} Excel test cases")

        for i, tc in enumerate(test_cases):
            with self.subTest(i=i, username=tc["username"]):
                self.driver.get("https://www.saucedemo.com/")
                self._do_login(tc["username"], tc["password"])

                if tc["expected"] == "success":
                    self.assertIn("/inventory.html", self.driver.current_url,
                                  f"Login should succeed for {tc['username']}")
                elif tc["expected"] == "locked_out":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Locked out error should appear for {tc['username']}")
                elif tc["expected"] == "error_message":
                    error = self._get_error_message()
                    self.assertTrue(len(error) > 0,
                                    f"Error message should appear for {tc['username']}")

                print(f"  [PASS] {tc['username']} - {tc['expected']}")
                self.driver.get("https://www.saucedemo.com/")

    def cleanup_files(self):
        """Remove generated test data files"""
        for f in ["login_test_data.csv", "login_test_data.xlsx"]:
            if os.path.exists(f):
                os.remove(f)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Recorded Output

```text
test_login_csv_data (__main__.TestLoginDataDriven.test_login_csv_data)
Test login using CSV test data ... 
Running 3 CSV test cases
  [PASS] standard_user - success
  [PASS] locked_out_user - locked_out
  [PASS] wrong_user - error_message
ok
test_login_excel_data (__main__.TestLoginDataDriven.test_login_excel_data)
Test login using Excel test data ... 
Running 3 Excel test cases
  [PASS] standard_user - success
  [PASS] locked_out_user - locked_out
  [PASS] problem_user - success
ok
test_login_json_data (__main__.TestLoginDataDriven.test_login_json_data)
Test login using JSON test data ... 
Running 6 JSON test cases
  [PASS] standard_user - success
  [PASS] locked_out_user - locked_out
  [PASS] wrong_user - error_message
  [PASS]  - error_message
  [PASS] standard_user - error_message
  [PASS]  - error_message
ok

----------------------------------------------------------------------
Ran 3 tests in 17.707s
login_test_data.csv
username,password,expected
standard_user,secret_sauce,success
locked_out_user,secret_sauce,locked_out
wrong_user,wrong_pass,error_message

login_test_data.xlsx
username	password	expected
standard_user	secret_sauce	success
locked_out_user	secret_sauce	locked_out
problem_user	secret_sauce	success
```

## What Is Happening

The browser is initialized, the specified Selenium actions are performed, and the test framework checks the expected conditions. The recorded output shows the result of the supplied run.

### Data-Driven Flow

1. JSON test cases are prepared.
2. CSV test data is generated and read.
3. Excel test data is generated and read.
4. SauceDemo login is executed for each data set.
5. Expected success/error behavior is asserted.

## Expected Result

The experiment should complete with the tests passing as shown in the recorded output. Execution time and browser-specific details may vary by environment.

## Notes

- Google Chrome must be installed.
- Selenium must be able to start ChromeDriver.
- Internet access is required for the web pages used by these experiments.
- Keep the required supporting files in the expected project structure.
