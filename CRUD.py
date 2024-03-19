import psycopg2

conn = psycopg2.connect (database="School",
                        host="localhost",
                        user="postgres",
                        password="password",
                        port="5432")
conn.autocommit = True

cursor = conn.cursor()

def getAllStudents():
    #Gets all rows from the students table and prints it all
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

def addStudent(first_name, last_name, email, enrollment_date):
    #Adds a student with the specified variables
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))

def updateStudentEmail(student_id, new_email):
    #Updates the specified student's email based on their id
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))

def deleteStudent(student_id):
    #Deletes the specified student based on their id
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id))

userInput = -1

#When the user inputs 0, close the program otherwise do as the user specified and loop again
while userInput != "0":
    userInput = input("0. Exit \n1. Get all students \n2. Add student \n3. Update student email \n4. Delete student\n")

    if userInput == "1":
        getAllStudents()

    elif(userInput == "2"):
        fname = input("Input student's first name \n")
        lname = input("Input student's last name \n")
        email = input("Input student's email \n")
        date = input("Input student's enrollment date \n")
        addStudent(fname, lname, email, date)

    elif(userInput == "3"):
        id = input("Input student's id \n")
        email = input("Input student's new email \n")
        updateStudentEmail(id, email)

    elif(userInput == "4"):
        id = input("Input student's id \n")
        deleteStudent(id)


        