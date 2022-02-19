import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
sum1_fair = 0
sum2_fair = 0
draws_fair = 0
sum1_unfair = 0
sum2_unfair = 0
draws_unfair = 0

print("This is a fair game")
for x in range(100):
    pass
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        print("P2 wins!")
        sum2_fair=sum2_fair+1
    else:
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            sum1_fair=sum1_fair+1
        elif sum2>sum1:
            print("P2 wins!")
            sum2_fair=sum2_fair+1
        else:
            print("draw!")
            draws_fair=draws_fair+1

print("This is an unfair game")
tmp=0
for x in range(100):
    pass
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=10
    while sum1<16:
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        print("P2 wins!")
        sum2_unfair=sum2_unfair+1
    else:
        player2=[]
        sum2=0
        while sum2<16:
            
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures or card[0]==10:
                    if sum2>0:
                        sum2=sum2+10
                else:
                    sum2=sum2+card[0]     
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            sum1_unfair=sum1_unfair+1
        elif sum2>sum1:
            print("P2 wins!")
            sum2_unfair=sum2_unfair+1
        else:
            print("draw!")
            draws_unfair=draws_unfair+1
print("In a fair game")
print("P1 has",sum1_fair,"wins")
print("P2 has",sum2_fair,"wins")
print("There are",draws_fair,"draws")

print("In an unfair game")
print("P1 has",sum1_unfair,"wins")
print("P2 has",sum2_unfair,"wins")
print("There are",draws_unfair,"draws")
