import itertools as it

def fct(x):
    val = 1
    for i in range(1,x+1):
        val = val * i
    return(val)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a,b = map(int,input().strip().split())
        v = fct(b) / (fct(a) * fct(b-a))
        print(int(v))
