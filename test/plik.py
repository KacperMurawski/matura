import matplotlib.pyplot as plt  
import numpy
x = numpy.linspace(-2*numpy.pi, 2*numpy.pi,1000)
y = numpy.sin(x)
plt.plot(x,y)
plt.show()
