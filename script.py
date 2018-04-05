# Creating a line graph from data
#Changing the appearance of the line
#Zooming in on different parts of the axis
#Putting labels on titles and axes
#Creating a more complex figure layout
#Adding legends to graphs
#Changing tick labels and positions
#Saving what you've made'''

import codecademylib
from matplotlib import pyplot as plt
x=[0,1,2,3,4,5]
y1=[6,7,8,9,10,11]
y2=[12,13,14,15,16,17]
plt.plot(x,y1,color='pink',marker='o')
plt.plot(x,y2,color='gray',marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend([x,y1,y2],loc=4)
plt.show
