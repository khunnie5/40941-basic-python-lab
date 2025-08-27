import random

w=input()
score=0
for x in range(100):
    tw=''
    for x in range(len(w)):
        tw+=chr(random.randint(97,122))
    score+=(w>tw)
    print(f'{w} {tw} {"bigger"*(w>tw) or "smaller"}')
print(f'score {score}/100')