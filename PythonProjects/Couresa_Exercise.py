###########################
# Couresa Exercise
###########################
# Function
#
# def greeting( name, dep):
#     print("Welcome " , name)
#     department = dep
#     print("To the department: ", department)
#
# greeting( "John", "IT")

# Return value
# def time_seconds(hour, minutes, seconds):
#     total_second = hour*3600 + minutes*60 + seconds
#     return total_second
# TS = time_seconds(1,30,0)
# print("time in seconds : ", TS)

# ==================================================
# Return Multiple values
#
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     min = (seconds- (hours*3600)) // 60
#     sec = seconds- (hours*3600) - (min * 60)
#     return hours, min, sec
#
# hr, min, sec = convert_seconds(5300)
# print(hr)
# print(min)
# print(sec)

# result=convert_seconds(5300)    # tuple as function return more than one value
# print(type(result))

# ==================================================
# Reuse of the Code
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

# def month_days(month, days):
#     print(month+ " has "+ str(days)+" days.")
# month_days("June", 30)
# month_days("July", 31)
# ==================================================
# If-Else
# def is_positive(number):
#   if number > 0:
#     return True
#   else:
#     return False

# ==================================================
# Print name in this format --> Name: lastname, firstname
#
# def format_name(first_name, last_name):
# 	# code goes here
# 	if len(first_name)!=0 and len(last_name)!=0:
# 	elif len(first_name)==0 and len(last_name)==0:
# 		name = ""
# 		name = "Name: "+ last_name+", "+first_name
# 	elif len(first_name) !=0 and len(last_name)==0:
# 		name = "Name: "+ first_name
# 	elif len(first_name) ==0:
# 		name = "Name: "+ last_name
# 	return name
#
# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"
#
# print(format_name("", ""))
# # Should return an empty string
# ==================================================
# Find the longest word
# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2) >= len(word1) and len(word2) >= len(word3):
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)
#
# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))

# ==================================================
# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1).
# Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0,
# the function should return 0 instead of attempting the division.
# def fractional_part(numerator, denominator):
#     if numerator > 0 and denominator > 0:
#         number = numerator / denominator
#         return (number - int(number))
#     else:
#         return 0
#
# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0
# ==================================================
# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor =factor +1
#   return "Done"
#
# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT

# ==================================================
# def is_power_of_two(n):
#     # Check if the number can be divided by two without a remainder
#     while n % 2 == 0:
#         if n > 1:
#             return True
#         break
#     # If after dividing by two the number is 1, it's a power of two
#     if n == 1:
#         return True
#     # elif n== 0 :
#     #         return False
#     return False
#
#
# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False

# ==================================================
# def sum_divisors(n):
#   sum = 0
#   number = 1
#   if n!=0:
#     while number < n:
#       if (n % number) == 0 :
#         sum = sum + number
#       number +=1
#   # Return the sum of all divisors of n, not including n
#   return sum
#
# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

# ==================================================

# Result of multiplication should not exceeed through 25
# def multiplication_table(number):
# 	# Initialize the starting point of the multiplication table
# 	multiplier = 1
# 	# Only want to loop through 5
# 	while multiplier <= 5:
# 		result = number*multiplier
# 		# What is the additional condition to exit out of the loop?
# 		if result > 25 :
# 			break
# 		print(str(number) + "x" + str(multiplier) + "=" + str(result))
# 		# Increment the variable for the loop
# 		multiplier += 1
#
# multiplication_table(3)
# # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
#
# multiplication_table(5)
# # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
#
# multiplication_table(8)
# # Should print: 8x1=8 8x2=16 8x3=24
# ==================================================
# Validate the user through list and for loop
# def validate_users(users):
#     for user in users:
#         if is_valid(user):
#             print(user + " is valid")
#         else:
#             print(user + " is invalid")
#         name=['purplecat']
#         validate_users(name)

