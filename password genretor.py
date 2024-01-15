import random
import string
length=int(input("enter the length of your password"))
print("choose the characters for maintain your password:1. 1. Letters,2.Digits,3.Special Characters,4.Exit")
characterList = ""
while True:
    choice=int(input("enter your choice for password"))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
password = []
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))
 
