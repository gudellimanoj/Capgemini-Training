# def display(data):#display function
#     print(f"The area  {data}")
# def get_input():#get_input function
#     received_length=int(input('Enter the length '))
#     received_width=int(input('Enter the width'))
#     return (received_length,received_width)
# def area(length,width):#area function
#     data=int(length)*int(width)
#     return data
# def main():#main function
#     (length,width)=get_input()
#     data=area(length,width)
#     display(data)
# main()#calling main function

# AVERAGE OF 4 NUMBERS
# def display(average): #display function
#     print(f"The average of 4 numbers is {average}")
# def get_input(): #get_input function
#     number1=int(input('Enter the number1 '))
#     number2=int(input('Enter the number2'))  
#     number3=int(input('Enter the number3'))
#     number4=int(input('Enter the number4'))
#     return (number1,number2,number3,number4)
# def add(number1,number2,number3,number4):#add function
#     data=(number1+number2+number3+number4)
#     return data
# def average(data): #average function
#     average=data/4
#     return average
    
# def main(): #main function
#     (number1,number2,number3,number4)=get_input()

#     data=add(number1,number2,number3,number4)
#     Average=average(data)    
#     display(Average)
# main()#calling main function

# biggest of 3 numbers
# def display(biggest): #display function
#     print(f"The biggest of 3 numbers is {biggest}")
# def get_input(): #get_input function
#     a=int(input('Enter the number1 '))
#     b=int(input('Enter the number2'))
#     c=int(input('Enter the number3'))
#     if a>b and a>c:
#         return {'a':a}
#     elif b>a and b>c:
#         return {'b':b}
#     else:
#         return {'c':c}
# def main(): #main function
#     biggest=get_input()
#     display(biggest)
    
# main() #calling main function
# print('Hello world')

#multiplication of 2 numbers
# import dis
# def display(multiply): #display function
#     print(f"The multiplication of 2 numbers is {multiply}")
# def get_input(): #get_input function
#     number1=int(input('Enter the number1 '))
#     number2=int(input('Enter the number2'))  
#     return {number1,number2}
# def for_loop(n):#for_loop function
#     for i in range(n):
#         print(i)
# def multiply(number1,number2):#multiply function
#     return(number1*number2) 
# def main(): #main function
#     (number1,number2)=get_input()
#     data=multiply(number1,number2)
#     display(data)
#     for_loop(data)
# dis.dis(main)
# main()#calling main function

#prime number or not with less time complexity
# import math
# def prime_or_not(n): #prime_or_not function
#     if n<=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
        
#     return True
# def count_prime(n): #count_prime function_all the primes from 2 to n
#     count=0
#     for i in range(2,n+1):
#         if prime_or_not(i):
#             print('prime:',i)
#             count+=1
            
#     return count
# def get_input(): #get_input function
#     n=int(input('Enter the number'))
#     return n
# def main(): #main function
#     n=int(input('Enter the number'))
#     print(count_prime(n))
#     print(prime_or_not(n))
# main() #calling main function

#prime number or not with using while loop
import math
def prime_or_not(n): #prime_or_not function
    if n<=1:
        return False
    i=2
    while i<=int(math.sqrt(n)):
        if n%i==0:
            return False
        i+=1
    return True
def count_prime(n): #count_prime function_all the primes from 2 to n
    count=0
    i=2
    while i<=n:
        if prime_or_not(i):
            print('prime:',i)
            count+=1
        i+=1
    return count4
def get_input(): #get_input function
    n=int(input('Enter the number'))
    return n
def main(): #main function
    n=int(input('Enter the number'))
    print(count_prime(n))
    print(prime_or_not(n))
main() #calling main function



