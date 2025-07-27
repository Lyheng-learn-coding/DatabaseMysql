import json 
import os


class Student : 
    def __init__(self , Id , firstName , lastName , age , placeBirth , birthDate, PhoneNumber)  :
         self.Id =  Id
         self.firstName = firstName 
         self.lastName = lastName
         self.age = age 
         self.placeBirth = placeBirth
         self.birthDate = birthDate
         self.PhoneNumber = PhoneNumber
         
         
    @staticmethod    
    def saveToJson(record , fileName = "StudentData.json") : 
         if  os.path.exists(fileName) :
             with open(fileName , "r") as file :
                 try :
                     exist_data = json.load(file) 
                 except json.JSONDecodeError:
                     exist_data = []  #temporary empty list
         else :
             exist_data = []     # temporary empty list
             print("File not found, please create a file")
         exist_data.append(record)
         
         with open(fileName , "w") as file :
             json.dump(exist_data , file , indent=4) 

        
         
    def __str__(self):
            return (f"ID: {self.Id}, First name: {self.firstName}, Last name : {self.lastName}, \nAge: {self.age}, "
            f"Place of Birth: {self.placeBirth}, \nBirth Date: {self.birthDate}, Phone: {self.PhoneNumber}")
    
    
    def accept(self) :
        
         print("Option selected") 
         try :
            with open("StudentData.json" , "r") as file :
                data = json.load(file )
         except FileNotFoundError as e:
            print("File not found the reason is:" , e) 
            return 
            
         print("==================\n")
         for record in data :
                print(record)
         if not data :
                print("No students available to add.")
                return
         print("==================\n")
            
         # for user input 
         print("Do not enter the same ID it will override the previous one")
         studentId = int(input("Enter Student ID: "))
         FirstName = input("Enter first name: ")
         LastName = input("Enter last name: ")
         Age = int(input("Enter age: ")) 
         PlaceBirth = input("Enter place birth: ")
         BirthDate = input("Enter birth date (dd-mm-yyyy) :")
         phone = input("Enter phone number: ")
         
         print("Student added successfully")
         
         record = {
                "Id": studentId,
                "FirstName": FirstName,
                "LastName": LastName,
                "Age": Age,
                "PlaceBirth": PlaceBirth,
                "BirthDate": BirthDate,
                "PhoneNumber": phone
         }
         Student.saveToJson(record) 

    def  displayInfo(self ) : 

        print("==================\n")   
        try :
             with open("StudentData.json" , "r") as file :
                print(file.read()) 
        except FileNotFoundError as e:
            print("No data found in JSON file. reason:" , e)
         
  
    
    def search(self) :
        print("Search option selected")
        searchId = int(input("Enter student ID: "))
        print("==================\n")
     
        with open("StudentData.json" , "r") as file :
            try :
                data = json.load(file)
                for record in data:
                    if record["Id"] == searchId:
                        print("Student found in JSON file:")
                        print(record)
                        return
            except (json.JSONDecodeError , FileNotFoundError):
                print("No data found in JSON file.")
                return 

        

    def deleteInfo (self) :
        print("Delete option selected")
        print("Available students:")
        try :
            with open("StudentData.json" , "r") as file :
                data = json.load(file)
        except FileNotFoundError as e :
            print("No data found in JSON file. reason:", e)
            return 
        
        print("==================\n")
        for record in data :
            print(record)
        if not data :
            print("No student to delete")
            return
        print("==================\n")
        
        deleteId = int(input("\nEnter student ID to delete: "))
        newData = []
        for record in data :
            if record["Id"] != deleteId :
                newData.append(record)
                
                
        if len(newData) == len(data):
            print("Student not found.")
        else :
            with open("StudentData.json", "w") as file:
                json.dump(newData, file, indent=4)
            print(f"Student ID: {deleteId} has been deleted")
            print("Student deleted successfully")
                      
                    

    def updated(self):
        print("Update option selected")


        print("===Available students===")
        try :
            with open("StudentData.json" , "r") as file :
             data = json.load(file)
        except FileNotFoundError as e :
            print("No data found in JSON file. reason:", e)
            return 

        print("====================\n")
        # Student.displayInfo(self)  
        for record in data :
            print(record)
        if not data :
            print("No students available to update.")
            return
        print("====================\n")
        

        updateId = int(input("Enter student ID to update: "))
        student = None
        for record in data :
            if record["Id"] == updateId :
                student = record 
                break
            
        if not student:
            print("No student found with that ID.")
            return
        
        print("Student found:" , student)

        # First Name
        if input("\nChange FirstName? (y/n): ").lower() == "y":
                student["FirstName"] = input("Enter new FirstName: ")
        # Last Name
        if input("Change LastName? (y/n): ").lower() == "y":
                 student["LastName"] = input("Enter new LastName: ")
        # Age
        if input("Change Age? (y/n): ").lower() == "y":
                 student["Age"] = int(input("Enter new Age: "))
        # Place of Birth
        if input("Change PlaceBirth? (y/n): ").lower() == "y":
                student["PlaceBirth"] = input("Enter new PlaceBirth: ")
        # Birth Date
        if input("Change BirthDate? (y/n): ").lower() == "y":
               student["BirthDate"] = input("Enter new BirthDate (dd-mm-yyyy): ")
        # Phone Number
        if input("Change PhoneNumber? (y/n): ").lower() == "y":
              student["PhoneNumber"] = input("Enter new PhoneNumber: ")
        print("Student updated successfully!")

        with open("StudentData.json" , "w") as file :
                json.dump(data, file, indent=4)

        


def menu() :
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
            print("Invalid option.please try again!")
        
if __name__ == "__main__":
    menu()        


