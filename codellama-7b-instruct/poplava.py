if __name__ == '__main__':
    n, x = [int(i) for i in input().split()]
    
    if n % 2 == 0:
        print(-1)
        exit(0)
    
    odd_nums = list(range(1, n + 1))
    odd_nums.sort()
    odd_nums = odd_nums[::-1]
    
    if x % 2 == 0:
        print(-1)
        exit(0)
    
    nums = []
    for i in range(n // 2):
        nums.append(odd_nums[i])
        nums.append(odd_nums[- i - 1])
    
    if sum(nums) == x:
        print(*nums, sep=' ')
    else:
        print(-1)
# Generator time: 8.6475 seconds