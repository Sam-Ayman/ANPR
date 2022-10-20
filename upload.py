import os

from flask import Flask, redirect, jsonify, request, url_for, render_template, flash

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "./uploaded/"


@app.route("/")
def home():
    return render_template("index.html")


# Route to upload image
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            # print(image + "Uploaded to Faces")
            # flash('Image successfully Uploaded to Faces.')
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            filename = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            print("stored as:" + filename)
            print(filename)
            
            print(filename)
            return render_template("uploaded.html", filename=filename)
            
    return redirect("/")

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename= filename), code=301)
if __name__ == "__main__":
    app.run()