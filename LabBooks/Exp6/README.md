# Experiment 6: Dynamic Elements - Web Tables

**Module:** Automation with Selenium  
**Student:** Nilanjana Pal

## Overview

Traverses an HTML table, finds records by name, extracts selected columns, reads complete rows, extracts due amounts, and demonstrates table sorting.

## What This Experiment Demonstrates

This experiment is intended to show the Selenium concept covered in **Experiment 6** through a runnable Python automation script. The program prints progress messages so that each major operation can be verified from the terminal.

## Requirements

- Python 3.x
- selenium package
- Google Chrome
- Internet access to https://the-internet.herokuapp.com/tables

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
Experiment 6: Handling Dynamic Elements - Web Tables
Module: Automation with Selenium
Student: Nilanjana Pal

Assignment 5: The HTML Web Table Extractor
Tier 2: Advanced User Interactions
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_webtable_traversal():
    """Test WebTable row and column traversal"""
    print("Assignment 5: HTML Web Table Extractor")
    print("=" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")
    
    try:
        # Find the first table
        table = driver.find_element(By.ID, "table1")
        print("✓ Found table1")
        
        # Get all rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(f"✓ Total rows: {len(rows)}")
        
        # Get headers
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        header_texts = [header.text for header in headers]
        print(f"✓ Headers: {header_texts}")
        
        # Traverse all rows and columns
        print("\n--- Traversing Table ---")
        for i, row in enumerate(rows):
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:
                cell_data = [cell.text for cell in cells]
                print(f"  Row {i}: {cell_data}")
        
        print("\n✓ Table traversal completed!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_match_name_get_value():
    """
    Main task: Locate a specific row by matching a name string,
    then retrieve the value from a specific column next to it
    """
    print("\n=== THE WEB TABLE EXTRACTOR TASK ===")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")
    
    try:
        table = driver.find_element(By.ID, "table1")
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        # Get headers
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        header_texts = [h.text for h in headers]
        print(f"Table headers: {header_texts}")
        
        # Search criteria: (name to find, column to extract)
        search_criteria = [
            ("Smith", "Due"),          # Find Smith's Due amount
            ("Bach", "Email"),          # Find Bach's Email
            ("Conway", "Web Site"),     # Find Conway's Website
            ("Doe", "Due")              # Find Doe's Due amount
        ]
        
        print("\nResults:")
        print("-" * 50)
        
        for name, target_col in search_criteria:
            found = False
            for row in rows[1:]:  # Skip header row
                cells = row.find_elements(By.TAG_NAME, "td")
                cell_texts = [cell.text for cell in cells]
                
                # Check if this row contains the search name
                if name in cell_texts:
                    # Find the index of the target column
                    col_index = header_texts.index(target_col)
                    
                    # Get the value from the target column
                    target_value = cells[col_index].text if col_index < len(cells) else "N/A"
                    
                    print(f"  '{name}' → {target_col}: {target_value}")
                    found = True
                    break
            
            if not found:
                print(f"  '{name}' → {target_col}: NOT FOUND")
        
        print("-" * 50)
        print("\n✓ Web Table Extractor task completed!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")

def test_find_specific_row_details():
    """Get full details of a specific person from the table"""
    print("\n=== Get Full Details of a Person ===")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")
    
    try:
        table = driver.find_element(By.ID, "table1")
        rows = table.find_elements(By.TAG_NAME, "tr")
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        header_texts = [h.text for h in headers]
        
        # Find Frank Bach's full record
        search_name = "Bach"
        
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            cell_texts = [cell.text for cell in cells]
            
            if search_name in cell_texts:
                print(f"\nFound complete record for '{search_name}':")
                for header, value in zip(header_texts, cell_texts):
                    print(f"  {header}: {value}")
                break
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()

def test_dynamic_table_sorting():
    """Demonstrate handling dynamic table content (sorting)"""
    print("\n=== Dynamic Table Behavior (Sorting) ===")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")
    
    try:
        table = driver.find_element(By.ID, "table1")
        headers = table.find_elements(By.TAG_NAME, "th")
        
        print("Table headers (clickable for sorting):")
        for i, header in enumerate(headers):
            print(f"  {i}: {header.text}")
        
        # Click on Last Name header to sort ascending
        print("\n✓ Clicking 'Last Name' header to sort...")
        headers[1].click()
        time.sleep(1)
        
        # Check new first row
        rows = table.find_elements(By.TAG_NAME, "tr")
        first_row = rows[1].find_elements(By.TAG_NAME, "td")
        print(f"  After ascending sort, first row: {[c.text for c in first_row]}")
        
        # Click again to sort descending
        print("\n✓ Clicking 'Last Name' header again for reverse sort...")
        headers[1].click()
        time.sleep(1)
        
        rows = table.find_elements(By.TAG_NAME, "tr")
        first_row = rows[1].find_elements(By.TAG_NAME, "td")
        print(f"  After descending sort, first row: {[c.text for c in first_row]}")
        
        print("\n✓ Dynamic behavior (sorting) demonstrated!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()

def test_get_all_due_amounts():
    """Extract all Due amounts and compute total"""
    print("\n=== Extract All Due Amounts ===")
    print("-" * 50)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")
    
    try:
        table = driver.find_element(By.ID, "table1")
        rows = table.find_elements(By.TAG_NAME, "tr")
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        header_texts = [h.text for h in headers]
        
        # Find the Due column index
        due_col = header_texts.index("Due") if "Due" in header_texts else -1
        
        if due_col >= 0:
            print(f"Found '{header_texts[due_col]}' column at index {due_col}")
            
            total = 0.0
            amounts = []
            
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) > due_col:
                    amount_text = cells[due_col].text
                    # Store raw text for comparison
                    amounts.append(amount_text)
            
            print(f"  Due amounts: {amounts}")
            print(f"  Total records: {len(amounts)}")
            print("\n✓ All due amounts extracted successfully!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("=" * 60)
    print("EXPERIMENT 6: HANDLING DYNAMIC ELEMENTS - WEB TABLES")
    print("=" * 60)
    
    test_webtable_traversal()
    test_match_name_get_value()
    test_find_specific_row_details()
    test_get_all_due_amounts()
    test_dynamic_table_sorting()
    
    print("\n" + "=" * 60)
    print("✓ All web table experiments completed!")
```

## Sample Output

The following output is the output recorded with the experiment:

```text
EXPERIMENT 6: HANDLING DYNAMIC ELEMENTS - WEB TABLES
============================================================
Assignment 5: HTML Web Table Extractor
==================================================
✓ Found table1
✓ Total rows: 5
✓ Headers: ['Last Name', 'First Name', 'Email', 'Due', 'Web Site', 'Action']

--- Traversing Table ---
  Row 1: ['Smith', 'John', 'jsmith@gmail.com', '$50.00', 'http://www.jsmith.com', 'edit delete']
  Row 2: ['Bach', 'Frank', 'fbach@yahoo.com', '$51.00', 'http://www.frank.com', 'edit delete']
  Row 3: ['Doe', 'Jason', 'jdoe@hotmail.com', '$100.00', 'http://www.jdoe.com', 'edit delete']
  Row 4: ['Conway', 'Tim', 'tconway@earthlink.net', '$50.00', 'http://www.timconway.com', 'edit delete']

✓ Table traversal completed!
✓ Browser closed

=== THE WEB TABLE EXTRACTOR TASK ===
--------------------------------------------------
Table headers: ['Last Name', 'First Name', 'Email', 'Due', 'Web Site', 'Action']

Results:
--------------------------------------------------
  'Smith' → Due: $50.00
  'Bach' → Email: fbach@yahoo.com
  'Conway' → Web Site: http://www.timconway.com
  'Doe' → Due: $100.00
--------------------------------------------------

✓ Web Table Extractor task completed!
✓ Browser closed

=== Get Full Details of a Person ===
--------------------------------------------------

Found complete record for 'Bach':
  Last Name: Bach
  First Name: Frank
  Email: fbach@yahoo.com
  Due: $51.00
  Web Site: http://www.frank.com
  Action: edit delete

=== Extract All Due Amounts ===
--------------------------------------------------
Found 'Due' column at index 3
  Due amounts: ['$50.00', '$51.00', '$100.00', '$50.00']
  Total records: 4

✓ All due amounts extracted successfully!

=== Dynamic Table Behavior (Sorting) ===
--------------------------------------------------
Table headers (clickable for sorting):
  0: Last Name
  1: First Name
  2: Email
  3: Due
  4: Web Site
  5: Action

✓ Clicking 'Last Name' header to sort...
  After ascending sort, first row: ['Bach', 'Frank', 'fbach@yahoo.com', '$51.00', 'http://www.frank.com', 'edit delete']

✓ Clicking 'Last Name' header again for reverse sort...
  After descending sort, first row: ['Conway', 'Tim', 'tconway@earthlink.net', '$50.00', 'http://www.timconway.com', 'edit delete']

✓ Dynamic behavior (sorting) demonstrated!

============================================================
✓ All web table experiments completed!

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
