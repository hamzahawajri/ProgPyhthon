print("============== calculator program ==============")

num1 = input("Enter number one : ")

if num1.isdigit():
    print("choose operation" ,'\n'
          "  1_  +",'\n'
          "  2_  -",'\n'
          "  3_  *",'\n'
          "  4_  /",'\n'
          "  5_  ^",'\n'
          "  6_  %")
    print("========================")
op = input("Enter operation : ")

if op == '1' or op == '+':
    num2 = input("Enter number two : ")
    if num2.isdigit():
        result = int(num1) + int(num2)
        print('The Result is ',result)
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("umber without a decimal point " , b)
        if cho == '3':
            exit()


if op == '2' or op == '-':
    num2 = input("Enter number two :")
    if num2.isdigit():
        result = int(num1) - int(num2)
        print('The Result is ',result)
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("umber without a decimal point " , b)
        if cho == '3':
            exit()

if op == '3' or op == '*':
    num2 = input("Enter number two :")
    if num2.isdigit():
        result = int(num1) * int(num2)
        print('The Result is ',result)
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("number without a decimal point " , b)
        if cho == '3':
            exit()

if op == '4' or op == '/':
    num2 = input("Enter number two :")
    if num2.isdigit():
        result = int(num1) / int(num2)
        print('The Result is ',result)
        print("================================")
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("number without a decimal point " , b)
        if cho == '3':
            exit()

if op == '5' or op == '^':
    num2 = input("Enter number two :")
    if num2.isdigit():
        result = int(num1) ^ int(num2)
        print('The Result is ',result)
        print("================================")
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("number without a decimal point " , b)
        if cho == '3':
            exit()

if op == '6' or op == '%':
    num2 = input("Enter number two :")
    if num2.isdigit():
        result = int(num1) % int(num2)
        print('The Result is ',result)
        print("================================")
        print("1_  Zoom number",'\n'
              "2_  Take the number without a decimal point",'\n'
              "3_  Exit")
        cho = input("Choose the process you want : ")
        if cho == '1':
            a = int(result-0.5)+1
            print("zoom number",a)
        if cho == '2':
            b = int(result)
            print("number without a decimal point " , b)
        if cho == '3':
            exit()
