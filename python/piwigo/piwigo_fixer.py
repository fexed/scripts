import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def run_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        cursor.commit()
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


connection = create_server_connection("localhost", "user", "pwd", "photos")
N = read_query(connection, "SELECT id FROM piwigo_images WHERE date_creation IS NULL")
print(str(len(N)) + " rows to be edited")

for id in N:
	i = id[0]
	try:
		res = read_query(connection, "SELECT path FROM piwigo_images WHERE id = " + str(i))[0]
		print(str(i) + " with " + res[0])
		dataf = res[0].split("/")[5]
		data = [[],[],[]]
		data[0] = dataf[0:4]
		data[1] = dataf[4:6]
		data[2] = dataf[6:8]
		run_query(connection, "UPDATE piwigo_images SET date_creation = '" + data[0] + "-" + data[1] + "-" + data[2] + "' WHERE id = " + str(i))
	except:
		continue
