from collections import defaultdict
from typing import List
import sys

input = sys.stdin.readline

T = int(input().strip())



def main():
    n,k = map(int,input().split())
    times = list(map(int,input().split()))
    lists = [list(map(int,input().split())) for _ in range(k)]
    dicts = defaultdict(list)
    win_bulid = int(input().strip())
    dp = [0]*n
    for case in lists:
        dicts[case[1]].append(case[0])
    

    #print(f"times : {times}")
    print(f"dicts {dicts}")
    
    def dp(discovered:List[List[int]], sums:int = 0) -> None:
        if not(discovered[0]):
            return sums
        pos_list = discovered.pop()
        times_Table = []
            
        for pos in pos_list:
            times_Table.append(times[pos-1])
        
        #print(f"time_table {times_Table} , pos_list{pos_list}")
        sums += max(times_Table)
        #print(f"sums {sums}")
        tmp = []
        for i in pos_list:
            tmp.extend(dicts[i])
        discovered.append(list(set(tmp)))
            
        
        return dp(discovered,sums)
    
    sums = dp([[win_bulid]])
    print(sums)
    return


for _ in range(T):
    main()

