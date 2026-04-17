# class Employee :
#     def __init__(self,name,age,salary):          #constructor-run automatically when object is created
#         self.name=name                           #store values inside object
#         self.age=age
#         self.salary=salary
#     def __str__(self):                            #specila method- contro;s how objects is printed
#         return f"{self.name},{self.age},{self.salary}"      #return formatted string


# class EmployeeManager :
#     def __init__(self) :                           #create empty list to store employees
#         self.employee = []                          
#     def add_employee(self,name,age,salary):         #function to add employee
#         emp = Employee (name,age,salary)            #create new employee object
#         self.employees.append(emp)                  #add employee list
#         print("Employee added sucessfully!!")          #conformation message

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.age}, {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        print("Employee added successfully!")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                print(emp)

    def delete_by_age_range(self, min_age, max_age):
        self.employees = [
            emp for emp in self.employees
            if not (min_age <= emp.age <= max_age)
        ]
        print("Employees deleted in given age range.")

    def find_by_name(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                print(emp)
                return
        print("Employee not found.")

    def update_salary(self, name, new_salary):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                emp.salary = new_salary
                print("Salary updated successfully!")
                return
        print("Employee not found.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\n--- Employee System ---")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete by Age Range")
            print("4. Find by Name")
            print("5. Update Salary")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = int(input("Enter salary: "))
                self.manager.add_employee(name, age, salary)

            elif choice == "2":
                self.manager.list_employees()

            elif choice == "3":
                min_age = int(input("Enter min age: "))
                max_age = int(input("Enter max age: "))
                self.manager.delete_by_age_range(min_age, max_age)

            elif choice == "4":
                name = input("Enter name: ")
                self.manager.find_by_name(name)

            elif choice == "5":
                name = input("Enter name: ")
                salary = int(input("Enter new salary: "))
                self.manager.update_salary(name, salary)

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice, try again!")


# Run the program
if __name__ == "__main__":
    app = FrontendManager()
    app.run()
        