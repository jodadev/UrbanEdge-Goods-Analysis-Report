''' File Information
    The purpose of this file is to clean the data in a 'common clean'
    for each question of the client request - each question is 
    answered in separate Python files.

'''

import pandas as pd

def get_data():

    df = pd.read_csv('Sales Transaction v.4a.csv')

    # remove return records from data frame and save in separate data frame
    '''
        The dataset has a small percentage of transaction records where the 'Quantity' is 
        negative, meaning its a return transaction. So, we create a variable for them
        to use later and remove those records from the 'df' DataFrame variable.
    '''
    returns = df[df['Quantity'] < 0]
    df = df[df['Quantity'] >= 0]

    '''
        Now that we have our return transactions, the negative quantity records,
        removed, we want to find and remove the original sale transactions to
        ensure we are properly removing transactions that were returned (not just 
        the negative Quantity transaction but the associated sales transaction).

        To do this we must make the Quantity positive in 'returns' DataFrame
        so when we attempt to filter using Quantity among other features,
        it matches correctly. 
    '''
    returns['Quantity'] = returns['Quantity'].abs()
    # Filter df by excluding rows that match CustomerNo, ProductName, and Quantity in returns
    df = df[~df.set_index(['CustomerNo', 'ProductName', 'Quantity']).index.isin(
        returns.set_index(['CustomerNo', 'ProductName', 'Quantity']).index
    )]

    # DATE FEATURE ENGINEERING
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    '''
        The full dataset contains a Time series from December 2018 to December 2019.
        I decided to remove 2018 and only count 2019.
    '''
    df = df[df['Year'] == 2019]

    '''
        The transaction only has 'Price' and 'Quantity' information but not the
        subtotal, the line below generates each transactions subtotal.
    '''
    df['Subtotal'] = df['Price'] * df['Quantity']

    return df