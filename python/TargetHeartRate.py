
def inputNumber(str):
    print(str)
    age = input()
    if age.isdigit():
        return age
    else:
        inputNumber()

age = int(inputNumber("Enter Your Age : "))
restHR = int(inputNumber("Enter Your Resting Heart Rate : "))

intensity = 55
TargetHeartRate = 0
print("Intensity | Rate  ")
print("---------------------")

while intensity < 100:
    TargetHeartRate = (((220-age)-restHR)*intensity*0.01) + restHR
    print(str(intensity)+"%       | " + str(round(TargetHeartRate)) + " bpm")
    intensity = intensity + 5
    TargetHeartRate = 0
