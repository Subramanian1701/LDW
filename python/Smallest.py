#Smallest Number:
Smallest = None    #None is variable used for unknown value or absence of value
print(type(Smallest))
for i in [-1, 2, 6, -40, -30]:
    if Smallest is None:
        Smallest = i
    elif i < Smallest:
        Smallest = i
print ("Largest Number:", Smallest)