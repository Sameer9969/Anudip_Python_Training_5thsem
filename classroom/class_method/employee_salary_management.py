"""4. Employee Salary Management (Intermediate) 
Problem Statement: 
Create an Employee class containing employee ID, name, and monthly salary. 
Implement methods to: 
• Display employee details.  
• Calculate annual salary.  
• Increase salary by a given percentage.  
Sample Output: 
Employee Name : Rohan 
Monthly Salary: ₹50000 
Annual Salary : ₹600000 
Updated Salary: ₹55000 """

#employee salary management
class Employee:
    def __init__(self, emp_id, name, monthly_salary, increment=0):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary
        self.increment = increment
        self.annual_salary = 0
        self.updated_salary = 0

    # method to display employee details
    def display_details(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("Monthly Salary :", self.monthly_salary)
        print("Annual Salary :", self.calculate_annual_salary())
        print("Updated Salary :", self.calculate_updated_salary())

    # annual salary
    def calculate_annual_salary(self):
        self.annual_salary = self.monthly_salary * 12
        return self.annual_salary

    # updated salary
    def calculate_updated_salary(self):
        increase_amount = (self.monthly_salary * self.increment) / 100
        self.updated_salary = self.monthly_salary + increase_amount
        return self.updated_salary
#---------------------------------------------------
#----------------main manue ------------------------
#---------------------------------------------------
emp_id = int(input("enter the employee id :"))
name = input("enter the name :")
monthly_salary = int(input("enter the monthly salary :"))
increment = float(input("enter the increment percentage :"))

employee = Employee(emp_id, name, monthly_salary, increment)

print("employee report")
employee.display_details()

