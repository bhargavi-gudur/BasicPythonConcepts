class employee:
    message = "Employee Details"

    def __init__(self, name, salary, companyName, typejob):
        self.name = name
        self.salary = salary
        self.companyName = companyName
        self.jobType = typejob

    def salary_amount(self):
        print(employee.message)
        if not isinstance(self.salary, (int, float)):
            raise TypeError("Salary must be a number")
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
        return f" {self.name} earns {self.salary} in {self.companyName} as a {self.jobType}"
# Example usage of the employee class


bhargavi_employee = employee(
    "Bhargavi", 100000, "TechCorp", "senior Software Engineer")
print(bhargavi_employee.salary_amount())

suresh_employee = employee(
    "Suresh", 60000, "TechCorp", "Data Scientist")
print(suresh_employee.salary_amount())
