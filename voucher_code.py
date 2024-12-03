import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Function to clean data: Remove NaN, duplicates, and capitalize "Payment Method"
def clean_data(file_path):
    df = pd.read_excel(file_path)
    df = df.drop_duplicates().dropna(subset=['Payment Method', 'Total Items', 'Cost', 'Transaction Type', 'Basket'])
    df["Payment Method"] = df["Payment Method"].str.capitalize()
    return df


# Function to extract payment method, items, and cost data from all files
def extract_data(file_paths):
   
    dataframes = []
    for file_path in file_paths:
        df = clean_data(file_path)
        df = df[df["Transaction Type"] == "Payment"]  # Filter only payment transactions
        dataframes.append(df[["Payment Method", "Total Items", "Cost"]])
    # print(dataframes)
    return dataframes
    
    
# Function to calculate total and percentage of cost by payment method
def calculate_totals_and_percentages(dataframes):

    total_cost_by_day = []  # For stacked bar chart
    total_items_per_method = []
    combined_total_cost = pd.Series(dtype=float)  # For combined totals and percentages
    combined_total_items = pd.Series(dtype=float)  # For combined totals and percentages

    for df in dataframes:
        daily_total = df.groupby("Payment Method")["Cost"].sum()
        total_cost_by_day.append(daily_total)
        daily_items = df.groupby("Payment Method")["Total Items"].sum()
        combined_total_cost = combined_total_cost.add(daily_total, fill_value=0)
        combined_total_items = combined_total_items.add(daily_items, fill_value=0)
    
    # Calculate percentage for each payment method
    combined_percentage = (combined_total_cost / combined_total_cost.sum()) * 100
    # print(total_cost_by_day)    # stacked bar chart
    # print(combined_total_cost)   
    # print(combined_percentage)   # pie chart
    # print(combined_total_items)  # bar chart
    # print(total_items_per_method) # empty
    return total_cost_by_day, combined_total_cost, combined_percentage, combined_total_items


# Function to plot stacked bar chart and pie chart
def plot_charts(total_cost_by_day, combined_percentage, combined_total_items):
   
    # Create DataFrame for stacked bar chart
    # stacked_df = pd.DataFrame(total_cost_by_day)
    # stacked_df.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # stacked_df.fillna(0, inplace=True)  # Replace NaN with 0 for plotting

    # # Plot stacked bar chart

    #? stacked_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set3', edgecolor='black')
    # plt.title('Total Cost by Payment Method Over the Week')
    # plt.ylabel('Cost')
    # plt.xlabel('Day of the Week')
    # plt.legend(title='Payment Method')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # # plt.show()
    #? (for reference)
 
    df = pd.DataFrame(total_cost_by_day)
    df.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
    # print(df)
    my_plot = df.plot.bar(stacked=True)
    plt.savefig("daily_spenditures.png", bbox_inches = "tight")
    plt.title("Weekly Income")
    plt.xlabel("Days Of The Week")
    plt.ylabel("Sales (£)")
    plt.xticks(rotation=45)
    plt.show()
 
    # Plot pie chart

    #? combined_percentage.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), colormap='Set3')
    # plt.title('Percentage of Total Cost by Payment Method')
    # plt.ylabel('')  # Hide y-label for a cleaner pie chart
    # plt.tight_layout()
    # plt.show()
    #? (for reference)
    
    payment_methods = [ "Cash" , "Credit" , "Debit" , "Mobile Wallet", "Voucher" ]   #list==> sort ascending
    plt.pie(combined_percentage, labels=payment_methods, autopct="%.2f%%" , explode=([0, 0 , 0 , 0, 0.1]))
    plt.title("Weekly Income")
    plt.show()

    # bar chart for items sold

    df = pd.DataFrame({
    "Payment Method" : [
    "Cash",
    "Credit",
    "Debit",
    "Mobile Wallet",
    "Voucher"
    ], "Items Sold" : combined_total_items,})
    df = df.sort_values("Items Sold")
    bar_colours = ["red" if x=="Voucher" else "blue" for x in df["Payment Method"]]
    
    plt.bar(df["Payment Method"], df["Items Sold"], color=bar_colours)
    plt.title("Items Sold Per Payment method")
    plt.xlabel("Payment Method")
    plt.ylabel("Items Sold")
    plt.show()


# File paths for the 7 Excel files
file_paths = [
    "monday_voucher_data.xlsx",
    "tuesday_voucher_data.xlsx",
    "wednesday_voucher_data.xlsx",
    "thursday_voucher_data.xlsx",
    "friday_voucher_data.xlsx",
    "saturday_voucher_data.xlsx",
    "sunday_voucher_data.xlsx"
]

# Step 1: Extract data from all Excel files
dataframes = extract_data(file_paths)

# Step 2: Calculate totals and percentages
total_cost_by_day, combined_total_cost, combined_percentage, combined_total_items = calculate_totals_and_percentages(dataframes)

# Step 3: Plot stacked bar chart and pie chart
plot_charts(total_cost_by_day, combined_percentage, combined_total_items)
