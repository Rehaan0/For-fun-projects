import random
words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','-','_','=','+']
ranword = random.choice(words)
rannum = random.choice(numbers)
ransym = random.choice(symbols)
ranword2 = random.choice(words)
rannum2 = random.choice(numbers)
ransym2 = random.choice(symbols)
ranword3 = random.choice(words)
rannum3 = random.choice(numbers)
choice = [ranword, rannum, ransym, ranword2, rannum2, ransym2, ranword3, rannum3]
ranchoice = random.choice(choice)
ranchoice2 = random.choice(choice)
ranchoice3 = random.choice(choice)
ranchoice4 = random.choice(choice)
ranchoice5 = random.choice(choice)
ranchoice6 = random.choice(choice)
ranchoice7 = random.choice(choice)
ranchoice8 = random.choice(choice)
print(ranchoice,ranchoice2,ranchoice3,ranchoice4,ranchoice5,ranchoice6,ranchoice7,ranchoice8, sep="")
