##parent class
class employee:
    def __init__(self,name,base_pay):
        self.name=name
        self.base_pay=base_pay
    def get_pay(self):
        return self.base_pay
##modify actual parent class through child class calling.
class Sales(employee):
    def __init__(self, name , base_pay , sales_incentive):
        self.name=name
        self.base_pay=base_pay
        self.sales_incentive=sales_incentive
    def get_pay(self):
        return self.base_pay + self.sales_incentive
john=Sales('John Doe',30000,10000)
print("The Sales Employee Will Get",john.get_pay(),'INR')
class Software_Fresher_Intern(employee):
    def __init__(self , name , base_pay , join_bonus):
        self.name=name
        self.base_pay=base_pay
        self.join_bonus=join_bonus
    def get_pay(self):
        return self.base_pay + self.join_bonus
ayush=Software_Fresher_Intern('Ayush',10000,0)
print("The New Joinee Will Get ",ayush.get_pay(),'INR')
class Software_Developer(employee):
    def __init__(self , name, base_pay, year_bonus):
        self.name=name
        self.base_pay=base_pay
        self.year_bonus=year_bonus
    def get_pay(self):
        return self.base_pay + self.year_bonus
samiksha=Software_Developer('Samiksha',50000,12000)
print("The Software Developer Will Get ",samiksha.get_pay(),'INR')