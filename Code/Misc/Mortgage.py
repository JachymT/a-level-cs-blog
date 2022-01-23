# Mortgage calculator

def fixedInterest(principle, years, interestRate):
    amount = principle/(years*12)
    amount = amount + (interestRate*amount)
    return amount

def compoundInterest(p, t, r, n=12):
    amount = p * (r / n) * (1 + (r / n))**(n*t)
    amount = amount / ((1 + r / n)**(n*t) - 1)
    return amount

def main():
    principle = int(input("How much money do you want? £: "))
    years = int(input("How much time do you have? years: "))
    rate = float(input("How much interest do you want? %:"))
    interestRate = rate/100
    fixedORcomp = input("Fixed or Compound Interest? f/c: ")

    if fixedORcomp == "f":
        monthly = fixedInterest(principle, years, interestRate)
    else:
        monthly = compoundInterest(principle, years, interestRate)
  
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
