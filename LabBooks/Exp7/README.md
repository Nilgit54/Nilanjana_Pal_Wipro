# Experiment 7: Synchronization / Wait Types

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Demonstrates implicit waits, explicit waits, expected conditions, dynamic loading, and the difference between fixed delays and condition-based synchronization.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 7** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- Google Chrome
- Internet access to the dynamic-loading demo pages

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
Experiment 7: Synchronization / Wait Types
Module: Automation with Selenium
Student: Nilanjana Pal

Assignment 2: Synchronization & Explicit Waits
Tier 1: Core Fundamentals & Locators
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_implicit_wait():
    """Test implicit wait behavior"""
    print("Testing Implicit Wait")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    
    # Set implicit wait - applies to all elements globally
    driver.implicitly_wait(10)
    print("✓ Implicit wait set to 10 seconds")
    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    try:
        # Click Start button
        start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()
        print("✓ Clicked Start button")
        
        # With implicit wait, find_element will wait up to 10s for DOM presence
        finish_text = driver.find_element(By.ID, "finish")
        print(f"✓ Found finish element")
        print(f"  Text (may be empty without explicit wait): '{finish_text.text}'")
        print(f"  Displayed: {finish_text.is_displayed()}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_explicit_wait():
    """Test explicit wait behavior"""
    print("\nTesting Explicit Wait")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    try:
        # Click Start button
        start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()
        print("✓ Clicked Start button")
        
        # Explicit wait for element to be visible
        finish_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        print(f"✓ Element visible after explicit wait")
        print(f"  Text: '{finish_element.text}'")
        
        # Wait for text to be present in element
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        print("✓ Text 'Hello World!' confirmed in element")
        
        # Get final text
        finish_text = driver.find_element(By.ID, "finish").text
        print(f"✓ Final text: '{finish_text}'")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_expected_conditions():
    """Test various expected_conditions"""
    print("\nTesting Expected Conditions")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # 1. Element to be clickable
        start_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
        )
        print("✓ 1. element_to_be_clickable - Start button ready")
        start_button.click()
        
        # 2. Element to be visible
        finish = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        print("✓ 2. visibility_of_element_located - Finish element visible")
        
        # 3. Text to be present in element
        wait.until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        print("✓ 3. text_to_be_present_in_element - Text confirmed")
        
        print("\nOther commonly used expected_conditions:")
        print("  - presence_of_element_located")
        print("  - presence_of_all_elements_located")
        print("  - element_to_be_selected")
        print("  - alert_is_present")
        print("  - frame_to_be_available_and_switch_to_it")
        print("  - invisibility_of_element_located")
        print("  - element_to_be_clickable")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_comparison():
    """Compare implicit and explicit wait behavior"""
    print("\n=== IMPLICIT vs EXPLICIT WAIT COMPARISON ===")
    print("-" * 50)
    
    print("\nIMPLICIT WAIT:")
    print("  • Global setting - applies to ALL find_element calls")
    print("  • Set once using driver.implicitly_wait(seconds)")
    print("  • Waits for element PRESENCE in DOM only")
    print("  • Doesn't verify element visibility or enabled state")
    print("  • Can slow down tests if set too high")
    
    print("\nEXPLICIT WAIT:")
    print("  • Per-element/per-condition setting")
    print("  • Uses WebDriverWait + expected_conditions")
    print("  • Waits for SPECIFIC conditions")
    print("  • More efficient and precise")
    print("  • Highly recommended for dynamic content")
    
    print("\nRECOMMENDATION:")
    print("  ✓ Use explicit wait for dynamic elements")
    print("  ✓ Use implicit wait as a baseline")
    print("  ✗ Avoid time.sleep() - inefficient and flaky")
    
    # Demonstrate
    print("\n--- DEMONSTRATION ---")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    try:
        start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()
        print("\n✓ Clicked Start")
        
        # time.sleep approach (not recommended)
        time.sleep(5)
        print("✗ time.sleep(5): Waits fixed 5s - inefficient")
        
        # Explicit wait approach (recommended)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        print("✓ Explicit wait: Waits only until condition met")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_dynamic_loading_example1():
    """Test dynamic loading - Example 1"""
    print("\n=== DYNAMIC LOADING - EXAMPLE 1 ===")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    try:
        # Check initial state
        print("Checking initial state...")
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button"))
        )
        print(f"  Start button enabled: {start_button.is_enabled()}")
        print(f"  Start button text: '{start_button.text}'")
        
        # Click Start
        start_button.click()
        print("\n✓ Clicked Start button")
        time.sleep(1)
        
        # Check loading indicator
        loading = driver.find_element(By.ID, "loading")
        print(f"  Loading displayed: {loading.is_displayed()}")
        
        # Wait for text to be present (bypasses loading spinner)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        print("✓ Dynamic content loaded with explicit wait!")
        
        finish_element = driver.find_element(By.ID, "finish")
        print(f"  Finish text: '{finish_element.text}'")
        print(f"  Loading displayed after: {loading.is_displayed()}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

if __name__ == "__main__":
    print("=" * 60)
    print("EXPERIMENT 7: SYNCHRONIZATION / WAIT TYPES")
    print("=" * 60)
    
    test_implicit_wait()
    test_explicit_wait()
    test_expected_conditions()
    test_comparison()
    test_dynamic_loading_example1()
    
    print("\n" + "=" * 60)
    print("✓ All synchronization experiments completed!")
```

## Sample Output

The following output is the output recorded with the experiment:

```text
EXPERIMENT 7: SYNCHRONIZATION / WAIT TYPES
============================================================
Testing Implicit Wait
==================================================
✓ Implicit wait set to 10 seconds
✓ Clicked Start button
✓ Found finish element
  Text (may be empty without explicit wait): 'Hello World!'
  Displayed: True
✓ Browser closed

Testing Explicit Wait
==================================================
✓ Clicked Start button
✓ Element visible after explicit wait
  Text: 'Hello World!'
✓ Text 'Hello World!' confirmed in element
✓ Final text: 'Hello World!'
✓ Browser closed

Testing Expected Conditions
==================================================
✓ 1. element_to_be_clickable - Start button ready
✓ 2. visibility_of_element_located - Finish element visible
✓ 3. text_to_be_present_in_element - Text confirmed

Other commonly used expected_conditions:
  - presence_of_element_located
  - presence_of_all_elements_located
  - element_to_be_selected
  - alert_is_present
  - frame_to_be_available_and_switch_to_it
  - invisibility_of_element_located
  - element_to_be_clickable
✓ Browser closed

=== IMPLICIT vs EXPLICIT WAIT COMPARISON ===
--------------------------------------------------

IMPLICIT WAIT:
  • Global setting - applies to ALL find_element calls
  • Set once using driver.implicitly_wait(seconds)
  • Waits for element PRESENCE in DOM only
  • Doesn't verify element visibility or enabled state
  • Can slow down tests if set too high

EXPLICIT WAIT:
  • Per-element/per-condition setting
  • Uses WebDriverWait + expected_conditions
  • Waits for SPECIFIC conditions
  • More efficient and precise
  • Highly recommended for dynamic content

RECOMMENDATION:
  ✓ Use explicit wait for dynamic elements
  ✓ Use implicit wait as a baseline
  ✗ Avoid time.sleep() - inefficient and flaky

--- DEMONSTRATION ---
--------------------------------------------------

✓ Clicked Start
✗ time.sleep(5): Waits fixed 5s - inefficient
✓ Explicit wait: Waits only until condition met
✓ Browser closed

=== DYNAMIC LOADING - EXAMPLE 1 ===
--------------------------------------------------
Checking initial state...
  Start button enabled: True
  Start button text: 'Start'

✓ Clicked Start button
  Loading displayed: True
✓ Dynamic content loaded with explicit wait!
  Finish text: 'Hello World!'
  Loading displayed after: False
✓ Browser closed

============================================================
✓ All synchronization experiments completed!

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
