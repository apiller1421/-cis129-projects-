# File: cis129_lab06_Hotdog_Calc.py
# Author: [Alex Piller]
# Date: [3/25/2025]
# Description:calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

def get_total_hot_dogs():
    # Get user input
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    
    # Calculate total hot dogs needed
    total = people * hot_dogs
    return total

def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # Display results
    print(f"Minimum packages of hot dogs needed: {min_dogs}")
    print(f"Minimum packages of hot dog buns needed: {min_buns}")
    print(f"Hot dogs left over: {dogs_left}")
    print(f"Hot dog buns left over: {buns_left}")

def main():
    # Constants for package sizes
    DOGS = 10  # Hot dogs per package
    BUNS = 8   # Buns per package
    
    # Get total number of hot dogs needed
    total = get_total_hot_dogs()
    
    # Calculate leftover hot dogs and buns
    dogs_left = (DOGS - total % DOGS) % DOGS
    buns_left = (BUNS - total % BUNS) % BUNS
    
    # Calculate minimum packages needed
    min_dogs = math.ceil(total / DOGS)
    min_buns = math.ceil(total / BUNS)
    
    # Display the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)
