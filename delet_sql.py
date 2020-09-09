import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tvewNtpUEG', passwd='pltEI1kivk', db='tvewNtpUEG')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM tvewNtpUEG.users WHERE name = 'john'")

cursor.close()
conn.close()