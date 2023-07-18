print("**************************************************************")
print("                 Homeside Electricity Bill                   ")
print("                     Putalisadak, Nepal                       ")
print("**************************************************************")
Customer_Name = input("please Enter the name of the customer: ")
address = input("Please enter the Address of the Customer: ")
phone = input("Please enter the Phone number: ")
Unit = int(input("Please enter number of unit you consumed: "))
print("**************************************************************")
                     
            #  0-80 = 4 , 0% ; 80-150 = 10, 2%;  150-250 = 15 , 5% ; 250-350 = 18, 10%; 350-500 = 20, 12%; 500>= 22, 15%
if (Unit<=80):
    discount_money = 0
    Amount_after_discount= Unit * 4
    print("Dear", Customer_Name, "you have consumed " , Unit , "unit " , " and the total amount you have to pay is : " , Amount_after_discount)

elif (Unit>80 and Unit<=150):
    discount_money = 0.02
    Amount= 80*4 + (Unit-80) * 10
    Discount = (Unit-80) * 0.02     
    Amount_after_discount = Amount - Discount
    print("The total discount given is : " , Discount)
    print("Dear", Customer_Name, "you have consumed " , Unit ,"unit " ," and the total amount you have to pay is : " , Amount_after_discount)

elif (Unit>150 and Unit<=250):
    discount_money = 0.05
    Amount= 80*4 + (150-80)*10 + (Unit-150) * 15
    Discount1 = 70 * 0.02 * 10
    Discount2 = Unit * 0.05 *15
    Discount = Discount1 + Discount2
    Amount_after_discount = Amount - Discount
    print("The total discount given is : " , Discount)
    print("Dear", Customer_Name, "you have consumed " , Unit , "unit " , " and the total amount you have to pay is : " , Amount_after_discount)

elif (Unit>250 and Unit <=350):
    discount_money = 0.1
    Amount= 80*4 + 70*10 + (250-150)*15 +(Unit-250) * 18
    Discount1 = 70 * 0.02 * 10
    Discount2 = 100 * 0.05 *15
    Discount3 = Unit * 0.1 *18
    Discount = Discount1 + Discount2 + Discount3
    Amount_after_discount = Amount - Discount
    print("The total discount given is : " , Discount)
    print("Dear", Customer_Name, "you have consumed " , Unit , "unit " , " and the total amount you have to pay is : " , Amount_after_discount)

elif (Unit>350 and Unit <=500):
    discount_money = 0.12
    Amount= 80*4 + 70*10 + (250-150)*15 +(350-250) * 18 + (Unit - 350) * 20
    Discount1 = 70 * 0.02 * 10
    Discount2 = 100 * 0.05 *15
    Discount3 = 100 * 0.1 *18
    Discount4 = Unit * 0.12 *20
    Discount = Discount1 + Discount2 + Discount3 + Discount4
    Amount_after_discount = Amount - Discount
    print("The total discount given is : " , Discount)
    print("Dear", Customer_Name, "you have consumed " , Unit , "unit " , " and the total amount you have to pay is : " , Amount_after_discount)

else:
    discount_money = 0.15
    Amount= 80*4 + 70*10 + (250-150)*15 +(350-250) * 18 + (500 - 350) * 20 + (Unit - 500) * 22
    Discount1 = 70 * 0.02 * 10
    Discount2 = 100 * 0.05 *15
    Discount3 = 100 * 0.1 *18
    Discount4 = Unit * 0.12 *20
    Discount5 = Unit * 0.15 *22
    Discount = Discount1 + Discount2 + Discount3 + Discount4
    Amount_after_discount = Amount - Discount
    print("The total discount given is : " , Discount)
    print("Dear", Customer_Name, "you have consumed " , Unit , "unit " , " and the total amount you have to pay is : " , Amount_after_discount)
