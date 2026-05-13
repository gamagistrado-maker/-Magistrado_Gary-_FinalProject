"""
expense_manager.py

Contains the ExpenseManager class for managing expenses.
"""

from expense import Expense
from file_handler import FileHandler


class ExpenseManager:
    """
    Handles all expense operations.
    """

    def __init__(self):
        """
        Initialize expense manager and load saved data.
        """
        self.expenses = FileHandler.load_data()

    def add_expense(self):
        """
        Add a new expense.
        """
        try:
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")

            expense = Expense(category, amount, description)

            self.expenses.append(expense.to_dict())
            FileHandler.save_data(self.expenses)

            print("\nExpense added successfully!\n")

        except ValueError:
            print("\nInvalid amount input.\n")

    def view_expenses(self):
        """
        Display all expenses.
        """
        if not self.expenses:
            print("\nNo expenses found.\n")
            return

        print("\n===== ALL EXPENSES =====")

        for index, expense in enumerate(self.expenses, start=1):
            print(
                f"{index}. "
                f"{expense['category']} | "
                f"₱{expense['amount']} | "
                f"{expense['description']} | "
                f"{expense['date']}"
            )

    def search_expense(self):
        """
        Search expenses by category.
        """
        category = input("Enter category to search: ").lower()

        results = [
            expense for expense in self.expenses
            if expense["category"].lower() == category
        ]

        if results:
            print("\nSearch Results:")
            for expense in results:
                print(
                    f"{expense['category']} | "
                    f"₱{expense['amount']} | "
                    f"{expense['description']}"
                )
        else:
            print("\nNo matching expenses found.\n")

    def sort_expenses(self):
        """
        Sort expenses by amount.
        """
        self.expenses.sort(key=lambda x: x["amount"])

        print("\nExpenses sorted by amount.\n")

    def delete_expense(self):
        """
        Delete an expense by index.
        """
        self.view_expenses()

        try:
            index = int(input("\nEnter expense number to delete: ")) - 1

            if 0 <= index < len(self.expenses):
                deleted = self.expenses.pop(index)
                FileHandler.save_data(self.expenses)

                print(
                    f"\nDeleted expense: "
                    f"{deleted['description']}\n"
                )
            else:
                print("\nInvalid expense number.\n")

        except ValueError:
            print("\nInvalid input.\n")

    def monthly_summary(self):
        """
        Calculate total monthly expenses.
        """
        total = sum(expense["amount"] for expense in self.expenses)

        print(f"\nTotal Expenses: ₱{total:.2f}\n")