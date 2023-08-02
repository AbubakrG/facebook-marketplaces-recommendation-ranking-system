import pandas as pd

def input_data(file_path: str='products.csv', line_term: str=',') -> pd.DataFrame: # This function imports data from a .csv file and returns a pandas dataframe. It also deletes all incomplete rows.
    products_df = pd.read_csv(file_path, line_term) #utilise local parameters for conciseness and clarity. Takes in the csv as a pandas dataframe
    products_df = products_df.dropna() # deletes rows with at least one item missing.
    return products_df

def clean_price_data(price_data: pd.Series) -> pd.Series: # This function takes pandas series with prices. It returns all values as numerical (float) values by removing symbols and commas.
    products_df = input_data() # Takes the first function to load the dataset as a whole.
    price_data = products_df['price'] # from the dataset, narrow down to the price data.

    price_data = price_data.str.strip('£') # Removes pound symbol.
    price_data = price_data.replace(',','', regex=True) # Removes commas.
    price_data = price_data.astype('float64') # Convert to float.

    return price_data 

if __name__ == "__main__":
    clean_price_data(pd.Series)