# class Solution(object):
#     def intToRoman(self, num):
#         criterion = ['','1','11','111','12','2','21','211','2111','13']
#         num_ = list (map(str, list(range(0,10))))
#         num = str(num)
#
#         ans = []
#         for i in criterion :
#             i = i.replace('1','I')
#             i = i.replace('2','V')
#             i = i.replace('3','X')
#             ans.append(i)
#         dic1 = dict(list(zip(num_,ans)))
#
#         ans = []
#         for i in criterion :
#             i = i.replace('1','X')
#             i = i.replace('2','L')
#             i = i.replace('3','C')
#             ans.append(i)
#         dic2 = dict(list(zip(num_,ans)))
#
#         ans = []
#         for i in criterion :
#             i = i.replace('1','C')
#             i = i.replace('2','D')
#             i = i.replace('3','M')
#             ans.append(i)
#         dic3 = dict(list(zip(num_,ans)))
#
#         ans = []
#         for i in criterion :
#             i = i.replace('1','M')
#             i = i.replace('2','M')
#             i = i.replace('3','M')
#             ans.append(i)
#         dic4 = dict(list(zip(num_,ans)))
#         lst_dic = [dic4,dic3,dic2,dic1]
#
#         num = num.zfill(4)
#         lst = list(num)
#         strng = ''
#         for i,v in enumerate(lst) :
#             strng += lst_dic[i][v]
#         return(strng)

# 다른 방법으로 구현하기

class Solution(object):
    def intToRoman(self, num):
        transform ={1000:'M',900:'CM',500:'D',400:'CD',100:'C',
                    90:'XC',50:'L',40:'XL',10:'X',
                    9:'IX',5:'V',4:'IV',1:'I'}
        ans = ''
        for v,s in transform.items() :
            while num - v >= 0 :
                num = num - v
                ans += s
            if num == 0 :
                break
        return(ans)
