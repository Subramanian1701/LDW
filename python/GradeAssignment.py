# Display Grade for the respective Score
score = input("Enter the score:")

try:
    score = float(score)
except:
    print("Enter the valid numeric score range")
    quit()

if score > 1.0 or score < 0.0 :
    print("Enter the score range between 0.0 and 1.0")
    quit()
else:
    if score >= 0.9 :
        print("A")
    elif score >= 0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    else:
        print("F")

