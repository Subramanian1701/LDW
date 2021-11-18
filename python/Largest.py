#Largest Number:
largest = None
for i in [-1, 2, 6, -40, -30]:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
print ("Largest Number:", largest)