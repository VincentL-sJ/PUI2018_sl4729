import numpy as np
import matplotlib as mpl
import pylab as pl

%pylab inline

dist_container = []
for i in range(100):
    size=int(np.random.rand()*1900+10)
    dist=np.random.randn(size)
    dist_container.append(dist)
dist_container