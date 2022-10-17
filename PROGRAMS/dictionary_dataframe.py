#Program to create a dataframe using the dictionary

import pandas as pd
dict1={'Book':['Ikigai','Twisted Faith','Last of the Firedrakes','Rise of the Dawnstar'],'Shelf':[7,15,11,8]}
df1=pd.DataFrame(dict1)
print(df1)

