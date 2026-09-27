# Nilanjana_Pal_Wipro

This repository contains all lab work, capstone projects, and course
certificates completed as part of the **Selenium / Unit Test Frameworks**
training program.

It is organized into three main areas: 18 hands-on lab exercises, an
end-to-end e-commerce automation capstone project, and course
completion certificates.

---

## Repository Structure

```
Nilanjana_Pal_Wipro/
│
├── LabBooks/                          # Lab assignments (18 experiments)
│   ├── Exp1/  ├── Exp7/   ├── Exp13/
│   ├── Exp2/  ├── Exp8/   ├── Exp14/
│   ├── Exp3/  ├── Exp9/   ├── Exp15/
│   ├── Exp4/  ├── Exp10/  ├── Exp16/
│   ├── Exp5/  ├── Exp11/  ├── Exp17/
│   └── Exp6/  └── Exp12/  └── Exp18/
│
├── Capstone_Projects/                 # End-to-end e-commerce automation project
│   ├── __pycache__/                   # (auto-generated) Python bytecode cache
│   ├── screenshots/                   # (auto-generated) test execution screenshots
│   ├── create_test_data.py            # Generates test data (JSON/XLSX)
│   ├── ecommerce_automation.py        # Main Selenium automation script
│   ├── report_generator.py            # Generates the HTML execution report
│   ├── execution_report.html          # (auto-generated) test execution report
│   ├── test_data.json                 # Test data in JSON format
│   ├── test_data.xlsx                 # Test data in Excel format
│   ├── requirements.txt               # Python dependencies for this project
│   └── README.md                      # Capstone project-specific documentation
│
├── Certificates/                      # Course completion certificates
│   ├── .gitkeep
│   ├── Python_for_Automation.pdf
│   ├── Selenium_WebDriver_with_Python.pdf
│   ├── Test_Automation_with_Playwright_(Python)_&_Robot.pdf
│   └── README.md
│
└── README.md                          # This file
```

---

## About This Repository

| Folder | Description |
|---|---|
| **LabBooks** | 18 individual lab exercises (`Exp1` through `Exp18`) covering core testing concepts — `unittest` basics, assertions, fixtures, Selenium locators, waits, and Page Object Model framework building blocks. |
| **Capstone_Projects** | An integrated, end-to-end e-commerce test automation project combining Selenium automation, data-driven testing (JSON/XLSX), screenshot capture, and an auto-generated HTML execution report. |
| **Certificates** | Certificates of completion for the Python, Selenium, and Playwright/Robot Framework automation courses undertaken as part of this training. |

---

## Tech Stack

- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **Test Framework:** `unittest`
- **Design Pattern:** Page Object Model (POM)
- **Browser:** Google Chrome (via Selenium Manager / ChromeDriver)
- **Data-driven testing:** JSON, XLSX, and CSV test data
- **Reporting:** Auto-generated HTML execution reports + screenshots

---

## Getting Started

Install common dependencies (used across most experiments):

```bash
pip install selenium
```

For the capstone project specifically, install its dependencies from the
project's own requirements file:

```bash
cd Capstone_Projects
pip install -r requirements.txt
```

Each `LabBooks/ExpN` folder and the `Capstone_Projects` folder contains
its own scripts and, where applicable, its own dedicated `README.md`
with setup and run instructions specific to that project. Navigate into
the relevant folder and follow its README to run that particular test
suite.

---

## How to Navigate

1. **Looking for a specific concept or exercise?** → Check `LabBooks/Exp1` through `LabBooks/Exp18`, in numerical order.
2. **Looking for a complete, real-world framework example?** → Check `Capstone_Projects/`, a self-contained, runnable e-commerce automation project with data-driven testing, screenshots, and HTML reporting.
3. **Looking for proof of course completion?** → Check `Certificates/`.

---

## Author

**Nilanjana Pal**
Unit Test Frameworks – Selenium / Page Object Model training

---

## License

This repository is intended for educational and portfolio purposes.