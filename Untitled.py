#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import math

#np.set_printoptions(threshold=np.inf)

da = pd.read_csv('databaseAoMaAS.csv')
ta = pd.read_csv('data.tsv.csv')
ro = pd.read_csv('roles.csv', encoding = "ISO-8859-1")
le = pd.read_csv('name.csv')

da = da.dropna()
ta = ta.dropna()
ro = ro.dropna()
le = le.dropna()
da = da.groupby(['Name']).sum()

ro['Role No.'] = 1
ro = ro.groupby(['nconst']).sum()
role = pd.merge(ro,le,how='outer', on = "nconst")
role = role.drop(['nconst'], axis=1)
role = role.rename(index=str, columns={"primaryName": "Name"})
role = role.dropna()

data = pd.merge(da,ta,how='outer', on = "Name")
values = {'primaryProfession': 'actor', 'Winner': 0}
data = data.fillna(value=values)
data = data.groupby(['Name']).mean()

datarole = pd.merge(data,role,how='outer', on = "Name")
datarole = datarole.dropna()

datarole = datarole.sort_values(by="Winner", ascending = False)

display(datarole)


# In[ ]:





# In[ ]:





# In[ ]:




