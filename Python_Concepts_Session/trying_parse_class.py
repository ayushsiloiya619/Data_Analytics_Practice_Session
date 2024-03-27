import re
##Trying the parser 
class parse:
    def __init__(self , text):
        self.text=text
    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None
    def phone(self):
        match = re.search(r'\d{2}-\d{2}-\d{4}', self.text)
        if match:
            return match.group(0)
        return None
    def parse(self):
        return{
            'email':self.email(),
            'phone':self.phone()
        }
string = 'Contact us 12-23-5632 or test@gmail.com'
parser = parse(string)
print(parser.parse())
##fetching the result
##re.match() vs re.search() is that re.search searches the whole string , re.match goes only fot he first match and return the result.        