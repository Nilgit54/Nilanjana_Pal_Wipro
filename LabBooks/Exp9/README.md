# Experiment 9: Advanced Interactions

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Combines file-based test data handling (Excel, JSON, CSV, XML and properties), mouse/JavaScript interactions, and data-driven testing.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 9** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- openpyxl
- Google Chrome
- Internet access for the browser automation portions
- Write permission for generated data files

### Python package installation

Install Selenium with:

```bash
pip install selenium
```

For the Excel portion, install `openpyxl`:

```bash
pip install openpyxl
```

## How It Works

1. Python imports Selenium and the supporting classes required for this experiment.
2. A WebDriver session is created and the required demonstration page is opened.
3. Selenium locates or interacts with the required web elements.
4. The script performs the experiment-specific operation and prints verification messages.
5. Exceptions are handled where applicable.
6. The browser is closed in cleanup code so the WebDriver session does not remain open.

## Source Code

The following code is the experiment code supplied for this task:

```python
Experiment 9: Advance Interactions
Module: Automation with Selenium
Student: Nilanjana Pal

Covers:
- Reading/Writing data from Excel, JSON, CSV, XML, Properties files
- Mouse hover actions
- JavaScript execution
- Data-driven testing
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import csv
import os
import time
from openpyxl import Workbook, load_workbook
import xml.etree.ElementTree as ET
import configparser

# ============================================
# EXCEL HANDLING
# ============================================
def excel_write_data():
    """Write data to Excel file"""
    print("Writing Data to Excel File")
    print("-" * 40)
    
    wb = Workbook()
    sheet = wb.active
    sheet.title = "TestData"
    
    # Add headers
    headers = ["Username", "Password", "Expected Result"]
    sheet.append(headers)
    
    # Add test data
    test_data = [
        ["standard_user", "secret_sauce", "Login Successful"],
        ["locked_out_user", "secret_sauce", "Login Failed - Account Locked"],
        ["problem_user", "secret_sauce", "Login Successful"],
        ["performance_glitch_user", "secret_sauce", "Login Successful"]
    ]
    
    for row in test_data:
        sheet.append(row)
    
    wb.save("testdata.xlsx")
    print(f"✓ Excel file created with {len(test_data)} rows of data")
    return "testdata.xlsx"

def excel_read_data():
    """Read data from Excel file"""
    print("\nReading Data from Excel File")
    print("-" * 40)
    
    try:
        wb = load_workbook("testdata.xlsx")
        sheet = wb.active
        
        print(f"  Sheet name: {sheet.title}")
        print(f"  Max rows: {sheet.max_row}")
        print(f"  Max columns: {sheet.max_column}")
        
        headers = [cell.value for cell in sheet[1]]
        print(f"  Headers: {headers}")
        
        print("  Data:")
        for row in sheet.iter_rows(min_row=2, values_only=True):
            print(f"    {row}")
        
        print(f"  Cell B2: {sheet['B2'].value}")
        print(f"  Cell A3: {sheet['A3'].value}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error reading Excel: {e}")
        return False

def excel_update_data():
    """Update data in Excel file"""
    print("\nUpdating Excel File")
    print("-" * 40)
    
    try:
        wb = load_workbook("testdata.xlsx")
        sheet = wb.active
        sheet['A2'] = "standard_user_updated"
        wb.save("testdata.xlsx")
        
        wb = load_workbook("testdata.xlsx")
        sheet = wb.active
        print(f"✓ Updated & verified: A2 = {sheet['A2'].value}")
    except Exception as e:
        print(f"  ✗ Error updating Excel: {e}")

# ============================================
# JSON HANDLING
# ============================================
def json_write_data():
    """Write data to JSON file"""
    print("\nWriting Data to JSON File")
    print("-" * 40)
    
    data = {
        "test_data": [
            {"username": "standard_user", "password": "secret_sauce", "expected": "login_success"},
            {"username": "locked_out_user", "password": "secret_sauce", "expected": "login_failed"}
        ],
        "test_config": {
            "browser": "chrome",
            "timeout": 10,
            "headless": False
        }
    }
    
    with open("testdata.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("✓ JSON file created successfully")

def json_read_data():
    """Read data from JSON file"""
    print("\nReading Data from JSON File")
    print("-" * 40)
    
    try:
        with open("testdata.json", "r") as f:
            data = json.load(f)
        
        print(f"  Top-level keys: {list(data.keys())}")
        print(f"  Config: {data['test_config']}")
        print(f"  Test cases: {len(data['test_data'])}")
        
        for test in data['test_data']:
            print(f"    {test}")
        
        print(f"  Browser from config: {data['test_config']['browser']}")
        print(f"  First username: {data['test_data'][0]['username']}")
    except Exception as e:
        print(f"  ✗ Error reading JSON: {e}")

# ============================================
# CSV HANDLING
# ============================================
def csv_write_data():
    """Write data to CSV file"""
    print("\nWriting Data to CSV File")
    print("-" * 40)
    
    with open("testdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Test Case", "Username", "Password", "Expected Result"])
        test_cases = [
            ["TC001", "standard_user", "secret_sauce", "Login Success"],
            ["TC002", "locked_out_user", "secret_sauce", "Login Failed"],
            ["TC003", "problem_user", "secret_sauce", "Login Success"],
            ["TC004", "performance_glitch_user", "secret_sauce", "Login Success"]
        ]
        writer.writerows(test_cases)
    
    print("✓ CSV file created with 4 test cases")

def csv_read_data():
    """Read data from CSV file"""
    print("\nReading Data from CSV File")
    print("-" * 40)
    
    try:
        with open("testdata.csv", "r") as f:
            reader = csv.reader(f)
            headers = next(reader)
            print(f"  Headers: {headers}")
            print("  Data:")
            for row in reader:
                print(f"    {row}")
        print("  ✓ CSV reading completed")
    except Exception as e:
        print(f"  ✗ Error reading CSV: {e}")

# ============================================
# XML HANDLING
# ============================================
def xml_write_data():
    """Write data to XML file"""
    print("\nWriting Data to XML File")
    print("-" * 40)
    
    root = ET.Element("TestData")
    root.set("environment", "test")
    
    test_data = [
        {"id": "TC001", "username": "standard_user", "password": "secret_sauce"},
        {"id": "TC002", "username": "problem_user", "password": "secret_sauce"}
    ]
    
    for data in test_data:
        test_case = ET.SubElement(root, "TestCase")
        test_case.set("id", data["id"])
        ET.SubElement(test_case, "Username").text = data["username"]
        ET.SubElement(test_case, "Password").text = data["password"]
    
    tree = ET.ElementTree(root)
    tree.write("testdata.xml", encoding="utf-8", xml_declaration=True)
    print("✓ XML file created successfully")

def xml_read_data():
    """Read data from XML file"""
    print("\nReading Data from XML File")
    print("-" * 40)
    
    try:
        tree = ET.parse("testdata.xml")
        root = tree.getroot()
        
        print(f"  Root: {root.tag} (env={root.get('environment')})")
        for test_case in root.findall("TestCase"):
            test_id = test_case.get("id")
            username = test_case.find("Username").text
            password = test_case.find("Password").text
            print(f"    {test_id}: {username} / {password}")
        print("  ✓ XML reading completed")
    except Exception as e:
        print(f"  ✗ Error reading XML: {e}")

# ============================================
# PROPERTIES FILE HANDLING
# ============================================
def properties_write_data():
    """Write data to properties (INI) file"""
    print("\nWriting Data to Properties File")
    print("-" * 40)
    
    config = configparser.ConfigParser()
    config["browser"] = {"name": "chrome", "headless": "false", "timeout": "10"}
    config["application"] = {"url": "https://www.saucedemo.com/", "environment": "qa"}
    config["credentials"] = {"username": "standard_user", "password": "secret_sauce"}
    
    with open("testdata.properties", "w") as configfile:
        config.write(configfile)
    
    print("✓ Properties file created successfully")

def properties_read_data():
    """Read data from properties file"""
    print("\nReading Data from Properties File")
    print("-" * 40)
    
    try:
        config = configparser.ConfigParser()
        config.read("testdata.properties")
        
        print(f"  Browser: {config['browser']['name']}")
        print(f"  Timeout: {config['browser']['timeout']}")
        print(f"  URL: {config['application']['url']}")
        print(f"  Environment: {config['application']['environment']}")
        print(f"  Username: {config['credentials']['username']}")
        print("  ✓ Properties file reading completed")
    except Exception as e:
        print(f"  ✗ Error reading properties: {e}")

# ============================================
# MOUSE HOVER ACTIONS
# ============================================
def test_mouse_hover():
    """Test mouse hover actions"""
    print("\nTesting Mouse Hover Actions")
    print("-" * 40)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Login to access inventory
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # Hover over inventory item
        item = driver.find_element(By.CLASS_NAME, "inventory_item")
        actions = ActionChains(driver)
        actions.move_to_element(item).perform()
        print("✓ Mouse hovered over inventory item")
        
        # Hover over product image
        img = driver.find_element(By.CLASS_NAME, "inventory_item_img")
        actions.move_to_element(img).perform()
        print("✓ Mouse hovered over product image")
        
        # Hover with pause
        actions.move_to_element(item).pause(2).perform()
        print("✓ Hover with 2 second pause completed")
        
        print("✓ Mouse hover actions completed")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    finally:
        driver.quit()
        print("  ✓ Browser closed")

# ============================================
# JAVASCRIPT EXECUTION
# ============================================
def test_javascript_execution():
    """Test JavaScript command execution"""
    print("\nTesting JavaScript Execution")
    print("-" * 40)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Get page title
        title = driver.execute_script("return document.title;")
        print(f"✓ JS: Page title = '{title}'")
        
        # Get page URL
        url = driver.execute_script("return window.location.href;")
        print(f"✓ JS: Page URL = '{url}'")
        
        # Scroll down
        driver.execute_script("window.scrollBy(0, 500);")
        print("✓ JS: Scrolled down 500px")
        
        # Change element style
        username = driver.find_element(By.ID, "user-name")
        driver.execute_script(
            "arguments[0].setAttribute('style', 'border: 2px solid red;')",
            username
        )
        print("✓ JS: Changed element border to red")
        
        # Get window size
        result = driver.execute_script(
            "return {height: window.innerHeight, width: window.innerWidth};"
        )
        print(f"✓ JS: Window size = {result['width']}x{result['height']}")
        
        print("✓ JavaScript execution completed")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    finally:
        driver.quit()
        print("  ✓ Browser closed")

# ============================================
# DATA-DRIVEN LOGIN TEST
# ============================================
def test_data_driven_login():
    """Data-driven login test using Excel data"""
    print("\nData-Driven Login Test (using Excel data)")
    print("=" * 50)
    
    try:
        wb = load_workbook("testdata.xlsx")
        sheet = wb.active
        
        print(f"  Reading from '{sheet.title}' sheet, {sheet.max_row - 1} data rows")
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            username, password, expected = row
            print(f"\n  Test Case: {username}")
            
            driver = webdriver.Chrome()
            try:
                driver.get("https://www.saucedemo.com/")
                driver.find_element(By.ID, "user-name").send_keys(username)
                driver.find_element(By.ID, "password").send_keys(password)
                driver.find_element(By.ID, "login-button").click()
                time.sleep(2)
                
                if "/inventory.html" in driver.current_url:
                    print(f"    ✓ Result: Login Successful (as expected: {expected})")
                else:
                    print(f"    ✗ Result: Login Failed (expected: {expected})")
            except Exception as e:
                print(f"    ✗ Error: {e}")
            finally:
                driver.quit()
        
        print("\n  ✓ Data-driven testing completed")
    except Exception as e:
        print(f"  ✗ Error: {e}")

def cleanup_test_files():
    """Remove generated test data files"""
    print("\nCleaning Up Test Data Files")
    print("-" * 40)
    
    files = ["testdata.xlsx", "testdata.json", "testdata.csv", "testdata.xml", "testdata.properties"]
    for f in files:
        if os.path.exists(f):
            os.remove(f)
            print(f"  ✓ Removed {f}")
    
    print("  ✓ Cleanup completed")

if __name__ == "__main__":
    print("=" * 60)
    print("EXPERIMENT 9: ADVANCE INTERACTIONS")
    print("=" * 60)
    
    # Data file handling
    excel_write_data()
    excel_read_data()
    excel_update_data()
    json_write_data()
    json_read_data()
    csv_write_data()
    csv_read_data()
    xml_write_data()
    xml_read_data()
    properties_write_data()
    properties_read_data()
    
    # Selenium interactions
    test_mouse_hover()
    test_javascript_execution()
    
    # Data-driven testing
    test_data_driven_login()
    
    # Cleanup
    cleanup_test_files()
    
    print("\n" + "=" * 60)
    print("✓ All advance interaction experiments completed!")
```

