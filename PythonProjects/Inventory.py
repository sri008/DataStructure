#! python3.7.4
# # inventory.py

#
# Hero ={ 'ep01' : { 'a' : 1, 'b' : 4}, 'ep02' : {'c' :3 , 'd' : 4}}
#
# searchHero = input("Enter the name of hero")
#
#
# for k, v in Hero.values():    '''k is for key and v is for values'''
#     if k == searchHero:     '''it will search/match the input from user in the Hero dictionary'''
#         print("Inventory", v)
#         break
#     else:
#         continue

# Display Inventory items
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#  print("Inventory:")
#  item_total = 0
#  for k, v in inventory.items():
#      print(k ,"  ", v)
#      item_total=+v
#  print("Total number of items: " + str(item_total))
#
# displayInventory(stuff)

#To add item in Inventory
# inventory = {
#   'rope': 1,
#   'torch': 6,
#   'gold coin': 42,
#   'dagger': 1,
#   'arrow': 12
# }

#to be added loot, see add_to_inventory function (given as list in the assignment)
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# def addedInventory(inv,added_items):
#     added_itemsQ={}
#     total_items = 0
#     for items in added_items:
#         if items in added_itemsQ.keys():
#             added_itemsQ[items] += 1
#         else:
#             added_itemsQ[items] = 1
#
#     for i in added_itemsQ:
#         if not i in inv:
#             inv[i]=added_itemsQ[i]
#         else:
#             inv[i]=inv[i] + added_itemsQ[i]
#
#     for key, v in inv.items():
#         print(key, " ", v)
#         total_items+=v
#
#     print("Total number of items: " + (str(total_items)))
#
# addedInventory(inventory,dragonLoot)
