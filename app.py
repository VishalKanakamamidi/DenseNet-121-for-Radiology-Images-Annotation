import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'img1/')
    img_files = os.listdir("Out_img/")
    for img_file in img_files:
        os.unlink("Out_img//"+img_file)

    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    print(request.form["disease"])
    disease = request.form["disease"]
    
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    
    os.system("python denseNet_localization.py "+disease+" img1")
    os.unlink(destination)
    
    image_names = os.listdir('Out_img')
    print(image_names)
    

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("gallery.html", image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("Out_img", filename)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
