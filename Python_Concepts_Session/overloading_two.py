class a:
    def hello(self, name=None):
        if name is not None:
            print('Hello'+" "+name)
        else:
            print('Hello Buddy!')
obj=a()
obj.hello()
obj.hello('Ayush')
    