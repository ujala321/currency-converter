
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
class Manager(Employee):
    def __init__(self, emp_id, name, department):
        super().__init__(emp_id, name)
        self.department = department
    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")
e1 = Employee(101, "Alice")
m1 = Manager(102, "Bob", "Sales")
print("=== Employee ===")
e1.show_details()
print("\n=== Manager ===")
m1.show_details()



