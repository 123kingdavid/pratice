# capitals = {"USA": "washington D.C.",
#           "india": "New Delhi",
#             "china": "beijing",
#             "Russia": "moscow",
#             "Nigeria": "Abuja"}
# # print(capitals.get("Nigeria"))

#capitals.pop("china")
#keys = capitals.keys()
#print(keys)

# values = capitals.values
# for value in capitals.values():
#     print(value)

# for key, value in capitals.items():
#     print(f"{key}: {value}")

# for num in range(1999,-1,-2):
#     print(num)


menu = {"pizza": 50,
        "meatpie": 240,
        "popcorn" : 250,
        "fries": 150,
        "sausage": 300,
        "coke": 130,
        "soda": 20,
        "donut": 10}
cart = []
total = 0
print("-------- kings menus-------")
for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

print("---------your order------------")
for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print()
print(f" total is : ${total:.2f}")

