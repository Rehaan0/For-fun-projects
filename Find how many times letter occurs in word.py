print("Find how many times a letter occurs in a word ".center(55))
print("\n First it will ask what word you want. Then it will ask for a letter. Why it asks the letter is that it will find how many times that letter occurs in the word \n")
count = 0
word = input("Word: ")
letter = input("Letter: ")
for i in word:
  if i == letter:
    count += 1
if count != 0:
  print("\n The letter", letter, "appears", count, "times in the word. \n")
else:
  print("\n The letter", letter, "does not appear in the word. \n")
r = input("\n Try again(y/n): ")
while r == "y":
  count = 0
  word = input("Word: ")
  letter = input("Letter: ")
  for i in word:
    if i == letter:
      count += 1
  if count != 0:
    print("\n The letter", letter, "appears", count, "times in the word.")
  else:
    print("\n The letter", letter, "does not appear in the word.")
  r = input("\n Try again(y/n):")
while r == "n":
  print("------------------------------------".center(55))
  print("Thank you for trying out my program!".center(55))
  print("------------------------------------".center(55))
  break
