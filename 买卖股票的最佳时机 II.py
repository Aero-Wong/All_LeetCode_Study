
def main():
    #prices = [7,1,5,3,6,4]
    #prices = [1,2,3,4,5]
    #prices = [7,6,4,3,1]
    prices = [6,1,3,2,4,7]

"""
    earn = money = 0
    tmp = 1
    up = down = 0

    for i in range(1,len(prices)):
        if(prices[i] > prices[i-1]):
            down += 1
        if(prices[i] < prices[i-1]):
            up += 1
        else: 
            up += 0
            down += 0
    print(up,down)
                
    if(down < 4 and up < 4):
        if(prices[0] == 1):
            earn = prices[0]
            tmp = tmp * -1
            up -= 1
        for j in range(1,len(prices)):
            if(prices[j] < prices[j-1]):
                if(tmp == 1 and down > 0):
                    money = money + prices[j]
                    tmp = tmp * -1
                    up -= 1
                    print(money,tmp,down,up)
            if(prices[j] > prices[j-1]):
                if(tmp == -1 and up > 0):
                    money = prices[j] - money
                    earn = earn + money
                    money = 0
                    tmp = tmp * -1
                    down -= 1
                    print(earn,money,tmp,down,up)

    if(down >= 4 and up == 0):
        earn = prices[4] - prices[0]
        
    if(down == 0 and up >= 4):
        earn = 0
            
    print(earn)
 
 """

    earn = 0
    money = 0
    tmp = 1
    ups = []
    downs = []
    upsum = 0
    downsum = 0

    if(prices[0] > prices[1]):
        ups.append(prices[0])
    else:
        downs.append(prices[0])

    for i in range(1,len(prices)):
        if(prices[i] < prices[i-1]):
            if(len(ups) >= 0):
                ups.append(prices[i])
                tmp = tmp * -1
                print(ups)
        if(prices[i] > prices[i-1]):
            if(len(downs) >= 0):
                downs.append(prices[i])
                print(downs)
    
    if(len(downs)>=0 and len(ups)>=0):
        for u in range(len(ups)):
            a = int(ups[u])
            upsum = upsum + a
        for d in range(len(downs)):
            b = int(downs[d])
            downsum = downsum + b
        earn = downsum - upsum
    print(earn)

 
if __name__ == '__main__':
    main()
    