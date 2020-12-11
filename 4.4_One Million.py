#!/usr/bin/env python
# coding: utf-8

# # 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

# In[5]:


one_million = list(range(1, 1000001))


# In[6]:


for data in one_million:
    print(str(data), end =" ")


# In[ ]:




