# # raise1.py

# print("raise")

# try:
#     raise NameError('Hi There')
# except NameError as e:
#     print('An excepyion flew by!')
#     print("e:", e)

# print("exit")


class IsufficienBalaceError(Exception):
    pass

class Account:
    def __init__(self,balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise IsufficienBalaceError("잔고가 부족합니다.")
        self.balance -= amount
        return self.balance
    
lim = Account(1000)
lim.withdraw(2000)