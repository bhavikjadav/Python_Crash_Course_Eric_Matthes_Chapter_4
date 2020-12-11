#!/usr/bin/env python
# coding: utf-8

# # 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# # • Use a for loop to print each food the restaurant offers.
# # • Try to modify one of the items, and make sure that Python rejects the change.
# # • The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# In[8]:


foods = ("idli", "vada", "dosa", "sambhar", "chatuny")


# In[9]:


for food in foods:
    print(food.title())


# In[10]:


# foods[1] = "gulab jamun" # This line will throws the error as line 3 in the program definition.


# In[11]:


foods = ("idli", "gulaab jamun", "dosa", "pauwa", "chatuny")


# In[12]:


for food in foods:
    print(food.title())

