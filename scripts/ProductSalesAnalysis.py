''' File Information
 This file conducts analysis using the cleaned data from "Sales Transaction v.4a.csv"
 to answer the following questions:

    1a) Which products drive the highest sales volume and revenue?
    1b) Are there monthly patterns in product sales?

'''

import pandas as pd
from Modules.seaborn_methods import create_bar_graph, create_pie_chart
from CleanData import get_data

df = get_data()

# Q1a)
def q1a():
    # REVENUE
    product_revenue = df.groupby('ProductName', as_index=False)['Subtotal'].sum()
    product_revenue.rename(columns={'Subtotal': 'Total Revenue'}, inplace=True)
    # Separate top 5 from rest
    top_5 = product_revenue.sort_values(by='Total Revenue', ascending=False).head(5)
    others = product_revenue.sort_values(by='Total Revenue', ascending=False).iloc[5:]
    print(top_5)
    create_bar_graph(top_5['ProductName'], top_5['Total Revenue'], 'Top Products by Revenue')
    
    # Compare top against all other
    top_vs_other_rev = pd.DataFrame({
        'label': ['Top 5 Products', 'Other Products'],
        'value': [top_5['Total Revenue'].sum(), others['Total Revenue'].sum()]
    })
    create_pie_chart(top_vs_other_rev, 'value', 'label', title="Top 5 Products vs Other Products by Revenue")

    # VOLUME
    product_volume = df.groupby('ProductName', as_index=False)['Quantity'].sum()
    product_volume.rename(columns={'Quantity': 'Total Volume'}, inplace=True)
    # Separate top 5 from rest
    top_5 = product_volume.sort_values(by='Total Volume', ascending=False).head(5)
    others = product_volume.sort_values(by='Total Volume', ascending=False).iloc[5:]
    print(top_5)
    create_bar_graph(top_5['ProductName'], top_5['Total Volume'], 'Top Products by Volume')

    # Compare top against all other
    top_vs_other_vol = pd.DataFrame({
        'label': ['Top 5 Products', 'Other Products'],
        'value': [top_5['Total Volume'].sum(), others['Total Volume'].sum()]
    })
    create_pie_chart(top_vs_other_vol, 'value', 'label', title="Top 5 Products vs Other Products by Volume")
q1a()

# Q1b)
def q1b():
    # generate total monthly sales
    monthly = df.groupby('Month', as_index=False)['Subtotal'].sum()
    create_bar_graph(monthly['Month'], monthly['Subtotal'], "Total Monthly Sales Revenue", False)
q1b()