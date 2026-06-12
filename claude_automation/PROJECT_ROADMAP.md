# 🛡️ Cyber Risk to Value: Analytical Roadmap

## 📌 Project Overview
The goal of this project is to quantify the relationship between cyber security incidents and their resulting financial and market value impacts. By moving from descriptive statistics to predictive modeling, we aim to turn raw incident data into actionable risk intelligence.

---

## 🎯 1. Project Objectives

### Objective 1: Descriptive Statistics (The "What")
**Goal:** Establish a baseline understanding of the datasets.
*   **Data Profiling:** Analyze the distribution of key metrics (e.g., `total_loss_usd`, `downtime_hours`, `abnormal_return_1d`).
*   **Quality Audit:** Identify missing data patterns and outliers that could skew results.
*   **Frequency Analysis:** Determine the most common attack vectors and the most targeted industries.

### Objective 2: Comparative Analysis (The "Why")
**Goal:** Discover correlations and dependencies across different dimensions of risk.
*   **Cross-Dataset Integration:** Merge financial, operational, and market data into a single analytical frame.
*   **Segment Analysis:** Compare losses and recovery times across different sectors (e.g., Finance vs. Tech).
*   **Causality Exploration:** Analyze if "Operational Severity" (downtime/records lost) directly correlates with "Market Severity" (stock drop).

### Objective 3: Prediction Modelling (The "What Next")
**Goal:** Build a machine learning model to estimate the impact of a future breach.
*   **Feature Engineering:** Convert raw data (like `attack_vector`) into mathematical features the model can understand.
*   **Regression Modelling:** Develop models to predict `total_loss_usd` and `days_to_price_recovery`.
*   **Validation:** Test the model on "unseen" data to determine its accuracy and reliability.

---

## 🗺️ 2. The Roadmap

| Phase | Stage | Key Activities | Deliverable |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **Data Exploration** | Load CSVs $\rightarrow$ Basic stats $\rightarrow$ Cleaning $\rightarrow$ Distribution plots | `descriptive_report.md` |
| **Phase 2** | **Relational Analysis** | Data Merging $\rightarrow$ GroupBy Analysis $\rightarrow$ Correlation Matrices | `comparative_insights.md` |
| **Phase 3** | **Model Development** | Feature Selection $\rightarrow$ Model Training $\rightarrow$ Evaluation $\rightarrow$ Tuning | `prediction_model.py` |
| **Phase 4** | **Synthesis** | Combining findings into a final "Risk Framework" | `final_analysis.pdf` |

---

## 📚 3. Prerequisites (Learning Path)

Since we are using Python for this, here is what you should familiarize yourself with (or what I will be guiding you through):

### 🐍 Python & Data Manipulation
- **Pandas:** The gold standard for data. Learn `DataFrames`, `.groupby()`, `.merge()`, and `.describe()`.
- **NumPy:** Essential for handling numerical arrays and missing values (`NaN`).

### 📈 Data Visualization
- **Matplotlib & Seaborn:** Learning how to create Histograms (for distributions), Boxplots (for outliers), and Heatmaps (for correlations).

### 🤖 Machine Learning (Scikit-Learn)
- **The Pipeline:** Understanding the flow: `Data` $\rightarrow$ `Preprocessing` $\rightarrow$ `Model` $\rightarrow$ `Evaluation`.
- **Regression Concepts:** Linear Regression (simple) vs. Random Forest/XGBoost (complex/non-linear).
- **Evaluation Metrics:** Mean Absolute Error (MAE) and $R^2$ (R-Squared).

---

## ⏳ 4. Estimated Timeframes

| Objective | Estimated Time | Complexity | Priority |
| :--- | :--- | :--- | :--- |
| **Descriptive Stats** | 2–4 Days | Low | 🔴 High |
| **Comparative Analysis** | 1 Week | Medium | 🟠 Medium |
| **Prediction Modelling** | 1–2 Weeks | High | 🟡 Medium |
