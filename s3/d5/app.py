from flask import Flask
import mysql.connector

app = Flask(__name__)

# Replace the placeholders with your actual MySQL server details
hostname = 'localhost'  # Hostname or IP address of the MySQL server
username = 'root'  # MySQL username
password = 'namrata0704'  # MySQL password
# database = 'your_database'  # Optional: MySQL database name

@app.route('/')
def index():
    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            # database=database
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute a SELECT query
        query = "SELECT * FROM your_table"
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Process the results
        response = ''
        for row in results:
            # Access row data using index or column names
            response += str(row) + '<br>'

        return response

    except mysql.connector.Error as error:
        return "Error connecting to MySQL: " + str(error)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(port=11000)
