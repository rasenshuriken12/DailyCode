class Solution:
    def minCost(self, heights, cost):
        from collections import defaultdict
        hc=defaultdict(int)
        for h,c in sorted(zip(heights,cost)):
            hc[h]+=c
        sweep_lr=defaultdict(int)
        lst=list(hc)
        totcost=0
        prv=lst[0]
        for h in lst:
            sweep_lr[h]+=totcost*(h-prv)+sweep_lr[prv]
            prv=h
            totcost+=hc[h]
        mn=float('inf')
        sweep_rl=defaultdict(int)
        totcost=0
        prv=lst[-1]
        for h in lst[::-1]:
            sweep_rl[h]+=totcost*(prv-h)+sweep_rl[prv]
            mn=min(mn,sweep_lr[h]+sweep_rl[h])
            prv=h
            totcost+=hc[h]
        return mn