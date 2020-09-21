import password

fo = open("passwords1.txt", "r+")
lines = fo.readlines()
website_name = input("What website are you trying to login to?\n").lower().replace(" ", "")

# Sets file pointer to the beginning and checks to see if the website exists in the text file
fo.seek(0, 0)
website_exists = False
for i in lines:
    if website_name in i:
        website_exists = True

if not website_exists:
    print(password.add_password(lines, website_name, fo))
else:
    print(password.find_password(lines, website_name))

    answer = input("Would you like to change your password? [y/n]\n")

    if answer == "y":
        print(password.change_password(lines, website_name, fo))

fo.close()
