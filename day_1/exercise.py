# ITP Week 2 Day 1 Exercise

# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!
# for item in inventory:
#     print(item)
# for x, y in inventory.items():
#     print(x, y)
# decrement item by using an assignment operator (Day 2 Lecture line #130)

for k in inventory.keys():
    inventory[k] -= 1
print(inventory)

# NOTE: recall that item represents the key of the key:value pair

# SCENARIO: REMOVE ANY 0 ITEMS
# use an if statement to check if the value is 0 and then remove it
del_list = []
for k in inventory.keys():
    if inventory[k] == 0:
        del_list.append(k)
for x in del_list:
    del inventory[x]
print(inventory)
