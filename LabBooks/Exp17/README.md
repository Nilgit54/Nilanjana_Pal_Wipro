# Experiment 17 – Selenium Page Object Model (POM) Framework

**Module:** Unit Test Frameworks – Page Object Model
**Student:** Nilanjana Pal

A Selenium-based test automation framework built using the **Page Object
Model (POM)** design pattern, tested against the SauceDemo
(https://www.saucedemo.com/) demo e-commerce site.

---

## Project Structure

```
exp17/
│
├── pages/                     # Page classes (locators + UI actions only)
│   ├── __init__.py
│   ├── pagebase.py            # BasePage - common Selenium utility methods
│   ├── loginpage.py           # LoginPage - login screen locators & actions
│   └── dashboard.py           # DashboardPage - inventory/cart locators & actions
│
├── tests/                     # Test classes (test logic only)
│   ├── __init__.py
│   ├── testloginpom.py        # Login page test cases
│   └── testdashboard_pom.py   # Dashboard/cart test cases
│
├── utils/                     # Reusable utility/helper classes
│   ├── __init__.py
│   ├── config.py              # Config reader (properties/JSON)
│   ├── csvread.py             # CSV test data reader
│   └── screenshots.py         # Screenshot capture utility
│
├── testdata/                  # (auto-generated) test data files
│   ├── config.properties
│   └── login_data.csv
│
├── reports/
│   └── screenshots/           # (auto-generated) captured screenshots
│
├── testrun.py                 # Main runner - executes the full test suite
└── README.md
```

> NOTE: `testrun.py` imports from `test.testloginpom` and
> `test.testdashboard`, but the folder is named `tests/` and the dashboard
> file is `testdashboard_pom.py`. Make sure your folder/module names and
> import statements match exactly (either rename the folder to `test/` and
> the file to `testdashboard.py`, or update the imports in `testrun.py`
> to `from tests.testloginpom import TestLoginPagePOM` and
> `from tests.testdashboard_pom import TestDashboardPagePOM`) - otherwise
> you'll get a `ModuleNotFoundError` when running.

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

From the project root (`exp17/`), simply run:

```bash
python testrun.py
```

This will:
1. Generate the config utility output (`testdata/config.properties`)
2. Generate the CSV test data file (`testdata/login_data.csv`)
3. Run the full POM test suite (Login tests + Dashboard tests)
4. Print a detailed summary of results to the console

### Run individual test files (optional)

```bash
python -m tests.testloginpom
python -m tests.testdashboard_pom
```

---

## What Gets Generated After Running

| File/Folder | Description |
|---|---|
| `testdata/config.properties` | Sample config file with base URL, browser, and credentials sections |
| `testdata/login_data.csv` | Sample login test data (valid, locked-out, problem, and invalid users) |
| `reports/screenshots/login_success_<timestamp>.png` | Screenshot captured automatically after a successful login test |

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

**Login Page Tests (`testloginpom.py`)** - 6 tests
- Login page loads correctly
- Valid login succeeds
- Invalid credentials show error message
- Locked-out user shows error message
- Empty fields show validation error
- Successful login redirects to `/inventory.html` (+ screenshot captured)

**Dashboard Page Tests (`testdashboard_pom.py`)** - 4 tests
- Dashboard loads after login with inventory items visible
- Add and remove an item from the cart
- Open the shopping cart page
- Add multiple items to the cart

**Total: 10 tests**

---

## Sample Output

```
======================================================================
RUNNING PAGE OBJECT MODEL (POM) TEST SUITE
======================================================================
Added TestLoginPagePOM (6 tests)
Added TestDashboardPagePOM (4 tests)
...
----------------------------------------------------------------------
Ran 10 tests in 79.872s

OK

======================================================================
TEST SUMMARY
======================================================================
Tests run: 10
Failures: 0
Errors: 0

ALL POM TESTS PASSED!
```

---

## Design Notes

- **`PageBase`** centralizes common Selenium logic (waits, clicks, JS-safe
  text entry for React inputs, navigation helpers) so page classes stay lean.
- **Page classes** (`LoginPage`, `DashboardPage`) contain only locators
  and UI interaction/verification methods, no assertions.
- **Test classes** contain only test logic and assertions, keeping
  Selenium/browser details fully abstracted away via the page objects.
- **Utilities** (`Config`, `CSVReader`, `Screenshot`) are reusable across
  any page/test class.