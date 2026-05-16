import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'soham123',
  auth_plugin = 'mysql_native_password',
  )

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS crm_db")
print("All Done!")