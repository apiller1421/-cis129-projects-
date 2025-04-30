# File: CIS129_AlexPiller_lab10.py
# Author: [Alex Piller]
# Date: [4/29/2025]
# Description: a script that inputs a dollar amount, then prints the amount in check-protected format in a field of 10 characters with leading asterisks

def check_protection(amount):
    # Format the amount with 2 decimal places
    formatted_amount = f"{amount:,.2f}"
    
    # Add leading asterisks to make the total length 10
    protected_amount = f"{formatted_amount:*>10}"
    
    # Print result
    print(protected_amount)
    print("-" * 10)
    print("0123456789")
