

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from template import params

plt.plot(dates, sales, **params)


x = np.array([1,8])
y = np.array([3, 10])

df = pd.read_csv('./data/transactions1.csv')
df1 = pd.read_csv('./data/transactions2.csv')
print(df.head())

# plt.plot(x, y)
# plt.plot(df["Date"], df["SalesAmount"])
# df["SalesAmount"].hist()
# df["SalesAmount"].plot(kind="pie")

dates = df["Date"]
sales = df["SalesAmount"]
# plt.hist(sales)
# plt.plot(dates,sales, 'o')
plt.plot(
    dates,
    sales,
    marker='D',
    color="red",
    linewidth=2,
    label="Sales Data",
    linestyle=":"
)

plt.plot(
    dates[:7],
    df1['SalesAmount'],
    color='green'
)
plt.title("Sales Data", fontweight="bold", fontfamily="monospace", fontsize=28)

plt.xlabel("Date", color="green", fontsize=14, fontweight='bold')

plt.ylabel('Amount', color="green", fontsize=14, fontweight='bold')

plt.grid()

# create a new subplot
plt2 = plt.subplot(1,2,2)
# plot the new data
plt2.plot(df1["Date"], df1["SalesAmount"])
# plt.tight_layout(pad=2.5)

# create the figure and axes objects
# fig, ax = plt.subplots()

# fig.suptitle('2026 Sales')

# ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
# ax.plot(dates, sales)

plt.show()

#showcase different lines
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, linestyle = "--")
plt.show()

plt.plot(xpoints, ypoints, linestyle = ":")
plt.show()

plt.plot(xpoints, ypoints, linestyle = "-")
plt.show()