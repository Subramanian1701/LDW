# Largest and Smallest Number using user input values
largest = None                                    # NoneType variable initialization
smallest = None
List = []                                         #Blank List Creation
while True :
    sval = input("Enter the number: ")
    if sval == "done" :
        break
    try : 
        ival = int(sval)
    except :
        print("Invalid input")
        continue
    List.append(ival)

# Finding Largest Value
for largeval in List :
    if largest is None :
        largest = largeval
    elif largeval > largest:
        largest = largeval
print("Maximum is", largest)

# Finding Smallest Value
for smallval in List :
    if smallest is None :
        smallest = smallval
    elif smallval < smallest:
        smallest = smallval
print("Minimum is", smallest)
