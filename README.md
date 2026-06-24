# SauceDemo Micro-Frontend Test Automation Suite
![CI](https://github.com/Pan-Pankracy/pw-py-petproject/actions/workflows/python-tests.yml/badge.svg)

A professional, standalone test automation framework custom-engineered in Python to validate security gates, authentication handshakes, and user interface state continuity on the SauceDemo e-commerce platform.

This suite leverages **Playwright** for high-performance browser automation, **pytest** as the core test runner, and integrates advanced capabilities like concurrent multi-threaded execution and dynamic runtime configuration.

---

## 🚀 Key Architectural Features

* **Page Object Model (POM):** Complete decoupling of test logic from the application DOM, abstracting UI elements into reusable class properties.
* **Parallel Execution Topology:** Configured via `pytest-xdist` to run asynchronous browser instances concurrently across up to 3 worker threads, drastically reducing execution time.
* **Decoupled Configuration Matrix:** Environment variables (URLs, credentials) are externalized using a `.env` schema and injected dynamically through global `pytest` fixtures.
* **Automated Telemetry & Tracing:** Out-of-the-box configuration to record and serialize complete system state traces (`retain-on-failure`) for rapid debugging of pipeline drops.

---

## 📂 Project Structure

```text
pw_py_petproject/
│
├── pages/
│   ├── __init__.py
│   └── login_page.py          # POM abstraction for authentication components
│
├── tests/
│   ├── __init__.py
│   └── test_login.py          # High-fidelity test scenarios and validation steps
│
├── .env                       # Local environment configuration matrix (ignored from Git)
├── conftest.py                # Global fixtures, lifecycle interception, and telemetry hooks
├── pytest.ini                 # Master runtime options and execution topology configuration
└── requirements.txt           # Project dependencies and explicit package versions

```

---

## 🛠️ Installation & Setup Instructions

Follow these exact terminal commands sequentially to initialize your environment and execute the test suite locally.

### 1. Navigate to the Project Root

Open your terminal and navigate to the directory containing the project:

```bash
cd qa-automation-boilerplate

```

### 2. Establish an Isolated Virtual Environment

Create a dedicated virtual environment to prevent package version conflicts on your local operating system:

```bash
# Create the virtual environment named 'venv'
python -m venv venv

# Activate on macOS / Linux:
source venv/bin/activate

# Activate on Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Activate on Windows (Command Prompt):
.\venv\Scripts\activate.bat

```

### 3. Install Core Framework Dependencies

Upgrade the package manager and install all explicit dependency versions listed in the project manifest:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Provision Playwright Browser Binaries

Download and initialize the underlying sandbox browser binaries needed for execution:

```bash
playwright install chromium

```

### 5. Configure the Local Environment Matrix

Create a file named `.env` in the root of your directory and populate it with the following configuration variables:

```env
BASE_URL=[https://www.saucedemo.com](https://www.saucedemo.com)
TEST_USER=standard_user
TEST_PASSWORD=secret_sauce

```

---

## 🏁 Running the Test Suite

The test runner configuration is managed entirely by the `pytest.ini` core file, meaning execution parameters remain clean, highly streamlined, and automated.

### Standard Test Execution

Run all tests concurrently in headed mode (3 workers) as specified in `pytest.ini`:

```bash
pytest

```

### Run a Specific Test Module

Isolate execution to a single designated test file:

```bash
pytest tests/test_login.py

```

### Headless Execution Override

To run the tests invisibly (ideal for background execution or CI/CD pipelines), override the default ini settings:

```bash
pytest --headless

```

---

## 📊 Test Artifacts & Debugging

If a test scenario fails, the framework automatically records and serializes a compressed trace file according to your `retain-on-failure` configuration. You can inspect the step-by-step UI actions, network logs, and console states using the native Playwright Inspector:

```bash
playwright show-trace test-results/path-to-your-failed-test/trace.zip