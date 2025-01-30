# from datetime import date
# class Customer:
#     def __init__(self, customer_id,first_name,last_name,phone,email,street,city,state,zip_code):
#         self.customer_id=customer_id
#         self.first_name=first_name
#         self.last_name=last_name
#         self.phone=phone
#         self.email=email
#         self.street=street
#         self.city=city
#         self.state=state
#         self.zip_code=zip_code
#     def get_fullname(self):
#         return f'{self.first_name} {self.last_name}'
# class Order:
#     def __init__(self, order_id, order_status, order_date, required_date, shipped_date, store_id, staff_id):
#         self.order_id = order_id
#         self.order_status = order_status
#         self.order_date = order_date
#         self.required_date = required_date
#         self.shipped_date = shipped_date
#         self.store_id = store_id
#         self.staff_id = staff_id
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def get_total_price(self):
#         return sum(item.get_total() for item in self.items)

# class Order_item:
#     def __init__(self, order_id, product_id, quantity, list_price, discount):
#         self.order_id = order_id
#         self.product_id = product_id
#         self.quantity = quantity
#         self.list_price = list_price
#         self.discount = discount

#     def get_total(self):
#         return self.quantity * self.list_price * (1 - self.discount / 100)

# class Transaction:
#     def __init__(self, transaction_id, customer, order):
#         self.transaction_id = transaction_id
#         self.customer = customer
#         self.order = order

#     def get_transaction_details(self):
#         return {
#             "Transaction ID": self.transaction_id,
#             "Customer": self.customer.get_fullname(),
#             "Order ID": self.order.order_id,
#             "Total Amount": f"${self.order.get_total_price():.2f}",
#             "Order date":self.order.order_date.strftime("%Y-%m-%d"),
#             "Order Items": [
#                 {"Product ID": item.product_id, "Quantity": item.quantity, "Price": item.get_total()}
#                 for item in self.order.items
#             ]
#         }

# # Creating Customer
# customer1 = Customer(101, "gudelli", "manoj", 9676148598, "gudellimanoj@gmail.com", "medchal", "Hyderabad", "Telangana", 501401)

# # Creating Order
# order = Order(101, 1, date.today(), date.today(), None, 10, 5)

# # Creating Order Item and adding it to Order
# order_item1 = Order_item(101, 201, 2, 500, 10)
# order.add_item(order_item1)

# # Creating Transaction
# transaction1 = Transaction(5001, customer1, order)

# # Printing transaction details
# details = transaction1.get_transaction_details()
# for key, value in details.items():
#     print(f"{key}: {value}")


# Abstract method
# from abc import ABC,abstractmethod
# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
#     def show(self):
#         print("Concrete Method")
# class Son(Father):
#     def disp(self):
#         print("Son is implementing the abstract class")
# class Daughter(Father):
#     def disp(self):
#         print("Daughter is implementing  the abstract method")

# s=Son()
# s.disp()
# s.show
# d=Daughter()
# d.disp()
# d.show

# Pan Card 
# from abc import ABC,abstractmethod
# class Person(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age=age
#         self.pancard_number=None
#     def set_pancard(self,pancard_number):
#         self.pancard_number=pancard_number
#     @abstractmethod
#     def display(self):
#         pass
# class Father(Person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#     def display(self):
#         print(f"Father Name:{self.name},Father Age:{self.age},FatherPancard:{self.pancard_number}")
# class Son(Father):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#     def display(self):
#         print(f"Son Name:{self.name},Son Age:{self.age},SonPancard:{self.pancard_number}")
# father=Father("rajamouli",49)
# son=Son("manoj",20)
# father.set_pancard("#111111")
# son.set_pancard("#000000")
# son.display()
# father.display()



from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")
    def stop_engine(self):
        print("Car Engine Stopped")
car=Car()
car.start_engine()
car.stop_engine()


