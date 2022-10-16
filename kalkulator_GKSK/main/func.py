import hashlib
from flask import render_template
safe_eval = lambda expr, exec_eval = lambda expr : str(eval(expr, {'__builtins__':{}},{})), checking = lambda expr: [[True if len(expr) > 104 else False],{True for i in ["builtins","**","popen","os","eval","exec","'",'"',"]","["," "] if i in expr}] : (lambda check=checking(expr) : "error..." if check[0][0] or len(check[1]) > 0 else exec_eval(expr))()
template_index = lambda conditions,ip, name_file = lambda ip : hashlib.md5(str(ip).encode()).hexdigest() : [
            render_template("hasil.html",data={"hasil": safe_eval(conditions),"history":str(name_file(ip))}),
            open(str(name_file(ip)),"a").write("\n"+ conditions+ "=" + safe_eval(conditions) + "\n")  if safe_eval(conditions) != "error..." else False            
        ] 
template_history = lambda name_file: (lambda history = [content.replace("\n","") for i in open(name_file,"r").readlines() if (content := i) != "\n"]: { i:history[i] for i in range(len(history))})()