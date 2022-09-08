import random, time
tt = [1661248367,
1661248369,
1661248383,
1661248362,
1661248368,
1661248363,
1661248361,
1661248362,
1661248352,
1661248291]
e = [7418, 5631, 6888, 2451, 6560, 194, 4466, 3420, 3156, 1832]
s = b'slashroot6'

# x = 1661248284    
x = time.time()
while 1:        
    loop = 0
    for i in range(len(e)):
        random.seed(x)
        rand = random.randint(1, 9999)
        if  rand== e[i]:
            loop = 0
            continue
        else:      
            loop = 1  
            break
    if loop:
        x -=1
        # print(x)
    else:
        print(x)
        break
    
# while 1:        
#     loop = 0
#     for i in range(len(e)):
#         random.seed(x ^ s[i] + i)
#         rand = random.randint(1, 9999)
#         if  rand== e[i]:
#             # print(x)
#             loop = 0
#             continue
#         else:      
#             loop = 1  
#             break
#     if loop:
#         x -=1
#         # print(x)
#     else:
#         print(x)
#         break







import os, struct, base64, random
from flask import render_template, make_response, session

class Rand():

    def __init__(self,t) -> None:
        self.t = t    

    def set_sign(self):
        key = self.check_key()
        if key !=0:
            self.sign = self.request.cookies.get('_sign')
            self.key = key
            # self.new_signature()
        else:
            # print('new')
            self.key = int.from_bytes(os.urandom(7), 'big')
            self.sign = base64.b64encode(struct.pack('d',(self.key >> 3) * 2**-53))
            # self.sign = base64.b64encode(struct.pack('d',((self.bigint + self.t) >> 3) * 2**-53))
            # self.old_signature()

    # def new_signature(self):
    #     # print('kena')
    #     self.bigint = int.from_bytes(os.urandom(7), 'big')
    #     self.sign = base64.b64encode(struct.pack('d',((self.bigint + self.t) >> 3) * 2**-53))


    # def old_signature(self):
    #     self.sign = self.request.cookies.get('_sign')
    #     self.bigint = self.get_key_session()

    # def get_float_session(self):
    #     try: 
    #         # return struct.unpack('d',base64.b64decode(self.request.cookies.get('_sign')))[0]
    #         return base64.b64decode(self.request.cookies.get('_sign'))
    #     except Exception:
    #         return False

    # def get_key_session(self):
    #     try:
    #         return int(self.get_float_session()*2**53) * pow(2,3)
    #     except Exception:
    #         return False

    def check_key(self) -> bool:
        # e = 
        try:
            bytes_urandom = base64.b64decode(self.request.cookies.get('_sign'))
            key = int.from_bytes(bytes_urandom,'big')
            if session.get(key) != None:
                return key
            return 0
            
            # int_urandom = self.get_float_session()
            # print(session.get(int_byte), int_byte)
                # self.setup_old_signature()
                # self.new_signature()
            # if session.get(int_urandom >> 7) != None:
            #     # self.setup_old_signature()
            #     return True            
            #     # self.new_signature()
            # return False

            # print(int_urandom >> 7 == self.bigint >> 7)
            # check valid signature
            # if self.from_cookie:
            #     if session.get(int_urandom >> 7) != None:
            #         return True
            #     return False

            # print('checked')
            # return int_urandom >> 7 == self.bigint >> 7

        except Exception as e:
            print('ERROR',e)
            # self.new_signature()
            return False

    def set_seed(self) ->  bytes:
        random.seed(self.bigint)
        random.seed(struct.pack('d',random.random()))

    def random(self) -> int:
        return random.randint(1,1024)
        
class Main(Rand):
    
    # from_cookie = 0 # use into super().check_signature()
    def __init__(self,t, request, template = 'index.html', data={}) -> None:

        self.template = template
        self.data = data
        self.request = request

        super().__init__(t)
        self.set_sign()

        # print(self.bigint,self.sign)
        # if  request.cookies.get('_sign') == None:
        #     # self.from_cookie = 0
        #     self.new_signature()
        # else:
        #     # self.from_cookie = 1
        #     self.check_and_renew_signature()

    def __call__(self):
        res = make_response(render_template(self.template,data=self.data))
        self.set_seed()
        session[self.key] = {'role': 'user', 'skor' : 0, 'number_guesss': [self.random() for i in range(10)]}
        res.set_cookie('_sign', self.sign, httponly=True)
        return res

    # def set_admin(self):
    #     self.set_seed()
    #     session[self.key] = {'role': 'admin', 'skor' : 10, 'number_guesss': [self.random() for i in range(10)]}


    # def set_session(self):
    #     res = make_response(render_template(self.template,data=self.data))
    #     self.set_seed()
    #     session[self.bigint >> 7] = {'role': 'user', 'skor' : 0, 'number_guesss': [self.random() for i in range(10)]}
    #     res.set_cookie('_sign', self.sign, httponly=True)
    #     return res

    def check_guessing(self, session):
        number_guess = int(self.request.form.get('number_guess'))
        # s = session[self.bigint >> 7]
        # ret_val = {'msg': 'Wrong!', 'session': s}
        # print('1 ===========',s)
        if len(s['number_guesss']) == 0:
            return 'Victory!, this is the flag for you: slashroot6{}'
        if number_guess == s['number_guesss'][0]:
            session[self.bigint >> 7]['skor'] += 1
            del session[self.bigint >> 7]['number_guesss'][0]
            return 'Correct!'
        return 'Wrong'
        

    def set_view(self,**args) -> make_response:            
        if args.get('data') != None: 
            self.data = args['data']
        if args.get('template') != None: 
            self.template = args['template']
        # self.set_session()
        # return self.res
    