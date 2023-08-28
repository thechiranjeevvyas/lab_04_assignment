class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"{self.emp_id} - {self.name} (Age: {self.age}, Salary: {self.salary})"
    
def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]
    
    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        employees.sort(key=lambda emp: emp.age)
    elif choice == 2:
        employees.sort(key=lambda emp: emp.name)
    elif choice == 3:
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid choice.")
        return
    
    print("\nSorted Employee Data:")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    main()
