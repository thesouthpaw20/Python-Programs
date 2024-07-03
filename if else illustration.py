def calculate_bill(units):
    if units <= 200:
        bill = units * 0.50
    elif units <= 400:
        bill = 200 * 0.50 + (units - 200) * 0.65
    elif units <= 600:
        bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
    else:
        bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00
    
    if bill > 400:
        bill = bill + (bill * 0.15)
    
    if bill < 100:
        bill = 100
    
    return bill

units = float(input("Enter the number of units consumed: "))
print(f"Total bill: Rs. {calculate_bill(units)}")
