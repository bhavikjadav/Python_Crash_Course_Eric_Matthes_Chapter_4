#!/usr/bin/env python
# coding: utf-8

# # 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# # • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# # • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

# In[6]:


animals = ["cat", "dog", "tiger"]


# In[7]:


for animal in animals:
    print("A " + animal.title() + " would make a great pet.")


# In[8]:


print("All above displayed animal have same chractiristics like: ")
print("All the animals have 4 legs.")
print("All the animals have a tail.")
print("All the animals are mostly same.." + ":)")


# In[9]:


print("Any of these animals would make a great pet!")


# In[ ]:




