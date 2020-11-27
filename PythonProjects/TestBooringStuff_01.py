# Split function

# reply = input("Enter the x and y value, separated by spaces")
# pieces = reply.split()
#
# x = float(pieces[0])
# y = float(pieces[1])
#
# print(" \n the value of x :\n",x)

# Memory Management

# x = 1
# c = 3 % 2
# print("The address of x is : ",id(x))
# print("The address of c is : ",id(c))

# Complex number
#
# root of -1

# x = 9 + 6j
# print("the type of x is :", type(x))
# print("the value of x is :", x)

#################################
#   FACTOR - ITERATORS AND GENERATORS

# def factors(n):
#     result =[]
#     for k in range(1, n+1):
#         if n % k == 0:
#             result.append(k)
#     return result
#
# x = factors(100)
# print(x)


# def factors(n):         // generator that compute factors
#     for k in range(1, n + 1):
#         if n % k == 0:
#             yield k
#
# x = factors(100)
#
# for i in x:
#     print(i)

######################################
#  Special variable __name__
# Case 1 :
# def main():
#     print("heloo world from module")
#
# if __name__ == "__main__":
#     main()

# else: print("before if __name function")

# Case 2 :
# def calculate(base,height):
#     print("The value of __name__ : ", __name__)
#     return 1/2 * (base*height)
#
# if __name__ == "__main__" :
#     print("I am in module area")
#     a = calculate(8,9)
#     print("area : ", a)

#############################
#   FUN STUFF

# Ch = input("Enter the char")[0]
# print(Ch)

#########################################
#   Pass arguments through command prompt
#
# import sys
# import math
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print("Sum of both the argument is :", x+y)

# print("Jacob", end="")
# print("rancho")

##########################################
#  TUPLE
#
# import math
# def Area_Circumfrence(radius):
#     """ Return (circumference, area) of a circle of radius r """
#     c = 2 * math.pi * radius
#     a = math.pi * radius * radius
#     return (c, a)  """Tuple as a Return Value"""
#
# if __name__=='__main__':
#     x=Area_Circumfrence(10)
#     print("Circumfrence of circle is :", x[0])
#     print("Area of circle is:", x[1])

############################################
# STRING Methods
#
# while True:
#     print("Enter your age \n")
#     age = input()
#     if age.isdecimal():
#         break
#     print("Please in numeric form")
#
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')


# print("Enter the sentence")
# x = input().split()


# print("\nthe words you entered :\n")
# print(x[2])

# for i in range(0,len(x)):
#     print(x[i])
#     i+1

######################################################################
# ''' Count words in a list  and put in new dictionary '''

# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# count=0
# added_item = {}
# for i in dragonLoot:
#     if i in added.keys():
#         added_item[i]+=1
#     else:
#         added_item[i] = 1
#
# print(added_item)


############################################################################
# Regular expression
# Regex  function are in "re" module

# import re
# haRegex = re.compile(r'(Ha){3,5}')
# mo1 = haRegex.search('HaHaHa HaHaHaHaHa')
# print(mo1.group())

################################################################
# 1) Complete the function to return the result of the conversion
# def convert_distance(miles):
#     km = miles * 1.6
#     return km
# my_trip_miles = 55

# # 2) Convert my_trip_miles to kilometers by calling the function above
# my_trip_km = convert_distance(my_trip_miles)
#
# # 3) Fill in the blank to print the result of the conversion
# print("The distance in kilometers is " + str(my_trip_km)
#
# # 4) Calculate the round-trip in kilometers by doubling the result,
# #    and fill in the blank to print the result
# print("The round-trip in kilometers is ", my_trip_km * 2)



def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = ___
		# What is the additional condition to exit out of the loop?
		if ___ :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		___ += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24