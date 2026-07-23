# PK Foods Price Intelligence 

## Business Context

Food price volatility directly impacts household budgets, retail pricing strategies, and supply chain planning across Pakistan's urban markets. Procurement teams, policy makers, and retailers struggle with fragmented price data across cities, making it difficult to identify pricing inefficiencies, optimize sourcing decisions, or anticipate market shifts. Without centralized analytics, organizations rely on manual surveys and anecdotal evidence, leading to suboptimal procurement and missed cost-saving opportunities.

This project addresses that gap by consolidating 1,100 price records from 10 major Pakistani cities into a structured analytical framework. The dashboard transforms raw market survey data into actionable intelligence on revenue distribution, price dispersion, and category-level trends. By quantifying price gaps between cities and tracking volatility patterns, the analysis supports data-driven decisions in procurement, inventory management, and market positioning.

The resulting insights help stakeholders understand where food commodities are overpriced or underpriced relative to national averages, which cities present the highest revenue potential, and which categories carry the greatest cost volatility. This enables more strategic sourcing, better negotiation leverage with suppliers, and improved forecasting for retail and distribution operations.

## Design Approach

The dashboard follows executive briefing principles: KPI cards provide immediate situational awareness, city and category analyses are separated for focused decision-making, and visual hierarchy guides viewers from high-level metrics to detailed breakdowns. All charts are designed to answer specific business questions with clear titles, reference lines for context, and consistent formatting for rapid comprehension.

For a detailed technical review of chart effectiveness, visualization improvements, and design recommendations, see [DASHBOARD_REVIEW.md](DASHBOARD_REVIEW.md).

---

## 📊 Improved Visualizations

This project includes enhanced chart generation with business-oriented titles, consistent color schemes, and improved data visualization best practices.

### Revenue by City — Horizontal Bar Chart

![Revenue by City](Chart_Revenue_by_City_v2.png)

> **Business Question:** Which cities generate the most revenue?
> 
> **Key Insight:** Hyderabad leads at PKR 1.6M (12.0% share), while Peshawar generates the lowest revenue at PKR 1.0M (7.7% share). The chart uses a gradient color scheme from emerald (highest) to red (lowest) with an average reference line at PKR 1.34M.

### Average Price by Category — Horizontal Bar Chart

![Price by Category](Chart_Price_by_Category_v2.png)

> **Business Question:** Which food categories are most expensive?
> 
> **Key Insight:** Beverages command the highest average price at PKR 912/kg, followed by Meat (PKR 848/kg) and Oil (PKR 722/kg). Vegetables are the most affordable at PKR 95/kg. The chart uses three-tier color coding: purple (premium), teal (mid-range), and amber (affordable).

### Price Volatility by Category

![Price Volatility](Chart_Price_Volatility_v2.png)

> **Business Question:** Which categories have the most price instability?
> 
> **Key Insight:** Pulses show the highest price range (PKR 154), indicating significant market volatility. Premium categories (Beverages, Meat, Oil) show wider price ranges than affordable categories.

### Revenue Concentration — Pareto Analysis

![Revenue Concentration](Chart_Revenue_Concentration_v2.png)

> **Business Question:** What percentage of revenue comes from top cities?
> 
> **Key Insight:** Top 3 cities (Hyderabad, Karachi, Islamabad) account for 33% of total revenue, indicating moderate market concentration. The Pareto chart combines bar and line visualization to show both individual city performance and cumulative distribution.

### KPI Cards Layout

![KPI Cards](Chart_KPI_Cards_v2.png)

> **Design Approach:** Six KPI cards organized in a 3x2 grid with visual hierarchy — Total Revenue (primary), Total Records and Avg Price/Kg (secondary), and city/item metrics (tertiary). Each card uses color-coded borders for quick identification.

---

### Original Dashboard Preview

#### Main Dashboard — PK Foods Price Intelligence

![PK Foods Dashboard](Pk_Food_project_dashboard.png)

> The main dashboard displays KPI cards (Total Records, Revenue, Avg Price/Kg), revenue breakdown by city, and average price by category in a dark-themed, professional layout.

#### Revenue by City & Category Distribution

![Revenue & Category Charts](Chart_Data.png)

