# Lab 7 The Theater Seating Lab
# Name: Alex Piller
# Date: 4/4/2025

# Constants for the theater sections
SECTION_NAMES = ['A', 'B', 'C']
SECTION_PRICES = {'A': 20, 'B': 15, 'C': 10}
NUMBER_OF_SEATS_PER_SECTION = {'A': 300, 'B': 500, 'C': 200}

def display_welcome():
    print("Welcome to the Movie Theater ! ")
    print("Here are the seating sections and their details:\n")
    for section in SECTION_NAMES:
        print(f"${SECTION_PRICES[section]} per ticket, {NUMBER_OF_SEATS_PER_SECTION[section]} seats available")
    print("-" * 50)

def get_tickets_sold(section):
    max_seats = NUMBER_OF_SEATS_PER_SECTION[section]
    while True:
        try:
            sold = int(input("Enter number of tickets sold in section {section}: "))
            if 0 <= sold <= max_seats:
                return sold
            else:
                print("Please enter a number between 0 and {max_seats}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_income(sold, price):
    return sold * price

def display_subtotal(section, sold, income):
    print("Section {section}:")
    print("  Tickets Sold: {sold}")
    print("  Subtotal: ${income:.2}")
    print("-" * 30)

def main():
    display_welcome()
    total_income = 0
    total_tickets = 0
    print("Ticket Sales Summary:\n")

    for section in SECTION_NAMES:
        sold = get_tickets_sold(section)
        income = calculate_income(sold, SECTION_PRICES[section])
        display_subtotal(section, sold, income)
        total_income + = income
        total_tickets + = sold

    print("Overall Tickets Sold: {total_tickets}")
    print("Total Income: ${total_income:.2}")

if __name__ == "__main__":
    main()
