def Leap():
    year=int(input("Enter Year : "))
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print("Leap Year")
            else:
                print("Non Leap year")
        else:
            print("Leap year")
    else:
        print("Non Leap Year")
Leap()