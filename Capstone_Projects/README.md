E-Commerce Test Automation Capstone Project

An end-to-end automated testing framework designed for e-commerce web applications using Python and Selenium WebDriver. This framework features data generation, automated visual evidence capturing on key steps and failures, and automatic HTML report creation upon test execution.

📁 Project Structure

Capstone_Projects/
├── screenshots/             # Execution screenshots captured automatically during test runs
├── create_test_data.py      # Script to generate fresh input datasets (JSON & Excel)
├── ecommerce_automation.py  # Main execution suite (runs tests & auto-generates the HTML report)
├── execution_report.html    # Generated HTML execution report containing test results
├── report_generator.py      # Helper module for building and formatting HTML reports
├── requirements.txt         # Required Python dependencies
├── test_data.json           # Output JSON test dataset
└── test_data.xlsx           # Output Excel test dataset


🛠️ Prerequisites & Setup

Ensure you have Python and your preferred web driver (e.g., Microsoft Edge WebDriver or ChromeDriver) installed on your system.

Install all required dependencies:

pip install -r requirements.txt


⚙️ How to Run & View Project Components

1. View or Refresh Test Data (Optional)

To inspect or generate fresh test datasets (test_data.json and test_data.xlsx), run the test data generator script:

python create_test_data.py


2. Run the Automation Suite

To execute the e-commerce test cases, run the main automation script:

python ecommerce_automation.py


Note: Running ecommerce_automation.py automatically executes all UI interactions, captures visual evidence, and generates the execution_report.html file upon completion.

3. View the Execution Report

To inspect the test results and execution summary, simply open the generated HTML file in your web browser:

Double-click execution_report.html in your file explorer, or

Open execution_report.html directly inside your browser.

📸 Screenshots & Visual Evidence

Automatic Capture: Screenshots are captured automatically during execution for key workflow steps and any encountered assertion failures.

Storage Directory: All images are systematically saved inside the screenshots/ directory for visual verification and debugging.

📊 Core Features

Dynamic Data Generation: Generates multi-format test data files (.json and .xlsx) using create_test_data.py.

Automated HTML Reporting: Automatically outputs execution_report.html directly from the main test run.

Visual Audit Logs: Captures screenshots in the screenshots/ folder throughout the test lifecycle.