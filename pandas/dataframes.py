import numpy as np
import pandas as pd 
from numpy.random import randn

# np.random.seed(101)

# df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])

# print(df)

# booldf = df > 0

# print(df[booldf])

############################################################################################################################################################################################
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

print(df.nunique(), df.value_counts())
print()
print(df['col2'].unique())
#############################################################################################################################################################################################
print(df['col2'].apply(lambda x: x**2))


print()
print()
#############################################################################################################################################################################################
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df1 = pd.DataFrame(data)

print(df1)