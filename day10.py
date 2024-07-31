# Project Day 10 - Function calculator
## combining dictionaries and function
def add(a,b) :
    return a+b
def multiply(a,b) :
    return a*b
def minus (a,b) :
    return a - b
def divide (a,b) :
    return a/b


"""Input terus menerus tetapi operasi terakhir yang dijadikan first number kalau continue"""
operators = {"+" : add,
                    "-" :minus,
                    "/" : divide,
                    "*" : multiply}

text = int(input("""What's the first number?\n + \n - \n * \n /"""))
first_digit = text
print(f"first num : {first_digit}")
while True : 
    text2 = "Pick an operation"
    print(text2)
    operator = str(input())
    second_digit = int(input("Enter second number"))
    print(f"second num is  : {second_digit}")

    """Akses fungsi pada dictionaries"""

    operasi = operators[operator]
    answer = operasi(first_digit,second_digit)
    print(f"your first operation is {answer}")
    while True :
        ask = str(input("Want to continue? y/n"))
        if ask == "y" :
            second_digit = (input("What's the next number"))
            operator2 = str(input("pick an operation"))
            first_digit=answer
            operasi2 = operators[operator2]
            answer = operasi2(int(answer),int(second_digit))
            print(f"your next equation is = {answer}") 
        # elif  second_digit == "n" or ask == "n"  : #breaknya masih kurang efisien
        #     break
        else :
            break
    break
    


    

