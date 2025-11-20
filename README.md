# 📌 Sales Insights Analysis — Power BI + SQL + Python + MySQL  
*Retail Analytics Dashboard & Business Insights*

---

## 📊 Project Overview

An end-to-end analytical project delivering business performance insights using real sales data.  
Developed using:

✔ Python (ETL)  
✔ MySQL (Data Warehouse)  
✔ SQL (KPI analysis & data validation)  
✔ Power BI (Visualization & storytelling)

---

## 🎯 Business Objectives

- Analyze **global sales, profits & order volume**
- Identify **profitable segments, markets & categories**
- Measure **discount impact** on profit
- Support retail business decisions with insights

---

## 🧱 Data Pipeline Architecture

| Stage | Tool | Output |
|-------|------|--------|
| Data Source | CSV (Superstore Orders) | Raw data |
| ETL | Python + Pandas | Clean, structured data |
| Data Storage | MySQL | Fact table |
| Analytics | SQL | Business insights |
| BI | Power BI | Dashboards |

---

## 🗄️ Data Model (Star Schema)

**Fact Table**  
`sales_data` → Sales, Profit, Discount, Shipping Cost, Quantity

**Dimension Table**  
`DateTable` → Date, MonthName, Year, Quarter, Week, Calendar labels

🔗 Relationship:  
DateTable[Date] (1) → (*) sales_data[order_date]
Cross-filter: Both

yaml
Copy code

---

## 🧩 SQL Validation — Evidence Screenshots

### KPIs
| Metric | Output |
|--------|--------|
| Total Sales | ![](images/sql_total_sales.png) |
| Total Profits | ![](images/sql_total_profits.png) |
| Total Orders | ![](images/sql_total_orders.png) |

---

### Top Product Insights
![](images/sql_top_10_products_by_profits.png)
![](images/sql_top_10_product_by_sales.png)

---

### Revenue by Category & Sub-category
![](images/sql_sales_by_category_and_subcategory.png)

---

### Regional Revenue & Profit Performance
| Revenue | Profit |
|--------|-------|
| ![](images/sql_revenue_by_region.png) | ![](images/sql_profit_by_region.png) |

---

### Monthly Sales Trend
![](images/sql_monthly_sales_trend.png)

---

## 📌 Power BI Dashboards

### 📍 Page 1 — Sales Overview
![](images/BI_sales_overview.png)

---

### 💼 Page 2 — Product & Category Insights
![](images/BI_Product_&_Category_Insights.png)

---

### 👥 Page 3 — Customer & Profitability Analytics
![](images/BI_Customer_&_Profitability_Analytics.png)

---

## 🔎 Key Business Insights

- **Central region** = highest revenue & profit
- **Technology** = strongest revenue contributor
- **Furniture** = low margin → pricing improvement needed
- **High discounts (40%+) = Net losses**
- **Consumer segment** delivers **best profitability**

---

## 🛠️ Technology Stack

| Tool | Usage |
|------|------|
| Python | ETL Data cleaning |
| Pandas | Type casting, formatting |
| MySQL | Warehouse & SQL queries |
| SQL | KPI analysis |
| Power BI | Visualization |

---

## 📂 Repository Structure

sales-insights-project/
│-- Sales_Insights_Dashboard.pbix
│-- load_sales_data_mysql.py
│-- sql_queries.sql
│-- README.md
└── images/
├─ *.png (screenshots)

yaml
Copy code

---

## 🧠 Resume Highlights

- Built **scalable ETL → SQL → BI** pipeline  
- Designed **star schema** for time intelligence  
- Executed **advanced SQL** for business KPIs  
- Delivered insights for **profit optimization**

---

## 👤 Author

**Arun Pandiyan**  
Data Analyst | Aspiring Data Engineer  
📍 India  

🔗 LinkedIn: https://www.linkedin.com/in/arunpandiyan-thanasekaran/  
💻 GitHub: https://github.com/nameisarun  

---

## 🚀 Conclusion

This project showcases:

✔ Practical business analytics  
✔ Technical BI implementation  
✔ End-to-end data lifecycle ownership  

A complete portfolio-ready project demonstrating real-world impact 🔥

---