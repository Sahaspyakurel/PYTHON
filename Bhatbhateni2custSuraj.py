file_path='C:/Users/user/Documents/Applied Python/SunwayBilltext.txt'
def initialDisplay():
    display = ''' 
    *********************************--*********************************
    
                             Sunway Bhatbhateni system
                                maitedevi Kathmandu
                                
    *********************************--*********************************
    '''
    
    print(display)
    return display
    
def userinput():
    totalAmount =0
    customerName = input("Enter the customer Name : ")
    customerId = input("Enter the customer Id : ")
    address = input("Enter the customer Address : ") 
    items =  int(input('Enter  the number of items : '))
    priceList =[]
    quantityList =[]
    amountList =[]
    for i in range(items):
        price =  int(input(f"Enter the price of {i+1} items : Rs."))
        quantity = int (input(f"Enter  the quantity of {i+1} : "))
        amount = price * quantity
        priceList.append(price)
        quantityList.append(quantity)
        amountList.append(amount)
        totalAmount = int(totalAmount)+int(amount)
        
    return (customerId, customerName, address ,items,priceList, quantityList, amountList, price, quantity, amount,totalAmount)
def calculation(): 
    if totalAmount <= 500:
        discountPercentage = 1
        discoutedValue = totalAmount*0.01
        finalAmount = totalAmount - discoutedValue
    elif totalAmount > 500 and totalAmount <= 1000:
        discountPercentage = 3
        discoutedValue = 500*0.01 + (totalAmount-500)*0.03
        finalAmount = totalAmount - discoutedValue
    elif totalAmount > 1000 and totalAmount <= 1500:
        discountPercentage = 5
        discoutedValue = 500*0.01 + (1000-500)*0.03+(totalAmount-1000)*0.05
        finalAmount = totalAmount - discoutedValue
    elif totalAmount > 1500 and totalAmount <= 2000:
        discountPercentage = 8
        discoutedValue = 500*0.01 + \
            (1000-500)*0.03+(1500-1000)*0.05+(totalAmount-1500)*0.08
        finalAmount = totalAmount - discoutedValue
    else:
        discountPercentage = 10
        discoutedValue = 500*0.01 + \
            (1000-500)*0.03+(1500-1000)*0.05 + \
            (2000-1500)*0.08+(totalAmount-2000)*0.1
        finalAmount = totalAmount - discoutedValue
    return (discountPercentage, discoutedValue,finalAmount)
    
def outputData():
    a=''
    
    for i in range(items):
        a += f'''
              
              
              {str(i+1)} product  = Rs.{priceList[i]} * {quantityList[i]} items \n
                          Amount : Rs.{amountList[i]} \n
              '''

       
    
    display = f'''
    
    {initialDisplay()}
    ------------------------------------------------------------------------------------------------------------------------
    
    Customer Name : {customerName}
    
    Customer Id : {customerId}
    
    Customer Address : {address}
    
    Total Amount : { str(totalAmount)}
    {a}
    
    
 
     
     Mr/Mrs. {customerName}, you have purchased {items} items whose total price is {totalAmount} and discount is Rs.{discoutedValue} with discount rate {discountPercentage}%.So, You can to pay Rs.{finalAmount}

    ------------------------------------------------------------------------------------------------------------------------
    
    
    '''
    # initialDisplay()
    # print('------------------------------------------------------------------------------------------------------------------------')
    # print()
    # print(f"Customer Name : {customerName}")
    # print(f"Customer Id : {customerId}")
    # print(f"Customer Address : {address}")
    # print('Total Amount '+ str(totalAmount))
    # for i in range(items):
    #     print()
    #     print(f'{str(i+1)} product  = Rs.{priceList[i]} * {quantityList[i]} items' )
    #     print(f'            Amount : Rs.{amountList[i]}')
    #     print()
    # print(f'''Mr/Mrs. {customerName}, you have purchased {items} items whose total price is {totalAmount} and discount is Rs.{discoutedValue} with discount rate {discountPercentage}%.So, You can to pay Rs.{finalAmount}''')  
    # print()
    
    # print('------------------------------------------------------------------------------------------------------------------------')
    
    print(display)
    return  display
numberofUser=int(input("Enter the number of customer : "))

for j in range(numberofUser):
    customerId, customerName, address , items,priceList, quantityList, amountList ,price, quantity, amount ,totalAmount= userinput()
    discountPercentage, discoutedValue,finalAmount =  calculation() 
    outputData()
    with open (file_path,'w') as file:
     file.write(str(outputData()))
