#Austin Hastings
#CMP 131 86520
#Week 6
#Lab 1
#Problem 1
#1 OCT 2026
print("----------------")
print("Phone Bill")
print("----------------")
package= (input("Enter phone plan A, B, or C: ")).upper()
minutes= (int(input("Enter number of minutes used: ")))

monthly_charge = float(0.0)
additional_minutes = int(0)
additional_charge = float(0.0)

if package == "A":
    monthly_charge = float(39.99)
    
    if minutes > 450:
            additional_minutes = minutes - 450
            additional_charge =  additional_minutes * 0.45
            total = monthly_charge + additional_charge
            print("Monthly Bill")
            print("Selected package: ", package)
            print("Minutes used: ", minutes)
            print(f"Monthly charge: ${monthly_charge:.2f}")
            print("Additional minutes used: ", additional_minutes)
            print(f"Additional minutes charge:  ${additional_charge:.2f}")
            print(f"Total amount due: ${total:.2f}")
    else:
        total = monthly_charge
        print("Monthly Bill")
        print(f"Total amount due: ${total:.2f}")
        print("Selected package: ", package)
        print("Minutes used: ", minutes)
        print(f"Monthly charge: ${monthly_charge:.2f}")

elif package == "B":
    monthly_charge = float(59.99)

    if minutes > 900:
            additional_minutes = minutes - 900
            additional_charge = additional_minutes * 0.40
            total = monthly_charge + additional_charge
            print("Monthly Bill")
            print(f"Total amount due: ${total:.2f}")
            print("Selected package: ", package)
            print("Minutes used: ", minutes)
            print(f"Monthly charge: ${monthly_charge:.2f}")
            print("Additional minutes used: ", additional_minutes)
            print(f"Additional minutes charge:  ${additional_charge:.2f}")
    else:
        total = monthly_charge
        print("Monthly Bill")
        print(f"Total amount due: ${total:.2f}")
        print("Selected package: ", package)
        print("Minutes used: ", minutes)
        print(f"Monthly charge: ${monthly_charge:.2f}")

elif package == "C":
    monthly_charge = float(69.99)
    total = monthly_charge
    print("Monthly Bill")
    print(f"Total amount due: ${total:.2f}")
    print("Selected package: ", package)
    print("Minutes used: ", minutes)
    print(f"Monthly charge: ${monthly_charge:.2f}")

else:
    print("Invalid package. Please enter A, B, or C.")