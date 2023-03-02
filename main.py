import random
letters = ["A","B","C","D",F",G","H","I","J","K","L","M","N","O","P","Q","R","U","V","X","W","Y","Z"]
numbers = ["0","2","4,","5","6","7","8","9"]
symbols = ["@","#","$","%"]

print("bem-vindo ao criodor de senhas do bts")
nr_letters = int(input("quantidade de letras"))
nr_numbers = int(input("quantidade de numeros"))
nr_symbols = int(input("quantidade de simbolos"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"sua senha é:  {password}")