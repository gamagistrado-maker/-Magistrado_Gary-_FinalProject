"""
main.py

Entry point of the BudgetBuddy application.
"""

from expense_manager import ExpenseManager


def display_menu():
    """
    Display the main menu.
    """
    print("===== BUDGETBUDDY =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Sort Expenses")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")


def main():
    """
    Run the BudgetBuddy application.
    """
    manager = ExpenseManager()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.search_expense()

        elif choice == "4":
            manager.sort_expenses()

        elif choice == "5":
            manager.delete_expense()

        elif choice == "6":
            manager.monthly_summary()

        elif choice == "7":
            print("\nThank you for using BudgetBuddy!")
            break

        else:
            print("\nInvalid menu choice.\n")


if __name__ == "__main__":
    main()