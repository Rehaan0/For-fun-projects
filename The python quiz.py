print("The python quiz".center(55))
print("\n You get 3 chances for the entire quiz. There are totally 15 questions. If you lose all 3 of your chances, you lose the quiz! You get +1 points per correct answer. Lets see how well you know python!")
points = 0
chances = 3

#QUESTION 1

print("\n 1. What function is used to output text in python?")
print("A. print".center(55))
print("B. <p>".center(55))
print("C. echo".center(55))
print("D. output".center(55))
answer = input("A, B, C, or D: ")
if answer == "A":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is A. print")
  chances -= 1
  print(chances, "Chances remaining")

#QUESTION 2

print("\n 2. To ask input from the user, you have to use the ________ function.")
print("A. ask".center(55))
print("B. Answer".center(55))
print("C. input".center(55))
print("D. user.input".center(55))
answer = input("A, B, C, or D: ")
if answer == "C":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer!")
  chances -= 1
  print(chances, "Chances remaining")

#QUESTION 3

print("\n 3. What is used to perform specific functions if something is true?")
print("A. else".center(55))
print("B. if".center(55))
print("C. iftrue".center(55))
print("D. Not possible".center(55))
answer = input("A, B, C or D: ")
if answer == "B":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is B. if")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 4

print("\n 4. What function is used to perform specific functions if something is false?")
print("A. else".center(55))
print("B. if".center(55))
print("C. false".center(55))
print("D. iffalse".center(55))
answer = input("A, B, C, or D: ")
if answer == "A":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
  print("\n Fun fact: If you use the else function before using the if function, the code won't work!")
else:
  print("That is not the correct answer! The correct answer is A. else")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 5

