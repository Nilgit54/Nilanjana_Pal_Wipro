# Experiment 18 – Data-Driven POM Framework with Screenshots

**Module:** Unit Test Frameworks – Page Object Model
**Student:** Nilanjana Pal

A Selenium-based test automation framework extending the **Page Object
Model (POM)** pattern with **data-driven testing** (CSV-based test data)
and **automatic screenshot capture** on both success and failure, tested
against the SauceDemo (https://www.saucedemo.com/) demo e-commerce site.

---

## Project Structure

```
exp18/
│
├── pages/                     # Page classes (locators + UI actions only)
│   ├── __init__.py
│   ├── basepage.py             # BasePage - common Selenium utility methods
│   ├── login.py                 # LoginPage - login screen locators & actions
│   └── dashboard.py             # DashboardPage - inventory/cart locators & actions
│
├── utils/                      # Reusable utility/helper classes
│   ├── __init__.py
│   ├── config.py                # Config reader (properties/JSON)
│   ├── csvread.py               # CSV test data reader/generator
│   └── screenshots.py           # Screenshot capture utility (pass/fail)
│
├── testdata/                   # (auto-generated) test data files
│   └── login_data.csv
│
├── reports/
│   └── screenshots/            # (auto-generated) PASS_/FAIL_ prefixed screenshots
│
├── testdatadriven.py           # Main test runner - data-driven POM test suite
└── README.md
```

---

## Prerequisites

- Python 3.8+
- Google Chrome browser installed
- ChromeDriver matching your Chrome version (or let Selenium Manager handle it automatically with Selenium 4.6+)

Install dependencies:

```bash
pip install selenium
```

---

## How to Run

From the project root (`exp18/`), simply run:

```bash
python testdatadriven.py
```

This will:
1. Auto-generate the CSV test data file (`testdata/login_data.csv`) if it doesn't already exist
2. Run the full data-driven POM test suite (5 tests)
3. Capture a `PASS_` or `FAIL_` prefixed screenshot for each relevant test into `reports/screenshots/`
4. Print a detailed summary of results to the console

---

## What Gets Generated After Running

| File/Folder | Description |
|---|---|
| `testdata/login_data.csv` | Data-driven login test cases (valid, locked-out, problem, and invalid users) |
| `reports/screenshots/PASS_DDT_success_<username>_<timestamp>.png` | Screenshot for each successful data-driven login case |
| `reports/screenshots/PASS_DDT_locked_<username>_<timestamp>.png` | Screenshot for the locked-out user case |
| `reports/screenshots/PASS_DDT_error_<username>_<timestamp>.png` | Screenshot for the invalid credentials case |
| `reports/screenshots/PASS_login_success_demo_<timestamp>.png` | Screenshot from the standalone login-success test |
| `reports/screenshots/PASS_complete_flow_<timestamp>.png` | Screenshot from the full login → dashboard → cart flow |
| `reports/screenshots/FAIL_simulated_failure_<timestamp>.png` | Screenshot captured when a missing element exception is simulated |

Example generated `testdata/login_data.csv`:

```csv
username,password,expected
standard_user,secret_sauce,success
locked_out_user,secret_sauce,locked_out
problem_user,secret_sauce,success
wrong_user,wrong_pass,error_message
```

---

## Test Coverage

**`DataDrivenPOMFramework` (`testdatadriven.py`)** – 5 tests

1. **`test_data_driven_from_csv`** – Iterates through every row of `login_data.csv` using `subTest`, logging in with each username/password pair and asserting the expected outcome (success / locked out / error message), with a screenshot captured per case.
2. **`test_all_csv_cases_pass_condition`** – Validates that every CSV row's `expected` value is one of the recognized outcomes (`success`, `locked_out`, `error_message`).
3. **`test_screenshot_on_success`** – Logs in with valid credentials and captures a `PASS_` screenshot to demonstrate success-path screenshot capture.
4. **`test_screenshot_on_missing_element`** – Intentionally looks up a non-existent element to trigger a `NoSuchElementException`, captures a `FAIL_` screenshot, and asserts the screenshot file was actually created.
5. **`test_complete_pom_flow`** – End-to-end flow: login → dashboard loads → add two items to cart → open cart page → screenshot of the completed flow.

**Total: 5 tests**

---

## Sample Output

```
test_all_csv_cases_pass_condition (__main__.DataDrivenPOMFramework.test_all_csv_cases_pass_condition)
Verify each CSV case passes its expected condition ... ✓ All 4 CSV test cases validated
ok
test_complete_pom_flow (__main__.DataDrivenPOMFramework.test_complete_pom_flow)
Complete login → dashboard → cart flow using POM ... 
Complete POM Flow:
----------------------------------------
  ✓ Step 1: Login successful
  ✓ Step 2: Dashboard loaded with 6 items
  ✓ Step 3: 2 items in cart
  ✓ Step 4: Cart page opened
  ✓ Screenshot saved: reports/screenshots\PASS_complete_flow_20260926_075538.png
ok
test_data_driven_from_csv (__main__.DataDrivenPOMFramework.test_data_driven_from_csv)
Test login combinations from CSV test data ... 
Running 4 CSV test cases:
----------------------------------------
  [PASS] standard_user - login succeeded
  [PASS] locked_out_user - locked out error shown
  [PASS] problem_user - login succeeded
  [PASS] wrong_user - error shown correctly
ok
test_screenshot_on_missing_element (__main__.DataDrivenPOMFramework.test_screenshot_on_missing_element)
Demonstrate exception handling and screenshot on failure ... ✗ Simulated failure captured: reports/screenshots\FAIL_simulated_failure_20260926_075556.png
  Error: NoSuchElementException: Message: no such element: Unable to locate element
ok
test_screenshot_on_success (__main__.DataDrivenPOMFramework.test_screenshot_on_success)
Demonstrate screenshot capture on successful test ... ✓ Success screenshot: reports/screenshots\PASS_login_success_demo_20260926_075601.png
ok

----------------------------------------------------------------------
Ran 5 tests in 34.315s

OK
```

---

## Design Notes

- **`BasePage`** centralizes common Selenium logic (waits, clicks, JS-safe
  text entry for React inputs, navigation helpers) so page classes stay lean.
- **Page classes** (`LoginPage`, `DashboardPage`) contain only locators
  and UI interaction/verification methods, no assertions. `LoginPage`
  additionally waits for either navigation to the inventory page or an
  error message to appear before proceeding, making login more reliable.
- **`CSVReader`** both generates a sample `login_data.csv` (if missing)
  and reads it back as a list of dictionaries, driving the data-driven
  test cases.
- **`Screenshot`** provides `capture_success` / `capture_failure` helpers
  that automatically prefix filenames with `PASS_` or `FAIL_` and
  timestamp them, keeping the `reports/screenshots/` folder organized.
- **`test_screenshot_on_missing_element`** demonstrates how to catch a
  Selenium exception, capture evidence via screenshot, and still assert
  the screenshot file was written — a pattern useful for real failure
  diagnostics in CI pipelines.
- Test classes contain only test logic and assertions, keeping
  Selenium/browser details fully abstracted away via the page objects.