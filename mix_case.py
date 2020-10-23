mixed_case = "A Song of Ice and Fire"

print(mixed_case.isupper())  
print(mixed_case.islower())  

print("")
title_case = mixed_case.title()
print(title_case)  
print(mixed_case.upper())  
print(mixed_case.lower())  

print("")
print(mixed_case.istitle())   
print(mixed_case.startswith("A"))  
print(mixed_case.endswith("e"))  

print("")
words = mixed_case.split()
print(words)  
print("".join(words).isalpha())  