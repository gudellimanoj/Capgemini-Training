# #tuple implementation
# def get_data();
#     n=()
#     return n
# def get_data1():
#     n=(0,)
#     return n
# def get_data2():
#     n=(0,'NI',1,2,3)
#     return n
# def get_data3():
#     n=0,'NI',1,2,3
#     return n
# def get_data4():
#     n=('abc',('def','ghi'))
#     return n
# def get_data5():
#     n=tuple('spam')
#     return n
# def get_data6():
#     n=(1,2,3,4)
#     for i in n:
#         return t[i]
# def get_data7():
#     n=(1,2,3,4,5)
#     return n[1:3]
# def get_data8():
#     n=('abc',('def','ghi'))
#     return n[0][1:3]
    
# def main():
#     print("1. An empty tuple:", get_data())
#     print("2. A tuple with one element:", get_data1())
#     print("3. A tuple with multiple elements:", get_data2())
#     print("4. A tuple with multiple elements:", get_data3())
#     print("5. A tuple with nested tuple:", get_data4())
# main()

# Sets
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# #sets with duplicate elements
# set3 = {1,2,2,3,4,4,5,6,6,7}
# #union of two sets
# print("1. Union of two sets:", set1.union(set2))
# #intersection of two sets
# print("2. Intersection of two sets:", set1.intersection(set2))
# #difference of two sets
# print("3. Difference of two sets:", set1.difference(set2))
# #list into tuple
# list1 = [1,2,3,4,5]
# tuple1 = tuple(list1)
# print("4. List converted into tuple:", tuple1)
# #tuple into list
# tuple2 = (1,2,3,4,5)
# list2 = list(tuple2)
# print("5. Tuple converted into list:", list2)



# creating a claSS of employee

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Salary:", self.salary)
#     def update_salary(self):
#         self.salary = self.salary+1000
#         print("Salary updated to:", self.salary)

# if __name__ == "__main__":
#     e1 = Employee("John", 25, 25000)
#     e2 = Employee("Jane", 24, 24000)
#     e1.display()
#     e2.display()
#     e1.update_salary()
#     e1.display()     
# if __name__ == "__main__":



#tuples
# def get_input():
#     n=()
#     return n
# def get_input1():
#     n=(0,)
#     return n
# def get_input2():
#     n=(0,'NI',1.2,3)
#     return n
# def get_input3():
#     r=0,'Ni',1.2,3
#     return r
# def get_input4():
#     t=('abc',('def','ghi'))
#     return t
# def get_input5():
#     t=tuple('spam')
#     return t
# def get_input6():
#     t=(1,2,3,4,5)
#     for i in t:
#         return t[i]
# def get_input7():
#     t=(1,2,3,4,5)
#     return t[1:3]
# def get_input8():
#     t=('abc',('efg','hij'))
#     return  t[0][1:3]
# def main():
#     n = get_input()
#     n1=get_input1()
#     n2=get_input2()
#     n3=get_input3()
#     n4=get_input4()
#     n5=get_input5()
#     n6=get_input6()
#     n7=get_input7()
#     n8=get_input8()
#     print(n)
#     print(n1)
#     print(n2)
#     print(n3)
#     print(n4)
#     print(n5)
#     print(n6)
#     print(n7)
#     print(n8)
# main()
#sets
# empty_set=set()
# print(empty_set)
# #set with elements
# s={1,2,3,4,5}
# print(s)
# #set with duplicate elements
# s={1,2,2,3,3,4,4,5,5}
# print(s)
# #union
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Union',s.union(t))
# print('Union using or:',s|t)
# #intersection
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Intersection',s.intersection(t))
# print('Internsection using and:',s&t)
# #difference
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Difference',s-t)
# print('Difference using inbuilt:',s.difference(t))
# #list into tuple:
# list=[1,2,3]
# tuple=tuple(list)
# print(tuple)
# # Convert a tuple into a list
# tuple1 = (1, 2, 3)  # Use a variable name other than 'tuple' to avoid confusion
# list1 = list(tuple1)
# print(list1)  # Output: [1, 2, 3]
# class Employee:
#     def _init_(self,employee_id,name, age,salary,postion):
#         self.employee_id=employee_id
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.postion = postion
        
#     def display(self):
#         print(f"Employee_id:{self.employee_id} ,Name: {self.name}, Age: {self.age}, Salary: {self.salary} , Position: {self.postion}") 
#     def salary_update(self):
#         self.salary = self.salary + 1000
# if _name=='main_':
#     emp1=Employee(1,'John',30,5000,'Software Engineer')
#     emp1.display()
#     emp1.salary_update()
#     emp1.display()



