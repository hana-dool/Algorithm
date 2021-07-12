exception = ('-', '_', '.')


def solution(new_id):
    new_id_1 = new_id.lower()
    # print(new_id_1)

    new_id_2 = ''
    for i in new_id_1:
        if i.isalnum():
            new_id_2 = new_id_2 + i
        elif i in exception:
            new_id_2 = new_id_2 + i
    # print(new_id_2)
    while new_id_2.find('..') != -1:
        new_id_2 = new_id_2.replace('..', '.')

    new_id_3 = new_id_2
    # print(new_id_3)

    if new_id_3 == '.':
        new_id_3 = ''
    else:
        if new_id_3[0] == '.':
            new_id_3 = new_id_3[1:]
        if new_id_3[-1] == '.':
            new_id_3 = new_id_3[:-1]
    new_id_4 = new_id_3
    # print(new_id_4)

    if new_id_4 == '':
        new_id_4 = 'a'
    new_id_5 = new_id_4
    # print(new_id_5)

    if len(new_id_5) >= 16:
        new_id_5 = new_id_5[:15]
    if new_id_5[0] == '.':
        new_id_5 = new_id_5[1:]
    if new_id_5[-1] == '.':
        new_id_5 = new_id_5[:-1]
    new_id_6 = new_id_5
    # print(new_id_6)

    new_id_7 = new_id_6
    while len(new_id_7) <= 2:
        new_id_7 = new_id_7 + new_id_7[-1]
    # print(new_id_7)

    answer = new_id_7
    return answer