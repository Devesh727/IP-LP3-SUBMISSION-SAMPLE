#code2
def leap_yr(n):
    if n % 400 == 0:            #checking divisibility by 400
        return True
    if n % 100 == 0:            #checking divisibility by 100
        return False
    if n % 4 == 0:              #checking divisibility by 4
        return True
    return False

print(leap_yr(int(input())))
