

import pandas as pd
import matplotlib.pyplot as plt

from sas7bdat import SAS7BDAT

with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

print(df_sas.head())