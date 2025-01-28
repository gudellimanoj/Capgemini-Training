
import mysql.connector

# *Database Connection*
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="manoj@123",  # Replace with your MySQL password
            database="sample_db"
        )
        print("Database connected successfully!")
        return connection
    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None
    
def main():
    connect_to_db()

main()
