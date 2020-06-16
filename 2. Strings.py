import numpy as np
import pandas as pd
#Working with Text data
s = pd.Series(['data', 'scientist', 'python', np.nan, 'pandas'])
s
s[1:]


s.str.lower()
s.str.upper()
s.str.len()

#string methods on Index are especially useful for cleaning up or transforming DataFrame columns
data = pd.DataFrame(np.random.randn(3,2), columns=[' one ', ' two '],index=range(3))
data
#ince df.columns is an Index object, we can use the .str accessor
data.columns.str.strip()
data.columns.str.upper()
data.columns.str.strip().str.lower().str.replace('o', 'k')

#Splitting based on any character
s
s.str.split('t')

#Elements in the split lists can be accessed using get or [] notation:
s.str.split('t').str.get(1)
s.str.split('t').str[0]

#to limit the number of splits:
s.str.split('a',expand=True, n=1)

#To replace
s.str.replace('da|sci', 'on ', case=False)

#Concatenation
s.str.cat()
s.str.cat(sep='-')
s.str.cat(sep=',', na_rep='-')

#By default, missing values are ignored so use na_rep
s.str.cat(['A', 'B', 'C', 'D','E'])

#Concatening 's' and 'b'
b = pd.Series(['z', 'a', 'b', 'd', 'e'], index=[-1, 0, 1, 3, 4])
b
s
s.str.cat(b, join='right', na_rep='-')
s.str.cat(b, join='left', na_rep='-')
s.str[0]





