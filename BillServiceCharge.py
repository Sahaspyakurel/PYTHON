print("**************************************************************")
print("                 Unicampus Electricity Bill                   ")
print("                     Putalisadak, Nepal                       ")
print("**************************************************************")
name = input("please Enter the name of the customer: ")
address = input("Please enter the Address of the Customer: ")
phone = input("Please enter the Phone number: ")
unit = int(input("Please enter number of unit you consumed: "))
print("**************************************************************")

if unit <= 80:
    amount = unit*4
    service_charge = 0
    d_amount = 0/100*amount
    total_service= amount+service_charge
    after_damount=total_service-d_amount

elif unit > 80 and unit <= 150:
    amount = 80*4+(unit-80)*10
    service_charge= (((unit-80)*10)*5)/100
    d_amount = (((unit-80)*10)*5)/100
    total_service= amount+service_charge
    after_damount=total_service-d_amount

elif unit > 150 and unit <= 250:
    amount = (80*4)+((150-80)*10)+(unit-150)*12
    d_amount = (((150-80)*10)*2)/100+(((unit-150)*12)*5)/100
    service_charge = (((150-80)*10)*5)/100+(((unit-150)*12)*5)/100
    total_service= amount+service_charge
    after_damount=total_service-d_amount

elif unit > 250 and unit <= 350:
    amount = (80*4)+((150-80)*10)+((250-150)*12)+(unit-250)*15
    d_amount = (((150-80)*10)*2)/100+(((250-150)*12)*5)/100+(((unit-250)*15)*10)/100
    service_charge = (((150-80)*10)*5)/100+(((250-150)*12)*5)/100+(((unit-250)*15)*8)/100
    total_service= amount+service_charge
    after_damount=total_service-d_amount

elif unit > 350 and unit <= 500:
    amount = (80*4)+((150-80)*10)+((250-150)*12)+(350-250)*15+(unit-350)*18
    d_amount = (((150-80)*10)*2)/100+(((250-150)*12)*5)/100 +(((350-250)*15)*10)/100+(((unit-350)*18)*12)/100
    service_charge =(((150-80)*10)*5)/100+(((250-150)*12)*5)/100 +(((350-250)*15)*8)/100+(((unit-350)*18)*10)/100
    total_service= amount+service_charge
    after_damount=total_service-d_amount

else:
    amount = (80*4)+((150-80)*10)+((250-150)*12) + (350-250)*15+(500-350)*18+(unit-500)*20
    d_amount = (((150-80)*10)*2)/100+(((250-150)*12)*5)/100+(((350-250)*15)* 10)/100+(((500-350)*18)*12)/100+(((unit-500)*20)*18)/100
    service_charge = (((150-80)*10)*5)/100+(((250-150)*12)*5)/100+(((350-250)*15)* 8)/100+(((500-350)*18)*10)/100+(((unit-500)*20)*12)/100
    total_service= amount+service_charge
    after_damount=total_service-d_amount

print("**************************************************************")
print("                 Unicampus Electricity Bill                   ")
print("                     Putalisadak, Nepal                       ")
print("**************************************************************")
print("Customer Name:", name, "                  Customer Address:", address)
print("Phone:",phone,"                           Unit Consumed:", unit)
print("Bill Amount:", amount,"                            Sercice Charge",service_charge)
print("Total Amount:", total_service, "                   Total discount:",d_amount)
print("After Discount Amount: ", after_damount)
print("Your total bill is:",amount,"+",service_charge,"amount Mr.", name," you got discount \n and discount  price is", d_amount," and After discount amount is Rs.", after_damount, ".")
print("**************************************************************")