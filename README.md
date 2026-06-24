# AI-Code-reviewer
frontend - https://ai-code-reviewer-meet.streamlit.app/
backend -  https://ai-code-reviewer-gscg.onrender.com/


AI Code Reviewer is a Python-based code analysis application that automatically reviews Python code for **syntax issues, complexity, possible bugs, security vulnerabilities, and code quality**.  
It combines **static code analysis**, **machine learning**, and a **web-based interface** to provide instant code review feedback.

The project is built with:

- **FastAPI** for the backend API
- **Streamlit** for the frontend UI
- **Radon** for complexity analysis
- **Bandit** for security scanning
- **Scikit-learn** for bug prediction
- **Joblib** for loading the trained ML model

---

# Features

## 1) Syntax Checking
Checks whether the submitted Python code contains any syntax errors.

## 2) Complexity Analysis
Analyzes code complexity using **Radon** and reports cyclomatic complexity for functions.

## 3) Bug Prediction
Uses a trained machine learning model to identify whether the code may contain style or logic issues.

## 4) Security Scanning
Uses **Bandit** to scan the code for potential security vulnerabilities.

## 5) Code Quality Score
Generates an overall score out of **100** based on multiple quality indicators.

## 6) Suggestions for Improvement
Provides suggestions to improve:
- readability
- maintainability
- code quality
- security practices

---

# Project Overview

This project allows users to paste Python code into a web interface and receive a structured review report.

The system performs multiple layers of analysis:

1. **Syntax check**
2. **Cyclomatic complexity analysis**
3. **Bug prediction using ML**
4. **Security scanning using Bandit**
5. **Suggestions generation**
6. **Code quality scoring**

---

# Project Structure

```bash
AI-Code-reviewer/
│
├── backend/
│   ├── __init__.py
│   ├── main.py                     # FastAPI backend API
│   ├── analyzer.py                 # Core code review logic
│   ├── ml_model.py                 # ML model training script (if stored here)
│   └── models/
│       ├── bug_classifier.pkl      # Trained ML classifier
│       └── vectorizer.pkl          # Saved vectorizer
│
├── app.py                          # Streamlit frontend
├── requirements.txt               # Python dependencies
└── README.md
