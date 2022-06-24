import matplotlib.pyplot as plotter

 

# The slice names of a population distribution pie chart

pieLabels= 'Asia', 'Africa', 'Europe', 'North America' 

# Population data

populationShare = [30,30,20,21]
figureObject, axesObject = plotter.subplots()

 

# Draw the pie chart

axesObject.pie(populationShare,labels=pieLabels,autopct='%1.2f',startangle=90)

 

# Aspect ratio - equal means pie is a circle

axesObject.axis('equal')

 

plotter.show()
