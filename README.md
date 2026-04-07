# AI-Powered Smart EDA Web App

### Automated Exploratory Data Analysis with LLM-Driven Insights

---

## Overview

This project is an intelligent **AI-powered data analysis web application** built using Streamlit. It allows users to upload any CSV dataset and instantly perform **automated Exploratory Data Analysis (EDA)** along with **AI-generated insights**.

Unlike traditional EDA tools, this system combines **deterministic data processing pipelines** with **LLM-based interpretation**, ensuring both accuracy and meaningful analysis.

---

## Key Features

* Upload any CSV dataset dynamically
* Automatic data cleaning & datatype detection (numeric, categorical, datetime)
* Smart visualization pipeline:
  * Distribution plots
  * Count plots
  * Boxplots
  * Correlation heatmap
* Handles real-world data issues (missing values, mixed datatypes)
* AI-generated insights using LLM (no hardcoded analysis)
* Fast and interactive UI built with Streamlit
* Compact and structured dashboard layout

---

## Architecture

This project follows a **hybrid AI + deterministic system design**:

* **Data Layer:** Pandas-based preprocessing and schema detection
* **Visualization Layer:** Matplotlib & Seaborn for structured EDA
* **AI Layer:** LLM agent for generating human-like insights
* **Interface:** Streamlit web application

This ensures: Reliable computations
              Meaningful insights
              Scalable architecture

---

## Tech Stack

* **Language:** Python
* **Frontend/UI:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **AI Integration:** OpenAI API / LLM-based agent
* **Version Control:** Git & GitHub

---

## Project Structure

```bash
AI-Data-Analyst-Smart-EDA/
│── app.py
│── requirements.txt
│── README.md
│── agents/
│     ├── analyst_agent.py
│     └── coder_agent.py
│── utils/
│     └── schema_extractor.py
│── data/
│── Results/
```

---

## Getting Started

### 1) Clone the Repository

```bash
git clone https://github.com/mansityagi0606-lab/AI-Data-Analyst-Smart-EDA-.git
cd AI-Data-Analyst-Smart-EDA-
```

---

### 2) Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3) Run the Application

```bash
streamlit run app.py
```

---

## 4)Application Preview
<img width="742" height="556" alt="screenshot1" src="https://github.com/user-attachments/assets/3e06b35c-156b-4e75-8e17-e173885f5423" />

<img width="715" height="603" alt="screenshot6" src="https://github.com/user-attachments/assets/5abcd6a6-718c-4409-9a46-3e27201dabe1" />

## Use Cases

* Quick dataset understanding for data scientists
* Academic and research data exploration
* Business analytics prototyping
* Automated reporting workflows
* AI-assisted data interpretation

---

