import matplotlib.pyplot as plt

Expense_Categories = ['Groceries', 'Utilities', 'Transportation', 'Dining Out', 'Entertainment']
Amount_Spent = [500, 300, 200, 400, 250]
calm_colors = ['#6A9FB5', '#88C0A8', '#A3BE8C', '#EBCB8B', '#D08770']

#create a figure
plt.figure(figsize=(6,4))

#horizontal bar chart
plt.barh(Expense_Categories, Amount_Spent, color=calm_colors)

#labels and title
plt.title('Monthly Expenses Distribution', color='black', fontsize=18, fontweight='heavy')
plt.xlabel('Expense Categories', color='#4A4A4A', fontsize=14)
plt.ylabel('Amount Spent', color='#4A4A4A', fontsize=14)


#display the chart
plt.show()


