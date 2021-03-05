#! usr/bin/python3

# users 
class User():
    
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.email = email 
        
    def show_details(self):
        print('Personal Details\n')
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'email: {self.email}')
        
# bank 
class Bank(User):
    
    def __init__(self, name, age, email):
        super().__init__(name, age, email) # prevents us from having to rewrite parent args 
        self.balance = 0
        
    def deposit(self, amount=None):
        amount = input('Deposit amount: \n\n')
        self.balance = self.balance + int(amount)
        print('Account balance has been updated...')
        
    def view_acct(self):
        q = input('Would you like to view your account balance y/n? ')
        if q.lower() == 'y':
            print(f'Account: {self.balance}')
        else:
            return f'Hello {self.name}'
        
x = User('Adrian Brown', 23, 'test@email.com')
x.show_details()
y = Bank('Adrian', 23, 'email@email.com')
y.deposit()
y.view_acct()