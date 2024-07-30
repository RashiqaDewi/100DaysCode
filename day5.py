#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
huruf = []
simbol = []
angka = []
for i in range (nr_letters) :
    huruf.append(random.choice(letters)) # i totally forgot about this, you dont need to define it by =. just do the function per usual
for i in range (nr_symbols) :
    simbol.append(random.choice(symbols))
for i in range (nr_numbers) :
    angka.append(random.choice(numbers))
pass1 = "".join(huruf)
pass2 = "".join(simbol)
pass3 = "".join(angka)
password = pass1+pass2+pass3
print(f"Here's you password : {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

huruf = []
simbol = []
angka = []
for i in range (nr_letters) :
    huruf.append(random.choice(letters)) # i totally forgot about this, you dont need to define it by =. just do the function per usual
for i in range (nr_symbols) :
    simbol.append(random.choice(symbols))
for i in range (nr_numbers) :
    angka.append(random.choice(numbers))

pass1 = "".join(huruf)
pass2 = "".join(simbol)
pass3 = "".join(angka) 
passwor = list(pass1+pass2+pass3)
random.shuffle(passwor)
shuffled_password = ''.join(passwor)
print(f"Here's your password : {shuffled_password}")

    





    



