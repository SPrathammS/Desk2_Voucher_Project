import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")
# print (df)
df= df.set_index("Transaction ID")   # removes repeats of serial numbers, by setting the 'Transaction ID' col as index
df= df.drop("Till ID", axis=1)  # removes 'Till ID' col, as its the same throughout the dataset, not comparing diff tills. 'axis=1' aligns cols horizontally than vertically

df = df.dropna(how='any')   # removes'NaN' in 'any' row/col; for (dropna; how=any/all) 
# to confirm duplicates- can look at transaction IDs and time stamp, whether they are the exact same
df = df.drop_duplicates()  # built iin function to scan and drop/remove duplicates
df.at[15.0, "Cost"] = 6.0  # not updating the whole 'df' variable; but just replacing the value 'at' certain point in the updated 'df' data frame variable
#! time stamp data_type was not registering as 'date obj' but as 'float'(due to the decimal base)
def float_to_time(time_record):
    time_record = str(time_record)
    hours, minutes = time_record.split(".")
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp 

df["Time"] = df["Time"].apply(float_to_time)
# df["Time"] = pd.to_datetime(df["Time"])

# data patterns - tall/wide 
# print(df)

def split_basket(basket_string):
    items = basket_string.split(",")
    # "Tea, Tea, Tea, Coffee"
    # ["Tea", " Tea", " Tea", " Coffee"]
    # stripped_items = []
    # for item in items:
    #     stripped_items.append(item.strip())
    
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
print(df)

exploded_data = df.explode("Basket")
print(exploded_data["Basket"].value_counts())




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
