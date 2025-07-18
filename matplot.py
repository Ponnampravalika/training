import matplotlib.pyplot as plt
#basic lineplot
"""x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.title("linechart")
plt.xlabel("x-axis")
plt.ylabel("y=axis")
plt.grid(True)
plt.show()"""
#Barchart
"""categories=['a','b','c']
values=[10,20,15]
plt.bar(categories,values)
plt.title("bar chart")
plt.show()"""
#scatterplot
x=[1,2,3,4,5]
y=[2,4,1,8,7]
plt.scatter(x,y,color='red')
plt.title("scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
