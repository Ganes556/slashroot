
import string


get = 'h'
# '

all_key = "(){$}.;=^_"
blacklist = {'!':"('}'^'\\')","@":"('}'^'=')","[":"('`'^';')","]":"('`'^'=')","|":"('_'^'#')"} 

# abc = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
abc = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':''}
ABC = {'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':''}
num = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}

temp_sim = string.punctuation
res_simb = dict(zip(temp_sim,['']*len(temp_sim)))

for i in all_key:        
    res_simb[i] = f"'{i}'"

for i in all_key:
    for j in all_key:
        cr = chr(ord(i)^ord(j))
        if(cr in abc.keys()):            
            abc[cr] = "('" + i + "' ^ '"  + j + "')"
            break



val = list(filter(lambda x: x != '',abc.values()))

not_empty = lambda y: list(filter(lambda x: y[x] != '',y))  
empty = lambda y: list(filter(lambda x: y[x] == '',y))  


# get uppercase and punctuation

for i in all_key:
    for j in not_empty(abc):
        x = chr(ord(i)^ord(j))        
        # print(x)
        if ABC.get(x) != None:                       
            ABC[x] = "(" + abc[j] + '^' + f"'{i}'" + ")"
            break
        if res_simb.get(x) != None:            
            res_simb[x] = "(" + abc[j] + '^' + f"'{i}'" + ")"
            break

for i in all_key:
    for j in not_empty(ABC):
        x = chr(ord(j)^ord(i))

        if abc.get(x) != None:                  
            if abc.get(x) == '':
                abc[x] = "(" + ABC[j] + '^' + f"'{i}'" + ")"

        if res_simb.get(x) != None:
            if res_simb.get(x) == '':
                res_simb[x] = "(" + ABC[j] + '^' + f"'{i}'" + ")"

        if num.get(x) != None:                  
            if num.get(x) == '':
                num[x] = "(" + ABC[j] + '^' + f"'{i}'" + ")"

for i in not_empty(ABC):
    for j in not_empty(abc):
        x = chr(ord(i)^ord(j))   
        # print(x)     
        if res_simb.get(x) != None:
            if res_simb.get(x) == '':
                res_simb[x] = "(" + ABC[i] + '^' + f"{abc[j]})"                 
        if num.get(x) != None:
            # print(ABC[I],abc[i])
            if num.get(x) == '':            
                num[x] = "("+ ABC[i] + ")" + '^' + f"{abc[j]}"                

# print(abc.get('l'))
# exit()
for i in not_empty(ABC):
    for j in not_empty(res_simb):
        x = chr(ord(i)^ord(j))
        # if x == 'l':
        #     print(ABC[I],res_simb[i])
        #     exit()     
        # print(x)   
        if abc.get(x) != None:  
            if abc.get(x) == '':          
                abc[x] = "(" + ABC[i] + "^" + f"({res_simb[j]})" + ")"

        if res_simb.get(x) != None:  
            if res_simb.get(x) == '':          
                res_simb[x] = "(" + ABC[i] + "^" + f"({res_simb[j]})" + ")"                


# print(not_empty(ABC))
# print(not_empty(abc))
# exit()

for i in not_empty(abc):
    for j in not_empty(res_simb):
        x = chr(ord(i)^ord(j))
        # if(x == 'l'):
        #     print(i)
        #     print(abc[i],res_simb[I])
        #     exit()
        # print(x)
        if ABC.get(x) != None:            
            if ABC.get(x) == '': 
                ABC[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"
        if res_simb.get(x) != None:  
            if res_simb.get(x) == '':          
                res_simb[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"

for i in not_empty(res_simb):
    for j in not_empty(abc):
        x = chr(ord(i)^ord(j))
        if x in empty(res_simb):
            print(x)
        # if res_simb.get(x) != None:  
        #     if res_simb.get(x) == '':          
        #         res_simb[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"
        
        # if ABC.get(x) != None:            
        #     if ABC.get(x) == '': 
        #         ABC[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"


        # if res_simb.get(x) != None:  
        #     if res_simb.get(x) == '':          
        #         res_simb[x] = "(" + abc[i] + "^" + f"({res_simb[j]})" + ")"


print(empty(res_simb))
print(empty(abc))
print(empty(ABC))
print(empty(num))


# print(res_simb['['],res_simb[']'])
# combine = {**abc,**res_simb,**ABC,**num}

# strings = "a"
# payload = ".".join([combine[i] for i in strings]).replace('"','').replace(" ","")
# print(payload)

# print(F"'$_'.({ABC['G']}).({ABC['E']}).({ABC['T']});")
# print(res_simb['['])
# print(res_simb.values())