> **Left:** Bar chart comparing total revenue (PKR) across all 10 cities — Hyderabad leads at PKR 1.6M.  
> **Right:** Pie chart showing average price distribution by food category — Beverage and Meat hold the largest shares.

---

## ✨ Features

- **Comprehensive Price Tracking** — 1,100 records across 10 cities and 35 food items
- **Interactive Dashboard** — KPI cards, revenue breakdowns, and category analysis
- **City-Level Analytics** — Revenue share, average prices, and performance status per city
- **Category Insights** — Price ranges, averages, and record counts for 9 food categories
- **Price Volatility Analysis** — Statistical analysis of price fluctuations across markets
- **Gap Analysis** — Identifies price disparities between cities and items
- **Price Classification** — Categorizes items into Low/Medium/High/Premium tiers
- **Monthly KPI Tracking** — Time-series monitoring of price and volume trends

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Microsoft Excel | Data modeling, analysis, and dashboard development |
| Pivot Tables | Data aggregation and cross-tabulation |
| Advanced Charting | Bar charts, pie charts, and KPI visualizations |
| Conditional Formatting | Data highlighting and status indicators |
| Structured Data Modeling | Relational data organization and integrity |

---

## 📁 Project Structure

```
📁 Excel_Analystics/
│
├── 📊 PK_FOOD_PRICE_PER_KG-project1.xlsx     ← Core dataset (1,100 records)
├── 📊 Source_Market_Survey_PK.xlsx           ← Raw market survey data
│
├── 📈 chart_data.xlsx                        ← Chart source data
├── 📈 City_Coverage_Performance.xlsx         ← City-level performance metrics
├── 📈 Monthly_KPI_tracker.xlsx               ← Monthly KPI tracking
│
├── 🔍 gap_Analysis.xlsx                      ← Price gap & market gap analysis
├── 🔍 Price_Level.xlsx                       ← Price level classification
├── 🔍 Price_Review_per_Kg.xlsx               ← Per-kg price review breakdown
├── 🔍 Volatility_of_price_in_PK_FOOD_PRICE.xlsx ← Price volatility analysis
│
├── 🖼️ Pk_Food_project_dashboard.png          ← Dashboard screenshot
├── 🖼️ Chart_Data.png                         ← Revenue & category charts
│
└── 📄 README.md                              ← Project documentation
```

