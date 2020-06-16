import numpy as np
import pandas as pd

Salary = pd.read_csv('C:/Users/admin/Desktop/Salary_Data.csv')
print(Salary)
type(Salary)
#To get top 5 rows
Salary.head()
#To get info about Salary_Data.csv
Salary.info()

#To convert into string
#print(Salary.to_string())
#Salary.info()

abc=Salary.to_string()
print(abc)
type(abc)
abc.info()


#Getting a newcolumn based on old coulmns
Salary.assign(New = Salary['YearsExperience'] * Salary['Salary'])
#Getting plot
Salary.query('Salary > 100000').plot(kind='scatter', x='YearsExperience', y='Salary')

Salary.mean(0)#0 means based on coolumns
Salary.mean(1)#1 means based on rows
#skipna option signaling whether to exclude missing data (True by default):
Salary.sum(0, skipna=False)

#Examples
#   Function	  Description
#    count	     Number of non-NA observations
#    sum       Sum of values
#    mean	     Mean of values
#    mad	     Mean absolute deviation
#    median	 Arithmetic median of values
#    min	    Minimum
#    max	    Maximum
#    mode	    Mode
#    abs	    Absolute Value
#    prod	    Product of values
#    std	    Bessel-corrected sample standard deviation
#    var	    Unbiased variance
#    sem	    Standard error of the mean
#    skew	    Sample skewness (3rd moment)
#    kurt	    Sample kurtosis (4th moment)
#    quantile	 Sample quantile (value at %)
#    cumsum	 Cumulative sum
#    cumprod	 Cumulative product
#    cummax	 Cumulative maximum
#    cummin	 Cumulative minimum

Salary.describe()
Salary.describe(include=['number'])

# To include only number object if both numbers and strings are there.
Salary.describe(percentiles=[.05, .25, .75, .95])


#For a non-numerical Series object
s = pd.Series(['a', 'b', np.nan, 'c', 'd', 'a'])
s
s.describe()
s.describe(include=['number'])
# To include only 'object' not 'number' type.

# To count all values
data = np.random.randint(1000, 9999, size=10)
data
pd.Series(data).value_counts()
pd.Series(data).mode()


df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                    'numeric': [1, 2, 3],
                    'object': ['a', 'b', 'c']
                   })

df
df.describe(include='all')





















