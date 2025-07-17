from collections import ChainMap
d1={'a':1,'b':6}
d2={'b':3,'c':4}
cm=ChainMap(d1,d2)
print(cm['b'])
print(cm['c'])