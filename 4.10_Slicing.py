#!/usr/bin/env python
# coding: utf-8

# # 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# # • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# # • Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# # • Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

# In[20]:


fav_places = ["miami", "loandon", "santrioni", "malasiya", "egypt", "austria"]


# In[21]:


print("First three places in the list are : ")
for place in fav_places[:3]:
    print(place.title())


# In[22]:


print("Middle three places in the list are : ")
for place2 in fav_places[2:5]:
    print(place2.title())


# In[23]:


print("Last three places in the list are : ")
for place3 in fav_places[3:]:
    print(place3.title())

