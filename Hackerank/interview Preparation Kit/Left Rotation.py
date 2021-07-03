first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

a = list(map(int, input().rstrip().split()))

def rotLeft(a, d):
    r = a[:d]
    l = a[d:]
    return(l+r)

result = rotLeft(a, d)
print(result)

