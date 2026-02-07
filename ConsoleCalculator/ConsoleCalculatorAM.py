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
            print("Դատարկ դաշտ")
            return False
        if checknum(num) == 2 and checkzero(num) == 3:
            print(f"Մութքագրվածը թիվ չէ և սկսվում է զրոյով ({num})")
            return False
        elif checknum(num) == 2 and checkzero(num) == 2:
            print(f"Մութքագրվածը թիվ չէ և սկսվում է զրոներով ({num})")
            return False
        elif (checknum(num) == 1 or checknum(num) == 3) and checkzero(num) == 3:
            print(f"թիվը չպետք է սկսի զրոյով ({num})")
            return False
        elif (checknum(num) == 1 or checknum(num) == 3) and checkzero(num) == 2:
            print(f"թիվը չպետք է սկսի զրոներով ({num})")
            return False
        elif checknum(num) == 2 and checkzero(num) == 1:
            print(f"Մութքագրվածը թիվ չէ ({num})")
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
        print("Գործողությունը սխալ է (Միայն +, -, *, /, %)")
        return False

def accept(ans):
    if ans in "Yy":
        return "y"
    if ans in "Nn":
        print("Նորից փորձեք")
        return "n"
    return False

def do_op(op):
        if op == "+":
            print(f"Պատասխանը՝ {calcnum(num1) + calcnum(num2)}")
        elif op == "-":
            print(f"Պատասխանը՝ {calcnum(num1) - calcnum(num2)}")
        elif op == "*":
            print(f"Պատասխանը՝ {calcnum(num1) * calcnum(num2)}")
        elif op == "/":
            print(f"Պատասխանը՝ {calcnum(num1) / calcnum(num2)}")
        elif op == "%":
            print(f"Պատասխանը՝ {calcnum(num1) % calcnum(num2)}")
        else:
            print("Թվանշանները սխալ են")

while True:
    num1 = input("Առաջին թվանշան - ")
    while calcnum(num1) is False:
        num1 = input("Առաջին թվանշան - ")
    print(f"Առաջին թվանշանը {calcnum(num1)} է")
    num2 = input("Երկրորդ թվանշան - ")
    while calcnum(num2) is False:
        num2 = input("Երկրորդ թվանշան - ")
    print(f"Երկրորդ թվանշանը {calcnum(num2)} է")
    op1 = input("Գործողություն - ")
    if calcnum(num2) == 0 and op1 == "/":
        print("զրոյի վրա չեն բաժանում")
        continue
    else:
        while not checkop(op1):
            op1 = delspace(input("Գործողություն - "))
        print(f"Գործողությունը {delspace(op1)} է")
        temp = accept(input(f"Հաշվե՞լ {calcnum(num1)} {delspace(op1)} {calcnum(num2)} (y/n) "))
        while not temp in ["y", "n"]:
            temp = accept(input("y կամ n "))
        if temp == "y":
            do_op(op1)
        elif temp == "n":
            continue