```

### Chart Specifications

For detailed color palettes, typography standards, and implementation guidelines, see:
- [visualization_style_guide.md](visualization_style_guide.md) — Complete style guide with color codes and chart specifications
- [DASHBOARD_REVIEW.md](DASHBOARD_REVIEW.md) — Comprehensive analysis of dashboard effectiveness and improvement recommendations

---

## 💻 Usage

### Viewing the Dashboard
1. Open `PK_FOOD_PRICE_PER_KG-project1.xlsx`
2. Navigate to the "Dashboard" sheet
3. Interact with pivot tables and charts to explore data

### Exploring Analysis Files
- **City Coverage Performance** — Review city-by-city revenue and status
- **Monthly KPI Tracker** — Track price trends over time
- **Gap Analysis** — Identify pricing inefficiencies across markets
- **Price Volatility** — Analyze statistical price fluctuations
- **Price Level** — View item classifications by price tier

### Data Refresh
- Source data is in `Source_Market_Survey_PK.xlsx`
- Update the core dataset and refresh pivot tables to incorporate new data

---

## 🏆 Key Metrics

| Metric | Value |
|--------|-------|
| 📋 Total Records | 1,100 transactions |
| 💰 Total Revenue (PKR) | 13,423,064 |
| ⚖️ Avg Price / Kg | PKR 372 |
| 🏆 Top Revenue City | **Hyderabad** — PKR 1,608,801 |
| 🐟 Most Expensive Item | **Fish (Pomfret)** — PKR 1,113/kg avg |
| 📊 Items Priced Above Avg | 29.9% |

---

## 🏙️ Revenue by City (PKR)

| City | Total Revenue | % Share | Avg Price/Kg | Status |
|------|---------------|---------|--------------|--------|
| Hyderabad | 1,608,801 | 12.0% | 417.6 | 🏆 HIGHEST |
| Karachi | 1,568,588 | 11.7% | 421.0 | ✅ ACTIVE |
| Islamabad | 1,460,893 | 10.9% | 343.8 | ✅ ACTIVE |
| Quetta | 1,459,146 | 10.9% | 399.7 | ✅ ACTIVE |
| Faisalabad | 1,382,163 | 10.3% | 347.9 | ✅ ACTIVE |
| Rawalpindi | 1,342,984 | 10.0% | 409.4 | ✅ ACTIVE |
| Lahore | 1,279,284 | 9.5% | 349.4 | ✅ ACTIVE |
| Sialkot | 1,174,601 | 8.8% | 368.8 | ✅ ACTIVE |
| Multan | 1,114,521 | 8.3% | 325.3 | ✅ ACTIVE |
| Peshawar | 1,032,082 | 7.7% | 338.3 | ⚠️ LOWEST |
| **TOTAL** | **13,423,064** | **100%** | — | — |

---

## 🥩 Average Price by Category (PKR/Kg)

| Rank | Category | Avg Price/Kg | Max | Min | Records |
|------|----------|--------------|-----|-----|---------|
| 1 | Beverage | 911.6 | 1,185.1 | 638.1 | 48 |
| 2 | Meat | 847.8 | 1,102.1 | 593.5 | 174 |
| 3 | Oil | 721.7 | 938.1 | 505.2 | 65 |
| 4 | Condiment | 450.7 | 585.9 | 315.5 | 62 |
| 5 | Dairy | 413.8 | 537.9 | 289.7 | 94 |
| 6 | Pulses | 256.6 | 333.5 | 179.6 | 102 |
| 7 | Fruit | 185.6 | 241.3 | 129.9 | 184 |
| 8 | Grain | 141.9 | 184.5 | 99.3 | 180 |
| 9 | Vegetable | 94.9 | 123.4 | 66.5 | 191 |

---

## 💡 Key Insights

- 🏆 **Hyderabad** generates the highest revenue (12%) with the highest average price per kg (PKR 417.6)
- 🐟 **Fish (Pomfret)** is the most expensive item at PKR 1,113/kg on average
- 🥤 **Beverages** are the priciest category (PKR 911.6/kg avg), followed by Meat and Oil
- 🥦 **Vegetables** are the most affordable category (PKR 94.9/kg avg) with the highest record count (191)
- ⚠️ **Peshawar** has the lowest total revenue and average price per kg — a potential under-served market
- 📊 Nearly **30% of items** are priced above the national average, indicating significant price dispersion

---

## 🔮 Future Improvements

- [ ] Automate data ingestion from market survey sources
- [ ] Add interactive slicers for dynamic filtering by city, category, and date range
- [ ] Integrate Power BI for enhanced visualization capabilities
- [ ] Implement price forecasting using historical trends
- [ ] Add comparative analysis with regional and international markets
- [ ] Create automated report generation with executive summaries
- [ ] Build a web-based dashboard using Python (Streamlit/Dash) for broader accessibility
- [ ] Incorporate inflation-adjusted price trends over multiple years

---

## 📚 Learning Outcomes

- **Excel Advanced Features** — Pivot tables, Power Query, and advanced charting techniques
- **Data Cleaning & Transformation** — Raw survey data handling, format normalization, and inconsistency resolution
- **Dashboard Design** — Professional dark-themed dashboards with KPI scorecards and visual hierarchies
- **Statistical Analysis** — Averages, volatility metrics, and price distributions across large datasets
- **Business Intelligence** — Translating raw data into actionable market insights for decision-making
- **Data Storytelling** — Presenting complex analytics in clear, visual formats for non-technical stakeholders

---

## 👤 Author

**Innocent Watsala**

- 🌍 Based in United Arab Emirates
- 📊 Data Analyst specializing in Excel, SQL, and Python
- 🎯 Focused on data cleaning, EDA, and business intelligence

### Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR-LINKEDIN-HERE)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:watsala.digital@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/INNOCENT256-UG)

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify for your own portfolio or learning purposes.

---

## 🙏 Acknowledgments

- Data sourced from Pakistan market surveys and ground-level price collections
- Built as a portfolio project demonstrating Excel analytics and dashboard design capabilities
- Inspired by real-world food price monitoring systems used by government and NGOs

---

<div align="center">
  <i>"Every dataset tells a story. My job is to find it."</i>
</div>

---

*Last updated: 2025 | Data covers 10 major Pakistani cities | 1,100 price records analyzed*
