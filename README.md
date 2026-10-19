# Enterprise UI Automation Framework – Books to Scrape

A UI automation framework built with Python, Playwright, and Pytest to validate website functionality, featuring reusable page objects, HTML and Allure reporting, Docker, and GitHub Actions CI/CD.

## 1. Project Overview

Automates functional validation of [Books to Scrape](https://books.toscrape.com/index.html) and login-related behavior on [Quotes to Scrape](https://quotes.toscrape.com/).

## 2. Features

- Homepage and heading validation
- Random book navigation and data consistency checks
- Broken link validation
- Product image and pagination validation
- Login and logout-link validation
- Reusable Page Object Model (POM)
- HTML and Allure reports
- Docker containerization and GitHub Actions CI/CD

## 3. Tech Stack

Python 3.12, Playwright, Pytest, pytest-playwright, pytest-html, Allure, Chromium, Docker, and GitHub Actions.

## 4. Installation Guide

Clone the repository:

```bash
git clone https://github.com/akms-limon/Enterprise-UI-Automation-Framework
cd Enterprise-UI-Automation-Framework
```

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

For Linux browser dependencies, if needed:

```bash
python -m playwright install --with-deps chromium
```

## 5. Environment Setup

The `pytest.ini` configuration sets the test directory, naming conventions, and default Chromium browser. Python dependencies are listed in `requirements.txt`. Java and the Allure CLI are required to generate and open Allure HTML reports.

## 6. Running Tests

Run all tests:

```bash
python -m pytest
```

Run a specific test:

```bash
python -m pytest tests/test_homepage.py
```

Run with a visible browser:

```bash
python -m pytest --headed --slowmo 1000
```

## 7. Project Structure

```text
├── .github/
│   └── workflows/
│       └── playwright.yml
├── tests/
│   ├── __init__.py
│   ├── pages/
│   │   ├── home_page.py
│   │   ├── book_details_page.py
│   │   └── login_page.py
│   ├── test_homepage.py
│   ├── test_book_navigation.py
│   ├── test_book_details_consistency.py
│   ├── test_broken_links.py
│   ├── test_image_validation.py
│   └── test_login.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 8. Test Case Coverage

| Test Case | Validation |
|---|---|
| Homepage | URL, title, headings, and book listing |
| Random Book Navigation | Five randomly selected books, details page, title, and book information |
| Data Consistency | Homepage and details-page titles and prices for five random books |
| Broken Links | Unique hyperlinks and HTTP response statuses |
| Images and Pagination | Image visibility, `src`, `alt`, `thumbnail` class, and up to five pages |
| Login and Logout | Login-page navigation, form submission, logout action, and verification of the logged-out state |

## 9. Report Generation Guide

The framework supports local and GitHub Actions reporting.

### HTML Report Guide

```bash
mkdir -p reports
python -m pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser.

### Allure Report Guide

Generate test results and the HTML report:

```bash
python -m pytest --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```

`allure-results/` stores raw results, while `allure-report/` contains the generated HTML report.

#### Live Allure Report

View the latest published Allure report:

[https://akms-limon.github.io/Enterprise-UI-Automation-Framework/](https://akms-limon.github.io/Enterprise-UI-Automation-Framework/)

GitHub Actions automatically publishes the report after a successful test run on the `main` branch.

## 10. Docker Setup and Execution

Build the image:

```bash
docker build -t ui-automation-framework .
```

Run tests and preserve report files on the host:

```bash
mkdir -p reports allure-results

docker run --rm \
  -v "$(pwd)/reports:/app/reports" \
  -v "$(pwd)/allure-results:/app/allure-results" \
  ui-automation-framework
```

Generate the Allure HTML report afterward using the commands in the Allure section.

## 11. GitHub Actions Setup

Workflow: `.github/workflows/playwright.yml`

The workflow runs tests on pushes and pull requests. On a successful
push to `main`, it generates the Allure HTML report and publishes it
to GitHub Pages. Test reports are also uploaded as workflow artifacts.

View workflow logs in the **Actions** tab and download the
`test-reports` artifact when needed.

## 12. Design Decisions

- **POM:** Separates page-specific locators and interactions from test logic.
- **DRY and reusability:** Reuses page objects and fixtures.
- **Reliable synchronization:** Uses Playwright's automatic waiting and assertions instead of hardcoded waits.
- **CI/CD:** Automates test execution and report collection.
- **Docker:** Provides a consistent test environment.

## 13. Known Limitations

- Tests depend on external website and network availability.
- Random selection can vary between runs.
- Image and pagination validation covers a maximum of five pages.
- External link checks can be affected by redirects and temporary network failures.
- Quotes to Scrape is a demo site; its login test is not a production security test.
- Docker and Allure CLI require their respective runtime dependencies.