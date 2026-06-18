# Factory Compliance Monitoring System

## Overview

This project presents a **Policy-Grounded AI System for Occupational Health & Safety Compliance Monitoring** developed as part of the Genesys AI Internship Assessment.

The system combines computer vision, policy parsing, severity assessment, and automated logging to detect workplace safety violations from factory surveillance images. It is designed to assist safety officers by identifying unsafe behaviors, mapping them to compliance policies, and maintaining a history of detected violations.

---

## Problem Statement

Industrial environments often rely on manual monitoring of safety compliance. Human observation can be inconsistent, time-consuming, and difficult to scale.

This project aims to automate compliance monitoring by:

* Detecting safe and unsafe workplace behaviors
* Mapping detections to policy-defined violations
* Assigning severity levels
* Maintaining a searchable violation history
* Providing an interactive dashboard for monitoring

---

## Key Features

### Policy Parsing & Rule Generation

* Extracts compliance information from a policy document
* Generates structured rules in JSON format
* Associates behaviors with severity levels and policy sections

### Computer Vision Detection

Classifies workplace activities into:

1. Safe Walkway Violation
2. Unauthorized Intervention
3. Opened Panel Cover
4. Carrying Overload with Forklift
5. Safe Walkway
6. Authorized Intervention
7. Closed Panel Cover
8. Safe Carrying

### Severity Assessment

Each detected behavior is mapped to:

* SAFE
* LOW
* MEDIUM
* HIGH
* CRITICAL

based on policy rules.

### Automated Logging

All detections are automatically stored in an SQLite database with:

* Timestamp
* Predicted Class
* Severity
* Policy Section
* Confidence Score
* Image Reference

### Interactive Dashboard

Built using Streamlit.

Features include:

* Image Upload
* Behavior Classification
* Confidence Score Display
* Policy Information Display
* Severity Visualization
* Violation Statistics
* Historical Violation Records

---

## System Architecture

Policy PDF
↓
Policy Parser
↓
Rule Generator
↓
rules.json
↓
Detection Model
↓
Severity Engine
↓
SQLite Database
↓
Streamlit Dashboard

---

## Dataset

The project uses a factory surveillance dataset containing:

* Safe behaviors
* Unsafe behaviors
* Forklift operations
* Walkway compliance scenarios
* Equipment intervention activities

The original dataset is not included in this repository due to storage limitations.

---

## Project Structure

```text
Genesys_AI_Assessment/

├── compliance_policy/
├── config/
├── database/
├── outputs/
├── src/
│   ├── dashboard/
│   ├── detection/
│   ├── policy_parser/
│   ├── reports/
│   └── severity/
├── README.md
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Hanzala095/Genesys_AI_Assessment.git
cd Genesys_AI_Assessment
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

```bash
streamlit run src/dashboard/app.py
```

The dashboard will open in your browser.

---

## Results

The system successfully:

* Parses compliance policies
* Generates policy-grounded rules
* Classifies workplace behaviors
* Assigns severity levels
* Logs violations automatically
* Displays monitoring information through a dashboard

---

## Screenshots

### Dashboard Home

See:

```text
docs/dashboard_home.png
```

### Prediction Example

See:

```text
docs/prediction_result.png
```

### Violation History

See:

```text
docs/database_history.png
```

---

## Future Improvements

* Real-time CCTV stream integration
* Object detection using YOLO
* Multi-camera monitoring
* Email/SMS alerts
* Advanced reporting and analytics
* Role-based access control

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Pandas
* SQLite
* Streamlit
* PyMuPDF

---

## Author

**Muhammad Hanzala Khan**

BS Artificial Intelligence
PAF-IAST Haripur

Developed for the Genesys AI Internship Assessment.
