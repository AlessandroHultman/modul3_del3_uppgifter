# M3P4, Alessandro och Tage

def login(users):
    while True:
        user = input("User: ")
        password = input("Password: ")
        if user in users and password == users[user]:
            return user
        else:
            print("\nInvalid username or password\n")
            continue

#Testkod
users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print()
print(f"Welcome {user1}")
print()
users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print()
print(f"Welcome {user2}")
