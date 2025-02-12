# Get Missing Number From the Give Array
Cases = [
    [3,0,1],
    [0,1],
    [9,6,4,2,3,5,7,0,1]
]

def get_missing_no(nums):
    return sum(range(len(nums)+1)) - sum(nums)

def main():
    for case in Cases:
        ans = get_missing_no(case)
        print(
            f'For array {case} the missing no is {ans}'
        )
    
if __name__ == '__main__':
    main()