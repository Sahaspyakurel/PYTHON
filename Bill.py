initial_display="Pyakurel Home Electricity Bill"
print(initial_display)
Unit=int(input("Enter consumed unit: "))                      
            #  0-80 = 4 , 80-150 = 10, 150-250 = 15 , 250 + = 20
if (Unit<=80):
    Amount= Unit * 4
    print(Amount)
elif (Unit>80 and Unit<=150):
    Amount= 80*4 + (Unit-80) * 10
    print(Amount)
elif (Unit>150 and Unit<=250):
    Amount= 80*4 + (150-80)*10 + (Unit-150) * 15
    print(Amount)
else:
    Amount= 80*4 + 70*10 + (250-150)*15 +(Unit-250) * 20
    print(Amount)