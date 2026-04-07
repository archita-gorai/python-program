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


class Subscriber:
    def __init__(self):
        self.subscription_status="Active"
        self.discount_rate=0.2
    def apply_premium_discount(self,price):
        final_price=price*(1-self.discount_rate)    
        print(f"Subscribers discount applied ! New price:{final_price}")

class ProCustomer(Customer, Subscriber):
    def __init__(self,username,email,loyalty_points=0):
        Customer.__init__(self,username,email,loyalty_points=0)
        Subscriber.__init__(self)
    def show_dashboard(self):
        print(f"Welcome back")    

vip1=ProCustomer("A","abc.gmail.com")
vip1.login()
vip1.place_order("Laptop")
vip1.apply_premium_discount(40000)
vip1.show_dashboard()