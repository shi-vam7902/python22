from cmath import e

try:

    a = (int(input("Enter Number One:1")))
    b = (int(input("Enter Number One:1")))
    c = a/b
except ValueError:
    print("U cant divide the number by 0")
except Exception as e:
    print("This is the Error we want",e)

