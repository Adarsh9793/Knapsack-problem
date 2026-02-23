# This problem is Knapsack under recurssion 

def solve(weight , value , currW , currI):

    if currI == 0 or currW == 0:
        return 0
    
    if currW < weight[currI-1]:
        currI-=1
        return solve(weight , value , currW , currI)
    
    currI-=1
    return max(value[currI] + solve(weight , value , currW - weight[currI] , currI) , solve(weight , value , currW , currI))

def knapsack(totalW , weight , value):
    ans = solve(weight , value , totalW , len(weight))
    return ans

weight = [1,2,3]
value = [6,10,12]
targetW = 5
print(knapsack(targetW , weight , value))