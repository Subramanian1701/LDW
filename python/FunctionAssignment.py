# Function Assignment
# Function for Gross Pay Calculation
def computepay(hours, rate, dailyhours):
    if hours > dailyhours :
        Additionalhours = hours - dailyhours
    else:
        Additionalhours = 0
        dailyhours = hours
    grosspay = (dailyhours * rate) + (Additionalhours * rate * 1.5)
    return grosspay

# Main block
hrs = input("Enter the worked hours:")
rt = input("Enter the rate per hour:")

try: 
    hrs = float(hrs)
    rt = float(rt)
    dhrs = float(40)
except:
    print("Error, Please enter the numeric input")
    quit()

gpay = computepay(hrs, rt, dhrs)
print("Pay", gpay)