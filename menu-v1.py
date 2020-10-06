# M3P4, Alessandro och Tage

options = {"a":"Add item", "l":"List items", "q":"Log out"}

print("Select an action")
for action in options:
    print(f"{action}) {options[action]}")
    
while True:
    option = input("Option: ")
    if option in options:
        print(f"\nYou selected option {option}) {options[option]}")
        break
    else:
        continue
