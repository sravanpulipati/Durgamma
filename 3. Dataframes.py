#DataFrame is a 2-dimensional labeled data structure.
import numpy as np
import pandas as pd
#From dict of Series or dicts
a = {'data' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'Scientist' : pd.Series([11., 12., 13., 14.], index=['a', 'b', 'c', 'd'])}

type(a)
b = pd.DataFrame(a)
type(b)
b
a
#To get only data column values.
ab=pd.DataFrame(a, index=['c', 'a', 'b'], columns=['Scientist'])
ab
b.index


#From dict of ndarrays / lists
d = {'one' : [1, 2, 3, 4], 'two' : [4, 3, 2, 1]}
pd.DataFrame(d)

#From a list of dicts
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data)

#Operations using dataframe
a
a['data']
a['data'] * a['Scientist']
del a['data']

#Indexing / Selection
#Operation	                        Syntax        	Result
#Select column	                    a[col]	          Series
#Select row by label	             a.loc[label]	   Series
#Select row by integer location 	a.iloc[loc]	   Series
#Slice rows                      	a[1:4]	      DataFrame
#Select rows by boolean vector  	a[bool_vec]	  DataFrame
b['data']
b['Scientist']
a['data']
a['Scientist']
a
b
b.loc['b']
b.iloc[2]
b.columns

#Some example of creating dataframes

ab = np.random.randint(10,20)
ab

df = pd.DataFrame(np.random.randn(10,5), columns=['A', 'B', 'C', 'D','E'])
df

index = pd.date_range('1/1/2000', periods=4)
index


