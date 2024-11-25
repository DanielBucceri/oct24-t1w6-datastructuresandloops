# def update_warehouse_product_database():
#     warehouse_product_database = {
#         "Xbox": 77,
#         "PS5": 912,
#         "Switch": 311,
#         "Steam Deck": 51,
#         "Valve Index": 102
#     }
#     todays_orders = {
#         "Xbox": 12,
#         "PS5": 112,
#         "Switch": 310,
#         "Steam Deck": 51,
#         "Valve Index": 62
#     }

#     for prod in warehouse_product_database:
#         warehouse_product_database[prod] = warehouse_product_database[prod] + todays_orders[prod]
#         print(warehouse_product_database[1])
#     # Using todays orders update the warehouse product database.
#     return warehouse_product_database

# print(update_warehouse_product_database())


# def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
#     entry_ticket_cost = 15
#     entry_ticket_cost = entry_ticket_cost if age < 60 else entry_ticket_cost - 5
#     candy_cost = 10 if has_membership == False else 5
#     parking_cost = 3 if transport_type == "car" else 0  # to do

#     print(entry_ticket_cost, candy_cost, parking_cost)

#     return entry_ticket_cost + candy_cost + parking_cost

# print (calculate_total_cost_of_visiting_cinema(60, True, 'car'))

# def sum_to_x(target_integer):
#     count = 0
#     result = 1
#     while count <= target_integer:
#         result = result + count 
#         count += 1
#         print(result)
#     return result
# print(sum_to_x(6))

# count = 0
# x = False
# while x == False: 

#     count += 1
#     print(count)



import pandas as pd

def compound_and_multiply(value, iterations):
    """
    Multiplies the value by 5 and compounds it by 10% for the specified iterations.
    """
    results = []
    base_value = initial_value
    for _ in range(iterations):
        value = base_value * 5
        value *= 0.10
        base_value += value
        results.append(base_value)
    return results

# Input values
initial_value = 5000
iterations = 10

# Calculate results
results = compound_and_multiply(initial_value, iterations)

# Create a DataFrame
df_results = pd.DataFrame({
    "Iteration": range(1, iterations + 1),
    "Value": results
})

# Display the results
print(df_results)

# Optionally save to a CSV file
df_results.to_csv("compound_results.csv", index=False)
