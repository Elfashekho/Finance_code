import matplotlib.pyplot as plt

# Personal Finance Program

# Initial values stored in a dictionary
initial_values = {
    "main_account": 30000,  # Main bank account balance
    "monthly_income": 10000,  # Monthly income
    "rent": 60000 / 12,  # Monthly rent
    "cc_payment": 5000,  # Monthly credit card payment
    "other_expenses": 500 + 400 + 900 + 300 + 2000 + 2000,  # Bills
    "cc_debt": 50000  # Initial cc_debt
}

# Display the initial values in a table-like format
print("=== Initial Values ===")
print(f"Main Account: {initial_values['main_account']}")
print(f"Monthly Income: {initial_values['monthly_income']}")
print(f"Rent: {initial_values['rent']}")
print(f"Credit Card Payment: {initial_values['cc_payment']}")
print(f"Other Expenses: {initial_values['other_expenses']}")
print(f"Credit Card Debt: {initial_values['cc_debt']}\n")

# Loop through 12 months
main_account = initial_values['main_account']
monthly_income = initial_values['monthly_income']
rent = initial_values['rent']
cc_payment = initial_values['cc_payment']
other_expenses = initial_values['other_expenses']
cc_debt = initial_values['cc_debt']

# Initialize savings tracking
savings = 0  # Savings accumulator

# Create a list to store the main account balance for each month (for plotting)
main_account_history = []

for month in range(1, 25):  # Loop from 1 to 24 (24 months)
    print(f"\n=== Month {month} Finances ===")
    print(f"Main Account Balance at Start: {main_account}")
    print(f"Credit Card Debt at Start: {cc_debt}")
    
    # Stop credit card payments if debt is cleared
    if cc_debt <= 0:
        cc_payment = 0
        print("Credit card debt has been fully paid off. No further payments required.")

    # Calculate new balance after rent, CC payment, and income
    new_balance = main_account - rent - cc_payment - other_expenses + monthly_income

    # Update credit card debt
    if cc_debt > 0:
        cc_debt -= cc_payment
        if cc_debt < 0:  # Avoid negative debt
            cc_debt = 0

    # Additional savings calculator
    total_expenses = rent + cc_payment + other_expenses
    savings = monthly_income - total_expenses

    # Display savings or overspending
    if savings > 0:
        print(f"You save: {savings} this month.")
    else:
        print(f"You are overspending by {-savings} this month!")
    
    # Update the main account balance
    main_account = new_balance 
    print(f"Updated Main Account Balance After Month {month}: {main_account}")
    print(f"Remaining Credit Card Debt: {cc_debt}")
    
    # Alert when savings reach between 350,000 and 400,000
    if main_account >= 350000 and main_account <= 400000:
        print("\033[91mALERT: Your savings have reached between 350,000 and 400,000!\033[0m")


    # Introduce a payment of 7,000 every 3 months
    if month % 3 == 0 and month<= 24:
        main_account -= 7000
        print(f"Payment of 7,000 made at the end of Month {month}. New Balance: {main_account}")

    # Stop the loop early if credit card debt is cleared and continue tracking
    if cc_debt == 0 and cc_payment == 0:
        print("\nCredit card payments ended. Continuing to track finances for remaining months.")
    # Store the main account balance after each month for plotting
    main_account_history.append(main_account)

# Final report
print("\n=== Final Financial Report ===")
print(f"Final Main Account Balance: {main_account}")
print(f"Final Credit Card Debt: {cc_debt}")



# Plot the main account balance over the 24 months
plt.plot(range(1, 25), main_account_history, marker='o', linestyle='-', color='c', label='Main Account Balance')
plt.title('Main Account Balance Over 24 Months')
plt.xlabel('Month')
plt.ylabel('Balance ($)')
plt.grid(True)
plt.axhline(y=350000, color='r', linestyle='--', label='Savings Alert (350,000)')
plt.legend()
plt.show()
