import mysql.connector as mysql
import pandas as pd
from datetime import date

def buy_fii(ticker: str, quantity: int, date: date, value: float):
  """
    Records a purchase of a Fundo de Investimento Imobiliário (FII) in the database.

    This function performs the following steps:
    1. Establishes a connection to a MySQL database using the provided credentials.
    2. Inserts the purchase data (ticker, quantity, date, value) into the 'compras' table.
    3. Commits the changes to the database.
    4. Closes the connection to the database.

    Parameters:
    ticker (str): The ticker symbol of the FII.
    quantity (int): The number of units purchased.
    date (date): The date of the purchase.
    value (float): The purchase price per unit.

    Notes:
    - Ensure that the 'compras' table exists in the 'fiis' database and has the columns 'fundo', 'quantidade', 'data', and 'value'.
    - The function assumes that the database credentials (host, user, password) are correct and that the 'fiis' database exists.
  """
  
  # Connect to the MySQL database
  db = mysql.connect(
      host="localhost",
      user="user",
      passwd="password",
      database="fiis"  # Database name
  )

  cursor = db.cursor()

  # Insert purchase data into the database
  cursor.execute("""
      INSERT INTO compras (fundo, quantidade, data, valor)
      VALUES (%s, %s, %s, %s)
  """, (ticker, quantity, date, value))

  # Commit the changes
  db.commit()

  # Close the connection
  cursor.close()
  db.close()


def all_purchases() -> pd.DataFrame:
  """
    Retrieves all purchases from the 'compras' table in the database and returns them as a DataFrame.

    This function performs the following steps:
    1. Establishes a connection to a MySQL database using the provided credentials.
    2. Executes a SQL query to select all purchase records from the 'compras' table ordered by date in descending order.
    3. Fetches the result set and converts it into a pandas DataFrame.
    4. Closes the connection to the database.
    5. Returns the DataFrame containing all purchases.

    Returns:
    pd.DataFrame: A DataFrame containing all purchase records with columns corresponding to the 'compras' table.

    Notes:
    - Ensure that the 'compras' table exists in the 'fiis' database.
    - The function assumes that the database credentials (host, user, password) are correct and that the 'fiis' database exists.
  """
  
  db = mysql.connect(
      host="localhost",
      user="user",
      passwd="password",
      database="fiis"  # Database name
  )

  cursor = db.cursor()

  # Execute query to retrieve all purchases
  cursor.execute("""
      SELECT * FROM compras ORDER BY data ASC;
  """)

  purchases = cursor.fetchall()

  df = pd.DataFrame(purchases, columns=["ID", "Fundo", "Quantidade", "Data", "Valor"])

  cursor.close()
  db.close()

  return df

def purchases_group_fii_quantity() -> pd.DataFrame:
  """
    Retrieves the total quantity of shares (cotas) purchased for each Fundo de Investimento Imobiliário (FII)
    from the 'compras' table in the database and returns them as a pandas DataFrame.

    This function performs the following steps:
    1. Establishes a connection to a MySQL database using the provided credentials.
    2. Executes a SQL query to select the total quantity of shares for each FII from the 'compras' table,
       grouped by the 'fundo' column.
    3. Fetches the result set and converts it into a pandas DataFrame.
    4. Closes the connection to the database.
    5. Returns the DataFrame containing the total quantity of shares for each FII.

    Returns:
    pd.DataFrame: A DataFrame containing two columns: 'fundo' (the FII ticker symbol) and 'total_cotas' (the total quantity of shares purchased).

    Notes:
    - Ensure that the 'compras' table exists in the 'fiis' database.
    - The function assumes that the database credentials (host, user, password) are correct and that the 'fiis' database exists.
  """
  # Connect to the MySQL database
  db = mysql.connect(
      host="localhost",
      user="user",
      passwd="password",
      database="fiis" 
  )

  cursor = db.cursor()

  # Query to get the total cotas for each fundo
  cursor.execute("""
      SELECT fundo, SUM(quantidade) AS total_cotas 
      FROM compras AS c 
      GROUP BY fundo;
  """)

  # Fetch all results from the executed query
  fund_data = cursor.fetchall()

  # Convert the result set into a pandas DataFrame
  df = pd.DataFrame(fund_data, columns=["fundo", "total_cotas"])

  # Close the connection
  cursor.close()
  db.close()

  return df

def purchases_group_fii_value() -> pd.DataFrame:
  """
    Retrieves the total value of purchases for each Fundo de Investimento Imobiliário (FII)
    from the 'compras' table in the database and returns them as a pandas DataFrame.

    This function performs the following steps:
    1. Establishes a connection to a MySQL database using the provided credentials.
    2. Executes a SQL query to select the total value of purchases for each FII from the 'compras' table,
       grouped by the 'fundo' column.
    3. Fetches the result set and converts it into a pandas DataFrame.
    4. Closes the connection to the database.
    5. Returns the DataFrame containing the total value of purchases for each FII.

    Returns:
    pd.DataFrame: A DataFrame containing two columns: 'fundo' (the FII ticker symbol) and 'total_valor' 
    (the total value of purchases for each FII).

    Notes:
    - Ensure that the 'compras' table exists in the 'fiis' database.
    - The function assumes that the database credentials (host, user, password) are correct and that the 'fiis' database exists.
  """
  db = mysql.connect(
      host="localhost",
      user="user",
      passwd="password",
      database="fiis" 
  )

  cursor = db.cursor()

  # Query to get the total cotas for each fundo
  cursor.execute("""
      SELECT fundo, SUM(valor) AS total_valor
      FROM compras AS c 
      GROUP BY fundo;
  """)

  # Fetch all results from the executed query
  fund_data = cursor.fetchall()

  # Convert the result set into a pandas DataFrame
  df = pd.DataFrame(fund_data, columns=["fundo", "total_valor"])

  # Close the connection
  cursor.close()
  db.close()

  return df