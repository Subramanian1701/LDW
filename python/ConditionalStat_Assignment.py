# Conditional Statement Assignment
hours = input("Enter the worked hours:")
rate = input("Enter the rate per hour:")

try: 
    hours = float(hours)
    rate = float(rate)
    dailyhours = float(40)
except:
    print("Error, Please enter the numeric input")
    quit()

# Gross Pay Calculation
if hours > dailyhours :
    Additionalhours = hours - dailyhours
else:
    Additionalhours = 0
    dailyhours = hours

grosspay = (dailyhours * rate) + (Additionalhours * rate * 1.5)
print(grosspay)