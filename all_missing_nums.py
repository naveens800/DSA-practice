Cases = [
    [4,3,2,7,8,2,3,1],
    [1,1]
]

def get_all_missing_no(nums):
    miss = []
    for i in range(1, len(nums)+1):
        if i not in nums:
            miss.append(i)
    return miss


def main():
    for case in Cases:
        ans = get_all_missing_no(case)
        print(
            f'For array {case} the missing nums are {ans}'
        )
    
if __name__ == '__main__':
    main()