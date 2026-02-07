nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","]
ops = ["+", "-", "*", "/", "%"]

def replacecomma(num):
    result = ""
    for i in num:
        if i == ",":
            result += "."
        else:
            result += i
    return result

def delspace(num):
    result = ""
    for i in num:
        if i == " ":
            result += ""
        else:
            result += i
    return result

def calcnum(c_num):

    def checknum(num):
        num = delspace(num)
        num = replacecomma(num)
        dot_count = 0
        for i in range(len(num)):
            if num[i] == ".":
                dot_count += 1
                if dot_count > 1:
                    return 2
            if i == 0 and num[i] == "-":
                continue
            if num[i] not in nums:
                return 2
            if len(num) == 0:
                return 2
        if dot_count == 0:
            return 3
        else:
            return 1

    def checkzero(num):
        num = delspace(num)
        num = replacecomma(num)
        if num[0] in "-.,":
            num = num[1:]
        if len(num) > 1 and num[0] == "0":
            i = 0
            while i < len(num) and num[i] == "0":
                i += 1
            if num[i-1] == "0" and num[i-2] == "0":
                return 2
            if i == len(num):
                return 3
            if num[i] in ".,":
                return 1
            if num[i] not in nums and ",.":
                return 3
            return 3
        return 1

    def errorcode(num):
        num = delspace(num)
        if num == " " or num == "":
            print("Empty input")
            return False
        if checknum(num) == 2 and checkzero(num) == 3:
            print(f"Input is not a number and starts with zero ({num})")
            return False
        elif checknum(num) == 2 and checkzero(num) == 2:
            print(f"Input is not a number and starts with multiple zeros ({num})")
            return False
        elif (checknum(num) == 1 or checknum(num) == 3) and checkzero(num) == 3:
            print(f"Number cannot start with zero ({num})")
            return False
        elif (checknum(num) == 1 or checknum(num) == 3) and checkzero(num) == 2:
            print(f"Number cannot start with multiple zeros ({num})")
            return False
        elif checknum(num) == 2 and checkzero(num) == 1:
            print(f"Input is not a number ({num})")
            return False
        return True

    def tofloat(num):
        if errorcode(num):
            num = delspace(num)
            num = replacecomma(num)
            if checknum(num) == 3:
                num = int(num)
            else:
                num = float(num)
            return num
        return False
    if tofloat(c_num) is False:
        return False
    return tofloat(delspace(replacecomma(c_num)))

def checkop(op):
    if delspace(op) in ops:
        return True
    else:
        print("Invalid operation (Only +, -, *, /, %)")
        return False

def accept(ans):
    if ans in "Yy":
        return "y"
    if ans in "Nn":
        print("Try again")
        return "n"
    return False

def do_op(op):
        if op == "+":
            print(f"Result: {calcnum(num1) + calcnum(num2)}")
        elif op == "-":
            print(f"Result: {calcnum(num1) - calcnum(num2)}")
        elif op == "*":
            print(f"Result: {calcnum(num1) * calcnum(num2)}")
        elif op == "/":
            print(f"Result: {calcnum(num1) / calcnum(num2)}")
        elif op == "%":
            print(f"Result: {calcnum(num1) % calcnum(num2)}")
        else:
            print("Numbers are incorrect")

while True:
    num1 = input("First number - ")
    while calcnum(num1) is False:
        num1 = input("First number - ")
    print(f"First number is {calcnum(num1)}")
    num2 = input("Second number - ")
    while calcnum(num2) is False:
        num2 = input("Second number - ")
    print(f"Second number is {calcnum(num2)}")
    op1 = input("Operation - ")
    if calcnum(num2) == 0 and op1 == "/":
        print("Cannot divide by zero")
        continue
    else:
        while not checkop(op1):
            op1 = delspace(input("Operation - "))
        print(f"Operation is {delspace(op1)}")
        temp = accept(input(f"Calculate {calcnum(num1)} {delspace(op1)} {calcnum(num2)}? (y/n) "))
        while not temp in ["y", "n"]:
            temp = accept(input("y or n "))
        if temp == "y":
            do_op(op1)
        elif temp == "n":
            continue