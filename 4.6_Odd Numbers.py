#!/usr/bin/env python
# coding: utf-8

# # 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

# In[16]:


odd_numbers = list(range(1, 20, 2))


# In[17]:


for number in odd_numbers:
    print(str(number), end=" ")


# In[ ]:




