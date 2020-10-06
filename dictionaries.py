# M3P4, Alessandro och Tage

users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
print("Användare:\n")
for user in users:
    print(user)

print("\nAnvändare och lösenord:\n")
for user in users:
    print(f"{user}) {users[user]}")

data = {
"nisse":["luva", "vante"],
"bosse":["spik", "skruv", "hammare"], 
"stina":["tidsmaskin"]
}

print("\nAnvändare och deras data:\n")
for user in data:
    print(f"{user}) {data[user]}")

search_user = input("\nSlå upp en avändare: ")
if search_user in data:
    print(f"Data lagrat för {search_user}: {data[search_user]}")
else:
    print("\nAnvändaren mimmi finns inte")