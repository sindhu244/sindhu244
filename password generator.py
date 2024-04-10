import random

def generatePassword(pwlengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pwlengths:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)

        passwords.append(password)

    return passwords

def replaceWithNumber(pword):
    replace_index = random.randrange(len(pword))
    return pword[:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]

def replaceWithUppercaseLetter(pword):
    replace_index = random.randrange(len(pword))
    return pword[:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Passwords = generatePassword(passwordLengths)

    for i, password in enumerate(Passwords):
        print("Password #" + str(i+1) + " = " + password)

main()
