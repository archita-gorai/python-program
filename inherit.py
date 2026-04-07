class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def login(self):
        print(f"{self.username} has logged in")

class Customer(User):
    def __init__(self,username,email,loyalty_points=0):
        super().__init__(username,email)
        self.loyalty_points=loyalty_points

    def place_order(self,item):
        print(f"{self.username} has ordered {item}.")

customer_1=Customer("A","abc@gmail.com")
customer_1.login()
customer_1.place_order("Laptop")                    