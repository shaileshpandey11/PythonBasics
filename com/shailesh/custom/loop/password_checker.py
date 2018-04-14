correct_password = "jvm"

firstname = input("Enter first name :")
lastname = input("Enter last name :")

password = input("Enter password :\n")

while correct_password != password:
    password = input("Wrong password! Please check caps lock button. Enter again \n")

message = "Hello %s %s, you are logged in" % (firstname,lastname)

print(message)
