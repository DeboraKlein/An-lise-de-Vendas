# Analytical Intelligence Project

## 1. Business Understanding
---

#### Business Context:
This project analyzes real data from a nutritional supplements e-commerce platform focused on B2C (business-to-consumer) sales in the health and wellness sector. The goal is to understand sales behavior over a 12-month period and propose analytical solutions to support commercial decision-making.

#### General Objective:
Conduct exploratory and predictive analysis of commercial performance, focusing on seasonality, operational efficiency, and variables that directly influence revenue.

#### Specific Objectives:
- Identify seasonal patterns and monthly variations
- Evaluate operational metrics such as conversion rate, average ticket, and revenue per visit
- Test predictive approaches for sales forecasting
- Generate strategic recommendations based on analytical evidence
- Diagnose variables with the greatest impact on commercial performance

---

## 2. Data Understanding
---

#### Data Source:
Mercado Livre platform  
#### Analysis Period:
October 2024 to September 2025  
#### Records:
12 complete months (October 2025 excluded due to inconsistency)  
#### Key Metrics:
- Visits  
- Unique buyers  
- Conversion rate (%)  
- Number of sales  
- Units sold  
- Gross sales  
- Average ticket  
- Average price per unit  

---

## 3. Data Preparation
---

- Initial ETL performed using Power Query for structural cleaning
- Data conversion in Python (handling decimal separators and numeric types)
- Creation of auxiliary variables: month number, moving averages, percentage variation
- Chronological ordering and cross-validation with original data

---

## 4. Modeling
---

#### Model 1 — Machine Learning (Random Forest Regressor)

**Configuration:**
- Training: 9 months  
- Testing: 3 months  

**Variables used:** visits, buyers, conversion rate, average ticket, among others

**Results:**
- MAE: R$ 1,803.76  
- MAPE: 42.2%  
- R²: –2.46  
- Predictions up to 50% below actual values  

**Diagnosis:**
The model is not recommended for immediate use due to low performance and limited data. Extreme seasonality and the small sample size (12 time points) hinder generalization.

**Most relevant variables identified:**
- Unique buyers  
- Number of sales  
- Visits  
- Average sale value  

---

## 5. Alternative Modeling
---

#### Model 2 — Moving Averages + Seasonal Factors

**Approach:**
- Calculation of 3- and 6-month moving averages  
- Identification of monthly seasonal factors  
- Forecast adjustments based on trend and seasonality  
- Alert System:

🔴 Sales below average (>20%)  
🟢 Sales above average (>20%)  
🟡 Sales within expected range  

**Forecasts for October–December:**
- October: R$ 3,800  
- November: R$ 3,200  
- December: R$ 4,500  

---

## 6. Evaluation
---

**Comparison of Approaches:**

| Model                        | MAE       | MAPE   | R²     | Recommendation       |
|-----------------------------|-----------|--------|--------|----------------------|
| Machine Learning (RF)       | R$ 1,803  | 42.2%  | –2.46  | ❌ Not recommended    |
| Moving Averages + Seasonality | —         | —      | —      | ✅ Recommended        |

---

## 7. Deployment
---

**Operational Action Plan:**
- Reinforce inventory during high season months  
- Launch reactivation campaigns during critical months  
- Monitor monthly with automated alerts  
- Review quarterly with updated data  

**Realistic Targets for 2025:**
- Annual revenue: R$ 40,000 – R$ 45,000  
- Average ticket: R$ 220  
- Conversion rate: 0.75%  

---

## 8. Next Steps
---

- Implement practical model in commercial planning  
- Create dashboard with key metrics  
- Collect monthly data to strengthen predictive power  
- Reassess ML model with 24+ months of data  
- Develop recommendation system based on purchase behavior  

---

## 9. Technologies Used
---

- **Power Query**: Initial data preprocessing and cleaning  
- **Python (pandas, numpy)**: Data manipulation and statistical analysis  
- **Matplotlib / Seaborn**: Data visualization  
- **Scikit-learn**: Predictive modeling with Random Forest  
- **Jupyter Notebook**: Development and documentation environment  

---

## 10. How to Run the Project
---
**Clone the repository:**
```bash
git clone https://github.com/DeboraKlein/Analise-de-Sazonalidade-e-Modelagem-Preditiva.git
````
**Install dependencies:**
````
pip install -r requirements.txt
````
**Run the main notebook:**
````
notebooks/Analise-de-Sazonalidade-e-Modelagem-Preditiva.ipynb
````
**To run the practical model:**
````
scripts/modelo_pratico.py
````
Results will be saved to:

- ``relatorio_analise_completa.csv``

- ``relatorio_ia_achados.txt``

---

## Conclusion
---
- The analysis revealed strong growth potential, with annual revenue of R$ 32,835 and a +194.4% increase over 12 months. However, this growth is accompanied by pronounced seasonality, with monthly variations 
exceeding 300%, requiring more precise operational planning. 

- High-performing months (September, July, and December) concentrate sales peaks that should be anticipated with inventory reinforcement, promotional campaigns, and a prepared team. Conversely, critical months 
like April and February demand retention strategies, customer reactivation, and a focus on average ticket to mitigate downturns.

- The attempt to apply Machine Learning showed that with only 12 time points, the model is unreliable for forecasting. In contrast, the use of moving averages and seasonal factors proved more effective in 
generating realistic forecasts and guiding quarterly targets.

- The business should prioritize increasing its base of unique buyers, optimizing conversion rates, and raising the average ticket — variables that demonstrated the greatest impact on revenue. With the 
implementation of a continuous monitoring system and structured data collection, it will be possible to evolve toward more robust predictive models and personalized recommendation strategies.
---
