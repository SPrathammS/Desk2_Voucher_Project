import pandas as pd
import matplotlib.pyplot as plt

# #! function for cleaning data
def data_cleaning (df):
    df = df.set_index("Transaction ID")
    df = df.dropna(how="any")
    df = df.drop_duplicates()
    
    df["Payment Method"] = [i.capitalize() for i in df["Payment Method"]]
    df_clean = df.dropna(subset=['Payment Method'])

    df["Payment Method"] = df["Payment Method"].str.lower()
 
    payment_counts = df_clean['Payment Method'].value_counts()
    print(payment_counts["Voucher"]) 
   
    payment_percentages = (payment_counts / payment_counts.sum()) * 100
    print (payment_percentages["Voucher"])
    return(df_clean)
   

# #! try to make a loop as its iteration
df1 = pd.read_excel("monday_voucher_data.xlsx")
df2 = pd.read_excel("tuesday_voucher_data.xlsx")
df3= pd.read_excel("wednesday_voucher_data.xlsx")
df4= pd.read_excel("thursday_voucher_data.xlsx")
df5= pd.read_excel("friday_voucher_data.xlsx")
df6= pd.read_excel("saturday_voucher_data.xlsx")
df7= pd.read_excel("sunday_voucher_data.xlsx")

df1 = data_cleaning(df1)
df2 = data_cleaning(df2)
df3 = data_cleaning(df3)
df4 = data_cleaning(df4)
df5 = data_cleaning(df5)
df6 = data_cleaning(df6)
df7 = data_cleaning(df7)

#! sum of item and cost for each payment method
# Filter for rows where Transaction Type is "Payment"
# payment_data = df[df["Transaction Type"] == "Payment"]
# payment_data = df1[df1["Transaction Type"] == "Payment"]
# payment_data = df2[df2["Transaction Type"] == "Payment"]
# payment_data = df3[df3["Transaction Type"] == "Payment"]
# payment_data = df4[df4["Transaction Type"] == "Payment"]
# payment_data = df5[df5["Transaction Type"] == "Payment"]
# payment_data = df6[df6["Transaction Type"] == "Payment"]

# # Group by Payment Method and calculate the total cost
# total_cost_by_payment_method = payment_data.groupby("Payment Method")["Cost"].sum()

# # Display the result
# print(total_cost_by_payment_method)



# Assume df1, df2, df3, df4, df5, and df6 are already loaded DataFrames.
# You can replace this with loading logic for your specific case.

dataframes = [df1, df2, df3, df4, df5, df6, df7]

# Dictionary to store total cost by payment method for each DataFrame
total_cost_results = {}

# Iterate over the list of DataFrames
for i, df in enumerate(dataframes, start=1):
    # Filter for rows where Transaction Type is "Payment"
    payment_data = df[df["Transaction Type"] == "Payment"]
    
    # Group by Payment Method and calculate the total cost
    total_cost_by_payment_method = payment_data.groupby("Payment Method")["Cost"].sum()
    
    # Store the result in the dictionary
    total_cost_results[f"DataFrame_{i}"] = total_cost_by_payment_method

# Print the results for each DataFrame
for df_name, total_cost in total_cost_results.items():
    print(f"\nTotal Cost by Payment Method in {df_name}:\n{total_cost}")
# Combine total costs across all DataFrames
combined_total_cost = pd.concat(total_cost_results).groupby("Payment Method").sum()

print("\nCombined Total Cost by Payment Method Across All DataFrames:\n", combined_total_cost)

# print(total_cost_by_payment_method)
# cost_percentages = (total_cost_by_payment_method / total_cost.sum()) * 100
# print(total_cost_by_payment_method)
# # print(total_cost.sum())
# print (cost_percentages)

percentage_results = {}

for i, df in enumerate(dataframes, start=1):
    # Filter for rows where Transaction Type is "Payment"
    payment_data = df[df["Transaction Type"] == "Payment"]
    
    # Group by Payment Method and calculate the total cost
    total_cost_by_payment_method = payment_data.groupby("Payment Method")["Cost"].sum()
    
    # Calculate the overall total cost
    overall_total_cost = total_cost_by_payment_method.sum()
    
    # Calculate the percentage of total cost for each payment method
    percentage_by_payment_method = (total_cost_by_payment_method / overall_total_cost) * 100
    
    # Store the percentage result
    percentage_results[f"DataFrame_{i}"] = percentage_by_payment_method

# Print the percentage results for each DataFrame
for df_name, percentage in percentage_results.items():
    print(f"\nPercentage of Total Cost by Payment Method in {df_name}:\n{percentage}")
# Step 3: Combine total costs across all DataFrames
combined_total_cost = pd.concat([df[df["Transaction Type"] == "Payment"]
                                 .groupby("Payment Method")["Cost"].sum()
                                 for df in dataframes]).groupby("Payment Method").sum()

# Step 4: Calculate combined total cost and percentage
combined_total_cost_sum = combined_total_cost.sum()
combined_percentage = (combined_total_cost / combined_total_cost_sum) * 100

# Step 5: Print combined percentage result
print("\nCombined Cost Percentage by Payment Method Across All DataFrames:\n", combined_percentage)


#! capitalize payment method

#! make list for easy graph transformation

