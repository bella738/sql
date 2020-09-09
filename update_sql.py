import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tvewNtpUEG', passwd='pltEI1kivk', db='tvewNtpUEG')

conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE tvewNtpUEG.users SET id = '10' WHERE name = 'john'")

cursor.close()
conn.close()