from flask import Flask, request
import main
import cv2
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Azurrre!</h1>"


@app.route("/test", methods=['GET', 'POST'])
def ping_ML():
    # Save image, send local URL to model
    print("pinging model")
    image_filename = None
    image = request.files.get('testImage')
    if image.filename != '':
        image_filename = image.filename
        image.save(image_filename)
    text, prob = main.test_model(image_filename)
    return "Text: {}, Probability: {}".format(text, prob)
