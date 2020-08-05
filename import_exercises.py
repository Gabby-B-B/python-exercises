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

