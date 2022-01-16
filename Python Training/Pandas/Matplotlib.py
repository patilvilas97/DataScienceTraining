import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [48,43,45,57,38,34,37]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather Data')
plt.plot(x,y,color='red',linewidth=5,linestyle='dashdot')            ##Styles dotted, dashed, Helps to hold the graphics and style of the graph
plt.show()