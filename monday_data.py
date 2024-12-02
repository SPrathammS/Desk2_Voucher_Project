import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("monday_voucher_data.xlsx")
df = df.set_index("Transaction ID")
 
df = df.dropna(how="any")
df = df.drop_duplicates()

df_clean = df.dropna(subset=['Payment Method'])
 
payment_counts = df_clean['Payment Method'].value_counts()
print(payment_counts) 
payment_percentages = (payment_counts / payment_counts.sum()) * 100
print (payment_percentages)


