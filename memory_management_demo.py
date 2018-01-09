# reference cycle example
a = [1, 2, 0]
b = [3, 2, 0]
a[2] = b[0]
b[2] = a[0]

# simplest reference cycle example
c = list()
c.append(c)
# i.e.
c[0] = c

import gc


# dereference object c
del c
# get_count() returns a tuple of (threshold, no. of objects allocated, no. of objects de-allocated)
print(gc.get_count())
# With no arguments, run a full collection
print(gc.collect())
print(gc.collect())
