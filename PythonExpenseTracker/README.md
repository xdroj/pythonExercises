Python Expense Tracker
This is a simple command-line based Expense Tracker application written in Python. It allows users to record their expenses, view a list of all recorded expenses, calculate the total spending, and filter expenses by category.

Features
Add Expenses: Easily record new expenses by specifying an amount and a category.

List Expenses: View a comprehensive list of all expenses entered, showing both amount and category.

Total Expenses: Get a quick sum of all your recorded spending.

Filter by Category: Focus on expenses related to a specific category (e.g., "Food", "Transport").

Interactive Menu: User-friendly command-line interface for easy navigation.

How It Works
The application manages expenses in a list of dictionaries, where each dictionary represents an expense with an amount (float) and a category (string).

add_expense(expenses, amount, category): Appends a new expense dictionary {'amount': amount, 'category': category} to the expenses list.

print_expenses(expenses): Iterates through the given expenses list and prints the amount and category for each.

total_expenses(expenses): Uses a sum combined with a map and a lambda function to efficiently calculate the sum of all amount values in the expenses list.

filter_expenses_by_category(expenses, category): Employs the filter function with a lambda to return an iterator containing only the expenses that match the specified category.

main(): This function orchestrates the entire application. It runs an infinite while True loop presenting a menu to the user. Based on the user's input, it calls the appropriate helper functions and handles user input for amounts and categories.

Usage
To run the Expense Tracker, simply execute the Python script:

Bash

python your_script_name.py
(Replace your_script_name.py with the actual name of your Python file, e.g., expense_tracker.py)

Once launched, you will be presented with an interactive menu:

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice:
Menu Options:
1. Add an expense: Prompts you to enter the amount and category for a new expense.

2. List all expenses: Displays all expenses currently stored in the tracker.

3. Show total expenses: Calculates and shows the sum of all expenses.

4. Filter expenses by category: Asks for a category name and then lists only the expenses belonging to that category.

5. Exit: Terminates the program.

Example Session (Conceptual)
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 1
Enter amount: 50.75
Enter category: Food

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 1
Enter amount: 15.00
Enter category: Transport

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 2

All Expenses:
Amount: 50.75, Category: Food
Amount: 15.0, Category: Transport

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 3

Total Expenses:  65.75

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 4
Enter category to filter: Food

Expenses for Food:
Amount: 50.75, Category: Food

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 5
Exiting the program.
