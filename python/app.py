import random, time
import datetime
from randcrack import RandCrack
import hashlib
from base64 import encode, decode
# import z3

# rc = RandCrack()
# e = hashlib.sha256(str(random.randint(6666,999999)).encode()).hexdigest()

s = b'slashroot6'
d = []

for i in range(len(s)):
    random.seed()
    # t = round(time.time()) ^ random.randint() + i
    # print(t)
    # random.seed(t)
    c = random.randint(1, 9999)
    d.append(c)
    # print(c)
print(d)

# class PRNG:
#     seed = 0
#     def __init__(self, seed):
#         self.seed = seed
#     # def Seed(self):        
#     #     a = self.seed * 15485863
#     #     return (a * a * a % 2038074743) / 2038074743
    

#     def Next(self):
#         a = self.seed * 15485863
#         self.seed +=1
#         return (a * a * a % 2038074743) / 2038074743

# # a = PRNG(time.time())

# o = [0.7927972279260562,
# 0.07402458284059632,
# 0.3048789836731809,
# 0.7022481126845158
# ]
# 0.8701894688953316
# # 1661234346
# # a = PRNG(c)
# for i in range(5):
#     c = random.random()
#     print(c)
    # o.append(a.Next())
# print(o,c)



# x = time.time()
# while 1:        
#     random.seed(x)
#     loop = 0
#     if random.random() == o[0]:
#         print(x)
#         break
#     else:
#         print(x)
#         x -= 1
# while 1:        
#     random.seed(x)
#     loop = 0
#     for i in range(len(o)):
#         rand = random.random()
#         if  rand== o[i]:
#             loop = 0
#             continue
#         else:      
#             loop = 1  
#             break
#     if loop:
#         x -=1
#     else:
#         print(x)
#         break


# while 1:
#     results = []
#     # print(results)
#     for i in range(5):
#         a= (c+i) * 15485863
#         result = (a * a * a % 2038074743) / 2038074743
#         results.append(result)
#     if results == o:
#         print(c)
#         break
#     else:
#         c -=1
#         print(results)
#         continue

# a = PRNG(round(time.time()))

# for i in range(5):
#     print(round((a.Next() * 10)))

















# old = [10,
# 6,
# 6,
# 5,
# 10,]

# c = time.time()

# while 1:
#     news = []
#     for i in range(5):
#         random.seed(c+i)
#         news.append(random.randint(1,10))
#     if news == old:
#         print(c)
#         break
#     else: 
#         c -= 1
#         news.clear()
#         continue

# for i in range(5):
#     random.seed(1660996841.7247052 + i)
#     print(random.randint(1,10))
