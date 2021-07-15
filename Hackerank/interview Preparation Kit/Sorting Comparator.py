class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score > b.score :
            return(1)
        elif a.score == b.score :
            if a.name == b.name :
                return(0)
            elif a.name > b.name:
                return(1)
            else :
                return(-1)
        else :
            return(-1)


# 스코어부터 비교 후에, 이름순서순으로 비교
# a>b : 1
# a=b : 0
# a<b : -1