## Sample Output

The following output is the output recorded with the experiment:

```text
EXPERIMENT 9: ADVANCE INTERACTIONS
============================================================
Writing Data to Excel File
----------------------------------------
✓ Excel file created with 4 rows of data

Reading Data from Excel File
----------------------------------------
  Sheet name: TestData
  Max rows: 5
  Max columns: 3
  Headers: ['Username', 'Password', 'Expected Result']
  Data:
    ('standard_user', 'secret_sauce', 'Login Successful')
    ('locked_out_user', 'secret_sauce', 'Login Failed - Account Locked')
    ('problem_user', 'secret_sauce', 'Login Successful')
    ('performance_glitch_user', 'secret_sauce', 'Login Successful')
  Cell B2: secret_sauce
  Cell A3: locked_out_user

Updating Excel File
----------------------------------------
✓ Updated & verified: A2 = standard_user_updated

Writing Data to JSON File
----------------------------------------
✓ JSON file created successfully

Reading Data from JSON File
----------------------------------------
  Top-level keys: ['test_data', 'test_config']
  Config: {'browser': 'chrome', 'timeout': 10, 'headless': False}
  Test cases: 2
    {'username': 'standard_user', 'password': 'secret_sauce', 'expected': 'login_success'}
    {'username': 'locked_out_user', 'password': 'secret_sauce', 'expected': 'login_failed'}
  Browser from config: chrome
  First username: standard_user

Writing Data to CSV File
----------------------------------------
✓ CSV file created with 4 test cases

Reading Data from CSV File
----------------------------------------
  Headers: ['Test Case', 'Username', 'Password', 'Expected Result']
  Data:
    ['TC001', 'standard_user', 'secret_sauce', 'Login Success']
    ['TC002', 'locked_out_user', 'secret_sauce', 'Login Failed']
    ['TC003', 'problem_user', 'secret_sauce', 'Login Success']
    ['TC004', 'performance_glitch_user', 'secret_sauce', 'Login Success']
  ✓ CSV reading completed

Writing Data to XML File
----------------------------------------
✓ XML file created successfully

Reading Data from XML File
----------------------------------------
  Root: TestData (env=test)
    TC001: standard_user / secret_sauce
    TC002: problem_user / secret_sauce
  ✓ XML reading completed

Writing Data to Properties File
----------------------------------------
✓ Properties file created successfully

Reading Data from Properties File
----------------------------------------
  Browser: chrome
  Timeout: 10
  URL: https://www.saucedemo.com/
  Environment: qa
  Username: standard_user
  ✓ Properties file reading completed

Testing Mouse Hover Actions
----------------------------------------
✓ Mouse hovered over inventory item
✓ Mouse hovered over product image
✓ Hover with 2 second pause completed
✓ Mouse hover actions completed
  ✓ Browser closed

Testing JavaScript Execution
----------------------------------------
✓ JS: Page title = 'Swag Labs'
✓ JS: Page URL = 'https://www.saucedemo.com/'
✓ JS: Scrolled down 500px
✓ JS: Changed element border to red
✓ JS: Window size = 1036x695
✓ JavaScript execution completed
  ✓ Browser closed

Data-Driven Login Test (using Excel data)
==================================================
  Reading from 'TestData' sheet, 4 data rows

  Test Case: standard_user_updated
    ✗ Result: Login Failed (expected: Login Successful)

  Test Case: locked_out_user
    ✗ Result: Login Failed (expected: Login Failed - Account Locked)

  Test Case: problem_user
    ✓ Result: Login Successful (as expected: Login Successful)

  Test Case: performance_glitch_user
    ✓ Result: Login Successful (as expected: Login Successful)

  ✓ Data-driven testing completed

Cleaning Up Test Data Files
----------------------------------------
  ✓ Removed testdata.xlsx
  ✓ Removed testdata.json
  ✓ Removed testdata.csv
  ✓ Removed testdata.xml
  ✓ Removed testdata.properties
  ✓ Cleanup completed

============================================================
✓ All advance interaction experiments completed!
```

