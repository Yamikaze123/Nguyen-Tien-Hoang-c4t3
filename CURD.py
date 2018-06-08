items = ["T-Shirt","Sweater"]

action = input("Welcome to our shop, what do you want (C, U, R, D)").lower()
if action == "r":
     print("Our item:",*items)
elif action == "c":
    items.append(input("Enter new item:"))
    print("Our item:",*items)
elif action == "u":
    position = int(input("Update position"))
    if position >=0 and position<= len(items):
        items.insert(position-1, input("New item:"))
        items.pop(position)
        print("Our items:",*items)
    else:
        print("Ban nhap sai roi")
elif action == "d":
    delposition = int(input("Delete position?"))
    if delposition >= 0 and delposition <= len(items):
        items.pop(delposition-1)
        print("Our items:",*items)
    else:
            print("Ban nhap sai roi")
else:
    print("Ban nhap sai roi")