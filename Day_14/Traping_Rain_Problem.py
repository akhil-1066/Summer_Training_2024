nums = list(map(int,input().split()))
lmax, rmax = [0]*len(nums), [0]*len(nums)
lmax[0], rmax[-1] = nums[0], nums[-1]
for i in range(1, len(nums)):
    lmax[i] = max(lmax[i-1], nums[i])
for i in range(len(nums) - 2, - 1, -1):
    rmax[i] = max(rmax[i + 1], nums[i])
ans = 0
for i in range(1, len(nums) - 1):
    res = min(lmax[i], rmax[i]) - nums[i]
    if res > 0:
        ans += res
print(ans)