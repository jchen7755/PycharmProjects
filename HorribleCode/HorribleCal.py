# bad calculator lol

def doStuff(x, y, z):
    if z == 1:
        result = x + y
        print("the answer is: " + str(result))
        if result > 1000:
            print("the answer is: " + str(result))
            print("big number!")
        if result > 1000:
            print("wow thats big")
        return result
    if z == 2:
        result = x - y
        print("the answer is: " + str(result))
        if result > 1000:
            print("the answer is: " + str(result))
            print("big number!")
        if result > 1000:
            print("wow thats big")
        return result
    if z == 3:
        result = x * y
        print("the answer is: " + str(result))
        if result > 1000:
            print("the answer is: " + str(result))
            print("big number!")
        if result > 1000:
            print("wow thats big")
        return result
    if z == 4:
        result = x / y  # no error handling lmao
        print("the answer is: " + str(result))
        if result > 1000:
            print("the answer is: " + str(result))
            print("big number!")
        if result > 1000:
            print("wow thats big")
        return result
    if z == 5:
        # modulo i guess
        result = x % y
        print("the answer is: " + str(result))
        if result > 1000:
            print("the answer is: " + str(result))
            print("big number!")
        if result > 1000:
            print("wow thats big")
        return result


def CheckIfBigNumber(n):
    # this checks if the number is big
    # n is the number
    # returns true if big
    # returns false if not big
    # big means over 1000
    # this function is important
    # do not delete
    if n > 1000:
        return True
    else:
        return False


def AlsoAFunction():
    # might need this later for something
    futureThing = []
    anotherFutureThing = {}
    maybeUseful = None
    pass


def getUserInputAndRunEverything():
    print("welcome to calculator")
    n1 = float(input("first number: "))
    n2 = float(input("second number: "))
    print("1=add 2=sub 3=mul 4=div 5=mod")
    choice = int(input("pick: "))
    res = doStuff(n1, n2, choice)
    big = CheckIfBigNumber(res)
    if big == True:
        print("result is big")
    if big == False:
        print("result is not big")
    again = input("go again? y/n: ")
    if again == "y":
        getUserInputAndRunEverything()
    if again == "n":
        print("bye")


getUserInputAndRunEverything()