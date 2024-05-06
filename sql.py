import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records
cursor.execute('''INSERT INTO STUDENT VALUES ('Chandu', 'Data Science', 'A', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C', 78)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C', 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Yateesh', 'Data Science', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dinesh', 'Data Science', 'B', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sushanth', 'Devops', 'C', 79)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vinay', 'Data Science', 'C', 91)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Krishna', 'Data Science', 'A', 89)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dileep', 'Data Science', 'B', 87)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudheer', 'Devops', 'C', 75)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vishal', 'Data Science', 'C', 93)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Kishore', 'Data Science', 'A', 94)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Gopi', 'Data Science', 'B', 83)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Kushal', 'Devops', 'C', 77)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vamsi', 'Data Science', 'C', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('srinu', 'Data Science', 'A', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('David', 'Data Science', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sumanth', 'Devops', 'C', 82)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vineesh', 'Data Science', 'C', 89)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vivek', 'Data Science', 'A', 87)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()