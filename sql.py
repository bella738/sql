import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tvewNtpUEG', passwd='pltEI1kivk', db='tvewNtpUEG')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM tvewNtpUEG.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()