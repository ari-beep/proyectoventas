import mysql.connector

conexion = mysql.connector.connect(
    host="bk9xgxdyzcmoxl1dw1rr-mysql.services.clever-cloud.com",
    user="ujr1xl89lutip2zc",
    password="MD3gHZeeU0kgUpHwdP7p",
    database="bk9xgxdyzcmoxl1dw1rr"
)
if conexion.is_connected():
    print("conexion exitosa")