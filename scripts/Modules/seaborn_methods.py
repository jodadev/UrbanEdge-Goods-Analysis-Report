import matplotlib.pyplot as plt
import seaborn as sns

def create_pie_chart(data, value_col, label_col, title="Top Customer Revenue Distribution"):
 
    # Set Seaborn style
    sns.set(style="whitegrid")

    # Extract values and labels from the DataFrame
    values = data[value_col]
    labels = data[label_col]

    # Create the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

    # Add a title
    plt.title(title, fontsize=16)

    # Display the pie chart
    plt.show()

def create_bar_graph(x, y, title, show_values = True):
    ax = sns.barplot(x=x, y=y)
    if show_values:
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='top', xytext=(0, 10), textcoords='offset points')
    ax.set(title=title)
    plt.show()