#!/usr/bin/env python
# coding: utf-8

# # 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# In[7]:


cubes = list(range(1, 10))


# In[9]:


for value in cubes:
    print(str(value**3), end=" ")


# In[ ]:




