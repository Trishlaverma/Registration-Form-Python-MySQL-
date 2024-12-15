import mysql.connector

def create_connection():

    #Establishes and returns a connection to the MySQL server.

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="trishla@123#",
        database = "login",
        
    )