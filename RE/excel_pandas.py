import pandas as pd
data_df = pd.read_excel("成績中位數.xlsx", sheet_name=["107下", '108上'])
data_df['108上']['成績中位數']
