from 15_classes import LatLon

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"

class Department:
    # products with a list of tuples with signature (string, int)
    def __init__(self, name, products=[]):
        self.name = name
        self.products = [Product(*p) for p in products]

    def __str__(self):
     return f"No product available in {self.name} department yet"

class Store:
    def __init__(self, name, lat, lon, categories):
        self.name = name
        self.location = LatLon(lat, lon)
        self.categories = categories
        self.departments = [Department(d) for d in departments]

    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.departments}"

store = Store("LambdaStore", 44.13455, -121.123124, ["Clothing", "Cookware", "Books", "Sporting Goods"])
#print(store)

class


while True:
    selection = input("Select the number of a department or type 'exit' to leave: ")
    
    if selection == "exit":
        print("Thanks for shopping with us!")
        break
    #print("The user selected" + store.departments[int(selection))
    #add error handling so that when user inputs dept for non-existant dept, we'll notify
    # them that it doeesnt exist

    try:
        #casting might cause an error
        selection = int(selection)
        if selection >= len(store.departments):
            print("That's not a valid department")
        elif selection >= 0 and selection < len(store.departments):
            print(f"{store.departments[selection]}")
        else:
            print("Department numbers are positive")
    except ValueError:
        #User didnt give us dept as a number
        print("Please enter your choice as a number")

    #when should we break out of this loop?
    # lets et user type "exit" into selection to have them leave