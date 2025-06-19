menu={"pizza":70 ,"burger":50, "cold coffee":100,"momo":50 }
print("Welocome to Abhinav's Cafe!!\n")
print("Menu is here!!\n\nPizza : Rs70\nBurger : Rs50\nCold Coffee : Rs100\nMomo : 50")

order_total=0

item_1=input("\nWhat would you like to have : ")
if item_1 in menu:
    order_total+=menu[item_1]
    print("\nYour item has been added to you order")
else:
    print("\nItem is not available")

another_item=input("\nWould you like to add another item??(yes/no): ")
if another_item=="yes":
    item_2=input("\nEnter your second item : ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print("\nYour item has been added to you order")
    else:
        print("Item is not available ")
print("\nTotal amount you have to pay is : Rs",order_total)

