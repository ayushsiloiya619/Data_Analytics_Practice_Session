class TemperatureConverter():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5+32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9
    @staticmethod
    def kevin_to_celsius(k):
        return k-273.15
    @staticmethod
    def celsius_to_kevin(c):
        return 273+c
    @staticmethod
    def fahrenheit_to_kevin(f):
        return 5*(f+459.67)/9
    @staticmethod
    def kevin_to_fahrenheit(k):
        return 9*k/5 - 459.67
Result = TemperatureConverter()
print(Result.celsius_to_fahrenheit(32))