# ==================================================
# Factorial display with respect to number in the given range
#
# def factorial(n):
#     result = 1
#     for x in range(1,n+1):
#         result = result* x
#         x+=1
#     return result
#
# for n in range(0,9):
#     print(n, factorial(n))
# ==================================================
# multiple of 7 from 0 to 100
# for i in range(0,100):
#     if (i % 7) == 0:
#         print(i)
# ==================================================
# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
# Stop when succeeded
# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")
#
# retry(create_user, 3)
# retry(stop_service, 5)
# ==================================================
# Recursion example of factorial
# Calling funtion within function
# def factorial(n):
#     if n < 2:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
# ==================================================
# Should print one line per letter
# def show_letters(word):
# 	for x in word:
# 		print(x)
#
# show_letters("Hello")
# ==================================================
# Print the number of digit in a NUMBER
# def digits(n):
#     count = 0
#     if n == 0:
#         return 1
#     while (n>0):
#         count += 1
#         n = n//10
#     return count
#
# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1
# ==================================================
# # Should print the multiplication table shown above
# def multiplication_table(start, stop):
# 	for x in range(start, (stop+1)):
# 		for y in range (start, (stop+1)):
# 			print(str(x*y), end=" ")
# 		print()
#
# multiplication_table(1, 3)
# ==================================================
# count up and down
#
# def counter(start, stop):
#     x = start
#     if x > stop:
#         return_string = "Counting down: "
#         while (x >= stop):
#             return_string += str(x)
#             if x >stop:
#                 return_string += ","
#             x -=1
#     else:
#         return_string = "Counting up: "
#         while (x <= stop):
#             return_string += str(x)
#             if x != stop:
#                 return_string += ","
#             x +=1
#     return return_string
#
# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))  # Should be "Counting down: 2,1"
# print(counter(5, 5))  # Should be "Counting up: 5"

# ==================================================
# Print even number till the parameter

# def even_numbers(maximum):
# 	return_string = ""
# 	for x in range(2, (maximum+1),2):
# 		return_string += str(x) + " "
# 	return return_string.strip()
#
# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed4

# ===================================================
# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year
#why error? Variable not defined
# ==================================================
# for x in range(1, 10, 3):
#      print(x)
# #1
# #4
# #7
# ==================================================
# for x in range(10):
#     for y in range(x):
#         print(y)
## answer : 8
# ==================================================
# def votes(params):
# 	for vote in params:
# 	    print("Possible option:" + vote)
#
# votes(['yes', 'no', 'maybe'])
# ==================================================

# ==================================================
#       STRING
# ==================================================
# Match 1st and last character of a string
#
# def first_and_last(message):
#     if message:
#         return message[0] == message[-1]
#     return True
#
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))
# print(first_and_last("A"))

# Slicing a String
# word = "pineapple"
# print(word[:4])
# print(word[4:])

# word = "Pine Apple "
# print(word.upper())
# print(word.lower())
# print(word.split())
# print(word.strip())
# print(word.count("p"))
# print(word.endswith("le "))

# print( " Eat : ".join(["apple", "egg"]))

#  Return the Short FORM in UPPER CASE
# def initials(phrase):
#     words = phrase.upper()
#     result = ""
#     for word in words.split():
#         result += word[0]
#     return result
#
# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# Formatting the float value
# price =7.5
# with_tax = price*1.09
# print("{:.2f} ".format(with_tax))

# ==================================================
# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for word in input_string:
# 		# Add any non-blank letters to the
# 		# end of one string, and to the front
# 		# of the other string.
# 		if word.replace(" ",""):
# 			new_string = new_string + word
# 			reverse_string = word + reverse_string
# 	# Compare the strings
# 	if new_string.lower()==reverse_string.lower():
# 		return True
# 	return False
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# ==================================================
# def replace_ending(sentence, old, new):
#     # Check if the old string is at the end of the sentence
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the
#         # end with the new string
#         i = sentence.rfind(old)
#         new_sentence = sentence[:i]+new
#         return new_sentence
#
#     # Return the original sentence if there is no match
#     return sentence
#
#
# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# #Should display "The weather is nice in April"

# ==================================================

# def get_word(sentence, n):
# 	# Only proceed if n is positive
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")
#
# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

# ==================================================
#   LIST and TUPLES
# ==================================================

# Create a new list by skipping the index diff by 2

# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0
#
# 	# Iterate through the list
# 	for value in elements:
# 		# Does this element belong in the resulting list?
# 		if i<=len(elements):
# 			# Add this element to the resulting list
# 			new_list.append(elements[i])
# 		# Increment i
# 		i+=2
#
# 	return new_list
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# Same task acheived by enumerate ()
# def skip_elements(elements):
# 	# code goes here
# 	new_list = []
# 	for index, value in enumerate(elements):
# 		if index%2 == 0 :
# 			new_list.append(value)
# 	return new_list
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# ==================================================
# fruits= ["Apple", "banana", "oranges"]
# a,b,c = fruits
# print(a ," ",b," ",c )    # Apple   banana   oranges

# ==================================================
# def file_size(file_info):
# 	file_name, file_type, size= file_info
# 	return("{:.2f}".format(size / 1024))
#
# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# ==================================================
# change the extension of a specific file
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames=[]
# for word in filenames:
#     if word.endswith("hpp"):
#         index = word.index("hpp")
#         newword= word[0:index]+"h"
#         newfilenames.append(newword)
#     else:
#         newfilenames.append(word)
#
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# ==================================================
# language converter
# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = text.split()
#     for word in words:
#         # Create the pig latin word and add it to the list
#         word = word[1:]+word[0] + "ay"
#         say = say + " " + word
#         # Turn the list back into a phrase
#     return say
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
# # ==================================================

# set file permission in -rwx- format
# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for x in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if x >= value:
#                 result += letter
#                 x -= value
#             else:
#                 result += '-'
#     return result
#
#
# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

# # ==================================================
# def group_list(group, users):
#   members = group +": "+", ".join(users)
#   return members
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"
#
# # # ==================================================
#
# def guest_list(guests):
# 	for guest in guests:
# 		name, age, occu = guest
# 		print("{} is {} years old and works as {}".format(name, age, occu))
#
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
#
# #Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
#  """
#
# # ==================================================
#
# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			user_groups[user] = user_groups.get(user,[]) + [group]
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary
#
# 	return(user_groups)
#
# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

# ==================================================
# ==================================================

# Question 1
# The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

# def format_address(address_string):
#     # Declare variables
#     hno= ""
#     sname=""
#     # Separate the address string into parts
#     x = address_string.split()
#     # Traverse through the address parts
#     for y in x :
#     # Determine if the address part is the
#     # house number or part of the street name
#         if y.isdigit():
#             hno=y
#         else:
#             sname+=y
#             sname+= " "
#     # Does anything else need to be done
#     # before returning the result?
#
#     # Return the formatted string
#     return "house number {} on street named {}".format(hno, sname)
#
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# ==================================================
# Question 2
#
# The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

# def highlight_word(sentence, word):
# 	return( sentence.replace(word, word.upper()))
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# # ==================================================
# Question 3
#
# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

# def combine_lists(list1, list2):
#     list3=list2
#     for y in reversed(range(len(list1))):
#         list3.append(list1[y])
#     return list3
# # Generate a new list containing the elements of list2
# # Followed by the elements of list1 in reverse order
#
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))

# ==================================================
#Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].

# def squares(start, end):
# 	return [ x*x for x in range(start, end+1) ]
#
# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # ==================================================
# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

# def car_listing(car_prices):
#   result = ""
#   for key, value in car_prices.items():
#     result += "{} costs {} dollars".format(key, value) + "\n"
#   return result
#
# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# # ==================================================
# Question 6
#
# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

# def combine_guests(guests1, guests2):
#     new_list=guests2
#     for key, value in guests1.items():
#         new_list[key]=value
#     return new_list
#   # Combine both dictionaries into one, with each key listed
#   # only once, and the value from guests1 taking precedence
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))


# # ==================================================
# Question 7
# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

# def count_letters(text):
#   result = {}
#   convert_text = text.lower()
#   # Go through each letter in the text
#   for letter in convert_text:
#       if letter.isalpha():
#           if letter in result:
#               result[letter]+=1
#           else:
#               result[letter]=1
#   return result
#       # Check if the letter needs to be counted or not
#       # Add or increment the value in the dictionary
#
#
# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
#
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# # ==================================================
# What do the following commands return when animal = "Hippopotamus"?

# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

'''
pop
t
us
'''
# # ==================================================
# Question 9

#What does the list "colors" contain after these commands are executed?

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)   # output ['red', 'white', 'yellow', 'blue']
# # ==================================================

# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# host_addresses.keys()

# ==================================================

