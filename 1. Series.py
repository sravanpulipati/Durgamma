import numpy as np
import pandas as pd
#Series is a one-dimensional labeled array capable of holding 
#any data type (integers, strings, floating point numbers, Python objects, etc.)
#Series created using ndarray

s = pd.Series(np.random.randn(4), index=['d', 'a', 't', 'a'])
s
s.index

#constant number passed as data for series representation
ts=pd.Series(10,index=['A','B','C'])
ts

# using range 
ts1=pd.Series(range(3),index=['A','B','C'])
ts1

#using arange 
ts2=pd.Series(np.arange(1,20,7),index=['A','B','C'])
ts2

#using one-dimension array 
ts3=pd.Series(np.array(np.arange(1,20,7)),index=['A','B','C'])
ts3

#using 2-dimension array which gives error
ts4=pd.Series(np.array([np.arange(1,20,7)]),index=['A','B','C'])
ts4

#pandas array vs Numpy Array
type(pd.array(np.arange(1,20,7)))
type(np.array(np.arange(1,20,7)))


#Series can be instantiated from dicts


d = {'d' : 0, 'a' : 1, 'c' : 2}
s1 = pd.Series(d)
s1
type(s1)
s1.index
pd.Series(d, index=['a', 'b', 'c', 'd'])


#Series created using scalar value
pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])

#To access data using index
s
s.mean()
s[s < s.mean()]
s[:2]
s[:3]
np.exp(s)
s['d']
'f' in s
'a' in s
#Operations using Series
s * 2
s[1:] + s[:-1]


