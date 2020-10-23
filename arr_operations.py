arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]


del arctic_animals[4] # deleted tiger
arctic_animals.remove("elephant") # deleted elephant

arctic_animals.append("arctic fox") # adds arctic fox to end of list
arctic_animals.insert(2, "snowy owl") # inserts snowy owl at index (2)
# arctic_animals.sort()  # sorts array

print(arctic_animals)
print(arctic_animals.index("reindeer"))
