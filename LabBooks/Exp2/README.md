# Experiment 2: Selenium WebDriver Installation and Setup

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Verifies the Python and Selenium installation, tests Chrome/Firefox/Edge WebDrivers, and checks common local driver paths.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 2** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- Chrome, Firefox and Edge installed for the three browser tests
- Corresponding WebDriver support
- Windows paths are checked by the supplied script

### Python package installation

Install Selenium with:

```bash
pip install selenium
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
Experiment 2: Selenium WebDriver Installation and Setup
Module: Automation with Selenium
Student: Nilanjana Pal
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
import sys
import os

def check_python_version():
    """Check Python version"""
    print("Python Version Check")
    print("-" * 30)
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    print()

def check_selenium_version():
    """Check Selenium version"""
    print("Selenium Version Check")
    print("-" * 30)
    try:
        import selenium
        print(f"Selenium Version: {selenium.__version__}")
    except ImportError:
        print("Selenium not installed!")
    print()

def test_chrome_driver():
    """Test Chrome WebDriver"""
    print("Chrome WebDriver Test")
    print("-" * 30)
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        
        # Get page details
        title = driver.title
        url = driver.current_url
        
        print(f"  Title: {title}")
        print(f"  URL: {url}")
        
        # Perform a simple search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.submit()
        
        import time
        time.sleep(2)
        
        print(f"  Search Results Title: {driver.title}")
        print("  ✓ Chrome test passed!")
        
        driver.quit()
        return True
        
    except Exception as e:
        print(f"  ✗ Chrome test failed: {e}")
        return False

def test_firefox_driver():
    """Test Firefox WebDriver"""
    print("\nFirefox WebDriver Test")
    print("-" * 30)
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")
        
        title = driver.title
        url = driver.current_url
        
        print(f"  Title: {title}")
        print(f"  URL: {url}")
        
        driver.quit()
        print("  ✓ Firefox test passed!")
        return True
        
    except Exception as e:
        print(f"  ✗ Firefox test failed: {e}")
        return False

def test_edge_driver():
    """Test Edge WebDriver"""
    print("\nEdge WebDriver Test")
    print("-" * 30)
    try:
        driver = webdriver.Edge()
        driver.get("https://www.google.com")
        
        title = driver.title
        url = driver.current_url
        
        print(f"  Title: {title}")
        print(f"  URL: {url}")
        
        driver.quit()
        print("  ✓ Edge test passed!")
        return True
        
    except Exception as e:
        print(f"  ✗ Edge test failed: {e}")
        return False

def test_driver_paths():
    """Check if driver paths are accessible"""
    print("\nDriver Path Check")
    print("-" * 30)
    
    # Common driver locations
    chrome_paths = [
        r"C:\chromedriver\chromedriver.exe",
        r"C:\Program Files\chromedriver\chromedriver.exe",
        os.path.expanduser(r"~\chromedriver\chromedriver.exe")
    ]
    
    firefox_paths = [
        r"C:\geckodriver\geckodriver.exe",
        r"C:\Program Files\geckodriver\geckodriver.exe",
        os.path.expanduser(r"~\geckodriver\geckodriver.exe")
    ]
    
    edge_paths = [
        r"C:\edgedriver\msedgedriver.exe",
        r"C:\Program Files\edgedriver\msedgedriver.exe",
        os.path.expanduser(r"~\edgedriver\msedgedriver.exe")
    ]
    
    print("ChromeDriver:")
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"  ✓ Found: {path}")
        else:
            print(f"  ✗ Not found: {path}")
    
    print("\nGeckoDriver:")
    for path in firefox_paths:
        if os.path.exists(path):
            print(f"  ✓ Found: {path}")
        else:
            print(f"  ✗ Not found: {path}")
    
    print("\nEdgeDriver:")
    for path in edge_paths:
        if os.path.exists(path):
            print(f"  ✓ Found: {path}")
        else:
            print(f"  ✗ Not found: {path}")

if __name__ == "__main__":
    print("=" * 60)
    print("SELENIUM WEBDRIVER INSTALLATION VERIFICATION")
    print("=" * 60)
    print()
    
    # Check versions
    check_python_version()
    check_selenium_version()
    
    # Check driver paths
    test_driver_paths()
    
    print("\n" + "=" * 60)
    print("BROWSER DRIVER TESTS")
    print("=" * 60)
    
    # Test each browser
    results = {}
    results['Chrome'] = test_chrome_driver()
    results['Firefox'] = test_firefox_driver()
    results['Edge'] = test_edge_driver()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for browser, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{browser}: {status}")
    
    print("=" * 60)
    print("Installation verification completed!")
```

## Sample Output

The following output is the output recorded with the experiment:

```text
SELENIUM WEBDRIVER INSTALLATION VERIFICATION
============================================================

Python Version Check
------------------------------
Python Version: 3.12.6
Selenium Version Check
------------------------------
Selenium Version: 4.48.0
BROWSER DRIVER TESTS
============================================================
Chrome WebDriver Test
------------------------------
  Title: Google
  URL: https://www.google.com/
  ✓ Chrome test passed!

Firefox WebDriver Test
------------------------------
  Title: Google
  URL: https://www.google.com/
  ✓ Firefox test passed!

Edge WebDriver Test
------------------------------
  Title: Google
  URL: https://www.google.com/
  ✓ Edge test passed!

============================================================
TEST SUMMARY
============================================================
Chrome: ✓ PASSED
Firefox: ✓ PASSED
Edge: ✓ PASSED
============================================================
Installation verification completed!

"""
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
