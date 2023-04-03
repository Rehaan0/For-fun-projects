import random

print("RANDOM NUMBER GENERATOR".center(55))
print("----------------------- \n".center(55))
length = [8,9,10]
plength = random.choice(length)
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '/', '-', '+', '_', '[', ']', '{', '}', '|', ':', ';', ',', '.', '<', '>', '?']
if plength == 8:
  rl1 = random.choice(letters)
  rl2 = random.choice(letters)
  rl3 = random.choice(letters)
  rl4 = random.choice(letters)
  rn1 = random.choice(numbers)
  rn2 = random.choice(numbers)
  rs1 = random.choice(symbols)
  rs2 = random.choice(symbols)
  print(rl1,rs1,rn1,rl2,rs2,rl3,rl4,rn2)
elif plength == 9:
  rl1 = random.choice(letters)
  rl2 = random.choice(letters)
  rl3 = random.choice(letters)
  rn1 = random.choice(numbers)
  rn2 = random.choice(numbers)
  rn3 = random.choice(numbers)
  rs1 = random.choice(symbols)
  rs2 = random.choice(symbols)
  rs3 = random.choice(symbols)
  print(rs1 , rn1 , rl1 , rn2 , rs2 , rs3 , rn3 , rl2 , rl3)
elif plength == 10:
  rl1 = random.choice(letters)
  rl2 = random.choice(letters)
  rl3 = random.choice(letters)
  rl4 = random.choice(letters)
  rn1 = random.choice(numbers)
  rn2 = random.choice(numbers)
  rn3 = random.choice(numbers)
  rs1 = random.choice(symbols)
  rs2 = random.choice(symbols)
  rs3 = random.choice(symbols)
  print(rn1 , rl1 , rl2 , rs1 , rn2 , rn3 , rl3 , rl4 , rs2 , rs3)
print("")
r = input("Do you want to generate another password (y/n): ")
while r == 'y':
  length = [8,9,10]
  plength = random.choice(length)
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z']
  numbers = [1,2,3,4,5,6,7,8,9,0]
  symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '/', '-', '+', '_', '[', ']', '{', '}', '|', ':', ';', ',', '.', '<', '>', '?']
  print("")
  if plength == 8:
    rl1 = random.choice(letters)
    rl2 = random.choice(letters)
    rl3 = random.choice(letters)
    rl4 = random.choice(letters)
    rn1 = random.choice(numbers)
    rn2 = random.choice(numbers)
    rs1 = random.choice(symbols)
    rs2 = random.choice(symbols)
    print(rl1,rs1,rn1,rl2,rs2,rl3,rl4,rn2)
  elif plength == 9:
      rl1 = random.choice(letters)
      rl2 = random.choice(letters)
      rl3 = random.choice(letters)
      rn1 = random.choice(numbers)
      rn2 = random.choice(numbers)
      rn3 = random.choice(numbers)
      rs1 = random.choice(symbols)
      rs2 = random.choice(symbols)
      rs3 = random.choice(symbols)
      print(rs1 , rn1 , rl1 , rn2 , rs2 , rs3 , rn3 , rl2 , rl3)
  elif plength == 10:
    rl1 = random.choice(letters)
    rl2 = random.choice(letters)
    rl3 = random.choice(letters)
    rl4 = random.choice(letters)
    rn1 = random.choice(numbers)
    rn2 = random.choice(numbers)
    rn3 = random.choice(numbers)
    rs1 = random.choice(symbols)
    rs2 = random.choice(symbols)
    rs3 = random.choice(symbols)
    print(rn1 , rl1 , rl2 , rs1 , rn2 , rn3 , rl3 , rl4 , rs2 , rs3)
  print("")
  r = input("Do you want to generate another password (y/n): ")
while r == 'n':
  print("---------------------------------".center(55))
  print("Thanks for trying out my program!".center(55))
  print("---------------------------------".center(55))
  break
