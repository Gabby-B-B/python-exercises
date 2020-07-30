Identify the data type of the following values:

99.9 # is an integer
"False" # is a string
False #is a boolean
'0' #is a string
0 #is an integer
True #is a boolean
'True' # is a string
[{}] #a dictionary in a list
{'a': []} #list in a dictionary

# What data type would best represent:
# A term or phrase typed into a search box? string
# If a user is logged in? a boolean
# A discount amount to apply to a user's shopping cart? a dictionary and integer
# Whether or not a coupon code is valid? boolean
# An email address typed into a registration form? string
#The price of a product? integer
# A Matrix? integer
# The email addresses collected from a registration form? dictionary
# Information about applicants to Codeup's data science program? dictionary

For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2 # I predict an error because '1' is a string and 2 is an integer
6 % 4 # I predict that 4 can only go into 6 1 time and leave a remainder of 2
type(6 % 4) #I predict this will return that the product of this equation is an integer.
type(type(6 % 4))#I predict this will return that the product of this equation is an integer. What actually happened is that it returned type as the inner equation was a type equation.
'3 + 4 is ' + 3 + 4 # I predict an error because strings can't be concat with int.
0 < 0 #I predict that it will give the boolean result of false because 0 is not less than 0.
'False' == False #This will return the value of false because string cannot match boolean
True == 'True' #This will return the value of false because string cannot match boolean
5 >= -5 #This will return the value of true because 5 is larger than -5.
!False or False #nothing will happen because there is no command
True or "42" #True will print because 42 is a string and needs to be printed.
!True && !False #an error will occur, not pythonically correct
6 % 5 #will return 1
5 < 4 and 1 == 1 #will return false because 5 is not less than 4
'codeup' == 'codeup' and 'codeup' == 'Codeup' #will return false because c does not equal C
4 >= 0 and 1 !== '1' #error will occur because !== needs to be !=
6 % 3 == 0 #will return true because 6 does not fit into 3
5 % 2 != 0 #will return true because 5 does not fit into 2
[1] + 2 #error because list and int can't concat together
[1] + [2] #will add both together into one list
[1] * 2 #will make a list with [1,1]
[1] * [2] #error because cannot multiply lists only int
[] + [] == [] #this returned tru because [] does equal []
{} + {} #error because dictionaries cannot be concat this way


# Write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
little_mermaid = 3 * 3
brother_bear = 5 * 3
hercules= 1 * 3

total_cost = little_mermaid + brother_bear + hercules
print("Your total cost will be $",total_cost)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google= 400 * 6
amazon= 380 * 4
facebook= 350 * 10
paycheck = google + amazon + facebook
print("Your paycheck will be $",paycheck)


#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_empty= True
class_time= False
class_enroll = class_empty and class_time
print(class_enroll)

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
regular_member= True
offer_valid= True
premium_member= False

customer= regular_member and offer_valid or premium_member
print(customer)

#Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace
password_length= len(password) >= 5, print ("Password is greater than 5 characters.")
password_check= password != username, print ("Password is not the username")
username_length= len(username) <= 20, print ("Username is less than 20 characters")
space_check = (username[:1] != ' ' and username[:-1] != ' ') and (password[:1] != ' ' and password[:-1] != ' ')
good_username_and_password = password_length and username_length and password_check and space_check
print (good_username_and_password, "You have a good username and password.")