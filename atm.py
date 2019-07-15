balance = 2000
password = "1234"
chance = 3
while chance >0:
    code = input("Enter the password")
    if code == password:
        print("press 1 for checking balance")
        print("press 2 for withdrawing")
        print("press 3 for deposit")
        print("press 4 for password change")
        option = input("enter the option")
        if option == "1":
            print("your current balance is:",balance)
        elif option == "2":
            withdraw = int(input("enter the withdrawl amount"))
            if withdraw > balance:
                print("insufficient balance")
            else:
                balance = balance - withdraw;
                print("Amount Withdrawn:",withdraw)
                print("Currnet balance is:", balance)
                break
        elif option == "3":
            deposit = int(input("enter the deposited amount"))
            balance = balance + deposit;
            print("amount deposited:", deposit)
            print("Currnet balance is:", balance)
            break
        elif option == "4":
            newPassword = input("enter the new password")
            if len(newPassword) != 4:
                print("Password should be equal to 4 digits")
            else:
                password = newPassword
                print("password changed to", newPassword)
                break

    else:
        chance -= 1
        if chance == 0:
            print("Account blocked")
            break