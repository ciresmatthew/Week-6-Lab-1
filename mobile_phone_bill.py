# Student Name: Matthew Cires
# Course: CMP 131
# Week: Week 6
# Lab: Lab 01
# Assignment Title: Mobile Phone Service Bill
# Date: 10/06/26

print("--- Mobile Phone Packages ---")
print("Package A: $39.99/month, 450 minutes, $0.45 per additional minute")
print("Package B: $59.99/month, 900 minutes, $0.40 per additional minute")
print("Package C: $69.99/month, Unlimited minutes")

package = input("\nSelect a package (A, B, or C): ").upper()
minutes_used = int(input("Enter the number of minutes used: "))


if package != "A" and package != "B" and package != "C":
    print("Error: Invalid package selected.")

elif minutes_used < 0:
    print("Error: Minutes used cannot be negative.")

else:

    if package == "A":
        monthly_charge = 39.99

        if minutes_used > 450:
            additional_minutes = minutes_used - 450
            additional_charge = additional_minutes * 0.45
        else:
            additional_minutes = 0
            additional_charge = 0.00

    
    elif package == "B":
        monthly_charge = 59.99

        if minutes_used > 900:
            additional_minutes = minutes_used - 900
            additional_charge = additional_minutes * 0.40
        else:
            additional_minutes = 0
            additional_charge = 0.00

    
    else:
        monthly_charge = 69.99
        additional_minutes = 0
        additional_charge = 0.00

    
    total_bill = monthly_charge + additional_charge

    
    print("\n--- Monthly Phone Bill ---")
    print(f"Selected Package: {package}")
    print(f"Minutes Used: {minutes_used}")
    print(f"Monthly Package Charge: ${monthly_charge:.2f}")

    if package == "C":
        print("Included Minutes: Unlimited")
    else:
        print(f"Additional Minutes: {additional_minutes}")

    print(f"Additional-Minute Charge: ${additional_charge:.2f}")
    print(f"Total Amount Due: ${total_bill:.2f}")
