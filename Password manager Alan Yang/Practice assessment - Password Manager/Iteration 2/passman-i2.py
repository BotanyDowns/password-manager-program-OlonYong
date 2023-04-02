buffer = "\n>-------------------------------------------<\n"
def newpassword():
    account = input("Enter account name: ").lower()
    password = input("Enter password: ").lower()
    with open("Practice assessment - Password Manager\Iteration 2\saved.txt", "a") as file:
        file.write(f"{account} : {password}\n")
    print("Password added!")
    input("\nPress enter to continue ")

def getpassword():
    found = False
    account = input("Enter account: ").lower()
    with open("Practice assessment - Password Manager\Iteration 2\saved.txt", "r") as file:
        for line in file:
            if account == line.split(" : ")[0]:
                account, password = line.split(" : ")
                print(f"Username: {account}, Password: {password}")
                found = True
        if not found:
            print(f"No saved passwords found for {account}.")
    input("Press enter to continue ")

def deletepassword():
    account = input("Enter account name: ").lower()
    with open("Practice assessment - Password Manager\Iteration 2\saved.txt", "r") as file:
        lines = file.readlines()
    with open("Practice assessment - Password Manager\Iteration 2\saved.txt", "w") as file:
        for line in lines:
            if account == line.split(" : ")[0]:
                print(f"Successfully deleted password for {account}")
            else:
                file.write(line)
    input("\nPress enter to continue ")


def saved():
    with open("Practice assessment - Password Manager\Iteration 2\saved.txt") as file:
        for i in file:
            print(i)
    input()

def main():
    while True:
        print("\n\n\n\n\nChoose an option: \n1. Add Password\n2. Get Password\n3. Delete password\n4. View saved passwords\n5. Exit")
        choice = int(input("Your choice: "))
        print(buffer)
        if choice == 1:
            newpassword()
        elif choice == 2:
            getpassword()
        elif choice == 3:
            deletepassword()
        elif choice == 4:
            saved()
        elif choice == 5:
            break
        else:
            print("INVALID")
if True:
    main()