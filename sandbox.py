## Clean and join 'Images.csv' and 'Products.csv'
import pandas as pd
from clean_tabular_data import CleanData

# tabular_data = clean_tabular_data.CleanData

output_data_1 = CleanData.load_and_clean()

print(output_data_1)