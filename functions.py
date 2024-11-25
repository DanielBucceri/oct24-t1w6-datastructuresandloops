# functions - Reusable collection of code that performs a particular task

#declare function
def greet(name, age, country="australia"):
    print(f"Hello {name}! You are {age}? Damn thats old")
    print(f"{name} is from {country}")

#call function
person = "Daniel"
age = 29
greet(person, age) # greet(age=age, name = person) can also do explicit instead o positional like  instead of person placed in name postion.

def even_or_odd(num):
    if num % 2 == 0:
        return 'even'

    else:

        return "odd"

#when returning value with fucntion you can still print as below
print(even_or_odd(5)) 

even_or_odd(10)
even_or_odd(11123124141341231252345425)



#ed challenge
# def defeat_monsters_in_dungeon(Value):
#     dungeon = [
#         "Goblin",
#         "Gold coins",
#         "Dragon",
#         "Dragon",
#         "Bandit",
#         "Gold coins",
#         "Giant Snake"]
#     # Defeat the monsters!
#     i = 0
#     while i < len(dungeon):
#         if dungeon[i] != Value:
#            dungeon[i] = Value
#         i += 1

#     return dungeon

# print(defeat_monsters_in_dungeon("Gold Coins"))

def defeat_monsters_in_dungeon():
    dungeon = [
        "Goblin",
        "Gold coins",
        "Dragon",
        "Dragon",
        "Bandit",
        "Gold coins",
        "Giant Snake"
    ]
    # Replace all items with "Gold coins"
    for i in range(len(dungeon)):
        dungeon[i] = "Gold coins"  # Replace every element with "Gold coins"

    return dungeon

print(defeat_monsters_in_dungeon())



def update_warehouse_product_database():
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }
    # Using todays orders update the warehouse product database.
    return warehouse_product_database

update_warehouse_product_database()