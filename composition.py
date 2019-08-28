class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def anual_sal(self):
        return (self.pay*12)+self.bonus
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)

    def total(self):
        return self.obj_salary.anual_sal()

emp=Employee("sudheer",23,100000,1500)
print(emp.total())