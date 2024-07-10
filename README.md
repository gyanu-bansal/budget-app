# Budget App

This project implements a budgeting application in Python, featuring categories for expenses and methods to manage transactions within each category. The app includes functionality to deposit funds, withdraw funds, transfer funds between categories, and generate a spending chart based on the categories' expenditures.

## How to Use

### Prerequisites

- Python 3.x installed on your system.

### Running the Script

1. **Save the script** as `budget_app.py` or any name you prefer.
2. **Open a terminal or command prompt**.
3. **Navigate to the directory** where the script is saved.
4. **Run the script** by executing the following command:

    ```bash
    python budget_app.py
    ```

### Script Details

The script defines two main components: the `Category` class and the `create_spend_chart` function.

#### Category Class

- **Initialization (`__init__` method)**:
  - Accepts a category name upon creation.
  - Initializes an empty ledger to store transaction records.

- **Deposit Method (`deposit`)**:
  - Records a deposit transaction with an optional description.

- **Withdraw Method (`withdraw`)**:
  - Records a withdrawal transaction if funds are available.

- **Transfer Method (`transfer`)**:
  - Transfers funds between categories if sufficient balance is available.

- **Check Funds Method (`check_funds`)**:
  - Checks if sufficient funds are available for a specified amount.

- **String Representation (`__str__` method)**:
  - Provides a formatted string summarizing the category's ledger and total balance.

#### create_spend_chart Function

- **Parameters**:
  - `categories`: A list of `Category` objects representing different spending categories.

- **Returns**:
  - A string representing a bar chart showing the percentage of total expenditures per category.

### Example

The following example demonstrates the usage of the `Category` class and `create_spend_chart` function:

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
# Output:
# *************Food*************
# groceries              -10.15
# restaurant and more foo -15.89
# Total: 973.96

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15, "movies")
entertainment.withdraw(25, "concert")

print(create_spend_chart([food, clothing, entertainment]))
# Output:
# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60|          
#  50|    o     
#  40|    o     
#  30|    o     
#  20|    o  o  
#  10|    o  o  
#   0| o  o  o  
#     ----------
#      F  C  E  
