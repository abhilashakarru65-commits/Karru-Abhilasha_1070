# Checking the password 
password = "python123"

user1 = input("Enter password: ")

if user1 == password:
    print("Login Successful")
else:
    user2 = input("Try again: ")

    if user2 == password:
        print("Login Successful")
    else:
        print("Access Denied")