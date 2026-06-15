# spliting besicaluy break mtrix
# splitung is two type

import numpy as np
a=np.arange(16).reshape(4,4)

# horizontal
b=np.hsplit(a,2)
print(b)

# vertical
b=np.vsplit(a,2)
print(b)

