#Austin Hastings
#CMP 131 86520
#Week 6
#Lab 1
#Problem 1
#1 OCT 2026
print("-------------")
print("Software")
print("-------------")
units= int(input("Enter the number of units purchased: "))
price= float(99.00)
total= units * price
print()
if units >= 1:
    if units >=10 and units <= 19:
        discount= float(units * (price *.2))
        finalprice= float(total - discount)
        discount_percentage= float(20)
        print("Final price is: " f"${finalprice:.2f}")
    elif units >= 20 and units <= 49:
        discount= float(units * (price *.3))
        finalprice= float(total - discount)
        discount_percentage= float(30)
        print("Final price is: " f"${finalprice:.2f}")
    elif units >= 50 and units <= 99:
        discount= float(units * (price *.4))
        finalprice= float(total - discount)
        discount_percentage= float(40)
        print("Final price is: " f"${finalprice:.2f}")
    elif units >= 100:
        discount= float(units * (price *.5))
        finalprice= float(total - discount)
        discount_percentage= float(50)
        print("Final price is: " f"${finalprice:.2f}")
    else:
        print("Final price is: ", f"${total:.2f}" )
        discount= ("N/A")
        discount_percentage= ("N/A")
else: 
    print("Number not Valid")
print("Units purchased: ", units)
print("Price per unit: ", f"${price:.2f}")
print("Price before discount: ", f"${total:.2f}")
print("Discount percentage: ", f"%{discount_percentage:.2f}" )
print("Discount amount: ", f"${discount:.2f}" )