from BikeStores_database.module3 import Order
from BikeStores_database.module1 import Order_item
from BikeStores_database.module4 import Customer
from BikeStores_database.module2 import Transaction
from datetime import date
customer1=Customer(101,"gudelli","manoj",9999955555,"manojgudelli@gmail.com","medchal","Hyderabad","Telangana",501401)
customer2=Customer(102,"gudelli","manoj",9999955555,"manojgudelli@gmail.com","medchal","Hyderabad","Telangana",501401)
order=Order(101,1,date.today(),date.today(),None,10,5)
order2=Order(102,1,date.today(),date.today(),None,10,5)
order_item1=Order_item(101,201,2,500,10)
order_item2=Order_item(101,202,1,500,10)
order_item3=Order_item(102,202,1,500,10)
order.add_item(order_item1)
order.add_item(order_item1)
order2.add_item(order_item3)
transaction1=Transaction(5001,customer1,order)
transaction2=Transaction(5002,customer2,order2)
details=transaction1.get_transaction_details()
details2=transaction2.get_transaction_details()
for key,value in details.items():
    print(f"{key}: {value}")
for key,value in details2.items():
    print(f"{key}: {value}")
