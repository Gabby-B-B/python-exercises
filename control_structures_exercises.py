#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Conditional Basics
#prompt the user for a day of the week, print out whether the day is Monday or not
print("Please input a day of the week: ")
day = input()
if day.lower in input() == 'monday':
    print("Thank you for choosing Monday")
else:
    print("You did not choose Monday. Please choose another day of the week.")


# In[1]:


#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
print("Please input a day of the week: ")
day = input()
if day.lower() in input() == 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday':
    print(day, "is a weekday.")
else:
    print (day, "is on the weekend.")
    


# In[2]:


#create variables and make up values for

#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

print("Please input how many hours you worked.")
hours_worked= int(input())
print ("Please input your hourly rate of pay.")
hourly_pay= float(input())             
if hours_worked < 41:
    total_no_overtime= hours_worked * hourly_pay
    print("Your gross pay is: $",round(total_no_overtime, 2))
else:
    overtime_pay= hourly_pay * 1.5
    overtime_hours= hours_worked - 41
    hours= 40
    total_with_overtime = (hours * hourly_pay) + (overtime_hours * overtime_pay)
    print("Your gross pay is: $",round(total_with_overtime, 2))


# In[5]:


#2. Loop Basics
#While


# In[3]:


#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <16 :
    print(i)
    i+=1


# In[6]:


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
by_twos = 0
while by_twos <101:
    print(by_twos)
    by_twos +=2


# In[9]:


#Alter your loop to count backwards by 5's from 100 to -10.
minus_fives= 100
while minus_fives > -11:
    print(minus_fives)
    minus_fives -= 5


# In[35]:


#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
squareds = 2
while squareds < 1000000:
    print(squareds)
    squareds = squareds ** 2


# In[12]:


# Write a loop that uses print to create the output shown below.
minus_five= 100
while minus_five > 0:
    print(minus_five)
    minus_five -= 5


# In[ ]:


# B. For Loops


# In[36]:


#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
print("Please input a number:")
num= int(input())

for n in range(1,11):
    print(num, "x", n, "=", num*n)


# In[16]:


#Create a for loop that uses print to create the output shown below.
for n in range (10):
    print(str(n)*n)


# In[ ]:


# C. Break and Continue


# In[5]:


#Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to 
#output all the odd numbers between 1 and 50, except for the number the user entered.
print("Please enter an odd number between 1 and 50:")
odd_number= int(input())
if odd_number in range(0,51) and odd_number % 1 ==1:
    print("Thank you for choosing a valid number.")
else:
    print ("You did not choose a valid number. Please choose an odd number between 1 and 50.")


# In[7]:


#The input function can be used to prompt for input and use that input in your python code. 
#Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number,
#also note that the input function returns a string, so you'll need to convert this to a numeric type.)
print("Please enter a positive number:")
pos_num= int(input())
for pos_num in range(0, pos_num+1, 1):
    print(pos_num)


# In[3]:


#Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.
print("Please enter a positive integer:")
positive_integer= int(input())
for positive_integer in range(positive_integer, 0, -1):
    print(positive_integer)


# In[28]:


# 3. Fizz Buzz
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
i=1
for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)


# In[ ]:


#Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
#Example Output

#What number would you like to go up to? 5

#Here is your table!

#number | squared | cubed
#------ | ------- | -----
#1      | 1       | 1
#2      | 4       | 8
#3      | 9       | 27
#4      | 16      | 64
#5      | 25      | 125
#Bonus: Research python's format string specifiers to align the table
continues= input("Do you want to continue?")
while continues == "yes" or continues == "y":
    up_to= int(input("What number do you want to go up to?"))
    for n in range (n, up_to+1):
        squared= n ** 2
        cubed=  n ** 3
        print(f"{n} | {squared} | {cubed}")
    continues= input("Do you want to continue?")
    if continues not in ["yes", "y"]:
        print("The code will not continue per your request.")


# In[74]:


#5.
# Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
#F : 59 - 0
# BONUS Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
continues= input("Do you want to continue? ")
while continues == "yes" or continues == "y":
    numerical_grade = int(input("Please input a numerical grade from 1 to 100: "))
    if numerical_grade in range(87, 101):
        print(numerical_grade,"is an A.")
    elif numerical_grade in range(79,88):
        print(numerical_grade,"is a B.")
    elif numerical_grade in range(67,80):
        print(numerical_grade, "is a C.")  
    elif numerical_grade in range(60,67):
        print(numerical_grade, "is a D.")  
    elif numerical_grade <=59:
        print(numerical_grade, "is a F.") 
    continues= input("Do you want to continue?")
    if continues not in ["yes", "y"]:
        print("The code will not continue per your request")


# In[90]:


# 6. 
#Create a list of dictionaries where each dictionary represents a book that you have read. 
#Each dictionary in the list should have the keys title, author, and genre. 
#Loop through the list and print out information about each book.
#Prompt the user to enter a genre, 
#then loop through your books list and print out the titles of all the books in that genre.
books = [
    {
        "title": "Alan Turing: The Enigma",
        "author": "Andrew Hodges",
        "genre": "Biography"
    },
    {
        "title": "This is where I leave you",
        "author": "Jonathan Tropper",
        "genre": "Adult Fiction"
    },
    {
        "title": "Me",
        "author": "Elton John",
        "genre": "Biography"
    },
    {
        "title": "Orange is the new black: My year in a women's prison",
        "author": "Piper Kerman",
        "genre": "Biography"
    }
]


# In[ ]:




