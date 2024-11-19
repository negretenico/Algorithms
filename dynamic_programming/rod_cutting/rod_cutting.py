from typing import List
def rod_cutting(prices:List[int],target:int):
    r = [0] * (target+1)
    for i in range(1,target+1):
        q = float('-inf')
        for j in range(1,i+1):
            q = max(q,prices[i]+r[j-i])
        r[i] = q
    return r[target]


if __name__ =="__main__":
    print(    rod_cutting([1,5,8,9,10,17,17,20,24,30],4))