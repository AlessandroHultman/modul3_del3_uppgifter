# M3P4, Alessandro och Tage

users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
print()
while True:
    user = input("User: ")
    password = input("Password: ")
    if user in users and password == users[user]:
        print(f"\nWelcome {user}")
        break
    else:
        print("\nInvalid username or password\n")
        continue

