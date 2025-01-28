# a simple dictionary program
def main():
    d={}
    print("1. An empty dictionary:", d)
    d1={'name':'John', 'age':25}
    print("2. A dictionary with two key-value pairs:", d1)
    d2=dict([('name','John'), ('age',25)])
    print("3. A dictionary with two key-value pairs:", d2)
    d3={ 'name':{ 'first':'John', 'last':'Doe'}, 'age':25}
    print("4. A dictionary with nested dictionary:", d3)
    d4=dict(zip(['name','age'],['John',25]))
    print("5. A dictionary with two key-value pairs:", d4)
    
