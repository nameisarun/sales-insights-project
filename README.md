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
`SuperStoreOrders` → Sales, Profit, Discount, Shipping Cost, Quantity

**Dimension Table**  
`DateTable` → Date, MonthName, Year, Quarter, Week, Calendar labels

🔗 Relationship:  
DateTable[Date] (1) → (*) SuperStoreOrders[order_date]
Cross-filter: Both



---


## 🧩 SQL Results

### KPI Metrics
![SQL KPIs - Total Sales](Images/sql_total_sales.png)
![SQL KPIs - Profit](Images/sql_total_profits.png)
![SQL KPIs - Orders](Images/sql_total_orders.png)

### Top Products Analysis
![Top 10 Products - Sales](Images/sql_top10_sales.png)
![Top 10 Products - Profit](Images/sql_top10_profits.png)

### Category Performance
![Category Revenue](Images/sql_category_subcategory_sales.png)

### Regional Performance
![Regional Revenue](Images/sql_region_revenue.png)
![Regional Profit](Images/sql_region_profit.png)

### Monthly Trend
![Monthly Sales Trend](Images/sql_monthly_sales_trend.png)

### Segment Performance
![Segment Profit](Images/sql_segment_profit.png)

## 📊 Power BI Dashboards

### Page 1 — Sales Overview
![Sales Overview](Images/bi_sales_overview.png)

### Page 2 — Product & Category Insights
![Product Insights](Images/bi_product_category_insights.png)

### Page 3 — Customer & Profitability Analytics
![Customer & Profitability](Images/bi_customer_profitability_analytics.png)

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
│-- load_SuperStoreOrders_mysql.py
│-- sql_queries.sql
│-- README.md
└── Images/
├─ *.png (screenshots)



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
