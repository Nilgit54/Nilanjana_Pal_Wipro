# Experiment 5: Advanced Web Controls

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Handles JavaScript alerts/confirms/prompts, browser windows, iframes, keyboard actions, scrolling, and element-state checks.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 5** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- Google Chrome
- Internet access to https://the-internet.herokuapp.com/

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
Experiment 5: Advanced Web Controls - JavaScript Alerts, Windows, and Iframes
Module: Automation with Selenium
Student: Nilanjana Pal

This covers:
- Assignment 4: JavaScript Alerts and Confirms
- Assignment 6: Windows, Tabs, and Iframes
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_javascript_alert():
    """Test JavaScript Alert - Assignment 4 part 1"""
    print("Assignment 4: JavaScript Alerts")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    try:
        # Test 1: JS Alert
        print("\n--- Test 1: JS Alert ---")
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        time.sleep(1)
        
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"✓ Alert text: '{alert.text}'")
        alert.accept()
        print("✓ Alert accepted")
        
        result = driver.find_element(By.ID, "result").text
        print(f"✓ Result: {result}")
        
        # Test 2: JS Confirm - Dismiss
        print("\n--- Test 2: JS Confirm (Dismiss) ---")
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        confirm_button.click()
        time.sleep(1)
        
        confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"✓ Confirm text: '{confirm.text}'")
        confirm.dismiss()
        print("✓ Confirm box dismissed (Cancel clicked)")
        
        result = driver.find_element(By.ID, "result").text
        print(f"✓ Result: {result}")
        
        # Test 3: JS Confirm - Accept
        print("\n--- Test 3: JS Confirm (Accept) ---")
        confirm_button.click()
        time.sleep(1)
        
        confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
        confirm.accept()
        print("✓ Confirm box accepted (OK clicked)")
        
        result = driver.find_element(By.ID, "result").text
        print(f"✓ Result: {result}")
        
        # Test 4: JS Prompt with text input
        print("\n--- Test 4: JS Prompt (with send_keys) ---")
        prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        prompt_button.click()
        time.sleep(1)
        
        prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"✓ Prompt text: '{prompt.text}'")
        prompt.send_keys("Nilanjana Pal")
        print("✓ Text 'Nilanjana Pal' entered into prompt")
        prompt.accept()
        print("✓ Prompt accepted")
        
        result = driver.find_element(By.ID, "result").text
        print(f"✓ Result: {result}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_windows_tabs():
    """Test Windows and Tabs - Assignment 6 part 1"""
    print("\nAssignment 6: Windows and Tabs")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/windows")
    
    try:
        original_window = driver.current_window_handle
        print(f"✓ Original window handle: {original_window[:25]}...")
        print(f"✓ Original title: {driver.title}")
        
        # Open new window/tab
        link = driver.find_element(By.LINK_TEXT, "Click Here")
        link.click()
        time.sleep(2)
        
        # Get all window handles
        all_windows = driver.window_handles
        print(f"✓ Total handles: {len(all_windows)}")
        
        # Switch to new window
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                break
        
        # Get new window info
        print(f"✓ New window title: {driver.title}")
        print(f"✓ New window URL: {driver.current_url}")
        
        # Close the new window
        driver.close()
        print("✓ New window closed")
        
        # Switch back to original window
        driver.switch_to.window(original_window)
        print(f"✓ Switched back to: {driver.title}")
        print(f"✓ Current URL: {driver.current_url}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_iframes():
    """Test Iframes - Assignment 6 part 2"""
    print("\nAssignment 6: Iframes")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/iframe")
    
    try:
        # Switch to iframe context safely
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr"))
        )
        print("✓ Switched to iframe (id: mce_0_ifr)")
        
        # Locate the editable body inside the iframe
        editor_area = driver.find_element(By.ID, "tinymce")
        
        # Clear existing text using Ctrl+A and Backspace (avoiding editor_area.clear())
        editor_area.send_keys(Keys.CONTROL + "a")
        editor_area.send_keys(Keys.BACKSPACE)
        print("✓ Cleared existing editor content")
        
        # Enter new text into the editor
        editor_area.send_keys("Hello from within the iframe!")
        print("✓ Text entered inside iframe editor")
        
        # Verify text inside iframe
        text = editor_area.text
        print(f"✓ Text in editor: '{text}'")
        
        # Switch back to default DOM context
        driver.switch_to.default_content()
        print("✓ Switched back to main content")
        print(f"✓ Page title: {driver.title}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_advanced_controls():
    """Additional advanced controls demo"""
    print("\nAdditional Advanced Controls")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        # Keyboard events
        print("\n--- Keyboard Events ---")
        driver.get("https://the-internet.herokuapp.com/login")
        username = driver.find_element(By.ID, "username")
        
        actions = ActionChains(driver)
        actions.click(username)
        actions.send_keys("KEYBOARD_EVENT_TEST")
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        actions.perform()
        print(f"✓ Keyboard actions performed: {username.get_attribute('value')}")
        
        # Scroll operations
        print("\n--- Scroll Operations ---")
        driver.execute_script("window.scrollBy(0, 300)")
        time.sleep(1)
        print("✓ Scrolled down 300px")
        
        driver.execute_script("window.scrollTo(0, 0)")
        print("✓ Scrolled back to top")
        
        # Element state
        print("\n--- Element State ---")
        login_button = driver.find_element(By.CLASS_NAME, "radius")
        print(f"✓ Login button enabled: {login_button.is_enabled()}")
        print(f"✓ Login button displayed: {login_button.is_displayed()}")
        print(f"✓ Login button text: '{login_button.text}'")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

if __name__ == "__main__":
    print("=" * 60)
    print("EXPERIMENT 5: ADVANCED WEB CONTROLS")
    print("=" * 60)
    
    test_javascript_alert()
    test_windows_tabs()
    test_iframes()
    test_advanced_controls()
    
    print("\n" + "=" * 60)
    print("✓ All experiments completed!")
```

## Sample Output

The following output is the output recorded with the experiment:

```text
EXPERIMENT 5: ADVANCED WEB CONTROLS
============================================================
Assignment 4: JavaScript Alerts
==================================================

--- Test 1: JS Alert ---
✓ Alert text: 'I am a JS Alert'
✓ Alert accepted
✓ Result: You successfully clicked an alert

--- Test 2: JS Confirm (Dismiss) ---
✓ Confirm text: 'I am a JS Confirm'
✓ Confirm box dismissed (Cancel clicked)
✓ Result: You clicked: Cancel

--- Test 3: JS Confirm (Accept) ---
✓ Confirm box accepted (OK clicked)
✓ Result: You clicked: Ok

--- Test 4: JS Prompt (with send_keys) ---
✓ Prompt text: 'I am a JS prompt'
✓ Text 'Nilanjana Pal' entered into prompt
✓ Prompt accepted
✓ Result: You entered: Nilanjana Pal
✓ Browser closed

Assignment 6: Windows and Tabs
✓ Original title: The Internet
✓ Total handles: 3
✓ New window title: Settings - Reset settings
✓ New window URL: chrome://settings/triggeredResetProfileSettings
✓ New window closed
✓ Switched back to: The Internet
✓ Current URL: https://the-internet.herokuapp.com/windows
✓ Browser closed

Assignment 6: Iframes
==================================================
✓ Switched to iframe (id: mce_0_ifr)
✓ Cleared existing editor content
✓ Text entered inside iframe editor
✓ Text in editor: 'Your content goes here.'
✓ Switched back to main content
✓ Page title: The Internet
✓ Browser closed

Additional Advanced Controls
==================================================

--- Keyboard Events ---
✓ Keyboard actions performed: KEYBOARD_EVENT_TEST

--- Scroll Operations ---
✓ Scrolled down 300px
✓ Scrolled back to top

--- Element State ---
✓ Login button enabled: True
✓ Login button displayed: True
✓ Login button text: 'Login'
✓ Browser closed

============================================================
✓ All experiments completed!

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
