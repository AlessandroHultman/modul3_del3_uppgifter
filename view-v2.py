# M3P4, Alessandro och Tage

def view(description, strings):
    print(description+"\n")
    for index, name in enumerate(strings, start = 1):
	    print(f"{index}) {name}")

# Testkod
names = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]   
view("\nLista med namn\n", names)
print()
view("\nLista med djur\n", animals)