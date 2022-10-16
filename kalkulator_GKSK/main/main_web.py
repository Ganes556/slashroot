from flask import Flask, render_template, request,make_response
from func import *
app = Flask(__name__)
app.register_error_handler(404,lambda : "This page does not exist!")
app.add_url_rule("/","index",lambda : template_index(request.form["name"],request.remote_addr)[0] if request.method == "POST" else render_template("index.html") ,methods=["GET","POST"])
app.add_url_rule("/history","history", lambda : template_history(request.args.get("for")) if request.args.get("for") else make_response("Bad request!",400))
if __name__ == "__main__": app.run(host="localhost",port=5000,debug=1)