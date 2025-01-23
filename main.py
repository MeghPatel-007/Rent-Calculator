rent = int(input("What is the Amt of total rent to pay ? = "))
expenses = int(input("How much expenses have been done ? = "))
people = int(input("How many people live together ? = "))
Total_charge = 0

for i in range(0,3):
    if(i == 0):
        print("Give info abt Electric bills : ")
    elif(i == 1):
        print("Give info abt Gas bills : ")
    elif(i == 2):
        print("GIve info abt Water bills : ")
    previous_reading = int(input("What was the previous reading ? = "))
    current_reading = int(input("What is the current reading ? = "))
    base_rate = int(input("What is the base rate ? = "))
    usage_charge = (current_reading - previous_reading)*base_rate
    # print(usage_charge)
    Total_charge += abs(usage_charge)
    # print(Total_charge)

pay_per_person = (Total_charge + expenses + rent)/people

print(f"Amt to pay by per person is = $",pay_per_person)