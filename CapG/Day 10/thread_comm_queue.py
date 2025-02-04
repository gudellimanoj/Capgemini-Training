# import threading
# import time
# import queue

# def producer(queue):
#     for i in range(5):
#         queue.put(i)
#         print(f"Produced: {i}")
#         time.sleep(1)
# def consumer(queue):
#     while True:
#         item = queue.get()
#         if item is None:
#             break
#         print(f"Consumed: {item}")
#         time.sleep(1)

# q = queue.Queue()
# producer = threading.Thread(target=producer, args=(q,))
# consumer = threading.Thread(target=consumer, args=(q,))
# producer.start()
# consumer.start()
# producer.join()
# consumer.join()
# print("Done!")



