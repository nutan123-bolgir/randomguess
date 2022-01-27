import random
randomNumber=random.randrange(0,100)
print("random number has beeen generated")
guessed=False
while guessed == False:
    num=int(input("enter some guess:"))
    if num==randomNumber:
        guessed=True
        print("well done! you have guessed a number correctly!!!")
    elif num>100 and num<0:
        print("our guess is not between 0 and 100")
    elif num>randomNumber:
        print("number is high")
    elif num<randomNumber:
        print("number is low")
                    
