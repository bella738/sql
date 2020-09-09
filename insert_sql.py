import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tvewNtpUEG', passwd='pltEI1kivk', db='tvewNtpUEG')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into tvewNtpUEG.users (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()