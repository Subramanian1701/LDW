#Nested Conditional Statements
x = 42.0
if x>1 :
    print ('Greater than 1')
    if x<100:
        print('Less than 100')
elif x==42:
    print('Number is 42')
else:
    print('Some value')
print('All Done')