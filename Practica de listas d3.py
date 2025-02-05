print("\n Welcome to Dayashop market")
print("\n What option to choice")

name = []

while True:
    print("1. Add a item")
    print("2. View cart")
    print("3. Remove a item")
    print("4. calculate total")
    print("5. Exit")
        
    bum = input("\n What do you choice") 
    
    if bum == "1":
        name1 = input("What is item name")
        name1.append(name)
        print("The item is aggregate")
    
    elif bum == 2:
        if len(name) == 0:
        print("the car is empity")
        else:
            print("the item are")
            for w in range(len(name)):
                print(f")