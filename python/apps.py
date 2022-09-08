import random,time
class PRNG:
    seed = 0
    def __init__(self, seed):
        self.seed = seed

    def Next(self):
        a = self.seed * 15485863
        self.seed +=1
        return (a * a * a % 2038074743) / 2038074743

t = round(float(str(time.time()).split('.')[1]))
# print(t)
# exit()
a = PRNG(t)


# random.seed(a.Next())
# print(a.Next())
# print(t)


# 5184121
# 
# c = [3, 6, 3, 6, 5, 3, 2, 2, 6, 6, 2, 6, 1, 7, 7, 1, 3, 2, 1, 2]

c = [round(a.Next()*10) for i in range(20)]

# exit()
# exit()
# c = []
# for i in range(5):
#     c.append(a.Next())

bf = time.time()
for seed in range(99999,9999999):
    b = PRNG(seed)
    get = 0
    # random.seed(b.Next())
    for i in range(len(c)):
        if(round(b.Next()*10) == c[i]):
            get = 1
            continue
        else:
            get = 0
            break
    if get:
        print(seed)
        print(time.time() - bf)
        break
    print(seed)
    
    # if (seed * 15485863) * (seed * 15485863) * (seed * 15485863)  %  2038074743 == c[0]* 2038074743:
    #     print(seed)
    #     break
    