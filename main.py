from password import generate_password

fo = open("passwords.txt", "a+")

website_name = input("What website are you trying to login to?\n").lower().replace(" ", "")

# Sets file pointer to the beginning and checks to see if the website exists in the text file
fo.seek(0, 0)
website_exists = False
for i in fo.readlines():
    if website_name in i:
        website_exists = True

if not website_exists:
    password_length = input("How long would you like the password to be?\n")
    new_password = generate_password(password_length)
    fo.write(website_name + " " + new_password + "\n")
    print("Your new password is: " + new_password)
else:
    fo.seek(0, 0)
    for i in fo.readlines():
        if website_name in i:
            print("Your password is: " + i.split()[1])

fo.close();