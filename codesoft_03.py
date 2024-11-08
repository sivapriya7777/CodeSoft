import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z','A','B',
         'C','D','E','F','G','H','I','J','K','L','M','N','O','P',
         'Q','R','S','T','U','V','W','X','Y','Z',]
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','+']
print("Random Password Generator")
pw=int(input("Enter the length of password:"))
n_letters=int(input("How many letters do you want in password:"))
n_numbers=int(input("How many number do you want in password:"))
n_symbols=int(input("How many symbols do you want in password:"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
password = ''.join(random.sample(password, len(password)))
print("Password:",password)


         
