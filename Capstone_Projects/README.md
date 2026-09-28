# E-Commerce Test Automation Capstone Project

An end-to-end automated testing framework designed for an e-commerce web application using **Python and Selenium WebDriver**. The framework automates the complete customer shopping workflow, including login, product search, cart operations, test-data handling, screenshot capture, and HTML execution reporting.

---

## 📌 Capstone Assignment 1

### Automate a Web Application Using Selenium WebDriver with Python

### Business Scenario

A customer wants to purchase a product from an **E-Commerce website**.

The automation should:

1. Launch the browser
2. Login to the application
3. Search for a product
4. Add the product to the cart
5. Update the quantity
6. Verify cart details
7. Capture screenshots
8. Read test data from Excel/JSON
9. Handle popup/alerts if available
10. Generate an execution report

---

## 🌐 Application Used

For this capstone project, the **TutorialsNinja Demo E-Commerce Website** is used.

**Application:** TutorialsNinja Demo E-Commerce Website

**Application URL:**  
https://tutorialsninja.com/demo/

The website provides an e-commerce environment where products can be searched, added to the shopping cart, quantities can be updated, and cart information can be verified.

---

## 📁 Project Structure

```text
Capstone_Projects/
│
├── screenshots/
│   └── # Execution screenshots captured automatically during test runs
│
├── create_test_data.py
│   └── # Generates fresh test data in JSON and Excel formats
│
├── ecommerce_automation.py
│   └── # Main Selenium automation suite
│
├── execution_report.html
│   └── # Generated HTML execution report
│
├── report_generator.py
│   └── # Helper module for generating and formatting HTML reports
│
├── requirements.txt
│   └── # Required Python dependencies
│
├── test_data.json
│   └── # Generated JSON test dataset
│
└── test_data.xlsx
    └── # Generated Excel test dataset
```

---

## 🛠️ Prerequisites

Before running the project, make sure the following are installed:

- Python 3.x
- Google Chrome or Microsoft Edge
- Compatible ChromeDriver/EdgeDriver
- Selenium WebDriver
- Microsoft Excel support through `openpyxl`
- Any Python IDE such as VS Code, PyCharm, or IDLE

---

## 📦 Installation

Clone or download the project and navigate to the project directory.

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not being used, the main dependencies can be installed using:

```bash
pip install selenium openpyxl
```

---

## ⚙️ How to Run the Project

### 1. Generate Test Data

The project supports test data in both **JSON** and **Excel** formats.

To generate or refresh the test data files, run:

```bash
python create_test_data.py
```

This generates:

```text
test_data.json
test_data.xlsx
```

These files can then be used by the automation script as input test data.

---

### 2. Run the Automation Suite

Execute the main automation script:

```bash
python ecommerce_automation.py
```

The script automatically:

- Launches the browser
- Opens the TutorialsNinja website
- Performs the required e-commerce operations
- Reads the required test data
- Searches for products
- Adds products to the cart
- Updates cart quantity
- Verifies cart information
- Captures screenshots
- Handles available popups/alerts
- Generates the HTML execution report

---

### 3. View the Execution Report

After execution, the following file is generated:

```text
execution_report.html
```

Open the file directly in a web browser.

You can either:

- Double-click `execution_report.html`
- Right-click → **Open with Browser**
- Open the file manually in Chrome/Edge

The report contains the execution results and test-status information.

---

## 🧪 Automated Test Workflow

The automation follows an end-to-end customer purchase workflow.

### Step 1 — Launch Browser

The Selenium WebDriver launches the selected browser and opens the TutorialsNinja Demo website.

```text
Browser
   ↓
TutorialsNinja Demo Website
```

### Step 2 — Login

The automation enters the required login credentials and logs into the application.

```text
Login Page
   ↓
Enter Username
   ↓
Enter Password
   ↓
Click Login
```

### Step 3 — Search Product

The automation searches for the required product using the website's search functionality.

```text
Search Box
   ↓
Enter Product
   ↓
Search
   ↓
Search Results
```

### Step 4 — Add Product to Cart

The selected product is added to the shopping cart.

```text
Product
   ↓
Add to Cart
   ↓
Shopping Cart
```

### Step 5 — Update Quantity

The automation updates the quantity of the selected product in the shopping cart.

```text
Cart
   ↓
Select Quantity
   ↓
Update Cart
```

### Step 6 — Verify Cart Details

The automation verifies important cart information such as:

- Product name
- Quantity
- Price
- Total
- Cart contents

### Step 7 — Capture Screenshots

Screenshots are captured during important workflow steps and when failures occur.

The screenshots provide visual evidence of the automation execution.

### Step 8 — Read Test Data

Test data is generated and stored in:

```text
test_data.json
test_data.xlsx
```

The automation can use these files as input data for the test scenarios.

### Step 9 — Handle Popup/Alerts

Where applicable, Selenium handles browser alerts or application popups encountered during execution.

### Step 10 — Generate Execution Report

After the automation completes, an HTML execution report is generated automatically.

```text
ecommerce_automation.py
        ↓
Test Execution
        ↓
Screenshots
        ↓
Execution Results
        ↓
execution_report.html
```

---

## 📸 Screenshots & Visual Evidence

The framework automatically captures screenshots during execution.

Screenshots are stored in:

```text
screenshots/
```

Screenshots can be used for:

