print("Leap year or not\n".center(55))
year = int(input("Enter a year: "))
if year%2 == 0:
    print(year, "is a leap year.")
else:
    print( year, "is not a leap year.")
r = input("Do you want to try again?(y/n): ")
while r == "y":
    year = int(input("Enter a year: "))
    if year%4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    r = input("Do you want to try again?(y/n): ")
while r == "n":
    x = "------------------------------------"
    print(x.center(55))
    print("Thank you for trying out my program".center(55))
    print(x.center(55))
    break
