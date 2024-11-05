# task one method 1
def check_num(num):
    if num%3 == 0:
        print(num," divisible by 3")
    else:
        print(num," not divisible by 3")

check_num(91)


# task 1 method 2 

def check_number(num):
    num1 = num
    digit_sum = 0
    while num > 0:
        rem = num % 10
        num = num//10
        digit_sum += rem

    if digit_sum % 3 == 0:
        print(num1," divisible by 3")
    else:
        print(num1," not divisible by 3")
check_number(13)

# task 1 method 3

def checkNumber(num):
    digitsum = sum(map(int,str(num)))
    digitsum1 = list(map(int,str(num)))
    
    print(digitsum1)

checkNumber(1234)