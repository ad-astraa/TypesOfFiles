import csv

class EmployeeManagementSystem:
    def __init__(self, filename):
        self.filename = filename

    def add_employee(self, employee_data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee_data)
        print(f"Employee {employee_data[0]} added successfully!")

    def update_employee(self, employee_id, updated_data):
        employees = self.read_all_employees()
        found = False
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for employee in employees:
                if employee[0] == employee_id:
                    writer.writerow(updated_data)
                    found = True
                    print(f"Employee {employee_id} updated successfully!")
                else:
                    writer.writerow(employee)
        if not found:
            print(f"Employee {employee_id} not found.")

    def read_all_employees(self):
        employees = []
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            employees = list(reader)
        return employees

    def display_employees(self):
        employees = self.read_all_employees()
        for emp in employees:
            print(emp)
    def generate_report(self):
        employees = self.read_all_employees()
        department_counts = {}
        for emp in employees:
            department = emp[2]  # Assuming department is the third column
            if department in department_counts:
                department_counts[department] += 1
            else:
                department_counts[department] = 1
        print("Department-wise Employee Report:")
        for department, count in department_counts.items():
            print(f"{department}: {count} employees")
            
    def main():
        filename = 'employees.csv'
        system = EmployeeManagementSystem(filename)
        while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Display All Employees")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            employee_data = input("Enter employee details (ID, Name, Department, Position, Salary): ").split(',')
            system.add_employee(employee_data)
        elif choice == '2':
            employee_id = input("Enter employee ID to update: ")
            updated_data = input("Enter updated details (ID, Name, Department, Position, Salary): ").split(',')
            system.update_employee(employee_id, updated_data)
        elif choice == '3':
            system.display_employees()
        elif choice == '4':
            system.generate_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
