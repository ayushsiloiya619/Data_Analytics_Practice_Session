##Generating hash value for an employee record:
class Employee:
    def __init__(self,name,base_pay):
        self.name=name
        self.base_pay=base_pay
    def get_pay(self):
        return self.base_pay
class Sales(Employee):
    def __init__(self,name,base_pay,sale_incentive):
        self.name=name
        self.base_pay=base_pay
        self.sale_incentive=sale_incentive
    def get_pay(self):
        return self.base_pay+self.sale_incentive
class Software_Developer(Employee):
    def __init__(self,name,base_pay,year_bonus):
        self.name=name
        self.base_pay=base_pay
        self.year_bonus=year_bonus
    def get_pay(self):
        return self.base_pay + self.year_bonus
sales_team=Sales('Ayush Siloiya',50000,10000)
print("The Amount that is generated:",sales_team.get_pay(),'INR')
software_team=Software_Developer('Ayush Siloiya',80000,12000)
print("The Amount that is generated:",software_team.get_pay(),'INR')
print("The Hash Generated For Employee Record is: ")
Stored_HASHED=[hash(sales_team),hash(software_team)]
for x in Stored_HASHED:
    print("Value:",x)

