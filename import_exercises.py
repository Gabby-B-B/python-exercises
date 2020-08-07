#!/usr/bin/env python
# coding: utf-8

# Import and test 3 of the functions from your functions exercise file.
# 
# Import each function in a different way:
# 
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name
# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# In[1]:


import pythonintro as p


# In[12]:


from copy_function import calculate_tip as tp
tp(10,.1)


# In[13]:


from copy_function import is_two
is_two(2)


# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# 2. How many different ways can you combine two of the letters from "abcd"?

# In[ ]:


import itertools


# In[47]:


[''.join(p) for p in permutations('abc123')]


# In[46]:


alpha= "abcd"
a = combinations(alpha, 2)  
b = [' '.join(i) for i in a]
b


# In[6]:


import json
profiles = json.load(open('profiles.json'))


# In[41]:


## total number of users
total_number_of_users = len(profiles)
print('The total number of users is', total_number_of_users)


# In[39]:


## number of active users
active_users= len([profile for profile in profiles if profile['isActive']])
print("The number of active users is",active_users)


# In[38]:


## number of inactive users
inactive_users= len([profile for profile in profiles if not profile['isActive']])
print("The number of inactive users is", inactive_users )


# In[33]:


def balanced (balances):
    balances = [profile['balance'] for profile in profiles]
    balances = [balance.replace(',', '') for balance in balances]
    balances = [balance.replace('$', '') for balance in balances]
    balances = [float(balance) for balance in balances]
## Grand total of balances for all users
grand_total_of_all_balances= sum(balances)
print("The grand total of balances for all users is $", grand_total_of_all_balances)


# In[21]:


## Average balance per user
average_balance = sum(balances) / len(balances)
print("The average balance per user is $", round(average_balance, 2))


# In[36]:


## User with the lowest balance


# In[37]:


## User with the highest balance


# In[50]:


## Most common favorite fruit
most_common_favorite_fruits = [profile['favoriteFruit'] for profile in profiles]
count_fruits = {}
for fruit in most_common_favorite_fruits:
    if fruit in count_fruits:
        count_fruits[fruit] += 1
    else:
        count_fruits[fruit] = 1
max_count_fruits=max(count_fruits)
print("The most common favorite fruit is", max_count_fruits)


# In[51]:


## Least most common favorite fruit
min_count_fruits= min(count_fruits)
print("The least common favorite fruit is", min_count_fruits)


# In[ ]:


## Total number of unread messages for all users

