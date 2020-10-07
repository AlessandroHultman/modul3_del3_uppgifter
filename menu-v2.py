# M3P4, Alessandro och Tage

def menu(title, prompt, options):
    print(title + "\n")
    for action in options:
        print(f"{action}) {options[action]}")
    print()
    while True: 
        action = input(prompt)
        if action in options:
            return action
        else:
            continue


options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print()
print(f"You selected action {opt1}) {options1[opt1]}")
print()
options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print()
print(f"You selected option {opt2}) {options2[opt2]}")
