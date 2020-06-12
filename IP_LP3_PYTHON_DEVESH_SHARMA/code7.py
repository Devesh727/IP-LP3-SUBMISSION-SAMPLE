#CODE7
#C to F
C = float(input("Enter temperature in celsius: "))
F = (C * 9/5) + 32                      #conversion of C to F
print('%.0f°C is %.0f Fahrenheit' %(C, F))

#F to C
F = float(input("Enter temperature in fahrenheit: "))
C = (F - 32) * 5/9                      #conversion of F to C
print('%.0f°F is %.0f Celsius' %(F, C))
