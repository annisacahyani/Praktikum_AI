# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:27:10 2019

@author: ASUS
"""
training_split = 0.8
# In[3]: fitur ektraksio
# last column has genre, turn it into unique ids
alldata = np.column_stack((features, labels))
# In[3]: fitur ektraksi
np.random.shuffle(alldata)
splitidx = int(len(alldata) * training_split)
train, test = alldata[:splitidx,:], alldata[splitidx:,:]
# In[3]: fitur ektraksi
print(np.shape(train))
print(np.shape(test))
# In[3]: fitur ektraksi
train_input = train[:,:-10]
train_labels = train[:,-10:]
# In[3]: fitur ektraksi
test_input = test[:,:-10]
test_labels = test[:,-10:]
# In[3]: fitur ektraksi
print(np.shape(train_input))
print(np.shape(train_labels))