def get_spiral_matrix(nums:list):
    ans = list()
    while nums:
        if nums and nums[0]:
            ans += nums.pop(0)
        
        if nums and nums[0]:
            for row in nums:
                ans.append(row.pop())
        if nums:
            ans += nums.pop()[::-1]
        
        if nums and nums[0]:
            for row in nums[::-1]:
                ans.append(row.pop(0))
    return ans


def main():
    ip = [[1,2,3,4], [5,6, 7, 8], [9, 10, 11, 12]]

    print(get_spiral_matrix(ip))
    

if __name__ == '__main__':
    main()