import string
import random
length=int(input("enter the length of your password:"))
print("1.Digits\n2.Uppercase Letters\n3.Lowercase Letters\n4.Special Characters\n5.Exit")
characterlist=""
while(True):
  choice=int(input("enter your choices for your password:"))
  if(choice==1):
     characterlist+=string.digits
  elif(choice==2):
     characterlist+=string.ascii_uppercase
  elif(choice==3):
     characterlist+=string.ascii_lowercase
  elif(choice==4):
     characterlist+=string.punctuation
  elif(choice==5):
     break
  else:
     print("enter a valid choice")
password=[]
for i in range(length):
   randomcharacter=random.choice(characterlist)
   password.append(randomcharacter)
print("The random password is:"+"".join(password))