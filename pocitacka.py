
# coding: utf-8

# In[27]:

import pandas as pd
import numpy as np


# In[2]:

data = pd.read_excel(r'data/zu_prodeje.xlsx')


# In[8]:

statut = pd.read_excel(r'data/organizace_statut.xlsx')


# In[10]:

data = data.merge(statut, left_on='organizace', right_on='nazev', how='left')


# In[ ]:

def nuller(value):
    if (value != value):
        return 's'
    else:
        return value
    
data.status = data.status.apply(lambda x: nuller(x))


# In[26]:

#vsecko
#status: s - soukromé, v - veřejné, vz - vzdělávací
data.groupby('status')[['cena za produkt', 'cenacelkemzaobjednávku']].sum()


# In[25]:

#dmr5
data[data['kód produktu'] == 64111].groupby('status')[['cena za produkt', 'cenacelkemzaobjednávku']].sum()

