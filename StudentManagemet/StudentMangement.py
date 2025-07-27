student_database = {}    

class Student : 
    def __init__(self , Id , firstName , lastName , age , placeBirth , birthDate, PhoneNumber)  :
         self.Id =  Id
         self.firstName = firstName 
         self.lastName = lastName
         self.age = age 
         self.placeBirth = placeBirth
         self.birthDate = birthDate
         self.PhoneNumber = PhoneNumber
         
    def __str__(self):
            return (f"ID: {self.Id}, First name: {self.firstName}, Last name : {self.lastName}, \nAge: {self.age}, "
            f"\nPlace of Birth: {self.placeBirth}, \nBirth Date: {self.birthDate}, \nPhone: {self.PhoneNumber}")
    
    
    def accept(self) :
         # for user input 
         print("Do not enter the same ID it will override the previous one")
         studentId = int(input("Enter Student ID: "))
         FirstName = input("Enter first name: ")
         LastName = input("Enter last name: ")
         Age = int(input("Enter age: ")) 
         PlaceBirth = input("Enter place birth: ")
         BirthDate = input("Enter birth date (dd-mm-yyyy) :")
         phone = input("Enter phone number: ")
         
         student_info = Student( studentId , FirstName , LastName , Age , PlaceBirth ,BirthDate , phone) 
         student_database[studentId] = student_info
         print("Student added successfully")
         

    def  displayInfo(self ) : 
        if not student_database :
            print("No student data available")
            return 
        
        print("==================\n")
        for key , value in student_database.items() :
            print(f"Student {key} = {value}")

             
    
    def search(self) :
        print("Search option selected")
        searchId = int(input("Enter student ID: "))
        print("==================\n")
        student = student_database.get(searchId) 
        if student :
            print("Successfully found student")
            print(student)
        else :
            print("No student found")            
    
    
    def deleteInfo (self) :
        print("Delete option selected")
        if not student_database :   #if no student in database
            print("No student to delete")
            return
        print("Available students:")
        print("==================\n")
        for key , value in  student_database.items() :
            print(f"Student {key} = {value}\n")
        print("==================\n")
        
        deleteId = int(input("\nEnter student ID to delete: "))
        if deleteId in student_database:
            del student_database[deleteId]
            print(f"Student ID: {deleteId} has been deleted")
            print("Student deleted successfully")
        else :
            print("Unsuccessfully deleted student")
            print("Student not found")
           
        
            
    def updated(self):
        print("Update option selected")
        if not student_database:
          print("No student available")
          return

        for key, value in student_database.items() :
            print(f"Student {key} = {value}\n")


        updateId = int(input("Enter student ID to update: "))
        if updateId in student_database:
           student = student_database[updateId]
        # First Name
           if input("Change first name? (y/n): ").lower() == "y":
              student.firstName = input("Enter new first name: ")
        # Last Name
           if input("Change last name? (y/n): ").lower() == "y":
                student.lastName = input("Enter new last name: ")
        # Age
           if input("Change age? (y/n): ").lower() == "y":
               student.age = int(input("Enter new age: "))
        # Place of Birth
           if input("Change place of birth? (y/n): ").lower() == "y":
                student.placeBirth = input("Enter new place of birth: ")
        # Birth Date
           if input("Change birth date? (y/n): ").lower() == "y":
               student.birthDate = input("Enter new birth date (dd-mm-yyyy): ")
        # Phone Number
           if input("Change phone number? (y/n): ").lower() == "y":
              student.PhoneNumber = input("Enter new phone number: ")
           print("Student updated successfully!")
        else :
            print("Student ID not found.")
        

obj = Student(0 , "" , "" , 0 , "" , "" , "" )

while True :
    print("\n===System student management===")
    print("Choose an option: ")
    print("1. Add student")
    print("2. Search Student: ")
    print("3. Delete student: ")
    print("4. Updated student: ")
    print("5. Display student info")
    print("6. Exit")
    option = int(input("Enter an option: "))
    if option == 1 :
        obj.accept()
    elif option == 2 :
        obj.search()
    elif option == 3 :
        obj.deleteInfo()
    elif option == 4 :
        obj.updated()
    elif option == 5:
        obj.displayInfo()
    elif option == 6 :
        print("Exit the program!")
        break 
    else :
        print("Ïnvalid option.please try again!")
        
        


