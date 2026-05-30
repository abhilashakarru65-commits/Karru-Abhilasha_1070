#Temperature Predictor
temperature = int(input("Enter temperature: "))
if temperature < 0:
    print("Freezing Weather")

elif temperature <= 15:
    print("Cold Climate")

elif temperature <= 25:
    print("Pleasant Weather")

elif temperature <= 35:
    print("Hot Weather")

else:
    print("Extreme Heat")