# how many number are smaller than the current number


def smaller_than_current_brute_force(nums):
    ans = list()
    for num in nums:
        cnt = 0
        for j in range(len(nums)):
            if num != nums[j] and num > nums[j]:
                cnt += 1
        ans.append(cnt)
    return ans

def smaller_than_current(nums):
    temp = sorted(nums)
    seen = dict()
    ans = list()
    for i,n in enumerate(temp):
        if n not in seen:
            seen[n] = i
    
    for n in nums:
        if n in seen:
            ans.append(seen[n])
    return ans

if __name__ == '__main__':
    print(smaller_than_current([8,1,2,2,3]))
    print(smaller_than_current_brute_force([8,1,2,2,3]))