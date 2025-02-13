

def two_sum_brute_force(nums, t):
    for i in range(len(nums)-1):
        for j in  range(i+1, len(nums)):
            if nums[i] + nums[j] == t:
                return [nums[i], nums[j]]

def two_sum(nums, t):
    seen = set()
    for n in nums:
        second = t - n
        if second in seen:
            return n, second
        else:
            seen.add(n)
    

if __name__ == '__main__':
    print(two_sum_brute_force([2,11,7,15], 9))
    print(two_sum([2,11,7,15],9))