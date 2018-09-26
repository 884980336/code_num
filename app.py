# from flask import Flask,request,Markup,render_template
#
# from werkzeug.datastructures import FileStorage
# from tempfile import SpooledTemporaryFile
# app = Flask(__name__)
# print(app.jinja_env.filters)

# @app.route('/',methods=["GET","POST"])
# def hello_world():
#     if request.method == "GET":
#         return render_template("input.html")
#     else:
#         # print(request.method)
#         # print(request.files)
#         file_obj = request.files.get("file")
#         print(file_obj.filename)
#         for i in file_obj.stream:
#             print(str(i, encoding="utf8"))
#         # print(str(file_obj.stream.read(), encoding="utf8"))
#         return "OK"
from  app import app

if __name__ == '__main__':
    app.run()
