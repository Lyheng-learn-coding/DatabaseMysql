import mysql.connector

try:
# Create a connection
    db = mysql.connector.connect(
    host="localhost",  
    port = 3306 ,
    user="root",            
    password="",          
    database="Student_DB" 
)

    myCursor = db.cursor() 
    myCursor.execute("""
                 Create table if not exists Student (
                     ID int AUTO_INCREMENT PRIMARY KEY, 
                     FirstName varchar(255) , 
                     LastName varchar(255) ,
                     Age smallint Unsigned ,
                     PlaceBirth varchar(255) , 
                     BirhDate date ,
                     PhoneNumber varchar(255) 
                 )
                 """) 
    
    myCursor.execute("""
                     Create table if not exists SubjectScore (
                         StudentID int ,
                         SubjectName varchar(255) ,
                         Score float ,
                         PRIMARY KEY (StudentID, SubjectName),
                         FOREIGN KEY (StudentID) REFERENCES Student(ID)
                     )
                     """)



    while True : 
        print("===Student Management System===") 
        print("1. Add Student")
        print("2. Score Student")
        print("3. Display all students")
        print("4. Exit")
        choice = int(input("Enter your choice: ")) 
        if choice == 1 :
            print("Add data to students")
            firstName = input("Enter first name: ")
            LastName = input("Enter last name:")
            Age = int(input("Enter age: "))
            PlaceBirth = input("Enter place of birth: ")
            BirthDate = input("Enter birth date (yyyy-mm-dd) ")
            PhoneNumber = input("Enter phone number: ")

            insertValues  = (firstName, LastName, Age, PlaceBirth, BirthDate, PhoneNumber)
            myCursor.execute("insert into student (FirstName, LastName, Age , PlaceBirth, BirhDate, PhoneNumber) values (%s , %s, %s, %s, %s, %s)", insertValues)
            db.commit() 
            
  

            print("Data added successfully")
        elif choice == 2 :
            print("Display all students")
            myCursor.execute("select * from student")
            displayData = myCursor.fetchall() 
            for i in displayData :
                print(i)
                
            if not displayData :
                print("No students found.")
            else :
                print("All students displayed successfully\n")
    
            print("Add score to student") 

            studentID = int(input("Enter student ID: "))
            subjectName = input("Enter subject name: ")
            score  = float(input("Enter score:"))
            
            try :
                insertValues = (studentID , subjectName, score)
                myCursor.execute("insert into SubjectScore (StudentID , SubjectName , Score) Values (%s , %s , %s)" , insertValues)
                db.commit()
            except mysql.connector.Error as e :
                print("Error reason : " , e)   
            print("Score added successfully") 
            
        elif choice == 3 :
            print("Display all students with scores") 
            myCursor.execute("""
                             select 
                             student.ID , 
                             student.FirstName,
                             student.LastName,
                             subjectScore.subjectName,
                             subjectScore.Score
                             from student
                             inner join subjectScore on student.ID = subjectScore.StudentID

                             """)
            studentData = myCursor.fetchall() 
            for student in studentData :
                print(student)
                
            if not studentData: 
                print("No students found.")
            else :
                print("All students with scores displayed successfully")
        
        elif choice == 4 :
            print("Exit the system Good bye!")
            break
        else : 
            print("Invalid choice, please try again")
            


except mysql.connector.Error as err:
    print("❌ Failed to connect:", err)
else : 
    print("✅ Success! Connected to MySQL server.")
finally : 
    myCursor.close() 
    db.close() 
    

