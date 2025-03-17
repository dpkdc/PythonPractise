class bank_detail:
    def __init__(self,balanace, account_no):
        self.bal= balanace
        self.acc=account_no
    def credit(self,amount):
        self.bal+= amount
        print("Your account has been credited with", amount)
        print("Your updated balance",self.get_balance())

    def debit(self,amount):
        self.bal-= amount
        print("Your account has been debited with", amount)
        print(f'your updated balance {self.get_balance()}')


    def get_balance(self):
        return self.bal
acc1= bank_detail(20000,1234567890)
acc1.credit(1000)
acc1.debit(2000)
acc1.credit(47000)