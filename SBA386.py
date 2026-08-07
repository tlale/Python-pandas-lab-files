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
calm_colors = ['#6A9FB5','#E60000','#88C0A8', '#A3BE8C', '#EBCB8B', '#D08770','#4A4A4A','#333333' ]

#create a figure
plt.figure(figsize=(10,6))

#bar chart
plt.bar(df['month_number'], df['total_profit'], color=calm_colors[0],edgecolor='black')

#labels and title
plt.title('Company profit per month', color=calm_colors[-1], fontsize=18, fontweight='bold')
plt.xlabel('Month number', color=calm_colors[-2], fontsize=14)
plt.ylabel('Total profit', color=calm_colors[-2],  fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)
#custom y axis
plt.yticks([100000, 200000, 300000, 400000, 500000])

#display the chart
plt.show()
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
        label=col.capitalize()  +  " Sales Data"# remember the space before your string
    )

# Labels
plt.title('Sales Data', 
          color=calm_colors[0], fontsize=18, fontweight='bold')

plt.xlabel('Month number', color=calm_colors[1], fontsize=14)
plt.ylabel('Units Sold', color=calm_colors[1], fontsize=14)

# Gridlines
plt.grid(True, which='both', linestyle='--')

# Legend
plt.legend(loc='upper left',)



# X-axis ticks
plt.xticks(df['month_number'])

plt.tight_layout()
plt.show()

#“bathingsoap” sales data for each month and show it using a scatter plot
#  df['month_number'], 
#         df[col],
plt.scatter(df['month_number'],
            df['bathingsoap'],
             color=calm_colors[0],
             label='bathingsoap Sales data'
             )

plt.title('Bathingsoap Sales Data', 
          color=calm_colors[0], fontsize=18, fontweight='bold')
plt.xlabel('Month Number', color=calm_colors[1], fontsize=14)
plt.ylabel('Number of Units Sold', color=calm_colors[1], fontsize=14)
plt.grid(True, which='both', linestyle='--')
plt.legend(loc='upper left')
plt.xticks(df['month_number'])
plt.tight_layout
plt.show()

#SECTION 2
date=["25/12","26/12","27/12"]
temp=[8.5,10.5,6.8]
#buiding data frames using above data
df = pd.DataFrame({
    "Date": date,
    "Temperature": temp
})

#converting date to proper datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m")


plt.figure(figsize=(12, 6))

# Line chart using your first calm color
plt.plot(
    df['Date'],
    df['Temperature'],
    linestyle='-',
    linewidth=3,
    marker='o',
    color=calm_colors[0],        # your palette applied here
    markerfacecolor=calm_colors[0],
    markeredgecolor=calm_colors[0]
)

# Labels
plt.xlabel('Date', fontsize=14, color=calm_colors[1])
plt.ylabel('Temperature', fontsize=14, color=calm_colors[1])

# Title
plt.title('Date-wise Temperature', fontsize=18, fontweight='bold', color=calm_colors[2])

# Grid with "-" line style
plt.grid(True, linestyle='-')

plt.tight_layout()
plt.show()

#avarage weight against average height
height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]


#convert the column into the dataframe
df = pd.DataFrame({
    "Height": weight,
    "Weight": height
})
plt.figure(figsize=(12, 6))
plt.plot(
    df["Height"],
    df["Weight"],
    linestyle='--',
    linewidth=2,
    marker='o',
    color=calm_colors[0],
    markerfacecolor=calm_colors[0],
    markeredgecolor=calm_colors[0]
)
plt.xlabel("Weight in kg", fontsize=14, color=calm_colors[1])
plt.ylabel("Height in cm", fontsize=14, color=calm_colors[1])
plt.title(" Average weight with respect to average height", fontsize=18, fontweight='bold', color=calm_colors[2])
plt.legend()

plt.grid(True, linestyle='-')

plt.tight_layout()
plt.show()