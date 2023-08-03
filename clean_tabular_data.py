import csv
import pandas as pd
import chardet as cd

class CleanData:

    def _init_(self,name) -> None:
        self.name = name
        self.df = self.input_data(name)

    def clean_price_data(price_column: pd.Series) -> pd.Series:
        clean_column = price_column.replace(to_replace='[^0-9.]', value='', regex=True)
        float_column = pd.to_numeric(clean_column)
        return float_column

    def input_data(filepath: str, lineterminator: str = ",") -> pd.DataFrame:
        df = pd.read_csv(filepath, lineterminator=lineterminator)
        df.rename(columns={'create_time\r':'create_time'}, inplace=True)
        return df

    def load_and_clean(file_path, lineterminator):
        tabular_data = CleanData.input_data(file_path, lineterminator)
        tabular_data['price'] = CleanData.clean_price_data(tabular_data['price'])
        tabular_data.rename(columns = {'id':'product_id'}, inplace = True)

        return tabular_data

    # products_df = input_data() # Takes the first function to load the dataset as a whole.
    # price_data = products_df['price'] # from the dataset, narrow down to the price data.

    # price_data = price_data.str.strip('£') #
    # price_data = price_data.replace(',','', regex=True) 
    # price_data = price_data.astype('float64') # Convert to float.

    # return price_data 


if __name__ == "__main__":
    file_path = "products.csv"
    lineterminator = "\n"
    CleanData.load_and_clean(file_path, lineterminator)  