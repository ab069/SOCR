from flask import Flask, request, render_template
import os
from transformers import VisionEncoderDecoderModel
import torch
from PIL import Image
from transformers import TrOCRProcessor

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-small-printed")

def shaheenOCR(imagepath):
  
 # %cd /content/gdrive/MyDrive
  print("patxx: " + imagepath)

  pretrained="./model"
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  print("path0: " + imagepath)
  model = VisionEncoderDecoderModel.from_pretrained(pretrained)
  model.to(device)
  print("path: " + imagepath)
  image = Image.open(imagepath).convert("RGB")
#   image
  pixel_values = processor(image, return_tensors="pt").pixel_values
  outputs = model.generate(pixel_values.to(device))
  
  labels = outputs
  label_str = processor.decode(labels[0], skip_special_tokens=True)
  return label_str
  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/workplace")
def workplace():
    return render_template("workplace.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/shaheenocr", methods=["GET", "POST"] )
def shaheenocr():
    extractedText = "Hello"
    if request.method == "POST":
        # target = os.path.join(APP_ROOT, '/images/filename.png')
        filename = request.files.get('filename').filename
        target = './images/' + filename
        print("Received a POST request")

        # val = request.files['image']
        uploadedImage = request.files['filename']
        # print("Received from App:\t", val)
        print("request.method", request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        print('request.files', request.files.get('filename').filename)
        print('uploaded', uploadedImage)
        print("Saving Image to ", target)
        uploadedImage.save(target, buffer_size=16384)
        extractedText = filename
        uploadedImage.close()

        # processImageInModel function takes the path 'target
        # and returns text extracted from image
        # Just uncomment the following line  when it is done
        # and our app should be completed

        extractedText = shaheenOCR(target)
        print(extractedText)

    return render_template("shaheenocr.html", extractedText=extractedText)




@app.route("/englishocr", methods=["GET", "POST"] )
def englishocr():
    extractedText = "Hello"
    if request.method == "POST":
        # target = os.path.join(APP_ROOT, '/images/filename.png')
        filename = request.files.get('filename').filename
        target = './images/' + filename
        print("Received a POST request")

        # val = request.files['image']
        uploadedImage = request.files['filename']
        # print("Received from App:\t", val)
        print("request.method", request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        print('request.files', request.files.get('filename').filename)
        print('uploaded', uploadedImage)
        print("Saving Image to ", target)
        uploadedImage.save(target, buffer_size=16384)
        extractedText = filename
        uploadedImage.close()

        # processImageInModel function takes the path 'target
        # and returns text extracted from image
        # Just uncomment the following line  when it is done
        # and our app should be completed

        # extractedText = shaheenocr(target)
        # print(extractedText)

    return render_template("englishocr.html", extractedText=extractedText)






@app.route("/translation", methods=["GET", "POST"])
def translation():
    extractedText = "Hello"
    if request.method == "POST":
        # target = os.path.join(APP_ROOT, '/images/filename.png')
        filename = request.files.get('filename').filename
        target = './images/' + filename
        print("Received a POST request")

        # val = request.files['image']
        uploadedImage = request.files['filename']
        # print("Received from App:\t", val)
        print("request.method", request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        print('request.files', request.files.get('filename').filename)
        print('uploaded', uploadedImage)
        print("Saving Image to ", target)
        uploadedImage.save(target, buffer_size=16384)
        extractedText = filename
        uploadedImage.close()

        # processImageInModel function takes the path 'target
        # and returns text extracted from image
        # Just uncomment the following line  when it is done
        # and our app should be completed

        extractedText = shaheenocr(target)
        print(extractedText)

    return render_template("translation.html", extractedText=extractedText)




@app.route("/newProject", methods=["GET", "POST"])
def newProject():
    extractedText = "Hello"
    if request.method == "POST":
        # target = os.path.join(APP_ROOT, '/images/filename.png')
        filename = request.files.get('filename').filename
        target = './images/' + filename
        print("Received a POST request")

        # val = request.files['image']
        uploadedImage = request.files['filename']
        # print("Received from App:\t", val)
        print("request.method", request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        print('request.files', request.files.get('filename').filename)
        print('uploaded', uploadedImage)
        print("Saving Image to ", target)
        uploadedImage.save(target, buffer_size=16384)
        extractedText = filename
        uploadedImage.close()

        # processImageInModel function takes the path 'target
        # and returns text extracted from image
        # Just uncomment the following line  when it is done
        # and our app should be completed

        # extractedText = shaheenocr(target)
        # print(extractedText)

    return render_template("newProject.html", extractedText=extractedText)






if __name__ == '__main__':
    app.run()
