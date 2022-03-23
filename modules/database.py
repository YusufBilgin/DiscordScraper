import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self) -> None:
        self.create_connection()

    def create_connection(self) -> None:
        """Create a database connection and cursor 

        Returns:
            None: This func returns None
        """
        self.connection = None

        try:
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
        except Error:
            print(f"The error {Error} occurred")

        return None
