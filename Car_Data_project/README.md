# 🚗 Used Car Market Intelligence Dashboard

This project analyzes the used car market using **Python (for data cleaning)** and **Power BI (for visualization)**.

## 📊 Tools & Technologies
- Python (pandas, numpy)
- Power BI Desktop
- Excel

## 🧹 Data Cleaning (Python)
Script: `clean_cars.py`

Steps performed:
1. Removed null and duplicate records
2. Standardized column names
3. Converted string prices and mileage to numeric
4. Exported cleaned data as `cleaned_cars_data.xlsx`

## 📈 Dashboard Insights
Built with **Power BI**:
- Price declines sharply with age
- Dealers command higher prices
- Mileage penalty (price vs km driven)
- Top 10 high-value car models

## 📂 File Descriptions
| File | Description |
|------|--------------|
| `used_cars_data.xlsx` | Raw dataset |
| `cleaned_cars_data.xlsx` | Cleaned dataset |
| `clean_cars.py` | Python cleaning script |
| `Used_Car_Dashboard.pbix` | Power BI dashboard file |

## 🚀 How to Use
1. Run the Python script to clean data.
2. Open `Used_Car_Dashboard.pbix` in Power BI Desktop.
3. Connect to `cleaned_cars_data.xlsx`.

---

📧 **Author:** Chandu  
📅 Created: October 2025  
