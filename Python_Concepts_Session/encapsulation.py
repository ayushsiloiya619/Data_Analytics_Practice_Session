class Counter:
    def __init__(self):
        self.current=0
    def increment(self):
        self.current=self.current+1
    def decrement(self):
        self.current=self.current-1
    def value(self):
        return self.current
    def reset(self):
        self.current=0
encapsulation=Counter()
encapsulation.increment()
encapsulation.increment()
print(encapsulation.value())
encapsulation.decrement()
print(encapsulation.value())
encapsulation.reset()
print(encapsulation.value())