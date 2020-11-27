#  Class and object
# ==================================================
# Question 3
# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".
# define a basic city class

# class City:
# 	name = ""
# 	country = ""
# 	elevation = 0
# 	population = 0
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3399
# city1.population = 358052
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2290
# city2.population = 1241675
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9733509
#
# def max_elevation_city(min_population):
# 	# Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
# 	return_city = City()
#
# 	# Evaluate the 1st instance to meet the requirements:
# 	# does city #1 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city1.population>=min_population and city1.elevation>=return_city.elevation:
# 		return_city = city1
# 	# Evaluate the 2nd instance to meet the requirements:
# 	# does city #2 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city2.population>=min_population and city2.elevation>=return_city.elevation:
# 		return_city = city2
# 	# Evaluate the 3rd instance to meet the requirements:
# 	# does city #3 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city3.population>=min_population and city3.elevation>=return_city.elevation
# 		return_city = city3
#
# 	#Format the return string
# 	if return_city.name:
# 		return "{}, {}".format(return_city.name, return_city.country)
# 	else:
# 		return ""
#
# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""

# ==================================================
# We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"
# class Furniture:
# 	color = ""
# 	material = ""
#
# table = Furniture()
# table.color="brown"
# table.material="wood"
#
# couch = Furniture()
# couch.color="red"
# couch.material="leather"
#
# def describe_furniture(piece):
# 	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))
#
# print(describe_furniture(table))
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch))
# # Should be "This piece of furniture is made of red leather"

# ==================================================
# Inheritance
# ==================================================
# composition
# class Clothing:
#     stock = {'name': [], 'material': [], 'amount': []}
#
#     def __init__(self, name):
#         material = ""
#         self.name = name
#
#     def add_item(self, name, material, amount):
#         Clothing.stock['name'].append(self.name)
#         Clothing.stock['material'].append(self.material)
#         Clothing.stock['amount'].append(amount)
#
#     def Stock_by_Material(self, material):
#         count = 0
#         n = 0
#         for item in Clothing.stock['material']:
#             if item == material:
#                 count += Clothing.stock['amount'][n]
#                 n += 1
#         return count
#
#
# class shirt(Clothing):
#     material = "Cotton"
#
#
# class pants(Clothing):
#     material = "Cotton"
#
#
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)   # output is 10

# ==================================================
# ==================================================
