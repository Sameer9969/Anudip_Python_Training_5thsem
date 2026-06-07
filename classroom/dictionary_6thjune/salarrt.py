"""
wap to create a dictionary that contains the record of 10 employee where employee used as key and salary is used as the value so 
1. find out the total number of employee having salarry greater then 30000 ,   
2. display the list of the employee whoes salarry is below 20000   """


employee_data = {}

for i in range(1, 11):
    emplyee_id = int(input("enter the employee id: "))
    salary = int(input("enter the salary:) "))

    employee_data[emplyee_id] = salary

# 1.find out the total number of employee having salarry greater then 30000
count = 0

for salary in employee_data.values():
    if salary > 30000:
        count += 1

print("the total number of employee having salarry greater then 30000 :",count)

#  2. display the list of the employee whoes salarry is below 20000
print("Employees having salary below 20000:")

for employee_id, salary in employee_data.items():
    if salary < 20000:
        print(employee_id)

