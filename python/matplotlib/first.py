import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Create data
# x=np.arange(0,10)
# y=np.arange(11,21)

'''
# Plot the data in the form of graph
plt.scatter(x,y,c='r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My first graph')
plt.savefig('firstgraph.png') saves the graph in the form of a png file
plt.show()
'''


''' 
y=x*x
# Plot the new data in the form of graph
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My second graph')
plt.savefig('secondgraph.png')
plt.plot(x,y,'r*', linestyle='dashed', linewidth=2, markersize=12)
plt.show()
'''


'''
#Creating Subplots
y=x*x
plt.subplot(2,2,1)
plt.plot(x,y,'r*-')
plt.subplot(2,2,2)
plt.plot(x,y,'b--')
plt.subplot(2,2,3)
plt.plot(x,y,'go')
plt.subplot(2,2,4)
plt.plot(x,y,'yD')
plt.show()
'''


'''
#plotting straight line graph as y=mx+c
x=np.arange(1,11)
y=3*x+11
plt.title('My third graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y)
plt.show()
'''


'''
#compute the x and y coordinates for points on a sine curve
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.title('Sine wave form')
#plot the points using matplotlib
plt.plot(x,y)
plt.show()
'''

'''
#plotting subplots for sine and cosine functions
#compute the x and y coordinates for points on a sine and cosine curve
x=np.arange(0,7*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)

#setup a subplot grid that has height 2 and width 1, and set the first such subplot as active
plt.subplot(2,1,1)

#make the first plot
plt.plot(x,y_sin,'r')
plt.title('Sine wave form')

#setup a subplot grid that has height 2 and width 1, and set the second such subplot as active
plt.subplot(2,1,2)
#make the second plot
plt.plot(x,y_cos,'b')
plt.title('Cosine wave form')

plt.show()
'''


'''
# Bar Plots
x1=[2,8,10]
y1=[11,16,4]

x2=[3,9,11]
y2=[6,15,7]

plt.bar(x1,y1,align='center')
plt.bar(x2,y2,color='r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Bar Plots')
plt.legend()
plt.show()
'''

'''
#Histograms
a=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a)
plt.title('Histogram')
plt.show()
'''

'''
# Box Plots
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('Box Plot')
plt.show()
'''


#Pie chart
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

#plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart')

plt.axis('equal')
plt.show()
