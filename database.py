import mysql.connector
from datetime import date

host = "127.0.0.1"
port = 3306
user = "root"
password = ""
database = "KB"

conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

create_table_query = """
DROP TABLE IF EXISTS kalorieberegner;
CREATE TABLE IF NOT EXISTS kalorieberegner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE,
    gender ENUM('M', 'F', 'Other'),
    height FLOAT,
    weight FLOAT,
    Amr FLOAT
)
"""

cursor.execute(create_table_query, multi=True)
conn.commit()

check_table_query = "DESCRIBE kalorieberegner"
try:
    cursor.execute(check_table_query)
    result = cursor.fetchall()

    if result:
        print("Table 'kalorieberegner' exists.")
    else:
        print("Table 'kalorieberegner' does not exist.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

try:
    # Person 1
    insert_query1 = """
    INSERT INTO kalorieberegner (name, birthday, gender, height, weight, Amr)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data1 = ("Fahad", date(1990, 1, 1), 'M', 175.0, 70.0, 0.0)
    cursor.execute(insert_query1, data1)

    # Person 2
    insert_query2 = """
    INSERT INTO kalorieberegner (name, birthday, gender, height, weight, Amr)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data2 = ("Awad", date(1985, 5, 15), 'F', 160.0, 55.0, 0.0)
    cursor.execute(insert_query2, data2)

    conn.commit()
    print("To personer tilføjet til databasen.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()