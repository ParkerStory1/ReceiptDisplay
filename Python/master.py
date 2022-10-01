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
totallySatisfiedTip = userTotalCost * .2
satisfiedTip = userTotalCost * .15
dissatisfied = userTotalCost * .1

## Assign member discount 
memberDiscount = userTotalCost * .15

## Statements determining if the membership discount should be added. Followed by the tip and total being solved and formatted.
if memberStatus.lower() == "y":
    print("{0:<10s} {1:>20s}".format("DISCOUNT:", "15%\n"))
    if rating == "1":
        print("{0:<10s} {1:>20.2f}".format("TIP:", totallySatisfiedTip))                                  
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + totallySatisfiedTip -(userTotalCost + totallySatisfiedTip) * .15)))
    if rating == "2":
        print("{0:<10s} {1:>20.2f}".format("TIP:", satisfiedTip))                                  
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + satisfiedTip -(userTotalCost + satisfiedTip) * .15)))
    if rating == "3":
        print("{0:<10s} {1:>20.2f}".format("TIP:", dissatisfied))                                  
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + dissatisfied -(userTotalCost + dissatisfied) * .15)))
elif memberStatus.lower() == "n":
    if rating == "1":
        print("{0:<10s} {1:>20.2f}".format("TIP:", totallySatisfiedTip))
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + totallySatisfiedTip)))
    if rating == "2":
        print("{0:<10s} {1:>20.2f}".format("TIP:", satisfiedTip))                                  
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + satisfiedTip)))
    if rating == "3":
        print("{0:<10s} {1:>20.2f}".format("TIP:", dissatisfied))                                  
        print("{0:<10s} {1:>20.2f}".format("TOTAL:", (userTotalCost + dissatisfied)))

print()

print(border)
