📊 YouTube Monetization Analyzer
🚀 Project Overview

This project focuses on analyzing YouTube channel performance data to understand the key factors influencing ad revenue generation.

We follow a structured data science workflow — from data understanding to exploratory analysis and feature evaluation — to build a strong foundation for predictive modeling.

🎯 Objective

The goal of this project is to:

Identify key drivers of ad revenue
Understand relationships between engagement metrics and revenue
Prepare data for building reliable regression models
Enable future deployment (Streamlit app)
🧱 Project Workflow
✅ STAGE 0: Setup
Environment setup using:
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
Streamlit (for deployment)
Dataset loaded from local system
✅ STAGE 1: Load & Understand Data
Key Actions:
Loaded dataset using Pandas
Explored structure using:
.head()
.info()
.describe()
Data Understanding:
Identified:
Numerical features
Target variable → ad_revenue_usd
Checked:
Data types
Missing values
Duplicate records (including timestamp precision)
Key Insight:
Dataset is clean enough for analysis, with structured numerical features suitable for regression
✅ STAGE 2: Exploratory Data Analysis (EDA)
1. Univariate Analysis
Distribution plots for:
Views
Engagement rate
Watch time
Revenue
Insights:
Some features show skewness
Revenue distribution is not perfectly normal
2. Target Analysis (Important Stage)
Visualized relationship between each feature and ad_revenue_usd using:
Scatter plots
Box plots
Key Findings:
watch_time_per_view shows very strong relationship with revenue
engagement_rate has moderate impact
Some features show weak or no correlation
3. Visualization Optimization
Improved plotting:
Multiple plots in one screen
Better readability for interpretation
✅ STAGE 3: Correlation Analysis (Proof Layer)
Actions:
Generated correlation matrix
Focused on correlation with target variable
Key Results:
ad_revenue_usd          1.000000
watch_time_per_view     0.988061  ✅ VERY HIGH
engagement_rate         0.151485  ⚠️ LOW
views_per_subscriber   -0.000635  ❌ NO RELATION
Decisions Taken:
Dropped:
watch_time_per_view ❗ (to avoid multicollinearity dominance)
views_per_subscriber ❗ (no predictive value)
Insight:
Strong correlation does not always mean better modeling → risk of overfitting / leakage
🧠 Key Learnings
Correlation ≠ causation
High correlation features can dominate models
Feature selection is critical before modeling
Visual analysis helps validate statistical findings
📦 Tech Stack
Python
Pandas & NumPy
Matplotlib & Seaborn
Scikit-learn
Streamlit
🔜 Next Steps
Build regression models:
Linear Regression
Ridge / Lasso
Decision Tree / Random Forest
Evaluate models using:
MAE
MSE
R² Score
Deploy using Streamlit
📊 Future Enhancements
Feature engineering
Handling skewness
Outlier treatment
Model tuning (GridSearchCV)
Real-time prediction interface
💡 Conclusion

This project establishes a strong analytical foundation for predicting YouTube revenue by:

Cleaning and understanding data
Extracting meaningful insights
Selecting relevant features

It sets the stage for building robust and interpretable machine learning models.
