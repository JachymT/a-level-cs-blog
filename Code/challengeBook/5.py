#challenge 5, python programming booklet
#seconds from a date

from datetime import datetime

def main():
    #input formating
    birth = input("Enter your birthday in the form yyyy-mm-dd: ")
    birthdate = datetime.strptime(birth, "%Y-%m-%d")
    
    today = datetime.now()

    age = today - birthdate

    print("you are", age.days, "days old")
    print("or", age.days * 24, "hours")
    print("or", age.days * 24 * 60 , "minutes")
    print("or", age.days * 24 * 60**2 , "seconds")


if __name__ == "__main__":
    main()
