import sys
input = sys.stdin.readline
N = int(input())

car_in = [input().strip() for _ in range(N) ]
car_out = [input().strip() for _ in range(N) ]

# 그냥 오른쪽에 자기보다 작은 녀석이 있으면 안되는것.
mapping = dict(zip(car_in, list(range(1,N+1))))
car_out_number = []
for car in car_out :
    car_out_number.append(mapping[car])
cnt = 0
for start in range(N) :
    for end in range(start+1,N) :
        if car_out_number[start] > car_out_number[end] :
            cnt += 1
            break
print(cnt)
