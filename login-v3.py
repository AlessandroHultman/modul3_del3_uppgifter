# M3P4, Alessandro och Tage

def menu(title, prompt, options):
    print(title)
    for action in options:
        print(f"{action}) {options[action]}")
    print()
    while True: 
        action = input(prompt)
        if action in options:
            return action
            break
        else:
            continue

def login(users):
    while True:
        print()
        user = input("User: ")
        password = input("Password: ")
        if user in users and password == users[user]:
            return user
            break
        else:
            print("\nInvalid username or password")
            action = menu("", "Option: ", options)
            if action == "r":
                user = login(users)
                return user
            else:
                break

options = {"r":"Try again", "q":"Quit"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user = login(users)