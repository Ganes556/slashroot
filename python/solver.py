from math import floor
import os
import hashlib
import struct
import random, time
import base64
import z3

# t= time.time()
# random.seed(26975)
# print(random.random())

# seed = time.time()

# for i in range(5):
#     r = int.from_bytes(struct.pack('>d',seed),'big')
#     c = (r >> 3) * (2**-53)
#     print(c)
#     seed +=1
# 65.84670147691094  * (2**-53)

# float(str(time.time())[::-1])

# int.from_bytes(struct.pack('>d',seed),'big')

# print(struct.pack('>Q',rd))
# print(rr)
# exit()
# t = round(time.time())
# t = 1661389188
# t = 1631309180
t = 1661248284
# t = 1612543588
# t = round(float(str(time.time())[::-1]))

rand = os.urandom(7)
num = int.from_bytes(rand, 'big')
num2 = num + t
num_shiff = (num2) >> 3
a = (num_shiff) * 2**-53

e = base64.b64encode(struct.pack('d',a)) # cookie

def compare(e,times): # hidden
    e = struct.unpack('d',base64.b64decode(e))[0]

    int_urandom = int((e*2**53 * pow(2,3)) * pow(2,-3) * pow(2,3))
    # int_urandom = (((int(e*2**53) << 3) >> 3) << 3)

    # int_shiff = ((int(e*2**53) << 3) >> 3)

    # int_urandom -= times

    # print(int_urandom , num2)
    # print(int_shiff, num_shiff)
    # print(bin(int_urandom))
    # print(bin(num2))

    for i in range(0,8):
        gues_num = (int_urandom | i)-times
        if  gues_num == num:
            return gues_num

    
    # print(bin(int_urandom>>7))
    # print(bin(num>>7))
    # print(bin(int_urandom | num)
    # print((int_urandom >> 4) << 4,(num >> 4) << 4)
    # return int_urandom >> 4
    # << 3

    # if num2 >> 4 == int_urandom >> 4:
        
    # print(num,int_urandom)

    # t2 = round(time.time())
    # while 1:
    #     d = int_urandom - t2
    #     # if struct.pack('>Q',d)[1:-1] == rand[:-1]:
    #     if struct.pack('>Q',d)[1:] == rand:
    #         print(t2)
    #         break
    #     print(t2)
    #     t2 -=1
    #  [1:-1]  
    # return struct.pack('>Q',int_urandom)[1:-1] == rand[:-1]
        # print(struct.pack('>Q',int_urandom),rand)
        # return struct.pack('>Q',int_urandom)[1:-1]

def brute(e):
    52742816619857977
    e = struct.unpack('d',base64.b64decode(e))[0]
    # int_urandom = int((e*2**53 * pow(2,3)) * pow(2,-3) * pow(2,3))
    int_urandom = ((int(e*2**53) << 3) >> 3) << 3    
    print(bin(69746440148179339))
    g = []
    for i in range(0,8):
        gues_num = (int_urandom | i)
        print(bin(gues_num))
    exit()
    t_gues = round(time.time())
    g = []
    while 1:
        if len(g) >= 8:
            break
        for i in range(0,8):
            gues_num = (int_urandom | i)-t_gues
            if  gues_num == num:
                g.append([gues_num,t_gues])
        t_gues -=1
    return g
        # print(t_gues)
    # int_urandom -= times

# for i in range(0,100):

rand = os.urandom(7)
num = int.from_bytes(rand, 'big')
num2 = num + t
num_shiff = (num2) >> 3
a = (num_shiff) * 2**-53
brute('eGQNnkD57j8=')
# print(, t)

