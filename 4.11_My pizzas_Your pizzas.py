#!/usr/bin/env python
# coding: utf-8

# # 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# # • Add a new pizza to the original list.
# # • Add a different pizza to the list friend_pizzas.
# # • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

# In[5]:


my_pizzas = ["cheese", "pepperoni", "margreta", "butter"]
friends_pizzas = ["cheese", "pepperoni", "margreta", "canzui"]


# In[6]:


print("The following are my pizzas : ")
for pizza in my_pizzas:
    print(pizza.title())


# In[7]:


print("The following are my friends pizza : ")
for pizza in friends_pizzas:
    print(pizza.title())

