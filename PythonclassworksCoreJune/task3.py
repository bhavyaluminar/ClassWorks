#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code=int(input("Enter the code -1 -battery/2-Key/3-Electrical"))
amount=int(input("Enter the amount"))
if code==1:
    if(amount>1000):
        print("Bill Amount",amount*(90/100))
    else:
        print("Bill Amount", amount )

elif code==2:
    if(amount>100):
        print("Bill Amount", amount * (95 / 100))
    else:
        print("Bill Amount", amount )
elif code==3:
    if(amount>500):
        print("Bill Amount", amount * (90 / 100))
    else:
        print("Bill Amount", amount)
else:
    print("Bill Amount", "Invalid")








