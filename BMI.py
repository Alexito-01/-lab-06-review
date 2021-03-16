print("Welcome to BMI: ")
userWeight = input("Enter you weight (in pounds): ")
userHeight = input("Enter your height (in inches): ")
userHeightFloat = float(userHeight)

myBMIpy = round((703 * float(userWeight)) / (userHeightFloat * userHeightFloat), 2)

print("Your body mass index (BMI) is " + str(myBMIpy) + "%")