import os
from flask import Flask, render_template, request
__author__= 'Attique'
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods = ['POST'])
def upload():
    target=os.path.join(APP_ROOT, 'Docs/')
    print(target)


    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("files"):
        print(file)
        filename=file.filename
        destination="/".join([target,filename])
        print (destination)
        file.save(destination)
        f=request.files['file']
    return render_template("complete.html")
    #return file.filename

#def hello_world():
    #return 'Hello World!'


if __name__ == '__main__':
    app.run(port=4555,debug=True)
