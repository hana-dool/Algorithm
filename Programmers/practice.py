lst = [1,2,3,3,3,3,4,4,5,6,7]
xx = 2.5
start = 0
end = len(lst) - 1

while start <= end: # start 가 선 넘을떄 정지
    mid = (start + end) // 2
    if lst[mid] == xx: # 이 경우 같다 하더라도 올라가는게 핵심
        end = mid - 1
    elif lst[mid] < xx:
        start = mid + 1  # 같은것 찾아!
    elif lst[mid] > xx:
        end = mid - 1   # 같은것 찾아!
# end 가 멈춰서서, start 가 맞춰주는 느낌이네요. 그러므로 end를 출력하는게 맞죠 (start 가 변하다가 end를 넘어버릴떄 중지하니까요)
print(start) # end 가 선 넘었다는건? start 가 맞다는거.
print(end)
