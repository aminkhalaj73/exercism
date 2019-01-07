
def is_armstrong(number):
    sum = 0
    order = len(str(number))
    for i in str(number) :
        power = pow(int(i),order)
        sum += power
    if int(sum) == number :
        return True
    else :
        return False

            