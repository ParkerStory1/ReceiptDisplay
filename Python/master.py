# Name: Parker Story                        Date Assigned: 09/28/2022
#
# Course: 2000-44306                        Due Date: 10/04/2022
#
# File name: master.py
#
# Program Description:  In this program, the user will be asked several questions including the
#                       total cost of their purchase, their membership status, and overall level of 
#                       satisfaction with the service. After the information is received, the program 
#                       will dislpay a unique 'receipt' depending on the answers given by the user to 
#                       the previous questions.

border = "=" * 32

## Creating top section with border
print(border)
print("CHECKOUT".center(31))
print(border)

## Receive total cost from user
userTotalCost = float(input("\n Enter the total cost: "))

print()

## Creating membership section
print(border)
print("MEMBERSHIP".center(31))
print(border, "\n")

## Ask the user about membership status and store in 'memberStatus'
memberStatus = input(" Are you a member? (y/n): ")

print("\n")

## Statement displaying discount message if user inputs y or Y
if memberStatus.lower() == "y":
    print("  * * * * * * * * * * * * * * ")
    print("  *                         *")
    print("  * You get a 15% discount! *  ")
    print("  *                         *")
    print("  * * * * * * * * * * * * * *\n\n")
         
## Creating rating section
print(border)
print("RATING".center(31))
print(border)

print()

## Displaying 'Rate Your Experience' section
print("   +------------------------+")
print("   | Rate Your Experiennce! |")
print("   |  1 = Totally Satisfied |")
print("   |  2 = Satisfied         |")
print("   |  3 = Dissatisfied      |")
print("   +------------------------+")
   
print()

## Asking user to enter their rating and stores in 'rating'
rating = input("Enter rating (1 - 3): ")

## Creating payment section
print()
print(border)
print("PAYMENT".center(31))
print(border)

print()

## Assign tip values to variables
if rating == "1":
    tip = userTotalCost * .2
elif rating == "2":
    tip = userTotalCost * .15
else:
    tip = userTotalCost * .1

## Assign member discount 
memberDiscount = userTotalCost * .15

## Statements determining if the membership discount should be added. Followed by the tip and total being solved and formatted.
if memberStatus.lower() == "y":
    print("{0:<10s} {1:>20s}".format("DISCOUNT:", "15%\n"))
    total = userTotalCost + tip  - (userTotalCost + tip) * .15
else:
    total = userTotalCost + tip

print("{0:<10s} {1:>20.2f}".format("TIP:", tip))
print("{0:<10s} {1:>20.2f}".format("TOTAL:", total))

print()

print(border)
