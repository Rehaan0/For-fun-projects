print("Calculator \n".center(55))
print("Do you want to add, subtract, multiply or divide? \n")
operation = input("Add, Sub, Mul or Div: ")
if operation == "Add":
    print("Addition".center(55))
    print("\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbers "
          "as 0.")
    num1 = float(input("1st no: "))
    num2 = float(input("2nd no: "))
    num3 = float(input("3rd no: "))
    num4 = float(input("4th no: "))
    num5 = float(input("5th no: "))
    print(num1, "+", num2, "+", num3, "+", num4, "+", num5, "=", num1+num2+num3+num4+num5)
elif operation == "Sub":
    print("Subtraction".center(55))
    print("\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbers "
          "as 0.")
    num1 = float(input("1st no: "))
    num2 = float(input("2nd no: "))
    num3 = float(input("3rd no: "))
    num4 = float(input("4th no: "))
    num5 = float(input("5th no: "))
    print(num1, "-", num2, "-", num3, "-", num4, "-", num5, "=", num1-num2-num3-num4-num5)
elif operation == "Mul":
    print("Multiplication".center(55))
    print("\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbers "
          "as 1.")
    num1 = float(input("1st no: "))
    num2 = float(input("2nd no: "))
    num3 = float(input("3rd no: "))
    num4 = float(input("4th no: "))
    num5 = float(input("5th no: "))
    print(num1, "x", num2, "x", num3, "x", num4, "x", num5, "=", num1*num2*num3*num4*num5)
elif operation == "Div":
    print("Division".center(55))
    print("\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbers "
          "as 1.")
    num1 = float(input("1st no: "))
    num2 = float(input("2nd no: "))
    num3 = float(input("3rd no: "))
    num4 = float(input("4th no: "))
    num5 = float(input("5th no: "))
    print(num1, "/", num2, "/", num3, "/", num4, "/", num5, "=", num1/num2/num3/num4/num5)
r = input("Do you want to try again?(y/n): ")
while r == "y":
    print("\nDo you want to add, subtract, multiply or divide?\n")
    operation = input("Add, Sub, Mul or Div: ")
    if operation == "Add":
        print("Addition".center(55))
        print(
            "\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other number"
            "s as 0.")
        num1 = float(input("1st no: "))
        num2 = float(input("2nd no: "))
        num3 = float(input("3rd no: "))
        num4 = float(input("4th no: "))
        num5 = float(input("5th no: "))
        print(num1, "+", num2, "+", num3, "+", num4, "+", num5, "=", num1 + num2 + num3 + num4 + num5, "\n")
        r = input("Do you want to try again?(y/n): ")
    elif operation == "Sub":
        print("Subtraction".center(55))
        print(
            "\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbe"
            "rs as 0.")
        num1 = float(input("1st no: "))
        num2 = float(input("2nd no: "))
        num3 = float(input("3rd no: "))
        num4 = float(input("4th no: "))
        num5 = float(input("5th no: "))
        print(num1, "-", num2, "-", num3, "-", num4, "-", num5, "=", num1 - num2 - num3 - num4 - num5)
        r = input("Do you want to try again?(y/n): ")
    elif operation == "Mul":
        print("Multiplication".center(55))
        print(
            "\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbe"
            "rs as 1.")
        num1 = float(input("1st no: "))
        num2 = float(input("2nd no: "))
        num3 = float(input("3rd no: "))
        num4 = float(input("4th no: "))
        num5 = float(input("5th no: "))
        print(num1, "x", num2, "x", num3, "x", num4, "x", num5, "=", num1 * num2 * num3 * num4 * num5)
        r = input("Do you want to try again?(y/n): ")
    elif operation == "Div":
        print("Division".center(55))
        print(
            "\n You can enter up to 5 numbers but if you only wanna do a particular amount, just leave the other numbe"
            "rs as 1.")
        num1 = float(input("1st no: "))
        num2 = float(input("2nd no: "))
        num3 = float(input("3rd no: "))
        num4 = float(input("4th no: "))
        num5 = float(input("5th no: "))
        print(num1, "/", num2, "/", num3, "/", num4, "/", num5, "=", num1 / num2 / num3 / num4 / num5)
        r = input("Do you want to try again?(y/n): ")
while r == "n":
    print("------------------------------------".center(55))
    print("Thank you for trying out my program!".center(55))
    print("------------------------------------".center(55))
    break
