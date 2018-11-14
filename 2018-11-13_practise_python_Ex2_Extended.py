num = int(input("Please enter a number as num: "))
check = int(input("Please enter a number as check: "))
if num % check == 0:
    print("The number 'num' is a multiple of 'check' %s" % check)
else:
    print("The number 'num' is not a multiple of 'check' %s" % check)

