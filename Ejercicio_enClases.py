#import numpy as np

#a=np.array([1,2,3])
#print(a)

#b=np.array([(1,2,3),(4,5,6)])
#print(b)

import sys
import numpy as np
array_1=range(1000) #array NORMAL de mil elementos
print(array_1)
#muestra cuento de memoria utiliza el array normal
print(sys.getsizeof(16)*len(array_1))

array_2=np.arange(1000) #array NUMPY de mil elementos
#muestra cuanto de memoria utiliza el array creado con numpy
print(array_2.size*array_2.itemsize)