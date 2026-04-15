📊 YouTube Monetization Analyzer
🚀 Project Overview

This project analyzes YouTube performance data to identify the key drivers of ad revenue.

It follows a structured data science workflow — from data understanding to exploratory analysis and feature selection — to prepare for building robust regression models and deployment using Streamlit.

🎯 Objective
Understand factors influencing ad revenue (ad_revenue_usd)
Analyze relationships between engagement metrics and revenue
Perform feature selection to improve model performance
Prepare data for machine learning models and deployment
🧱 Project Workflow
✅ Stage 1: Load & Understand Data
Loaded dataset using Pandas
Explored structure using:
df.head()
df.info()
df.describe()
Checked:
Data types
Missing values
Duplicate records

📌 Insight:
Dataset is clean and suitable for regression modeling.

📊 Stage 2: Exploratory Data Analysis (EDA)
🔹 Univariate Analysis
Distribution plots for:
Views
Engagement rate
Watch time
Revenue

📌 Insights:

Some features show skewness
Revenue distribution is not perfectly normal
🔹 Target Analysis
Relationship between features and ad_revenue_usd using:
Scatter plots
Box plots

📌 Key Findings:

watch_time_per_view → Very strong relationship
engagement_rate → Moderate impact
Some features → Weak or no correlation
🔹 Visualization Optimization
Multiple plots in a single screen
Improved readability and comparison
📈 Stage 3: Correlation Analysis (Proof Layer)
Generated correlation matrix
Focused on correlation with target variable
📊 Key Results
Feature	Correlation	Insight
watch_time_per_view	0.988	Very High ✅
engagement_rate	0.151	Low ⚠️
views_per_subscriber	~0	No relation ❌
⚠️ Decisions Taken
Dropped watch_time_per_view
→ To avoid multicollinearity dominance
Dropped views_per_subscriber
→ No predictive value
🧠 Key Learning

High correlation does not always mean better modeling — it can lead to overfitting or data leakage.

🧠 Key Learnings
Correlation ≠ causation
Feature selection is critical
Strong predictors can dominate models
Visual analysis validates statistical findings
📦 Tech Stack
Python
Pandas & NumPy
Matplotlib & Seaborn
Scikit-learn
Streamlit
📁 Project Structure
youtube-monetization-analyzer/
│
├── notebook/
│   ├── 001-full-eda.ipynb
│   ├── 002-preprocessing.ipynb
│   ├── 003-model-building.ipynb
│
├── data/
│   └── youtube_data2.csv
│
├── streamlit/
│   └── app.py
│
├── requirements.txt
└── README.md
🔜 Next Steps
Build models:
Linear Regression
Ridge / Lasso
Decision Tree / Random Forest
Evaluate using:
MAE
MSE
R² Score
Deploy using Streamlit
📊 Future Enhancements
Feature engineering
Outlier handling
Skewness treatment
Hyperparameter tuning (GridSearchCV)
Interactive dashboard
💡 Conclusion

This project builds a strong foundation for predicting YouTube ad revenue by combining:

Data understanding
Exploratory analysis
Feature selection

It sets the stage for building accurate and interpretable machine learning models.
