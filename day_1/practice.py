# ITP Week 2 Day 1 (In-Class) Practice

# Dictionary

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

# verify the type of person_1 to be a dictionary by using type

print(type(person_1))

# add a key value pair to person_1 with the last_name of Doo

print(person_1.update({"last_name": "Doo"}))
print(person_1.items())

# update person_1 favorite_snack to "Scooby Snacks"

# person_1["favorite_snack"] = "Scooby Snacks"
person_1.update({"favorite_snack": "Scooby Snacks"})
print(person_1.items())

# Remove the "wears_glasses" key:value from person_1

del person_1["wears_glasses"]
print(person_1.items())
