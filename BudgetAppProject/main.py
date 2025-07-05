class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #deposit method
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, "description": description})

    def check_funds(self, amount):
        current_balance = self.get_balance()
        return amount <= current_balance

    #withdraw method
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    #check balance method
    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item['amount']
        return total_balance

    #transfer method
    def transfer(self, amount, category_obj):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category_obj.name}')
            category_obj.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    #str method defines category obj to be strings when printed
    def __str__(self):
        title = f'{self.name:*^30}\n' # Title with 30-character width, centered with '*'

        items_display = ''
        # Iterates through items to format its display in the ledger
        for item in self.ledger:
            description = item['description']
            amount = item['amount']
            # Formats description to 23 chars, left-justified.
            # Formats amount to 7 chars, right-justified, 2 decimal places.
            items_display += f"{description[:23].ljust(23)}{amount: >7.2f}\n"

        total = self.get_balance()
        total_line = f"Total: {total:.2f}"

        # Combines all to form a final string representation
        return title + items_display + total_line


#spend chart
def create_spend_chart(categories):
    chart_string = "Percentage spent by category\n"
    total_spent = 0
    category_spending = {}

    for category in categories:
        spent_in_category = 0
        for item in category.ledger:
            if item['amount'] < 0: # Only count withdrawals as 'spent'
                spent_in_category += abs(item['amount']) # Using absolute value
        category_spending[category.name] = spent_in_category
        total_spent += spent_in_category

    percentages = {}
    for category_name, spent_amount in category_spending.items():
        if total_spent == 0:
            percentage = 0
        else:
            percentage = (spent_amount / total_spent) * 100
        # Round down to the nearest 10%
        rounded_percentage = int(percentage // 10) * 10
        percentages[category_name] = rounded_percentage

    for i in range(100, -1, -10): # Loop from 100 down to 0, by 10s
        chart_string += str(i).rjust(3) + "| " # Adds percentage (e.g., "100| ")
        for category in categories:
            if percentages[category.name] >= i:
                # 'o' followed by two standard spaces
                chart_string += "o  "
            else:
                # Three standard spaces
                chart_string += "   "
        chart_string += "\n" # Newline after each percentage row


    # Horizontal line of dashes
    # Each category column is 3 chars wide + 1 space before the first column
    num_dashes = (len(categories) * 3) + 1
    # Four standard spaces to align under "100|"
    chart_string += "    " + "-" * num_dashes + '\n'

    # Vertical category names
    max_name_length = 0
    for category in categories:
        if len(category.name) > max_name_length:
            max_name_length = len(category.name)

    for i in range(max_name_length):
        # Five standard spaces to align the first character under the first 'o'
        chart_string += "     "
        for category in categories:
            if i < len(category.name):
                # Character followed by two standard spaces
                chart_string += category.name[i] + "  "
            else:
                # Three standard spaces for empty spots
                chart_string += "   "

        # Only add a newline if it's not the very last line of the entire chart
        if i < max_name_length - 1:
            chart_string += "\n"

    # CRITICAL FIX: Ensure the function returns the constructed string!
    return chart_string