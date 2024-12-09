#Bar Chart

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Method" : [
    "Cash",
    "Credit",
    "Debit",
    "Voucher"
],
    "Monday" : [10, 41, 25, 34],
    "Tuesday" : [10, 41, 25, 34],
    "Wednesday" : [10, 41, 25, 34],
    "Thursday" : [10, 41, 25, 34],
    "Friday" : [10, 41, 25, 34],
    "Saturday" : [10, 41, 25, 34],
    "Sunday" : [10, 41, 25, 34],
})

plt.bar("Method", "Monday")
#Take in payment for each method for each day, e.g. mon-card, mon-voucher, tue-card etc.
#
#
#
#
#
#
#Plot a stacked bar chart showing how much payment per method on each day

