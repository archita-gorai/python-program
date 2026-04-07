class bankaccount:


    def __init__(self,a,b,n):
         self.name=a
         self.__balance=b
         self.interest_rate=n
    def view_balance(self):
         return self.__balance    
    def deposit(self, amount):
         if amount>0:
              self.balance+=amount
              return self.balance
         return "Invalid deposit amount"
    def withdraw(self,amount):
         if 0<amount<=self.balance:
              return self.balance
         return "Insufficient balance or invalid amount"  
    def apply_interest(self):
         interest_amt=self.balance*bankaccount.interest_rate
         self.balance+=interest_amt
         return self.balance    
n=input("Enter the name of the account holder")
c=int(input("Enter the balance"))     
r=int(input("Rate of interest:"))
b1=bankaccount(n,c,r)
print(b1.name)
print(b1.__balance)
b2=bankaccount(n,c,r)
#print("balance of b1",b1.__balance)
#print("balance of b2",b2.__balance)