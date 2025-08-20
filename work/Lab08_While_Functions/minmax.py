M='empty'
m='empty'
while True:
    inputs=input()
    if (inputs=='end'):
        break
    M=int(inputs)*(M=='empty')or max(M,int(inputs))
    m=int(inputs)*(m=='empty')or min(M,int(inputs))
print(f'max: {M}\nmin: {m}')