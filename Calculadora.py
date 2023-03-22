a=int(input())    #calculadora
b=int(input())

print(a*b)

all_ops = ["*", "/", "+", "-"]
if operation in all_ops:
    print(eval(str(first_num) + operation + str(second_num)))