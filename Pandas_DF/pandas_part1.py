import numpy as np
import pandas as pd

df=pd.read_csv(filepath_or_buffer=r"C:\Users\syedn\OneDrive\Desktop\Test.csv")
pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)

print(df.head(3))
print(df.shape[0].df.shape[1])
