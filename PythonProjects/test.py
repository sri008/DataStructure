# # # 1) Complete the function to return the result of the conversion
# # def convert_distance(miles):
# #     km = miles * 1.6
# #     return km
# #
# # my_trip_miles = 55
# #
# # my_trip_km = convert_distance(my_trip_miles)
# #

# # print("The round-trip in kilometers is "+ str(my_trip_km * 2))
#
#
#
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = int(filesize/block_size)
#     #print(full_blocks)
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize%block_size
#     #print(partial_block_remainder)
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return (4096*full_blocks + 4096 )
#     return 4096
#
# print(calculate_storage(1))
# print(calculate_storage(4096))
# print(calculate_storage(4097))
# print(calculate_storage(6000))


###########################################################
###########################################################

# def fractional_part(numerator, denominator):
# 	# Operate with numerator and denominator to
# # keep just the fractional part of the quotient
# 	if numerator > 0 and denominator >0:
# 		number=numerator/denominator
# 		return(number - int(number))
#
# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0


################################
# Unsolved
#
#def sum_divisors(n):
#     x = 0
#     # Return the sum of all divisors of n, not including n
#     for i in list(range(n)):
#         if n % i == 0:
#             x=x +i
#             i=i+1
#         else:
#             i=i+1
#
# print(sum_divisors(3))


####################################
#
# a = input("")
# exchange={'G':'C','C':'G','T':'A','A':'U'}
# newb=""
# for i in range(len(a)):
#     for k,v in exchange.items():
#         if k==a[i]:
#             newb = newb[0:(i)] + exchange[k]
#         else:
#             continue
# print(newb)

# if any(char.isdigit() for char in a)==False:
#     for i in range(len(a)):
#         if a[i] == "G":
#             print(i)
#         #     a[i]=="C"
#         # else:
#         #     continue
#     print(a)
# else:
#     print("invalid Input")
    # # elif a[i]="C"
    #     a[i]="G"
    # elif a[i]="T"
    #     a[i]="A"
    # elif a[i]="A"
    #     a[i]="U"
##########################################################
##########################################################
# Couresa example
# total = 2048 + 4357 + 97658 + 125 + 8
# files = 5
# average = total / files
# print("The average size is:", average)
# print(type(average))