## What Is Happening

### 1. Browser automation
Selenium starts a browser through `webdriver.Chrome()` (and, where applicable, Firefox or Edge) and navigates to the target web page.

### 2. Element identification
The script uses Selenium locators such as `By.ID`, `By.NAME`, `By.XPATH`, `By.CSS_SELECTOR`, `By.CLASS_NAME`, and `By.TAG_NAME` where required by the experiment.

### 3. Interaction and validation
After locating an element, the script performs actions such as clicking, typing, selecting, switching windows/frames, reading text, or checking an element state. The printed `✓` messages indicate that the corresponding operation completed successfully.

### 4. Verification
The experiment checks important results such as page titles, URLs, selected values, extracted table data, displayed text, or login success.

### 5. Cleanup
The browser is closed with `driver.quit()` so the automation session is terminated even when an error occurs.

## Expected Result

A successful run should complete the experiment-specific actions and produce output consistent with the recorded sample output above. Exact dynamic values such as timestamps, browser window handles, generated screenshot filenames, or environment-dependent details may differ between runs.

## Notes

- Keep the browser and Selenium versions compatible.
- Make sure the internet is available because the supplied scripts use public demonstration websites.
- If a website changes its HTML structure, an existing locator may need to be updated.
- Run the script from a terminal/IDE where Python and the installed packages are available.
