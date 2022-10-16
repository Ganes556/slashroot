from flask import Flask, render_template, request
from func import *

app = Flask(__name__)

app.register_error_handler(404,lambda : "This page does not exist!")

app.add_url_rule("/","index",lambda : template_index(request.form["name"]) if request.method == "POST" else render_template("index.html") ,methods=["GET","POST"])

if __name__ == "__main__": app.run(host="localhost",port=21202,debug=0)