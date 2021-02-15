#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


# In[2]:


df = pd.read_csv("final_df.csv")


# In[5]:


df.head()


# In[3]:


df.columns


# In[8]:


X=df.drop('price',axis=1)
y=df.price


# In[9]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=51)


# In[10]:


model = pickle.load(open("RFR_nobroker.pkl","rb"))


# In[11]:


def predict_price(flooring, facing, location, area, bedroom, bathroom, balcony, parking, power, age, furnishing, transit):    
    floor_index = np.where(X.columns==flooring)[0][0]
    facing_index = np.where(X.columns==facing)[0][0]
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[26] = area
    x[0] = bedroom
    x[1] = bathroom
    x[2] = balcony
    x[3] = parking
    x[4] = power
    x[5] = age
    x[6] = furnishing
    x[7] = transit
    
    if floor_index >= 0:
        x[floor_index] = 1
        
        
    if facing_index >= 0:
        x[facing_index] = 1

    if loc_index >= 0:
        x[loc_index] = 1   
        
    prediction= model.predict([x])[0]
    prediction= np.exp(prediction)
    
    return int(prediction)


# In[ ]:




