# Programming techniques T3 - 3
# 03/12/2021
import time
import random

def task1():
    fever = 0
    total = 0
    hour = 1
    while hour < 7:
        temp = 0
        while temp <30 or temp >44:
            temp = int(input("Enter temperature: "))
        if temp > 37:
            fever = fever + 1
        total = total + temp
        hour = hour + 1
    average = round(total/(hour - 1),1) #round to 1 decimal place
    print("Average temperature:", average)
    print("Incidents of fever:", fever)

def task2():
    part = ""
    total = 0
    totalold = 0
    while part != "9999":
        part = input("enter a 4 digit part number: ")
        while len(part) != 4:
            print("Incorrect input try again")
        total += 1
        check = part[3]
        length = int(check)
        if length >5 and length <9:
            print("model is old")
            totalold += 1
    print (total, ": models inputted,", totalold, ": of the models are old")

def task31():
    total = [0,0,0]
    for i in range(1,31):
        for j in range(3):
            total[j] += int(input("test " + str(j) + " for student " + str(i)))

    average = [total[0]/30, total[1]/30, total[2]/30]
    classtotal = (average[0] + average[1] + average[2]) / 3
    print("average for test 1:", average[0])
    print("average for test 2:", average[1])
    print("average for test 3:", average[2])
    print("average for all tests:", classtotal)

def task32():
    while True:
        rand = round(random.uniform(0.01, 0.1),3)
        light = "LOW"
        time.sleep(rand)
        
        light = "HIGH"
        rand = round(random.uniform(0.01, 0.1),3)
        time.sleep(rand)

if __name__ == "__main__":
    pass
