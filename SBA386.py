import pandas as pd
import matplotlib.pyplot as plt
#read the csv file to work with
df = pd.read_csv('./data/woocommerce-product-export.csv')
#print(df)
#Show a concise summary of the columns using the info() method.
print('\n==========Summary of the columns==========')
print(df.info())
#Show a summary of statistics pertaining to the columns. 
print('\n==========Summary of the  Statistics==========')
print(df.describe(include='all'))

#Print the first five rows by default
print('\n==========first five rows==========')
print(df.head(5))

#Print the last five rows by default
print('\n==========last five rows==========')
print(df.tail(5))

#Print  the "total_profit" and “month_number” columns only.
print('\n==========Total profit per month ==========')
print(df[['total_profit', 'month_number']])

#Read the total profit of all months and show it using the Bar plot. 
print('\n==========Bar chart ==========')
# plt.xlabel
# plt.ylabel
# plt.title
calm_colors = ['#6A9FB5''#E60000','#88C0A8', '#A3BE8C', '#EBCB8B', '#D08770','#4A4A4A','#333333' ]

#create a figure
#plt.figure(figsize=(10,6))

# bar chart
# plt.bar(df['month_number'], df['total_profit'], color=calm_colors[0],edgecolor='black')

# #labels and title
# plt.title('Company profit per month', color=calm_colors[-1], fontsize=18, fontweight='bold')
# plt.xlabel('Month number', color=calm_colors[-2], fontsize=14)
# plt.ylabel('Total profit', color=calm_colors[-2],  fontsize=14)
# plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)
# #custom y axis
# plt.yticks([100000, 200000, 300000, 400000, 500000])

# #display the chart
# plt.show()
#hide above bar graph code to make the line dot graph
#

#sales data and multi line plot
plt.figure(figsize=(12, 6))

# each product and plot its monthly units sold
# Product columns based on your summary table
product_columns = ['facecream', 'facewash', 'toothpaste', 
                   'bathingsoap', 'shampoo', 'moisturizer']

for i, col in enumerate(product_columns):
    plt.plot(
        df['month_number'],
        df[col],
        linestyle='--',
        linewidth=3,
        marker='o',
        color=calm_colors[i % len(calm_colors)],
        markerfacecolor=calm_colors[i % len(calm_colors)],
        markeredgecolor=calm_colors[i % len(calm_colors)],
        label=col.capitalize()
    )

# Labels
plt.title('Units Sold Per Month for Each Product', 
          color=calm_colors[0], fontsize=18, fontweight='bold')

plt.xlabel('Month number', color=calm_colors[1], fontsize=14)
plt.ylabel('Units Sold', color=calm_colors[1], fontsize=14)

# Gridlines
plt.grid(True, which='both', linestyle='--')

# Legend
plt.legend(loc='upper left')

# X-axis ticks
plt.xticks(df['month_number'])

plt.tight_layout()
plt.show()