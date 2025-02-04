# file=open("sample.txt","w") 
# file.write("Hello World")
# file.close()

with open("sample.txt","r") as file:
    data=file.read()
    print(data) 
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())