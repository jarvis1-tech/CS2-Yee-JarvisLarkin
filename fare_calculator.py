# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number



# Travel Fare Calculator Version 2
FARE_RATE = 14

name = input("Enter passenger name: ")
if name.strip() == "":
    print("Invalid name, try again")
    name = input("Enter passenger name: ")

distance_str = input("Enter distance (km): ")
if not distance_str.replace('.', '', 1).isdigit() or float(distance_str) <= 0:
    print("Invalid distance, enter a number greater than 0")
    distance_str = input("Enter distance (km): ")
distance = float(distance_str)

passengers_str = input("Enter number of passengers: ")
if not passengers_str.isdigit() or int(passengers_str) <= 0:
    print("Invalid input, enter a whole number")
    passengers_str = input("Enter number of passengers: ")
passengers = int(passengers_str)

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))





