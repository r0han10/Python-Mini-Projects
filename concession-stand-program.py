menu = {"coconut": 159,
        "banana": 12.25,
        "guava": 89,
        "pineapple": 35,
        "malta": 339,
        "apple": 399,
        "amloki": 119,
        "pomelo": 79,
        "grapes": 159}

cart = []
total = 0

print("__________MENU__________")

for key, value in menu.items():
    print(f"{key:11}: {value:.2f} Taka")
print("_________________________") 

while True: 
    food = input("Enter what you want('q' to quit): ").lower()
    if food == 'q':
        break 
    elif menu.get(food) is not None:
        cart.append(food)

print( "\n" * 4 )
print("____________YOUR ORDER____________")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: {total:.2f} Taka ")
