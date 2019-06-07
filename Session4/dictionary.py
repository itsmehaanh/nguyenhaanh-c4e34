person = {
    "name":"Duc",
    "age" : 22,
    "ex-gf" : 3,
    "university":"FTU",
}
#key: value

# CRUD
# 1. READ
#1.1 READ one
# name = person["name"]
# print(name)

#1.2 READ many
#loop by keys
# for key in person.keys():
#     print(key)
# #loop by values
# for value in person.values():
#     print(value)

#loop by items
# for key,value in person.items():
#     print(key,value)

#2. CREATE/ UPDATE
# person["major"] = "Chinese"
# person["age"] = 25
# print(person)

#3. DELETE
# del person["ex-gf"]
# print(person)