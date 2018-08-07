class Signup():

    def __init__(self, f_name, l_name, phone_number, email, password): # Initializer / Instance Attributes
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        self.email = f_name+'.'+l_name+'@gmail.com'
        self.password = password

    def fullname(self): # instance method
        return '{} {}'.format(self.f_name, self.l_name) 

    def correct_password(self, correct):
        return '{} is not {}'.format(self.password, correct)    

    def submit(self): 
        pass  

# Instantiate the Signup object
client_1 = Signup('Mac','Macgyver', '077219034','', 123) 

# call our instance methods
print(client_1.fullname())
print(client_1.phone_number)
print(client_1.email)
print(client_1.password)
print(client_1.correct_password(234))
print(client_1.__dict__)

