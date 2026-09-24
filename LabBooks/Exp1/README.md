# Experiment 1: Introduction to Selenium

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Introduces Selenium WebDriver, opens Google, verifies the page title and URL, inspects basic browser information, and demonstrates multi-browser support.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 1** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- Google Chrome (primary example)
- ChromeDriver managed/available to Selenium
- Firefox and Edge only if the optional multi-browser test is enabled

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
Experiment 1: Introduction to Selenium
Module: Automation with Selenium
Student: Nilanjana Pal
"""

# Import Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_selenium_basic():
    """
    Basic test to demonstrate Selenium WebDriver initialization
    and basic operations.
    """
    print("Selenium Automation Test - Experiment 1")
    print("=" * 50)
    
    # Create Chrome options for headless mode (optional)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to a website
        driver.get("https://www.google.com")
        
        # Get the title of the page
        title = driver.title
        print(f"Page Title: {title}")
        
        # Verify page loaded
        assert "Google" in title, "Google page not loaded"
        print("✓ Page loaded successfully")
        
        # Get current URL
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        
        # Get page source length
        page_source_length = len(driver.page_source)
        print(f"Page source length: {page_source_length} characters")
        
        # Get window size
        window_size = driver.get_window_size()
        print(f"Window size: {window_size['width']}x{window_size['height']}")
        
        print("=" * 50)
        print("✓ All basic operations completed successfully!")
        
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        
    finally:
        # Close the browser
        driver.quit()
        print("✓ Browser closed successfully")

def test_multiple_browsers():
    """
    Test to demonstrate different browser support
    """
    print("\nTesting Different Browsers")
    print("=" * 50)
    
    # List of browsers to test
    browsers = [
        ("Chrome", webdriver.Chrome),
        ("Firefox", webdriver.Firefox),
        ("Edge", webdriver.Edge)
    ]
    
    for browser_name, webdriver_func in browsers:
        try:
            print(f"\nTesting {browser_name}...")
            driver = webdriver_func()
            driver.get("https://www.google.com")
            print(f"  ✓ {browser_name} - Title: {driver.title}")
            driver.quit()
            print(f"  ✓ {browser_name} - Browser closed")
        except Exception as e:
            print(f"  ✗ {browser_name} - Error: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    # Run basic test
    test_selenium_basic()
    
    # Uncomment to test multiple browsers
    # test_multiple_browsers()
```

## Sample Output

The following output is the output recorded with the experiment:

```text
Page Title: Google
✓ Page loaded successfully
Current URL: https://www.google.com/
✓ All basic operations completed successfully!
✓ Browser closed successfully

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
