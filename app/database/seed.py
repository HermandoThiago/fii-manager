import mysql.connector as mysql
import pandas as pd

def seed_database():
    """
        Connects to a MySQL database and populates the 'fundos' table with data from a CSV file.

        This function performs the following steps:
        1. Reads data from a CSV file located at './app/database/fiis.csv'. The CSV should contain a column named 'Fundos' with the names of the funds.
        2. Establishes a connection to a MySQL database using the provided credentials.
        3. Selects the 'fiis' database.
        4. Creates the 'fundos' table if it does not exist, with an 'id' column as an auto-incrementing primary key and a 'nome' column to store fund names.
        5. Inserts fund names from the CSV into the 'fundos' table.
        6. Commits the changes to the database.
        7. Closes the connection to the database.

        Notes:
        - Ensure the CSV file is at the specified path and contains a 'Fundos' column.
        - The function assumes that the database credentials (host, user, password) are correct and that the 'fiis' database exists.
    """

    try:
        fiis = pd.read_csv('./app/database/fiis.csv')

        # Connect to the MySQL database
        db = mysql.connect(
            host="localhost",
            user="user",
            passwd="password",
            database="fiis"  # Database name
        )

        cursor = db.cursor()

        # Select the database
        cursor.execute("USE fiis")

        # Create a sample table (adjust as needed)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fundos (
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                nome VARCHAR(10) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS compras (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fundo VARCHAR(10) NOT NULL,
                quantidade TINYINT NOT NULL,
                data DATE NOT NULL,
                valor DECIMAL(10, 2)
            )
        """)

        for fundo in fiis['Fundos']:
            cursor.execute("INSERT INTO fundos (nome) VALUES (%s)", (fundo,))

        # Commit the changes
        db.commit()

        # Close the connection
        cursor.close()
        db.close()

    except:
        print("Erro")

seed_database()