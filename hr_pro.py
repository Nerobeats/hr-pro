import datetime
class Employee:
    def __init__(self , name , age , salary , employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        return 2020 - self.employment_year
class Manager(Employee):
    #Manager class here
    def __init__(self , name , age , salary , employment_year , bonus_percentage):
        super().__init__(name , age , salary , employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus (self):
        return self.bonus_percentage * self.salary
employees_list = []
managers_list = []
def main():
    print("Welcome to HR Pro 2019\nOptions: ")
    print(" 1. Show employees  \n2. Show Managers \n3. Add an employee\n4. Add a manager \n 5. Exit ")
    choice = int(input("What would you like to do ?"))
    while(choice != 5):

        if choice == 1:
            for employee_inf in employees_list:
                print (f"Name : {employee_inf.name}, Age : {employee_inf.age}, Salary : {employee_inf.salary}, Working Years:  {employee_inf.get_working_years()}")
        elif choice == 2:
                for mngr in managers_list:
                    print (f"Name : {str(mngr.name)}, Age : {mngr.age}, Salary : {mngr.salary}, Working Years:  {mngr.get_working_years()}, Bonus: {mngr.get_bonus()}" )
        elif choice == 3:
            nameInput =input("Name: ")
            ageInput = input("Age: ")
            salaryInput = float(input("Salary: "))
            employment_year_input = int(input("Employment Year: "))
            employees_list.append((Employee(nameInput,ageInput,salaryInput,employment_year_input)))
        elif choice == 4:
            nameInput =input("Name: ")
            ageInput = input("Age: ")
            salaryInput = float(input("Salary: "))
            employment_year_input = int(input("Employment Year: "))
            bonus_input = float(input("Bonus Percentage: "))
            managers_list.append(Manager(nameInput, ageInput, salaryInput, employment_year_input, bonus_input))
        else:
            break
        print("Welcome to HR Pro 2019\nOptions: ")
        print(" 1. Show employees  \n2. Show Managers \n3. Add an employee\n4. Add a manager \n 5. Exit ")
        choice = int(input("What would you like to do ?"))


if __name__ == '__main__':
	main()
