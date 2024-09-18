import string
import random
ab=1
while(ab==1):
 len=int(input("Enter the Length of Password :"))
 if(len>=6):
   x = string.ascii_uppercase + string.digits + string.ascii_lowercase 
   x = random.choices(x, k=2) 
   a = random.choices(string.ascii_uppercase, k=2) 
   b = random.choices(string.digits, k=2)
   c = random.choices(string.ascii_lowercase, k=len-6)
   password = x+a+b+c
   random.shuffle(password)
   print("password : ",''.join(password))
   ab=0
 else:
     print("password should be at least of 6 digit, try again..")
        