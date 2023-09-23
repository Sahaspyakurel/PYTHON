file_path = 'C:/Users/user/Documents/Applied Python/Tax.txt'

def intitial_display():
    date = 1
    heading = f'''       Sunway TAX Calculator       
        Maitidevi, Kathmandu        
            {date}'''
    return heading 

def input_info():
    customers_info=[]
    num = int(input('Enter the number of customer:'))
    for i in range(num):
        customer_info = []
        name = input('Enter the name: ')
        address = input('Enter the Address: ')
        married_status = input('Married Status(M/U): ')
        monthly_income = int(input('Enter the monthly income: '))
        customer_info.append(name)
        customer_info.append(address)
        customer_info.append(married_status)
        customer_info.append(monthly_income)
        customers_info.append(customer_info)
    print(customers_info)
    return num,customers_info
    
def tax_Unmarried(annual_income):
    if annual_income <= 500000:
        tax_per= 1
        income_after_tax = (annual_income * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 500000 and annual_income <= 700000:
        tax_per= 10
        income_after_tax = (500000 * 1)/100+((annual_income-500000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 700000 and annual_income <= 1000000:
        tax_per= 20
        income_after_tax = (500000 * 1)/100+((700000-500000) * 10)/100+((annual_income-700000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 1000000 and annual_income <= 2000000:
        tax_per= 30
        income_after_tax = (500000 * 1)/100+((700000-500000) * 10)/100+((1000000-700000) * 20)/100+((annual_income-1000000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income> 2000000 and annual_income <= 5000000:
        tax_per= 36
        income_after_tax = (500000 * 1)/100+((700000-500000) * 10)/100+((1000000-700000) * 20)/100+((2000000-1000000) * 1)/100+((annual_income-5000000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    else:
        tax_per= 39
        income_after_tax = (500000 * 1)/100+((700000-500000) * 10)/100+((1000000-700000) * 20)/100+((2000000-1000000) * 1)/100+((5000000-2000000) * 36)/100+((annual_income-5000000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    return annual_income,income_after_tax,annual_income_after_tax    


def tax_married(annual_income):   
    if annual_income <= 600000:
        tax_per= 1
        income_after_tax = (annual_income * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 600000 and annual_income <= 800000:
        tax_per= 10
        income_after_tax = (600000 * 1)/100+((annual_income-600000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 800000 and annual_income <= 1100000:
        tax_per= 20
        income_after_tax = (600000 * 1)/100+((800000-600000) * 10)/100+((annual_income-800000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income > 1100000 and annual_income <= 2000000:
        tax_per= 30
        income_after_tax = (600000 * 1)/100+((800000-600000) * 10)/100+((1100000-800000) * 20)/100+((annual_income-1100000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    elif annual_income> 2000000 and annual_income <= 5000000:
        tax_per= 36
        income_after_tax = (600000 * 1)/100+((800000-600000) * 10)/100+((1100000-800000) * 20)/100+((2000000-1100000) * 1)/100+((annual_income-5000000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax
    else:
        tax_per= 39
        income_after_tax = (600000 * 1)/100+((800000-600000) * 10)/100+((1100000-800000) * 20)/100+((2000000-1100000) * 1)/100+((5000000-2000000) * 36)/100+((annual_income-5000000) * tax_per)/100
        annual_income_after_tax=annual_income-income_after_tax  
    return annual_income,income_after_tax,annual_income_after_tax    



def tax_calculation(status,income):
    yearly_income = income *12
    if status == 'U' or status == 'u':
        annual_income,income_after_tax,annual_income_after_tax=tax_Unmarried(yearly_income)
    elif status == 'M' or status == 'm':
        annual_income,income_after_tax,annual_income_after_tax= tax_married(yearly_income)
    return annual_income,income_after_tax,annual_income_after_tax

def value_print(cust_name, cust_address,cust_status,cust_annual_income,Income_after_tax,annual_income_a_tax):
    cust_info =f'''Name: {cust_name}\t\t Address: {cust_address}
Married Status:{cust_status}
Total Annual Income: {cust_annual_income}
Tax Income:{Income_after_tax}
Income after tax: {annual_income_a_tax}'''
    return cust_info

   
def final_print():
    num,customers_Info = input_info()
    initial= intitial_display()
    for i in range(num): 
        annual_income,income_after_tax,annual_income_after_tax = tax_calculation(customers_Info[i][2],customers_Info[i][3])
        print(initial)
        value = value_print(customers_Info[i][0],customers_Info[i][1],customers_Info[i][2],annual_income,income_after_tax,annual_income_after_tax)
        print(value)
        with open(file_path,'a') as f:
            f.write(initial+"\n")
            f.write(value)

final_print() 