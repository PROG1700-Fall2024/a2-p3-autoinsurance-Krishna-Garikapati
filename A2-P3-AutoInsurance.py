#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:  W0502117   
#Student Name:  Kishna Priyanka Garikapati

def main():
    #Three inputs
    Gender=input("Are you 'Male' or 'Female': ")
    Age=int(input("Enter your age: "))
    VehiclePrice=float(input("Enter the purchase price of the vehicle: "))
    #Conditions based on gender
    if Gender.lower()=="male":
        if 25>Age>=15:
            insurance=(0.25/12)*VehiclePrice
        elif 25<=Age<40:
            insurance=(0.17/12)*VehiclePrice
        elif 40<=Age<70:
            insurance=(0.10/12)*VehiclePrice
        else:
            insurance=0
    elif Gender.lower()=="female":
        if 25>Age>=15:
            insurance=(0.20/12)*VehiclePrice
        elif 25<=Age<40:
            insurance=(0.15/12)*VehiclePrice
        elif 40<=Age<70:
            insurance=(0.10/12)*VehiclePrice
        else:
            insurance=0
    #Output to display on console
    print("Your monthly insurance will be ${0:.2f}".format(insurance))
main()