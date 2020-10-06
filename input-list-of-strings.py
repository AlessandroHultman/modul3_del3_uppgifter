# M3P4, Alessandro och Tage

def add(prompt, strings):
    strings.append(prompt)
    return strings

def view(description, strings):
    print(description+"\n")
    for index, name in enumerate(strings, start = 1):
	    print(f"{index}) {name}")

strings = []
n = 5
print("n = " + str(n))

while len(strings) < n:
    string = input("\nLägg till en sträng: ")
    strings = add(string, strings)

description = f"\nDu har matat in följande {n} strängar"
view(description, strings)