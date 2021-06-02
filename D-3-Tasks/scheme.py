class scheme:
    def __init__(self):
        self.scheme_id = print()
        self.scheme_name = print()
    def sin(self):
        print('Please provide your Scheme name')
        s1 = input('Enter 1: ')
        s2 = input('Enter 2: ')
        print(f'1:{s1}||2:{s2}')
        self.scheme_id = int(input("Please press 1 or 2: "))
        if self.scheme_id == 1:
            return f'Scheme_name:{s1}'
        elif self.scheme_id == 2:
            return f'Scheme_name:{s2}'
        else:
            return('Please press 1 or 2')
    def mes(self):
        self.outgoing_rate = print('')
        self.message_charge  = print('')
        if self.scheme_id == 1:
            return('outgoing_rate=2||message_charge=1.50')
        elif self.scheme_id == 2:
            return('outgoing_rate=1||message_charge=0.50')
        else:
            return('Your plan is exhausted please recharge')
   

class customer(scheme):
    def __init__(self):
        scheme.__init__(self)
        self.cust_id = cid
        self.name = name
        self.mobile_no = no
    def display(self):
        return f'{self.name} has customer id: {self.cust_id} and mobile number: {self.mobile_no}'

cid = int(input('Enter customer id: '))
name = input('Enter your name: ')
no = int(input('Enter you mobile number: '))

s=scheme()
c=customer()
print(s.sin())
print(s.mes())
print(c.display())
