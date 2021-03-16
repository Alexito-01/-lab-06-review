celsius = input("Please enter a temperature in celsius: ")
# print(celsius)
# print(type(celsius))

fahrenheit = 9/5 * float(celsius) + 32
# print(fahrenheit)
# print(type(fahrenheit))

roundedf = round(float(fahrenheit), 2) 

print(str(celsius) + " degrees celsius is " + str(fahrenheit) + " degrees fahrenheit")