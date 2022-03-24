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

    def create_table(self, table_name: str, columns_dict: dict) -> None:
        """Create a table on db with the given name 

        Args:
            table_name (str): table name
            columns_dict (dict): a dictionary that contains column data
                                key: column name
                                value: column type

        Returns:
            None: none
        """

        query = F"CREATE TABLE IF NOT EXISTS {table_name} ("

        for i in columns_dict:
            if list(columns_dict.keys())[-1] == i:
                query += f"{i} {columns_dict[i]})"
                continue
            query += f"{i} {columns_dict[i]}, "

        try:    
            self.cursor.execute(query)
            self.connection.commit()
        except Error:
            print(f"The error {Error} occurred")

        return None

