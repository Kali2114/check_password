password = input("Podaj haslo: ")

lowercase = False
uppercase = False
space = False
special = False
number = False

for char in password:
    if char.islower():
        lowercase = True
    elif char.isupper():
        uppercase = True
    elif char.isspace():
        space = True
    elif char.isnumeric():
        number = True
    else:
        special = True

long = len(password) >= 8

correct = (lowercase and
           uppercase and
           not space and 
           special and 
           long and
           number
)

raport = ""

if correct:
    raport += "Hasło jest w porządku!" 
else:
    raport += "To musisz zmienić!\n"
    if not lowercase:
        raport += "- Nie ma małej litery!\n"
    if not uppercase:
        raport += "- Nie ma dużej litery!\n"
    if space:
        raport += "- Nie może być spacji!\n"
    if not special:
        raport += "- Nie ma znaku specjalnego!\n"
    if not long:
        raport += "- Nie ma 8 znaków!\n"
    if not number:
        raport += "- Nie ma cyfry!"

print(raport)
