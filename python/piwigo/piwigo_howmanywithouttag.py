import mysql.connector
from mysql.connector import Error
import random


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
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


connection = create_server_connection("localhost", "user", "password", "photos")
N = read_query(connection, "SELECT id FROM piwigo_images WHERE id NOT IN (SELECT image_id FROM piwigo_image_tag)")

print(str(len(N)))
