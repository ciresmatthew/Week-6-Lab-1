# Student Name: Matthew Cires
# Course: CMP 131
# Week: Week 6
# Lab: Lab 01
# Assignment Title: Software Quantity Discount
# Date: 10/06/26

units = int(input("Enter the number of software units purchased: "))


if units <= 0:
    print("Error: Number of units must be greater than zero.")

else:
    price_per_unit = 99.00

    
    original_cost = units * price_per_unit

    if units < 10:
        discount_rate = 0.00
    elif units < 20:
        discount_rate = 0.20
    elif units < 50:
        discount_rate = 0.30
    elif units < 100:
        discount_rate = 0.40
    else:
        discount_rate = 0.50

    discount_amount = original_cost * discount_rate
    final_cost = original_cost - discount_amount

    print("\n--- Software Purchase Report ---")
    print(f"Units Purchased: {units}")
    print(f"Price Per Unit: ${price_per_unit:.2f}")
    print(f"Original Cost: ${original_cost:,.2f}")
    print(f"Discount: {discount_rate * 100:.0f}%")
    print(f"Discount Amount: ${discount_amount:,.2f}")
    print(f"Final Cost: ${final_cost:,.2f}")
