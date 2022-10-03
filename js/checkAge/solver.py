import jwt

a = 1664599675820+1664599602000

e = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiZ3Vlc3MiLCJpZCI6ImQzMGY2ZjgwLTYxMDItNGU5Zi05Njc4LThmZmM4ZmJmMmM4ZiIsImlhdCI6MTY2NDY5NDM3OX0.QnDA112AxPl5yvhf82F_Jmh-JtbmaE3i159s3gKOvXo"

# c = 3327678363361
# jwt.decode(e,str(3327678363361),algorithms='HS256')
# 3327680117474
while 1:
    try:
        d = jwt.decode(e, str(a), algorithm='HS256')
        print("kena",a)
        exit()
    except jwt.InvalidTokenError:
        print("error",a)
        a -=1
        pass

    # if a == e:
    #     print(a)
    #     break
    # a-=1
# "xxx"

