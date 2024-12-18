# **Sales and Customer Insights Analysis**

This repository contains an analysis of product sales and customer purchase behaviors for an online (mock) store, **UrbanEdge Goods**. The goal of this analysis is to help the business owner, **Laura Chen**, identify key products and customer trends to drive informed decision-making.

## **Table of Contents**

1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [Analyses Conducted](#analyses-conducted)  
4. [Key Findings](#key-findings)  
5. [How to Use This Repository](#how-to-use-this-repository)  
6. [Visualizations](#visualizations)  

---

## **Project Overview**

This project aims to answer the following business questions for **UrbanEdge Goods**:

1. **Product Sales Analysis:**
   - Which products drive the highest sales volume and revenue?
   - Are there patterns in product sales over time (monthly trends)?

2. **Customer Insights:**
   - Are there any patterns in how frequently customers make purchases?
   - Which customers are contributing the most to our revenue?

The findings and recommendations will help optimize sales strategies and improve customer engagement.

---

## **Dataset**

The dataset used for this analysis is from [Kaggle](https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business).

### **Dataset Features**

- **TransactionNo:** Unique identifier for each transaction. (Cancelled transactions are marked with "C")
- **Date:** The date when each transaction occurred.
- **ProductNo:** Unique identifier for each product.
- **Product:** Product name.
- **Price:** Price per unit in pound sterling (£).
- **Quantity:** Number of units sold (negative values indicate returns/cancellations).
- **CustomerNo:** Unique identifier for each customer.
- **Country:** Country where the customer resides.

---

## **Analyses Conducted**

1. **Product Sales Analysis:**
   - Top products by sales volume and revenue.
   - Comparison of top 5 products versus other products.
   - Monthly patterns in product sales.

2. **Customer Insights:**
   - Frequency of customer purchases.
   - Identification of top customers by revenue.
   - Consistency in monthly purchasing patterns.

---

## **How to Use This Repository**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sales-customer-insights.git
   ```

2. **Dependencies:**
   - Install the required libraries using pip:
   ```bash
   pip install pandas matplotlib seaborn
   ```
   - Download dataset:
   ```
    https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business
   ```

3. **Run the Analysis:**
   - The analysis scripts are located in the `scripts` folder.
   - Example:
     ```bash
     python scripts/ProductSalesAnalysis.py
     ```
   - Do not run **scripts/ProductSalesAnalysis.py** as this is a module for other py files meant to have a cleaned DataFrame to work with.

4. **View the Report:**
   The detailed report is available [here](/Report.md).

---
