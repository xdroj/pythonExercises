Budget App
This is a Python console application designed to help users manage their personal finances by tracking income, expenses, and transfers across different budget categories. The application provides core budgeting functionalities and visualizes spending with a text-based bar chart.

Features
The Budget App includes the following features, implemented through the Category class and create_spend_chart function:

Category Class
Initialization: Create budget categories with a given name (e.g., "Food", "Clothing", "Entertainment").

deposit(amount, description=""): Adds a specified amount to the category's ledger. An optional description can be provided.

withdraw(amount, description=""): Attempts to subtract an amount from the category's ledger. This operation only proceeds if there are sufficient funds. An optional description can be provided. Returns True on successful withdrawal, False otherwise.

get_balance(): Returns the current total balance of the category.

transfer(amount, target_category): Transfers a specified amount from the current category to another Category object. This operation only proceeds if there are sufficient funds in the source category. Returns True on successful transfer, False otherwise.

check_funds(amount): A helper method that checks if the amount is less than or equal to the current balance of the category. Returns True if funds are sufficient, False otherwise.

String Representation (__str__): When a Category object is printed, it displays a formatted ledger showing deposits and withdrawals, along with the category's name and its current total balance.

create_spend_chart(categories) Function
Takes a list of Category objects as input.

Generates a text-based bar chart showing the percentage spent in each category (rounded down to the nearest 10).

The chart includes a title, percentage labels (100% down to 0%), the bar representation using 'o' characters, a horizontal separator, and the vertical names of the categories.

How to Use
To use this Budget App, you can import the Category class and create_spend_chart function into your Python script.

Example Usage
Python

# Import the necessary classes and functions
# Assuming your code is in a file named budget_app.py
# from budget_app import Category, create_spend_chart

# Create category instances
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Perform transactions
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")

clothing.deposit(300, "new wardrobe fund")
food.transfer(50, clothing) # Transfer from food to clothing
clothing.withdraw(25.50, "shirt")

auto.deposit(500, "car maintenance budget")
auto.withdraw(70.00, "gas refill")
auto.withdraw(30.00, "car wash")


# Check balances
print(f"Food balance: ${food.get_balance():.2f}")
print(f"Clothing balance: ${clothing.get_balance():.2f}")
print(f"Auto balance: ${auto.get_balance():.2f}")

# Print category ledgers
print("\n--- Food Category ---")
print(food)
print("\n--- Clothing Category ---")
print(clothing)
print("\n--- Auto Category ---")
print(auto)

# Generate and print the spend chart
print("\n" + create_spend_chart([food, clothing, auto]))
Getting Started
Clone the repository:

Bash

git clone https://github.com/yourusername/your-budget-app-repo.git
cd your-budget-app-repo
(Remember to replace yourusername and your-budget-app-repo with your actual GitHub details.)

Run the example:
Save the provided example usage code (or your own test code) in a Python file (e.g., main.py) in the same directory as your budget_app.py (or whatever you named your file containing the Category class and create_spend_chart function). Then run it from your terminal:

Bash

python main.py