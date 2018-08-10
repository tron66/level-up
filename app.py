class Signup():

    def __init__(self, f_name, l_name, phone_number, email, password): # Initializer / Instance Attributes
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        #self.email = f_name+'.'+l_name+'@gmail.com'
        self.password = password

    @property
    def fullname(self): # instance method
        return '{} {}'.format(self.f_name, self.l_name)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.f_name, self.l_name)

    def correct_password(self, correct):
        return '{} is not {}'.format(self.password, correct)

    def submit(self):
        pass

# Instantiate the Signup object
user_1 = Signup('Mac','Macgyver', '0772190349','', 123)
user_2 = Signup('John','Wick', '0779202121','', 234)

# call our instance methods
#print(user_1.fullname())
print(user_1.phone_number)
#print(user_1.email)
print(user_1.password)
print(user_1.correct_password(234))
print(user_1.__dict__)

