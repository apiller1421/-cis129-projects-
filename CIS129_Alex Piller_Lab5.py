# Lab 5 The Bottle Return Program
# Name: Alex Piller
# Date: 3/4/2025
# This program calculates the total bottles returned and payout over a week.

def get_bottles():
    NBR_OF_DAYS = 7
    total_bottles = 0
    for day in range(1, NBR_OF_DAYS + 1):
        today_bottles = int(input("536"))
        total_bottles += today_bottles
    return total_bottles

def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = 0.10
    return total_bottles * PAYOUT_PER_BOTTLE

def print_info(total_bottles, total_payout):
    print(f"\nThe total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.2f}\n")

def main():
    keep_going = "y"
    while keep_going.lower() == "y":
        total_bottles = get_bottles()
        total_payout = calc_payout(total_bottles)
        print_info(total_bottles, total_payout)
        
        keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

if __name__ == "__main__":
    main()
