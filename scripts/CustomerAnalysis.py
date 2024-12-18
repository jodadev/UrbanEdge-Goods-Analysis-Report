''' File Information
 This file conducts analysis using the cleaned data from "Sales Transaction v.4a.csv"
 to answer the following questions:

    2a) Are there any patterns in how frequently customers make purchases? 
    2b) Which customers are contributing the most to our revenue?

'''

import pandas as pd
from CleanData import get_data
from Modules.seaborn_methods import create_pie_chart, create_bar_graph
df = get_data()

# Question 2a)

def q2a(interval):

    def get_highest_consecutive_months(group):
        # Get unique months for the customer, sorted
        unique_months = sorted(group['Date'].unique())
        
        # Initialize variables to track the highest consecutive streak
        max_streak = 0
        current_streak = 1
        
        for i in range(1, len(unique_months)):
            # Check if the current month is consecutive to the previous month
            if (unique_months[i] - unique_months[i - 1]).days <= 31:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        
        # Final check for the last streak
        max_streak = max(max_streak, current_streak)
        
        return max_streak

    # Get streaks per customer
    customer_streaks = df.groupby('CustomerNo').apply(get_highest_consecutive_months)
    average_streak = customer_streaks.mean()
    print("\nAverage Highest Consecutive Streak:", average_streak)

    # Generate label and data series
    max = interval*int((12 / interval) + 1)
    values = []
    labels = []
    for x in range(interval,max,interval):
        values.append(len(customer_streaks[customer_streaks >= x]))
        labels.append(f'{x} Month')
    consistent_purchase_freq = pd.DataFrame({
        'label': labels,
        'value': values
    })

    # Create the pie chart
    create_pie_chart(consistent_purchase_freq, 'value', 'label', title='Consecutive Monthly Purchases per Customer')

q2a(interval=2)


# Question 2b)
def q2b():

    # Generate total revenue per customer then sort to find the top customers
    customer_total_spent = df.groupby('CustomerNo', as_index=False)['Subtotal'].sum()
    customer_total_spent = customer_total_spent.sort_values(by='Subtotal',ascending=False)

    # Extract top 5 and other customers to separate data frames
    top_5_customers = customer_total_spent.sort_values(by='Subtotal', ascending=False).head(5)
    other_customers = customer_total_spent.sort_values(by='Subtotal', ascending=False).iloc[5:]

    # Show pie chart of the top 5 
    top_5_customers['Label'] = top_5_customers['CustomerNo'].apply(lambda x: f"Customer {int(x)}")
    create_bar_graph(top_5_customers['Label'], top_5_customers['Subtotal'], 'Top 5 Customers by Revenue')
    create_pie_chart(top_5_customers, 'Subtotal', 'Label', title="Top 5 Customers by Revenue")

    # Find the percentage of top 5 vs other and display on pie chart
    top_5_total = top_5_customers['Subtotal'].sum()
    other_customers_total = other_customers['Subtotal'].sum()
    top_vs_other_df = pd.DataFrame({
        'Group': ['Top 5 Customers', 'Other Customers'],
        'Subtotal': [top_5_total, other_customers_total]
    })
    create_pie_chart(top_vs_other_df, 'Subtotal', 'Group', title="Top 5 Customers vs Others by Revenue")

q2b()