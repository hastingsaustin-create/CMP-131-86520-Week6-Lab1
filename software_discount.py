#Austin Hastings
#CMP 131 86520
#Week 6
#Lab 1
#Problem 1
#1 OCT 2026
print("-------------")
print("Software")
print("-------------")
units= (int(input("Enter the number of units purchased: ")))
price= float(99.00)
discount= 0
discount_percentage= 0
total= units * price
print()
if units >= 1:
    if units >=10 and units <= 19:
        discount= float(units * (price *.2))
        finalprice= float(total - discount)
        discount_percentage= int(20)
        print(f"Final price is: ${finalprice:.2f}")
        print("Units purchased: ", units)
        print(f"Price per unit: , ${price:.2f}")
        print(f"Price before discount: , ${total:.2f}")
        print(f"Discount percentage: , %{discount_percentage:.2f}" )
        print(f"Discount amount: , ${discount:.2f}" )

    elif units >= 20 and units <= 49:
        discount= float(units * (price *.3))
        finalprice= float(total - discount)
        discount_percentage= int(30)
        print(f"Final price is: ${finalprice:.2f}")
        print("Units purchased: ", units)
        print(f"Price per unit: , ${price:.2f}")
        print(f"Price before discount: , ${total:.2f}")
        print(f"Discount percentage: , %{discount_percentage:.2f}" )
        print(f"Discount amount: , ${discount:.2f}" )

    elif units >= 50 and units <= 99:
        discount= float(units * (price *.4))
        finalprice= float(total - discount)
        discount_percentage= int(40)
        print(f"Final price is: ${finalprice:.2f}")
        print("Units purchased: ", units)
        print(f"Price per unit: , ${price:.2f}")
        print(f"Price before discount: , ${total:.2f}")
        print(f"Discount percentage: , %{discount_percentage:.2f}" )
        print(f"Discount amount: , ${discount:.2f}" )

    elif units >= 100:
        discount= float(units * (price *.5))
        finalprice= float(total - discount)
        discount_percentage= int(50)
        print(f"Final price is: ${finalprice:.2f}")
        print("Units purchased: ", units)
        print(f"Price per unit: , ${price:.2f}")
        print(f"Price before discount: , ${total:.2f}")
        print(f"Discount percentage: , %{discount_percentage:.2f}" )
        print(f"Discount amount: , ${discount:.2f}" )

    else:
        print("Total price is: ", total)
        print("Units purchased: ", units)
        print(f"Price per unit: , ${price:.2f}")
        print(f"Price before discount: , ${total:.2f}")
        print(f"Discount percentage: , %{discount_percentage:.2f}" )
        print(f"Discount amount: , ${discount:.2f}" )

else: 
    print("Number not Valid")