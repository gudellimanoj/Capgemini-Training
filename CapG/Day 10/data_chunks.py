import threading
data_chunks = [
    list(range(1, 11)),
    list(range(11, 21)),
    list(range(21, 31))

]
def process_data(data):
    print(f"Processing {data}\n")
    result = sum(data)
    print(f"Result: {result}\n")
threads = []
for data in data_chunks:
    thread = threading.Thread(target=process_data, args=(data,))
    thread.start()
    thread.join()
print("Done!")
