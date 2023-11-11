year = int(input("The Present year is : "))
if year %4==0 :
    if year %100==0:
        if year %400==0:
            print("Leap year") 
        else:
            print("NO ,Not Leap Year.")
    else:
        print("Wow! Leap year")
else: 
    print("Not a Leap Year")