a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b = []
c = [1]
d = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
e = [1, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 6, 1]
f = [1, 1, 1, 1, 2]
#can easily return all matches by adding each match into an array and returning the array at the end
def findNumber(arr, number):
    n = 1
    ans = "number not in array" # number not found response, to be changed into the match in case it is found
    if len(arr) == 0:
        return "array is empty"
    elif len(arr) == 1:
        if arr[0] == number:
            return 0
        else:
            return ans

    #will check every 2
    while True:
        if arr[n-1] == number:
            ans = n-1
            return ans
        elif arr[n] == number:
            ans = n
            return ans
        elif arr[n+1] == number:
            ans = n+1
            return ans
        if n == len(arr)-2:
            break
        n += 3
    return ans

tests = [a, b, c, d, e, f]
for x in tests:
    control = 2
    print(f"testing now for the array {x}")
    print(f"the array length is {len(f)}")
    if type(findNumber(f, control)) == int:
        print(f"the first number 2 is in the place number {findNumber(f, control)}")
        print(f"check that the place {findNumber(f, control)} contains the correct number: {f[findNumber(f, control)]}")
    else:
        print(findNumber(f, control))