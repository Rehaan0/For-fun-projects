print("LIST OF ODD OR EVEN NUMBERS".center(55))
o1o2 = input("\n Odd or even numbers list: ")
num = int(input("\n till what number: "))
if o1o2 == "Odd" or o1o2 == "odd":
  for i in range(1, num, 2):
    print(i)
if o1o2 == "Even" or o1o2 == "even":
  num += 1
  for i in range(0, num, 2):
    print(i)
print(" ")
r = input("Do you want to retry(y/n): ")
print("")
while r == "y":
  print("ODD OR EVEN".center(55))
  o1o2 = input("\n Odd or even numbers list: ")
  num = int(input("\n till what number: "))
  if o1o2 == "Odd" or o1o2 == "odd":
    for i in range(1, num, 2):
      print(i)
  if o1o2 == "Even" or o1o2 == "even":
    num += 1
    for i in range(0, num, 2):
      print(i)
  r = input("Do you want to retry(y/n): ")
  print(" ")
while r == "n":
  print("------------------------------------".center(55))
  print("Thank you for trying out my program!".center(55))
  print("------------------------------------".center(55))
  break
