# example of threading 

import threading
import time
def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Number: {i}")
def print_letters():
    for letter in "ABCDE":
        time.sleep(2)
        print(f"Letter: {letter}")
# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
# Start threads
t1.start()
t2.start()
# Wait for threads to finish
t1.join()
t2.join()
print("Done!")

