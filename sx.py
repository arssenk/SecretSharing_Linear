# def perebir(lst):
#     a = []
#     for i in range(len(lst)- 2):
#         for j in range(i+1, len(lst) -1):
#             for k in range(j+1, len(lst)):
#                 a.append([lst[i], lst[j], lst[k]])
#     print(a)
# perebir([1,2,3,4,5])
import binascii
import time
start = time.time()
a = [i for i in range(10000000)]
this = time.time() - start
print(this)
print(chr(int('01001000' ,2)))

# b =binascii.a2b_qp(a)
# print(b)
# print(len('0110100001100101011011000110110001101111'))