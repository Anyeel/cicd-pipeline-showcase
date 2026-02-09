# CI/CD Pipeline Showcase 🚀

![Build Status](https://github.com/Anyeel/cicd-pipeline-showcase/actions/workflows/ci-cd.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.14-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Overview
This repository demonstrates a robust **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using **GitHub Actions**. The goal is to simulate a professional workflow that ensures code quality and reliability before merging.

## ⚙️ Workflow Architecture
The pipeline is defined in `.github/workflows/ci-cd.yml` and consists of two sequential stages:

1.  **Code Quality (Linting):** * Uses `flake8` to enforce PEP8 standards.
    * Prevents syntax errors and undefined names.
2.  **Unit Testing:**
    * Executes automated tests using `pytest`.
    * Dependent on the success of the linting stage to save resources.

## 🛠️ Tech Stack
* **CI/CD:** GitHub Actions
* **Language:** Python
* **Testing:** Pytest
* **Linting:** Flake8

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Anyeel/cicd-pipeline-showcase.git](https://github.com/Anyeel/cicd-pipeline-showcase.git)
Install dependencies:

```Bash
pip install -r requirements.txt
```
Run tests:

```Bash
pytest
```
