import numpy

types = numpy.load('arrests/types.npy', allow_pickle=True)
print(numpy.unique(types))