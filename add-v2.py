# M3P4, Alessandro och Tage

# Definition of the function add.

def add(prompt, strings):
    new_string = input(prompt)
    strings.append(new_string)
    return strings

# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louise"]
print(f"Ducks: {ducks}")
ducks = add("Add a duck: ",ducks)
print(f"Ducks: {ducks}")
ducks = add("Add a duck: ",ducks)
print(f"Ducks: {ducks}")

# Test of the function add with the list composers.

composers = composers = ["Mozart", "Bach"]
print(f"Composers: {composers}")
add("Add a composer: ", composers)
print(f"Composers: {composers}")