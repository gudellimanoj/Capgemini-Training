
# import csv
# data=[
#     ['Name','Age','City'],
#     ['John',25,'New York'],
#     ['Smith',30,'California'],
#     ['Sam',35,'Texas']
# ]
# with open("sample.csv","w",newline='') as file:
#     writer=csv.writer(file)
#     writer.writerows(data)
# print("CSV file created successfully!")

import csv

class CSVHandler:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def write(self):
        try:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Data successfully written to {self.filename}")
        except Exception as e:
            print(f"Error writing to CSV: {e}")

    def read(self):
        try:
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
        except Exception as e:
            print(f"Error reading CSV: {e}")

# Usage
data = [
    {"name": "manoj", "age": 21},
    {"name": "shanmuk", "age": 19},
    {"name": "sai", "age": 20}

]

csv_handler = CSVHandler(data, "output.csv")
csv_handler.write()
csv_handler.read()
