# 📚 FakeRestAPI Automation Project for Interview
Automated REST API tests for FakeRestAPI (Books and Authors endpoint).

## 🧰 Tech Stack
- Python + Pytest + Requests
- Allure for reporting with rich debug output implemented for better maintainability.
- Dockerized test execution
- GitHub Actions CI/CD implemented

## ✅ Test Coverage (20 Tests)
### This test suite has 20 test cases across Books and Authors APIs, covering:
- GET all books
- GET book by ID (valid/invalid)
- POST book (valid/missing fields/duplicate)
- PUT book (valid/invalid)
- DELETE book (valid/invalid)

## 🚀 Setup

### Prerequisites
- Python 3.11+
- Docker
- Allure Setup Notes:
  - Java must be installed to run Allure CLI.
  - utils/allure-2.35.1 contains the CLI.
  - Add the bin folder to your system PATH.

### 🔧 Clone the Repo
```bash
git clone https://github.com/miodrag-golubovikj/bookstore-api-tests.git
cd bookstore-api-tests