# class Employee:
#     def _init_(self,name,age,gender,position,base_salary,food_allowance,travel_allowance):
#         self.name = name
#         self.age=age
#         self.gender=gender
#         self.position=position
#         self.__basesalary=base_salary
#         self.__bonus=0
#         self.__deductions=0
#         self.__food_allowance=food_allowance
#         self.__travel_allowance=travel_allowance
#         self.__tax=0
#     def get_base_salary(self):
#         return self.__basesalary
#     def set_base_salary(self,salary):
#         if salary>=0:
#             self.__basesalary=salary
#         else:
#             print("Invalid salary")
#     def get_bonus_salary(self):
#         return self.__bonus
#     def set_bonus_salary(self,bonus):
#         if bonus>=0:
#             self.__bonus=bonus
#         else:
#             print("Invalid bonus")
#     def get_deductions(self):
#         return self.__deductions
#     def set_deductions(self,deductions):
#         if deductions>=0:
#             self.__deductions=deductions
#         else:
#             print("Invalid deductions")
#     def get_food_allowance(self):
#         return self.__food_allowance
#     def set_food_allowance(self,food_allowance):
#         if food_allowance>=0:
#             self.__food_allowance=food_allowance
#         else:
#             print("Invalid food allowance")
#     def get_travel_allowance(self):
#         return self.__travel_allowance
#     def set_travel_allowance(self,travel_allowance):
#         if travel_allowance>=0:
#             self.__travel_allowance=travel_allowance
#         else:
#             print("Invalid travel allowance")
#     def get_tax(self):
#         return self.__tax
#     def set_tax(self,tax):
#         if tax>=0:
#             self.__tax=tax
#         else:
#             print("Invalid tax")
#     def calculate_tax(self,tax_rate):
#         gross_salary=self.calculate_gross_salary()
#         self.__tax=(gross_salary)*(tax_rate/100)
#         return self.__tax
#     def calculate_net_salary(self,tax_rate):
#         gross_salary=self.calculate_gross_salary()
#         tax_rate1=self.calculate_tax(tax_rate)
#         return gross_salary-tax_rate1

#     def calculate_gross_salary(self):
#         return self._basesalary+self.bonus-self.deductions+self.food_allowance+self._travel_allowance
#     def display(self,tax_rate):
#         print(f'Name:{self.name}')
#         print(f'Age:{self.age}')
#         print(f'Gender:{self.gender}')
#         print(f'Position:{self.position}')
#         print(f'Base Salary:{self.__basesalary}')
#         print(f'Bonus Salary:{self.__bonus}')
#         print(F'Deductions Salary:{self.__deductions}')
#         print(f'Food Allowance:{self.__food_allowance}')
#         print(f'Travel Allowances:{self.__travel_allowance}')
#         print(f'Tax charged:{self.__tax}')
#         print(f'Calculated tax:{self.calculate_tax(tax_rate)}')
#         print(f'Net Salary:{self.calculate_net_salary(tax_rate)}')
#         print(f'Calculate Gross Salary:{self.calculate_gross_salary()}')
# if __name__ == "__main__":
#     name=input('Enter the name:')
#     age=int(input('Enter the age:'))
#     gender=input('Enter the gender:')
#     position=input('Enter the position:')
#     salary=int(input('Enter the salary:'))
#     food_allowance=int(input('Enter the food allowance:'))
#     travel_allowance=int(input('Enter the travel allowance:'))
#     tax=int(input('Enter the tax rate'))
#     emp=Employee(name,age,gender,position,salary,food_allowance,travel_allowance)
#     emp.display(tax)
#     bonus=int(input('Enter the bonus:'))
#     deductions=int(input('Enter the deductions:'))
#     emp.set_bonus_salary(bonus)
#     emp.set_deductions(deductions)
#     emp.set_tax(tax)
#     emp.display(tax)


#Inheritance
# class parent:
#     def display_parent(self):
#         print("This is a parent")
# class child(parent):
#     def display_child(self):
#         print('Thi is a child class')
# if __name__=='__main__':
#     child=child()
#     child.display_parent_class()

#CONSTUCTOR
#INHERITANCE CODE FOR EX:their is a school can can convet into a college  i.e ug and then convert into pg
# give me a example of inheritance 

class School:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def display(self):
        print(f"Name:{self.name}")
        print(f"Location:{self.location}")
class College(School):
    def __init__(self,name,location,ug_courses):
        super().__init__(name,location)
        self.ug_courses=ug_courses
    def display(self):
        super().display()
        print(f"UG Courses:{self.ug_courses}")
class University(College):
    def __init__(self,name,location,ug_courses,pg_courses):
        super().__init__(name,location,ug_courses)
        self.pg_courses=pg_courses
    def display(self):
        super().display()
        print(f"PG Courses:{self.pg_courses}")
if __name__=='__main__':
    name=input("Enter the name:")
    location=input("Enter the location:")
    ug_courses=input("Enter the ug courses:")
    pg_courses=input("Enter the pg courses:")
    u=University(name,location,ug_courses,pg_courses)
    u.display()
    