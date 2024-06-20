nums = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
profits = [5, 6, 5, 4, 11, 2]
ans = profits[:]
def is_possible(t1, t2):
    if t1[-1]<=t2[0]:
        return True
    return False
for i in range(1, len(nums)):
    for j in range(i):
        if is_possible(nums[j], nums[i]):
            ans[i] = max(ans[i], profits[i] + profits[j])
print(max(ans))