print("\n 5. What is a variable used to store?")
print("A. Integer".center(55))
print("B. Float".center(55))
print("C. String".center(55))
print("D. All of these".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. All of these")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 6

print("\n 6. What symbol do you use to create a comment?")
print("A. C".center(55))
print("B. #".center(55))
print("C. <".center(55))
print("D. $".center(55))
answer = input("A, B, C, or D: ")
if answer == "B":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is B. #")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 7

print("""\n 7. if chances _____ 0:
   print("Game over!
   
   Fill in the blank""")
print("A. ==".center(55))
print("B. --".center(55))
print("C. =".center(55))
print("D. equal".center(55))
answer = input("A, B, C, or D: ")
if answer == "A":
  print("That is the correct answer!")
  points += 1
  print(points,"Points")
else:
  print("That is not the correct answer! The correct answer is A. ==")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 8

print("\n 8. To output text using print function, you have to enter the text in ________ ")
print("A. Quotes [\' or \"]".center(55))
print("B. Brackets [()]".center(55))
print("C. Curly brackets [{}]".center(55))
print("D. Both A and B".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. Both A and B")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 9

print("\n 9. What programming language is this quiz about?")
print("A. C++".center(55))
print("B. Python".center(55))
print("C. JavaScript".center(55))
print("D. HTML".center(55))
answer = input("A, B, C, or D: ")
if answer == "B":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is B. Python")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 10

print("\n 10. What function do you use to convert a string into an integer?")
print("A. float".center(55))
print("B. int".center(55))
print("C. str".center(55))
print("D. Any of these can be used".center(55))
answer = input("A, B, C, or D: ")
if answer == "B":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is B. int")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 11

print("""\n 11. What is the input of the following code?
print(Hello world)""")
print("A. Hello world".center(55))
print("B. \"Hello world\"".center(55))
print("C. print(Hello World)".center(55))
print("D. Error".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. Error")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 12

print("\n 12. Python can be used to create games")
print("A. True".center(55))
print("B. False".center(55))
print("C. It depends".center(55))
print("D. Ignore this option".center(55))
answer = input("A, B, C, or D: ")
if answer == "A":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
elif answer == "D":
  print("I told you to ignore it")
  quit()
else:
  print("That is not the correct answer! The correct answer is A. True")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 13

print("\n 13. Using python, you can make ______")
print("A. Video games".center(55))
print("B. Quiz".center(55))
print("C. Rock Paper Scissors".center(55))
print("D. All of these".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. All of these")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 14

print("\n 14. What function can be used to create a loop?")
print("A. while".center(55))
print("B. for".center(55))
print("C. loop".center(55))
print("D. Both A and B".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. Both A and B")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

#QUESTION 15

print("\n 15. To enter a new line, Use the ______ command")
print("A. nl".center(55))
print("B. <br>".center(55))
print("C. nxtln".center(55))
print("D. None of these".center(55))
answer = input("A, B, C, or D: ")
if answer == "D":
  print("That is the correct answer!")
  points += 1
  print(points, "Points")
else:
  print("That is not the correct answer! The correct answer is D. None of these")
  chances -= 1
  print(chances, "Chances remaining")
while chances == 0:
  print("\n You lost the quiz! Please press the run button again to continue.")
  print("--------------------------------".center(55))
  print("Thank you for trying my program!".center(55))
  print("--------------------------------".center(55))
  quit()

print("\n The quiz has ended! You totally have ", points, "Points and finishied it with ", chances, "chances remaining.")
print("\n STATISTICS".center(55))
print("\n 0 - This score is literally not possible")
print("\n 1 to 5 - It seems you just started learning python. Keep learning and get better at Python!")
print("\n 6 to 10 - You propably know the basics of Python quite well! Keep training and become better at Python")
print("\n 11 to 15 - You are too experienced in Python for this quiz! But that does not mean you mastered Python. Keep learning and become better at Python!")
print("YOUR SCORE".center(55))
if points >= 1 and points <= 5:
  print("\n 1 to 5 - It seems you just started learning python. Keep learning and get better at Python!")
elif points >= 6 and points <= 10:
  print("\n 6 to 10 - You propably know the basics of Python quite well! Keep training and become better at Python")
elif points >= 11 and points <= 15:
  print("\n 11 to 15 - You are too experienced in Python for this quiz! But that does not mean you mastered Python. Keep learning and become better at Python!")

r = input("Do you want to try again?(y/n): ")
while r == "y":
  print("The python quiz".center(55))
  print("\n You get 3 chances for the entire quiz. There are totally 15 questions. If you lose all 3 of your chances, you lose the quiz! You get +1 points per correct answer. Lets see how well you know python!")
  points = 0
  chances = 3

  #QUESTION 1

  print("\n 1. What function is used to output text in python?")
  print("A. print".center(55))
  print("B. <p>".center(55))
  print("C. echo".center(55))
  print("D. output".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "A":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is A. print")
    chances -= 1
    print(chances, "Chances remaining")

  #QUESTION 2

  print("\n 2. To ask input from the user, you have to use the ________ function.")
  print("A. ask".center(55))
  print("B. Answer".center(55))
  print("C. input".center(55))
  print("D. user.input".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "C":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer!")
    chances -= 1
    print(chances, "Chances remaining")

  #QUESTION 3

  print("\n 3. What is used to perform specific functions if something is true?")
  print("A. else".center(55))
  print("B. if".center(55))
  print("C. iftrue".center(55))
  print("D. Not possible".center(55))
  answer = input("A, B, C or D: ")
  if answer == "B":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is B. if")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 4

  print("\n 4. What function is used to perform specific functions if something is false?")
  print("A. else".center(55))
  print("B. if".center(55))
  print("C. false".center(55))
  print("D. iffalse".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "A":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
    print("\n Fun fact: If you use the else function before using the if function, the code won't work!")
  else:
    print("That is not the correct answer! The correct answer is A. else")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 5

  print("\n 5. What is a variable used to store?")
  print("A. Integer".center(55))
  print("B. Float".center(55))
  print("C. String".center(55))
  print("D. All of these".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. All of these")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 6

  print("\n 6. What symbol do you use to create a comment?")
  print("A. C".center(55))
  print("B. #".center(55))
  print("C. <".center(55))
  print("D. $".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "B":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is B. #")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 7

  print("""\n 7. if chances _____ 0:
   print(\"Game over!\")
   
   Fill in the blank""")
  print("A. ==".center(55))
  print("B. --".center(55))
  print("C. =".center(55))
  print("D. equal".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "A":
    print("That is the correct answer!")
    points += 1
    print(points,"Points")
  else:
    print("That is not the correct answer! The correct answer is A. ==")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 8

  print("\n 8. To output text using print function, you have to enter the text in ________ ")
  print("A. Quotes [\' or \"]".center(55))
  print("B. Brackets [()]".center(55))
  print("C. Curly brackets [{}]".center(55))
  print("D. Both A and B".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. Both A and B")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 9

  print("\n 9. What programming language is this quiz about?")
  print("A. C++".center(55))
  print("B. Python".center(55))
  print("C. JavaScript".center(55))
  print("D. HTML".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "B":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is B. Python")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 10

  print("\n 10. What function do you use to convert a string into an integer?")
  print("A. float".center(55))
  print("B. int".center(55))
  print("C. str".center(55))
  print("D. Any of these can be used".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "B":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is B. int")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 11

  print("""\n 11. What is the input of the following code?
print(Hello world)""")
  print("A. Hello world".center(55))
  print("B. \"Hello world\"".center(55))
  print("C. print(Hello World)".center(55))
  print("D. Error".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. Error")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 12

  print("\n 12. Python can be used to create games")
  print("A. True".center(55))
  print("B. False".center(55))
  print("C. It depends".center(55))
  print("D. Ignore this option".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "A":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  elif answer == "D":
    print("I told you to ignore it")
    quit()
  else:
    print("That is not the correct answer! The correct answer is A. True")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 13

  print("\n 13. Using python, you can make ______")
  print("A. Video games".center(55))
  print("B. Quiz".center(55))
  print("C. Rock Paper Scissors".center(55))
  print("D. All of these".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. All of these")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 14

  print("\n 14. What function can be used to create a loop?")
  print("A. while".center(55))
  print("B. for".center(55))
  print("C. loop".center(55))
  print("D. Both A and B".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. Both A and B")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  #QUESTION 15

  print("\n 15. To enter a new line, Use the ______ command")
  print("A. nl".center(55))
  print("B. <br>".center(55))
  print("C. nxtln".center(55))
  print("D. None of these".center(55))
  answer = input("A, B, C, or D: ")
  if answer == "D":
    print("That is the correct answer!")
    points += 1
    print(points, "Points")
  else:
    print("That is not the correct answer! The correct answer is D. None of these")
    chances -= 1
    print(chances, "Chances remaining")
  while chances == 0:
    print("\n You lost the quiz! Please press the run button again to continue.")
    print("--------------------------------".center(55))
    print("Thank you for trying my program!".center(55))
    print("--------------------------------".center(55))
    quit()

  print("\n The quiz has ended! You totally have ", points, "Points and finishied it with ", chances, "chances remaining.")
  print("\n STATISTICS".center(55))
  print("\n 0 - This score is literally not possible")
  print("\n 1 to 5 - It seems you just started learning python. Keep learning and get better at Python!")
  print("\n 6 to 10 - You propably know the basics of Python quite well! Keep training and become better at Python")
  print("\n 11 to 15 - You are too experienced in Python for this quiz! But that does not mean you mastered Python. Keep learning and become better at Python!")
  print("YOUR SCORE".center(55))
  if points >= 1 and points <= 5:
    print("\n 1 to 5 - It seems you just started learning python. Keep learning and get better at Python!")
  elif points >= 6 and points <= 10:
    print("\n 6 to 10 - You propably know the basics of Python quite well! Keep training and become better at Python")
  elif points >= 11 and points <= 15:
    print("\n 11 to 15 - You are too experienced in Python for this quiz! But that does not mean you mastered Python. Keep learning and become better at Python!")

  r = input("Do you want to try again?(y/n): ")
while r == "n":
  print("------------------------------------".center(55))
  print("Thank you for trying out my program!".center(55))
  print("------------------------------------".center(55))
  break

#ANSWERS

#1. A
#2. C
#3. B
#4. A
#5. D
#6. B
#7. A
#8. D
#9. B
#10. B
#11. D
#12. A
#13. D
#14. D
#15. D
