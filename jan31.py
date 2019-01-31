import numpy as np
import scipy as sp
import pandas as pd

n = 100

t=pd.date_range('20190101',periods=n)
print(t)
df=pd.DataFrame(np.random.randn(n,10),index=t, columns=list('ABCDEFGHIJ'))
print(df.describe())
