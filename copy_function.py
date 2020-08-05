#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[90]:


def is_two (letter):
    if letter == 2 or letter == "2":
        return True
    else:
        return False



# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[9]:


def is_vowel (string):
    lvowel= ['a', 'e', 'i', 'o', 'u']
    uvowel= ['A', 'E', 'I', 'O', 'U']
    if (string in lvowel) or (string in uvowel):
        return True
    else:
        return False



# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[20]:


def is_consonant (string):
    lvowel= ['a', 'e', 'i', 'o', 'u']
    uvowel= ['A', 'E', 'I', 'O', 'U']
    if (string in lvowel) or (string in uvowel):
        return False
    else:
        return True
assert is_consonant("a") == False
assert is_consonant("U") == False
assert is_consonant("tomato") == True
assert is_consonant("N") == True
assert is_consonant("y") == True



# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[62]:


def word(stringer):
    if is_consonant(stringer[0])== True:
        return stringer.capitalize()
    else:
        return stringer.lower()
assert word("icedcoffee") == "icedcoffee"
assert word("cupofnoodles") == "Cupofnoodles"
assert word("twinkies") == "Twinkies"
assert word("apple") == "apple"



# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[93]:


def calculate_tip(num, num2):
    tip= num * num2
    total_bill= num + tip
    return total_bill
assert calculate_tip(50, .20) == 60
assert calculate_tip(100, .10)== 110


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied

# In[92]:


def apply_discount(num, num2):
    original_price= num
    discount_percentage= num2
    discount= num * num2
    total_price= num - discount
    return total_price
assert apply_discount (10, .20) == 8



# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[96]:


def handle_commas (string):
    return int(string.replace(",", ""))
assert handle_commas ("1,000") == 1000
assert handle_commas ("200,000") == 200000
assert handle_commas ("10")== 10



# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[102]:


def get_letter_grade (num):
    if num >= 90:
        return "A"
    elif num >= 80 and num <= 89:
        return "B"
    elif num >= 76 and num <= 79:
        return "C"
    elif num >= 70 and num <=75:
        return "D"
    elif num <= 60:
        return "D"



# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[130]:


def remove_vowels(string):
    vow = ["a", "e", "i", "o", "u"]
    chars = []
    for i in string: 
        if i.lower() not in vow:
            chars.append(i)
    return "".join(chars)



# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#         -anything that is not a valid python identifier should be removed
#         -leading and trailing whitespace should be removed
#         -everything should be lowercase
#         -spaces should be replaced with underscores
#     for example:
#         -Name will become name
#         -First Name will become first_name
#         -% Completed will become completed

# In[125]:


#def normalize_name(string):
 #   string = string.strip()
    #string = string.lower()
    #string = string.replace(" ", "_")
   # output=""
  #  for letter in string:
 #       if letter.isidentifier():
#            output += letter
#assert normalize_name(" I lOvE pYtHoN% ")== "i_love_python"
#print("Your normalize_name function is working properly.")


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#         cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#         cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[103]:


def cumulative_sum (lists):
    cumulative_list = []  
    length = len(lists)  
    cumulative_list = [sum(lists[0:x:1]) for x in range(0, length+1)]  
    return cumulative_list[1:]



# Bonus

# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 

# In[ ]:





# 2. Bonus write a function that does the opposite.

# In[ ]:





# 3. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#             col_index('A') returns 1
#             col_index('B') returns 2
#             col_index('AA') returns 27

# In[ ]: