import math
import pylab
from matplotlib import mlab

xmin = -20.0
xmax = 20.0

dx = 0.01
xlist = mlab.frange (xmin, xmax, dx)

pylab.ion()

for a in range (50):
    ylist = [math.sin (x + a) for x in xlist]
    tlist = [math.cos(2*x) for x in xlist]
    pylab.clf()
    pylab.plot (ylist, tlist)
    pylab.draw()
    pylab.pause(0.3)


pylab.close()