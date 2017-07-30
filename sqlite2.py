import sqlite3

conn = sqlite3.connect('test1.db')
print "opened database successfully"

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY) VALUES (5, 'sarath', 22, 'california', 20000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY) VALUES (6, 'bibi', 26, 'california', 30000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY) VALUES (3, 'nithi', 26, 'california', 40000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY) VALUES (4, 'sabari', 27, 'california', 50000.00)");

conn.commit()
print "Records create successfully";
conn.close()