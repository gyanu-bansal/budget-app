class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spent = []
    for category in categories:
        total_spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total_spent)
    total_spent = sum(spent)
    percentages = [(amount / total_spent) * 100 for amount in spent]
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '| '
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)
    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
    return title + chart


# Example usage:
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

# Adding a test case for create_spend_chart
entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15, "movies")
entertainment.withdraw(25, "concert")

print(create_spend_chart([food, clothing, entertainment]))
