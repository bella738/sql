import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tvewNtpUEG', passwd='pltEI1kivk', db='tvewNtpUEG')
conn.autocommit(True)
cursor = conn.cursor()
cursor.execute("INSERT into tvewNtpUEG.dogs (name, age, breed) VALUES ('tomy', 2, 'pudel')")
cursor.execute("INSERT into tvewNtpUEG.dogs (name, age, breed) VALUES ('bony', 1, 'labrador')")
cursor.execute("INSERT into tvewNtpUEG.dogs (name, age, breed) VALUES ('roy', 1, 'dalmaty')")
cursor.close()
conn.close()