#!/usr/bin/env python
# coding: utf-8

# In[4]:
import pandas as pd
df = pd.read_csv('Guitar-Notes.csv')
notes = df[['String-1','String-2','String-3','String-4','String-5','String-6']]
print(notes)
