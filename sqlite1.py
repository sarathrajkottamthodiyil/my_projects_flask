import sqlite3

conn = sqlite3.connect('test1.db')
print "opened database successfully";

conn.execute('''CREATE TABLE COMPANY
		(ID INT PRIMARY KEY   NOT NULL,
		NAME            TEXT  NOT NULL,
		AGE             INT   NOT NULL,
		ADRESS          CHAR(50),
		SALARY          REAL);''')
print "Table created successfully";

conn.close() 