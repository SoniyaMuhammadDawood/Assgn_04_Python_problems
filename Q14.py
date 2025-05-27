# Q14. Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dert_name, employee):
        self.deprt_name = dert_name
        self.employee = employee
    
    def showDetails(self):
        print("Department:", self.deprt_name)
        print("Employee:", self.employee.name)

emp = Employee("Soniya")
deprt = Department("IT Department", emp)
deprt.showDetails()