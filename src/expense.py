"""
expense.py

Contains the Expense class used to represent a single expense record.
"""

from datetime import datetime


class Expense:
    """
    Represents a student's expense.
    """

    def __init__(self, category, amount, description):
        """
        Initialize an expense object.

        Args:
            category (str): Expense category.
            amount (float): Expense amount.
            description (str): Expense description.
        """
        self.category = category
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """
        Convert expense object into dictionary format.

        Returns:
            dict: Expense data dictionary.
        """
        return {
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date
        }