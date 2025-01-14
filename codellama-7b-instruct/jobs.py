if __name__ == '__main__':
    input = int(input())
    s = int(input())
    jobs = [[] for _ in range(input+1)]
    money = []
    for i in range(input):
        a,b = map(int,input().split())
        jobs[a].append(b)
        if b!=0:
            jobs[b].append(a)
        else:
            money.append(a)

    def dfs(jobs,money):
        for i in range(len(money)):
            if money[i]>0:
                return -1
        if len(jobs)==0:
            return 0
        profit = -99999999
        for job in jobs:
            temp_profit = dfs(jobs[:-1],money)
            if temp_profit!=-1:
                temp_profit+=job[2]
                if temp_profit>profit:
                    profit=temp_profit
        return profit

    print(dfs(jobs,money))
# Generator time: 8.2584 seconds