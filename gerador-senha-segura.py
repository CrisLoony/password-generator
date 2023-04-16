from random import choice
print('"' * 40)
print(f'{"Password Generator"}')
print('"' * 40)

characters = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789*.-_@#&'

password_lenght = input("What's the password lenght? ")
amount_of_passwords = input("How many passwords you want to generate? ")

digit_password_lenght = password_lenght.isdigit()
digit_amount_of_passwords = amount_of_passwords.isdigit()

while digit_password_lenght == False or digit_amount_of_passwords == False:
    print("This isn't an valid choice, please insert a integer.")
    if digit_password_lenght:
        password_lenght = input("What's the password lenght? ")
    else:
        amount_of_passwords = input(
            "How many passwords you want to generate? ")

password_lenght = int(password_lenght)
amount_of_passwords = int(amount_of_passwords)
secure_password = ''
cont = 1

while cont <= amount_of_passwords:
    for char in range(password_lenght):
        secure_password += choice(characters)

    print(f"The {cont}º secure password is {secure_password}")
    secure_password = ''
    cont += 1
