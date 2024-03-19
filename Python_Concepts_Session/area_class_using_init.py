#Circle and Circumference
class Circle:
    def __init__(self,radius):
        self.pi = 3.14
        self.radius = radius
    def area(self):
        return self.pi * self.radius**2
    def circumference(self):
        return 2*self.pi * self.radius
Result = Circle(10)
print(Result.area())
print(Result.circumference())