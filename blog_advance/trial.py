# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         self.__init__()
#
#         listed = str(self.x).split()
#         print(listed)
#
#
# Solution.reverse(123)

def rever(x):
    listed = list(str(x))
    leng = len(listed)-1
    # print(listed)
    new_list = []
    for num in listed:
        new_list.append(num[leng - listed.index(num)])
        print(num)
    print(new_list)


rever(123)


