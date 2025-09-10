import random

temp=c1=c2=score1=score2=0
contestants=[]
c=int(input())
l=int(input())
for x in range(c):
    contestants+=[[''.join(chr(random.randint(97,122)) for q in range(4)),''.join(chr(random.randint(97,122)) for q in range(l)),0]]
while len(contestants)>1:
    c1=random.randint(0,(len(contestants)-1))
    c2=random.randint(0,(len(contestants)-1))
    while c2==c1:
        c2=random.randint(0,(len(contestants)-1))
    print(f'-- fight -- contestents left: {len(contestants)} contestant: {contestants[c1][0]} deck:|{contestants[c1][1]}| victories: {contestants[c1][2]} and contestent: {contestants[c2][0]} deck:|{contestants[c2][1]}| victories: {contestants[c2][2]} --')
    score1=score2=0
    while score1==score2:
        score1=score2=0
        card1,card2=contestants[c1][1][random.randint(0,len(contestants[c1][1])-1)],contestants[c2][1][random.randint(0,len(contestants[c2][1])-1)]
        print(f'{contestants[c1][0]} chooses card |{card1}| {contestants[c2][0]} chooses card |{card2}| - {"draw"*(card1==card2) or "|"+max(card1,card2)+"| wins"}')
        if card1!=card2:
            if card1>card2:
                score1+=1
            else:
                score2+=1
        print(f'{contestants[c1][0]} flips a coin',end='')
        if random.randint(0,1):
            score1+=1
            print(' wins')
        else:
            print(' loses')
        print(f'{contestants[c2][0]} flips a coin',end='')
        if random.randint(0,1):
            score2+=1
            print(' wins')
        else:
            print(' loses')
        if contestants[c1][2]!=contestants[c2][2]:
            print(f'{contestants[(c2,c1)[contestants[c1][2]>contestants[c2][2]]][0]} has more victories than {contestants[(c1,c2)[contestants[c1][2]>contestants[c2][2]]][0]}')
            if contestants[c1][2]>contestants[c2][2]:
                score1+=1
            else:
                score2+=1
        if score1==score2:
            print(f'-- result: draw. Both won {score1} trials --')
            continue
        print(f'{(contestants[c2][0],contestants[c1][0])[score1>score2]} wins with {max(score1,score2)} trials passed. giving card |{chr(max(97,abs(ord(card1)-ord(card2))+96))}| to winner')
        contestants[c1][1]=contestants[c1][1].replace(card1,'',1)
        contestants[c2][1]=contestants[c2][1].replace(card2,'',1)
        contestants[(c2,c1)[score1>score2]][1]+=chr(max(97,abs(ord(card1)-ord(card2))+96))
        contestants[(c2,c1)[score1>score2]][2]+=1
        print(f'-- result: {contestants[c1][0]} deck:|{contestants[c1][1]}| and {contestants[c2][0]} deck:|{contestants[c2][1]}| --')
        if not len(contestants[c1][1]):
            print(contestants[c1][0],"has been elimitated")
            contestants.pop(c1)
        elif not len(contestants[c2][1]):
            print(contestants[c2][0],"has been elimitated")
            contestants.pop(c2)
        print('')
print(f'\n--finished--\nwinner: {contestants[0][0]} with deck |{contestants[0][1]}| and {contestants[0][2]} victories')
    