- Successful test-step verification
- Failure analysis
- Debugging
- Visual evidence of test execution

Example:

```text
screenshots/
├── login.png
├── product_search.png
├── add_to_cart.png
├── cart_verification.png
└── failure.png
```

The exact filenames depend on the implementation and execution timestamp.

---

## 📊 Test Data Management

The project supports two test-data formats.

### JSON

Test data is stored in:

```text
test_data.json
```

JSON provides a lightweight and structured format for storing test inputs.

### Excel

Test data is stored in:

```text
test_data.xlsx
```

Excel data is handled using the `openpyxl` library.

This allows test cases to be executed using externally maintained test data rather than hard-coded values.

---

## 📋 Main Project Components

### `create_test_data.py`

Responsible for generating test datasets.

It creates:

```text
test_data.json
test_data.xlsx
```

### `ecommerce_automation.py`

This is the **main automation script**.

It is responsible for:

- Starting Selenium WebDriver
- Navigating to TutorialsNinja
- Performing customer actions
- Reading test data
- Performing cart operations
- Validating results
- Capturing screenshots
- Generating the execution report

Run using:

```bash
python ecommerce_automation.py
```

### `report_generator.py`

This module is responsible for creating and formatting the HTML execution report.

The generated report is:

```text
execution_report.html
```

### `requirements.txt`

Contains the Python packages required to execute the project.

Install them using:

```bash
pip install -r requirements.txt
```

### `test_data.json`

Contains generated test data in JSON format.

### `test_data.xlsx`

Contains generated test data in Excel format.

### `screenshots/`

Stores screenshots generated during test execution.

### `execution_report.html`

Contains the final HTML execution report showing the results of the automation execution.

---

## 🔄 Overall Execution Flow

```text
                START
                  │
                  ▼
          Launch Browser
                  │
                  ▼
       Open TutorialsNinja
                  │
                  ▼
               Login
                  │
                  ▼
          Search Product
                  │
                  ▼
          Select Product
                  │
                  ▼
          Add to Cart
                  │
                  ▼
        Update Quantity
                  │
                  ▼
        Verify Cart Details
                  │
                  ▼
        Capture Screenshots
                  │
                  ▼
       Handle Alerts/Popups
                  │
                  ▼
       Generate HTML Report
                  │
                  ▼
                 END
```

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation programming language |
| Selenium WebDriver | Browser automation |
| TutorialsNinja | Demo e-commerce application |
| JSON | Test-data storage |
| Excel | Test-data storage |
| OpenPyXL | Excel file handling |
| HTML | Execution report |
| Chrome/Edge | Web browser |

---

## ⭐ Core Features

### Dynamic Test Data Generation

The framework generates test data in both:

- JSON
- Excel

formats.

### Selenium Web Automation

The framework uses Selenium WebDriver to automate the customer shopping workflow.

### Screenshot Capture

Screenshots provide visual evidence of important execution steps and failures.

### HTML Reporting

An HTML report is automatically generated after execution.

### Data-Driven Testing

External JSON and Excel files allow test data to be separated from the automation code.

### End-to-End Testing

The framework automates the complete flow from launching the website through cart verification.

---

## ▶️ Quick Start

For a fresh execution, use:

```bash
pip install -r requirements.txt
```

Then generate the test data:

```bash
python create_test_data.py
```

Finally, execute the automation:

```bash
python ecommerce_automation.py
```

After execution, check:

```text
screenshots/
execution_report.html
```

for visual evidence and execution results.

---

## 📌 Expected Output

A successful execution should produce:

```text
Capstone_Projects/
│
├── screenshots/
│   ├── <execution screenshots>
│   └── <failure screenshots if any>
│
├── execution_report.html
├── test_data.json
└── test_data.xlsx
```

The HTML report should contain the execution status and relevant test information.

---

## 🎯 Assignment Requirements Coverage

| Assignment Requirement | Implementation |
|---|---|
| Launch browser | Selenium WebDriver |
| Login | Automated login workflow |
| Search product | TutorialsNinja search functionality |
| Add product to cart | Automated Add to Cart |
| Update quantity | Cart quantity update |
| Verify cart details | Cart validation |
| Capture screenshots | `screenshots/` directory |
| Read test data | JSON and Excel |
| Handle popup/alerts | Selenium alert/popup handling where applicable |
| Generate execution report | `execution_report.html` |

---

## 🏁 Conclusion

This project demonstrates an end-to-end **E-Commerce Test Automation Framework using Python and Selenium WebDriver**.

The framework automates the major customer shopping operations on the **TutorialsNinja Demo E-Commerce Website**, while also demonstrating:

- Web browser automation
- Data-driven testing
- JSON and Excel test-data handling
- Screenshot-based visual evidence
- Popup/alert handling
- Automated HTML reporting
- End-to-end test execution

**Application Used:** TutorialsNinja Demo E-Commerce Website  
**URL:** https://tutorialsninja.com/demo/

---

## 👩‍💻 Project

**Capstone Assignment 1 — Automate a Web Application Using Selenium WebDriver with Python**

**Domain:** E-Commerce

**Automation Tool:** Selenium WebDriver

**Programming Language:** Python

**Application:** TutorialsNinja Demo E-Commerce Website


[Watch Demo Video](https://drive.google.com/file/d/15QL-lVAlaBHaDs8s9c9VAfh9EZ7azlX4/view?usp=sharing)