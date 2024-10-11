''' Strings are collection of alphanumeric must be written in single or double quotes. strings are
Immutable'''
# Declaring a string

my_str = 'Hey I am  Python    '

''' These are the majorly uses string inbuilt functions'''

# String Manipulation
'''upper = my_str.upper() # Converting string in to capital letters

lower = my_str.lower() # Converting string in to small letters

check = my_str[0]=='r' # This checks wether that character present in that string are not

cap = my_str.capitalize() # This will covert the entrire string in to small letters except first letter

end = my_str.endswith('n') # This will checks, is that string ends with your desired char are not

count = my_str.count('h') # It will checks no of char's present in that string

split = my_str.split() # It splits the string in to list of string

strip = my_str.strip() # It removes the spaces in starting and the end of string

join = '$'.join(my_str) # It joins the specific char in the strings

en = my_str.encode() # It encodes the string

index = my_str.index('I') # It tells the index value of desired character

print(split)'''

# By using slicing we can get sub part of the string EX: my_str[0:3]

# WAP to find enterd value is palindrome are not

palindrome = input("Enter any character : ")
if palindrome[0] == palindrome[-1]:
    print (palindrome,"is a palindrome")
else:
    print(palindrome,"is not palindrome")
