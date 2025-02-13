import random

numbers=list(range(10))
symbols=list("~!@#$%^&*()_+|\[{?><,.`}]")
alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

numbers_lenght=int(input("How many Numbers do you need in your password :"))  # 5
symbols_lenght=int(input("How many  Symbols do you need in your password :"))
alphabet_lenght=int(input("How many alphabets do you need in your password :"))

password_list=[]
for i in range(numbers_lenght+1):
    password_list.append(str(random.choice(numbers)))

for i in range(symbols_lenght+1):
    password_list.append(random.choice(symbols))

for i in range(alphabet_lenght+1):
    password_list.append(random.choice(alphabets))

random.shuffle(password_list)
# print(password_list)

final_password=""
for i in password_list:
    final_password=final_password+i
print(f"Here is your computer generated Strong password : {final_password}")
