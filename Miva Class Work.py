# Hovercraft info
HOVERCRAFT_COST = 2000000
HOVERCRAFT_SALES = 3000000
MONTHLY_INSURANCE = 1000000

# This script repeatedly prompts the user for input until they enter a valid input
while True:
    user_input_sales = input("Your monthly sales: ")  # Input
    if user_input_sales.isdigit():
        user_input = int(user_input_sales)
        break
    else:
        print("Wrong input. Please enter a valid input.")

# Calculation
total_cost = HOVERCRAFT_COST * 10  # 10 hovercraft built every month
total_revenue = HOVERCRAFT_SALES * user_input
total_expense = total_cost + MONTHLY_INSURANCE
profit_loss = total_revenue - total_expense

# Output
if profit_loss > 0:
    print("Profit")
elif profit_loss < 0:
    print("Loss")
else:
    print("Broke Even")
