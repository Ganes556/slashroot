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

ea = base64.b64encode(struct.pack('d',a)) # cookie

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

    # e = struct.unpack('d',base64.b64decode(e))[0]
    e = base64.b64decode(e)

    e2 = int.from_bytes(b'\x00\x00\x00\x03','big')
    
    # int.from_bytes(e,'big')

    print(e2,e2.to_bytes((e2.bit_length() +7)//8,'big'))
    exit()
    # int_urandom = int((e*2**53 * pow(2,3)) * pow(2,-3) * pow(2,3))
    int_urandom = ((int(e*2**53) << 3) >> 3) << 3
    print(int_urandom)
    print(bin(36518736728911234))
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

print(brute(ea))

# print(compare(e,t))

# def generate_seed():
#     random.seed(num)
#     return struct.pack('d',random.random())


# e = struct.unpack('d',base64.b64decode(e))[0]
# print(convert_to_rand(e,t),rand[:-1])
# print(struct.unpack('d',base64.b64decode(e))[0])
# print(e)
#  == rand[:-1]
# if(compare(e,t)):
#     # rand[:-1]
#     random.seed(generate_seed(), version=2)
#     print(random.randint(1,99))

# if(convert_to_rand(e,t) == rand[:-1]):
#     random.seed(rand[:-1], version=2)
#     print(random.randint(1,99))




# for x in range(9999999999999999,99999999999999999):
    # solver = z3.Solver()
    # t2, x = z3.Ints('t2 x')
    # print(num)
    # y = z3.Int2BV(x + t2,64)
    # solver.add(z3.LShR(y,3) == e / 2**-53)
    # solver.add(int(e*2**53) << 3)
    # solver.add(x < 999999999999999)
    # solver.add(x > 9999999999999999)
    # solver.add(t2 > 999999999)
    # solver.add(t2 < 99999999999)
       # c = (x + t2) >> 3 == e / 2**-53
    #     print(x)
    # if solver.check() == z3.sat:
    #     c = solver.model().evaluate(t2).as_long()
        # if struct.pack('>Q',c)[1:-1] == rand[:-1]:
        #     print(x)
            # break
        # print(c)
            # x -=1
            
        # print(c, num)


    # x = z3.BitVec('x',64)
    # y = z3.LShR(x,3)
    # solver.add(y == e / 2**-53 )

    # if solver.check() == z3.sat:
    #     # print(num)
    #     int_urandom = solver.model().evaluate(x).as_long()
    #     t2 = round(time.time())

        # while 1:
        #     struct

# for i in range(5):    
#     print(random.randint(1,10))




# get_random = (int_urandom >> 3) * 2**-53
# print(a,get_random)

# print(a)
# print(get_random)
# solver = z3.Solver()


# print(a,rd)
# x = z3.BitVec('x',64)

# y = z3.LShR(x,3) 
# solver.add(y  == a / 2**-53 )

# if solver.check() == z3.sat:
#     solver.model()


# rand = int.from_bytes(m, 'big')
# c = (m >> 3) * 2**-53
# print(c)
# print(struct.unpack('>d',struct.pack('>Q',m)))


# class PRNG:
#     seed = 0
#     def __init__(self, seed):
#         self.seed = seed

#     def Next(self):
#         a = self.seed * 15485863
#         self.seed +=1
#         return (a * a * a % 2038074743) / 2038074743

# t = round(float(str(time.time())[::-1]))
# a = PRNG(t)
# c = []
# for i in range(5):
#     c.append(a.Next())

# for seed in range(99999,9999999):
#     if (seed * 15485863) * (seed * 15485863) * (seed * 15485863)  %  2038074743 == c[0]* 2038074743:
#         print(seed)
#         break

# solver = z3.Solver()

# seed = z3.Int('seed')
# seed = z3.Int('seed')

# solver.add((seed * 15485863) * (seed * 15485863) * (seed * 15485863)  %  2038074743 == 1247767213)

# solver.add(seed > 3000000)
# solver.add(seed < 9999999)

# if solver.check() == z3.sat:
#     print(solver.model().evaluate(seed))