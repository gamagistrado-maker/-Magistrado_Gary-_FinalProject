"""
file_handler.py

Handles saving and loading expense data using JSON files.
"""

import json
import os


class FileHandler:
    """
    Handles file operations for the expense tracker.
    """

    FILE_PATH = "data/expenses.json"

    @classmethod
    def save_data(cls, expenses):
        """
        Save expenses to JSON file.

        Args:
            expenses (list): List of expense dictionaries.
        """
        os.makedirs("data", exist_ok=True)

        with open(cls.FILE_PATH, "w") as file:
            json.dump(expenses, file, indent=4)

    @classmethod
    def load_data(cls):
        """
        Load expenses from JSON file.

        Returns:
            list: List of expense dictionaries.
        """
        if not os.path.exists(cls.FILE_PATH):
            return []

        with open(cls.FILE_PATH, "r") as file:
            return json.load(file)