def initial_Display():
    initial_display = "Sunway Bhatbhateni System, Maitidevi, Kathmandu"
    print (initial_display)

def inputInformation():
    Totalprice = 0
    cust_name= input("Enter customer name")
    cust_id = int(input("Enter customer id"))
    cust_add = input("Enter customer address")
    num_item = int(input("Enter item purchased"))
    item= []
    quantity= []
    for i in range (num_item):
        itemqty= int(input("Enter quantity of 1st item[{i+1}]:"))
        amtqty= int(input("Enter amount of item [{i+1}]:"))
        Totalprice = Totalprice +itemqty * amtqty
        item.append(itemqty)
        quantity.append(amtqty)
    return cust_name, cust_id, cust_add, num_item, item, Totalprice

    