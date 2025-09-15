# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

employees = { "Rohan":"Front-end devoloper",
             "Neha":"Back-end devoloper",
             "Niloy":"Coffee maker",
             "Rafsan":"Editor",
             "Rahi":"Marketing manager",
             "Ratul":"Script writer",
             "Rassel":"HR"}

# print(dir(employees))
# print(help(employees))

# if employees.get("Rassel"):
    # print("He is our employee ! ")
# else:
    # print("Doesn't exist ")    

# employees.update({"Jinnah":"Filmmaker"})   >this will add an item at the last place of the list
# employees.pop("Rohan")   > .pop() is used to delete any item 
# employees.popitem()    >will delete the last element of the list 
# employees.clear()     >delete all items from the set  

# keys =  employees.keys()
# for key in employees.keys():        
    # print(key)        >> you will see only key, i know, i don't have to write this. But the sound of my new keyboard is awsome-that's the reason          

# values =  employees.values()
# for value in employees.values():        
    #  print(value) 

# items = employees.items()
# print(items)    

for key, value in employees.items():
    print(f"{key}:{value}")