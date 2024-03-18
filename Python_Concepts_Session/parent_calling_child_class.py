##parent class
class shape:
    ##properties
    data1='abc'
    def no_of_slides(self):
        print("I have two slides")
    def color(self):
        print("My fav color is red")
##sub class

class Square(shape):
    ##properties
    data2='XYZ'
    def no_of_slides(self):
        print("I have four slides")
    def color(self):
        print("My fav color is green")
##calling the sub class
obj=Square()
obj.no_of_slides()
obj.color()

##calling the parent class
obj1=shape()
obj1.no_of_slides()
obj1.color()

