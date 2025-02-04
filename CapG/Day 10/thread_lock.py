# example code
# import threading
# import time
# def task(lock):
#     with lock:
#         print(f"{threading.current_thread().name} has acquired the lock")
#         time.sleep(2)
#         print(f"{threading.current_thread().name} has released the lock")
# lock=threading.Lock()
# t1=threading.Thread(target=task,args=(lock,))
# t2=threading.Thread(target=task,args=(lock,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# Real time example of threading with lock
import threading
import time
class TicketBoking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()
    def book_ticket(self,name):
        print(f"{name} is booking the ticket")
        with self.lock:
            if self.available_tickets>0:
                print(f"{name} has booked the ticket")
                self.available_tickets-=1
                time.sleep(1)
            else:   
                print(f"Sorry! {name} could not book the ticket")
booking_system=TicketBoking(1)
threads=[]
users=["Alice","Bob"]
for user in users:
    thread=threading.Thread(target=booking_system.book_ticket,args=(user,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("Done!")
