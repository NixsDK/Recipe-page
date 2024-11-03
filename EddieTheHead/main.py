import os
import sqlite3
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load additional configurations from config.json
def load_config():
    """Load configuration settings from config.json."""
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print("Error: config.json file not found.")
        return {}

# Connect to the database
def connect_db():
    """
    Establish a connection to the SQLite database specified in the .env file.
    
    Returns:
        sqlite3.Connection: A connection object to interact with the database.
    """
    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("Database name not found in environment variables.")
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Create a sample table if it doesn't already exist
def create_table():
    """
    Create a sample table named 'sample_table' if it doesn't already exist.
    This table will store sample data for our application.
    """
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sample_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER
                )
            """)
            connection.commit()
            print("Table 'sample_table' created successfully or already exists.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            connection.close()

# Insert sample data into the table
def insert_data(name, age):
    """
    Insert a new record into the sample_table.
    
    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sample_table (name, age) VALUES (?, ?)", (name, age))
            connection.commit()
            print(f"Data inserted: {name}, {age}")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")
        finally:
            connection.close()

# Fetch data from the table
def fetch_data():
    """
    Retrieve all records from the sample_table.
    
    Returns:
        list: A list of tuples representing each row in the table.
    """
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sample_table")
            data = cursor.fetchall()
            return data
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            connection.close()

# Main function to initialize and run the program
def main():
    """
    Main function to run the program, create the table,
    insert sample data, and fetch records from the database.
    """
    config = load_config()
    if config:
        print(f"Running {config.get('app_name', 'Application')} version {config.get('version', '1.0')}")

    # Initialize the database and insert sample data
    create_table()
    insert_data("Alice", 30)
    insert_data("Bob", 25)

    # Fetch and display the data
    data = fetch_data()
    print("\nData in the table:")
    for row in data:
        print(row)

if __name__ == "__main__":
    main()
