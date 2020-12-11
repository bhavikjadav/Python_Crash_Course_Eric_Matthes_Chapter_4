#!/usr/bin/env python
# coding: utf-8

# # 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# # • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# # • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# In[6]:


fav_pizzas = ["cheese", "pepperoni", "margreta"]


# In[7]:


for pizza in fav_pizzas:
    print(pizza.title())


# In[10]:


for pizza in fav_pizzas:
    print("I like " + pizza.title() + " pizza.")
print(fav_pizzas[0].title() + " pizza is my most favourite pizza.")
print(fav_pizzas[0].title() + " pizza consist blasty cheese on it.")
print(fav_pizzas[0].title() + " pizza make my mouth full of cheese..")
print("I really love pizza!")


# In[ ]:




