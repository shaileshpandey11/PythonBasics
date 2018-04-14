correct_password = "jvm"

password = input("Enter password :\n")

while correct_password != password:
    password = input("Wrong password! Please check caps lock button. Enter again \n")

print("Successfully Logged in")
