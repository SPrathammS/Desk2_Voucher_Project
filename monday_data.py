import pandas as pd
import matplotlib.pyplot as plt

def data_cleaning (df):
    df = df.set_index("Transaction ID")
    df = df.dropna(how="any")
    df = df.drop_duplicates()

    df_clean = df.dropna(subset=['Payment Method'])
 
    payment_counts = df_clean['Payment Method'].value_counts()
    # print(payment_counts["Voucher"]) 
    payment_percentages = (payment_counts / payment_counts.sum()) * 100
    print (payment_percentages["Voucher"])

df = pd.read_excel("monday_voucher_data.xlsx")
df1 = pd.read_excel("tuesday_voucher_data.xlsx")
df2= pd.read_excel("wednesday_voucher_data.xlsx")
df3= pd.read_excel("thursday_voucher_data.xlsx")
df4= pd.read_excel("friday_voucher_data.xlsx")
df5= pd.read_excel("saturday_voucher_data.xlsx")
df6= pd.read_excel("sunday_voucher_data.xlsx")
data_cleaning(df)
data_cleaning(df1)
data_cleaning(df2)
data_cleaning(df3)
data_cleaning(df4)
data_cleaning(df5)
data_cleaning(df6)


