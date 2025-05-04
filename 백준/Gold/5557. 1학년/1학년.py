N = int(input())
nums = list(map(int, input().split()))
prevNums = [0] * 21
prevNums[nums[0]] = 1
currNums = [0] * 21

for num in nums[1:-1]:
    for idx in range(0, 21):
        cnt = prevNums[idx]
        if (0 < cnt):
            if 0 <= idx + num <= 20:
                currNums[idx + num] += cnt
            if 0 <= idx - num <= 20:
                currNums[idx - num] += cnt
    prevNums = currNums.copy()
    currNums = [0] * 21

print(prevNums[nums[-1]])