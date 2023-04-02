passwords = {}
def add_password (account, password):
    passwords [account] = password
def get_password (account):
    return passwords.get(account,None)
def main():
    while True:
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            account = input("Enter account name: ").lower()
            password = input("Enter password: ")
            add_password(account, password)
        elif choice == "2":
            account = input("Enter account: ").lower()
            password = get_password(account)
            if password: 
                print(f"The password for {account} is: {password}.")
            else:
                print(f"No password found for {account}")
        elif choice =="3":
            break
        else:
            print("INVALID")
if __name__ == "__main__":
    main()