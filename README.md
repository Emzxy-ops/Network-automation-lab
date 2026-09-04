# 🌐 Network Automation Workstation & Lab

A dedicated local development and testing environment built to transition traditional network engineering workflows into code-driven, automated infrastructure management.

## 🚀 Project Overview
This repository serves as a sandbox for writing, testing, and executing network automation scripts. It bridges manual API testing with programmatic execution using Python.

---

## 🛠️ Workstation Stack & Tooling
- **Editor:** Visual Studio Code (VS Code)
- **Language:** Python 3.13+
- **API Testing:** REST Client (VS Code extension) for declarative, version-controlled HTTP requests.
- **Dependency Management:** Python Virtual Environments (`venv`) & `pip`.
- **Core Libraries:** `requests`

---

## 📂 Repository Structure

```text
Net_Auto_Lab/
│
├── venv/                   # Isolated local Python environment (Ignored by Git)
├── .gitignore              # Specifies intentionally untracked files to ignore
├── test.http               # Declarative REST Client requests for manual API validation
├── get_data.py             # Basic Python script demonstrating programmatic HTTP GET
└── test_connections.py     # Advanced script handling status codes, responses, & dictionary parsing
