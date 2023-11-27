import mysql.connector

host = "localhost"
port = 3306
user = "root"
password = ""
database = "kalorieberegner"

conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS kalorieberegner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE,
    gender ENUM('M', 'F', 'Other'),
    height FLOAT,
    weight FLOAT
)
"""

cursor.execute(create_table_query)
conn.commit()

# Check if the table exists by describing its structure
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

finally:
    cursor.close()
    conn.close()
