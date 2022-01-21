# Mortgage calculator

InterestRate = 3/100
MonthsInYear = 12
interval = 1         #12 = monethly; 1 = yearly


def main():
    total = int(input("How much money do you want? £: "))
    years = int(input("How much time do you have? years: "))
    charge = total/(years*interval)
    charge = charge + (InterestRate*charge)
    
    monthly = 0
    if interval == 1:
        monthly = charge/12
    else:
        monthly = charge

    yearly = monthly*12
    payment = yearly*years
    
    monthly = round(monthly,2)
    yearly = round(yearly,2)
    payment = round(payment,2)
    
    print("You will be paying £{0} a month".format(monthly))
    print("You will be paying £{0} a year".format(yearly))
    print("You will be paying £{0} in total".format(payment))

if __name__ == "__main__":
    main()
