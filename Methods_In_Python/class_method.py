class TemperatureConverter():
    @classmethod
    def celsius_to_fahrenheit(self,c):
        self.c=c
        return 9*c/5+32
    @classmethod
    def fahrenheit_to_celsius(self,f):
        self.f=f
        return 5*(f-32)/9
    @classmethod
    def kevin_to_celsius(self,k):
        self.k=k
        return k-273.15
    @classmethod
    def celsius_to_kevin(self,c):
        self.c=c
        return 273+c
    @classmethod
    def fahrenheit_to_kevin(self,f):
        self.f=f
        return 5*(f+459.67)/9
    @classmethod
    def kevin_to_fahrenheit(self,k):
        self.k=k
        return 9*k/5 - 459.67
Result = TemperatureConverter()
print(Result.celsius_to_fahrenheit(32))
