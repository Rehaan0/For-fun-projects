table = int(input("Which table do you want?: "))
print("")
print("Table".center(55))
print("")
totw = int(input("Do you want till 10(10) or 12(12)?: "))
if totw == 10:
  print("")
  t1=table*1
  t2=table*2
  t3=table*3
  t4=table*4
  t5=table*5
  t6=table*6
  t7=table*7
  t8=table*8
  t9=table*9
  t10=table*10
  print("1  x ", table , " = ", t1)
  print("2  x ", table , " = ", t2)
  print("3  x ", table , " = ", t3)
  print("4  x ", table , " = ", t4)
  print("5  x ", table , " = ", t5)
  print("6  x ", table , " = ", t6)
  print("7  x ", table , " = ", t7)
  print("8  x ", table , " = ", t8)
  print("9  x ", table , " = ", t9)
  print("10 x ", table , " = ", t10)

if totw == 12:
  print("")
  t1=table*1
  t2=table*2
  t3=table*3
  t4=table*4
  t5=table*5
  t6=table*6
  t7=table*7
  t8=table*8
  t9=table*9
  t10=table*10
  t11=table*11
  t12=table*12
  print("1  x ", table , " = ", t1)
  print("2  x ", table , " = ", t2)
  print("3  x ", table , " = ", t3)
  print("4  x ", table , " = ", t4)
  print("5  x ", table , " = ", t5)
  print("6  x ", table , " = ", t6)
  print("7  x ", table , " = ", t7)
  print("8  x ", table , " = ", t8)
  print("9  x ", table , " = ", t9)
  print("10 x ", table , " = ", t10)
  print("11 x ", table , " = ", t11)
  print("12 x ", table , " = ", t12)
print("")
r = input("Do you want to try another table? y/n: ")
while r == "y":
  print("")
  table = int(input("Which table do you want?: "))
  print("")
  print("Table".center(55))
  print("")
  totw = int(input("Do you want till 10(10) or 12(12)?: "))
  if totw == 10:
    print("")
    t1=table*1
    t2=table*2
    t3=table*3
    t4=table*4
    t5=table*5
    t6=table*6
    t7=table*7
    t8=table*8
    t9=table*9
    t10=table*10
    print("1  x ", table , " = ", t1)
    print("2  x ", table , " = ", t2)
    print("3  x ", table , " = ", t3)
    print("4  x ", table , " = ", t4)
    print("5  x ", table , " = ", t5)
    print("6  x ", table , " = ", t6)
    print("7  x ", table , " = ", t7)
    print("8  x ", table , " = ", t8)
    print("9  x ", table , " = ", t9)
    print("10 x ", table , " = ", t10)

  if totw == 12:
    print("")
    t1=table*1
    t2=table*2
    t3=table*3
    t4=table*4
    t5=table*5
    t6=table*6
    t7=table*7
    t8=table*8
    t9=table*9
    t10=table*10
    t11=table*11
    t12=table*12
    print("1  x ", table , " = ", t1)
    print("2  x ", table , " = ", t2)
    print("3  x ", table , " = ", t3)
    print("4  x ", table , " = ", t4)
    print("5  x ", table , " = ", t5)
    print("6  x ", table , " = ", t6)
    print("7  x ", table , " = ", t7)
    print("8  x ", table , " = ", t8)
    print("10 x ", table , " = ", t10)
    print("11 x ", table , " = ", t11)
    print("12 x ", table , " = ", t12)
  print("")
  r = input("Do you want to try another table? y/n: ")

while r == "n":
  o = "--------------------------------"
  l = "Thank you for trying my program!"
  print("")
  print(o.center(55))
  print(l.center(55))
  print(o.center(55))
  break
