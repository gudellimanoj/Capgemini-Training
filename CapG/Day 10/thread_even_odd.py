

import threading
import time
def even_numbers():
    for i in range(n):
        if i%2==0:
            time.sleep(2)
            print(f"Even Number: {i}")
def odd_numbers():
    for i in range(n):
        if i%2!=0:
            time.sleep(2)
            print(f"Odd Number: {i}")
n=int(input("Enter the range: "))
t1=threading.Thread(target=even_numbers)
t2=threading.Thread(target=odd_numbers)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")  


