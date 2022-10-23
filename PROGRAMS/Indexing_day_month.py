import pandas as pd 
days=[31,28,32,30]
months=["Jan","Feb","Mar","Apr"]
obj=pd.Series(index=months,data=days)
print(obj)
