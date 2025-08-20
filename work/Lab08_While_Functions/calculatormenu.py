def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
answers=[]

while True:
    menu=int(input())
    match menu:
        case 1:
            answers+=[f'answer: {add(int(input()),int(input()))}']
        case 2:
            answers+=[f'answer: {sub(int(input()),int(input()))}']
        case 3:
            answers+=[f'answer: {mul(int(input()),int(input()))}']
        case 4:
            break

print(*answers,'end',sep='\n')