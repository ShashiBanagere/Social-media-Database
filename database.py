import mysql.connector

# Function to connect to MySQL database
def connect_to_db():
    try:
        # Replace with your MySQL database credentials
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rasha123",
            database="social_media"
        )
        print("Connected to the database")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to execute a query
def execute_query(query, fetch=False):
    conn = connect_to_db()
    cursor = conn.cursor(buffered=True)  # Use buffered cursor to handle multiple queries
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
        if fetch:
            result = cursor.fetchall()
            return result
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the connection

# Function to insert user data into the database
def insert_user(username, password, first_name, last_name):
    query = f"INSERT INTO users (username, password, first_name, last_name) VALUES ('{username}', '{password}', '{first_name}', '{last_name}')"
    execute_query(query)

# Function to check if a user exists with given username and password
def check_user_credentials(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = execute_query(query, fetch=True)
    if result:
        if len(result) > 0:
            return True
    return False
