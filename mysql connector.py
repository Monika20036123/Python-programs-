import mysql.connector
conn=mysql.connector.connect(host="local host",password="MONIKAVENGADESAN",user="root")

if conn.is_connected():
    print("connection establishment")
