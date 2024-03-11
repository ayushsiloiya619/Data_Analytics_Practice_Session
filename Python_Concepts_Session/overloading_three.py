class compute:
    def area(self, x=None , y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=compute()
print(obj.area())
print(obj.area(2))
print(obj.area(3,4))
