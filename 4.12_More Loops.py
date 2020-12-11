#!/usr/bin/env python
# coding: utf-8

# # 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# In[6]:


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


# In[7]:


print("Printing the items of my_foods : ")
for item in my_foods:
    print(item.title())


# In[8]:


print("Printing the items of firend_foods : ")
for item in friend_foods:
    print(item.title())

