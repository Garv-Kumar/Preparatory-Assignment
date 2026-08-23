class Employee:

    def initialize(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary

    def display_details(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Monthly Salary:", self.monthly_salary)

    def modify_salary(self, new_salary):
        self.monthly_salary = new_salary

    def calculate_yearly_salary(self):
        return self.monthly_salary * 12


employee1 = Employee()

print("Enter details for Employee 1")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
monthly_salary = float(input("Enter monthly salary: "))

employee1.initialize(first_name, last_name, monthly_salary)

employee2 = Employee()

print()
print("Enter details for Employee 2")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
monthly_salary = float(input("Enter monthly salary: "))

employee2.initialize(first_name, last_name, monthly_salary)

print()
print("Employee 1 Details")
employee1.display_details()

print()
print("Employee 2 Details")
employee2.display_details()

print()
print("Yearly Salary Before 10% Increase")
print("Employee 1:", employee1.calculate_yearly_salary())
print("Employee 2:", employee2.calculate_yearly_salary())

new_salary1 = employee1.monthly_salary + employee1.monthly_salary * 10 / 100
employee1.modify_salary(new_salary1)

new_salary2 = employee2.monthly_salary + employee2.monthly_salary * 10 / 100
employee2.modify_salary(new_salary2)

print()
print("Yearly Salary After 10% Increase")
print("Employee 1:", employee1.calculate_yearly_salary())
print("Employee 2:", employee2.calculate_yearly_salary())