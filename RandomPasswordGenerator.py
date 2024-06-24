import random
import string

pass_length = int(input("Enter the password length:"))
print("1. Letters + Digits", "\n2. Letters + Special Characters", "\n3. Letters + Digits + Special Characters")

password = ''
choice = int(input("Enter your character set prefrences (3rd is prefered more):"))
if choice == 1:
        passwordlist = string.ascii_letters + string.digits
        
elif choice == 2:
        passwordlist = string.ascii_letters + string.punctuation
       
elif choice == 3:
        passwordlist = string.ascii_letters + string.digits + string.punctuation
        
else:
    print("Enter valid choice!!!")
    exit()
    
for i in range(pass_length):
            password = ''.join(random.choices(passwordlist))
            print(password, end = '')
        
            
        
    
