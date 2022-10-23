import pandas as pd
import numpy as np
d1= {'Devices': ['Laptop', 'Television','Mobile','Tablet'],
     'Codes' : ['05','09', '07', '01'],
     'Colour': ['Pink','Green','Grey','Blue']}
dfd=pd.DataFrame(d1)
print(dfd)


dfd.to_csv("c:\\sanjana\\devices.csv")


