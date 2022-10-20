import os
from app import app
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename

from FNPR import predict

ALLOWED_EXTENSIONS = set([ 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Image successfully uploaded and displayed below')
		file_path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
		result=predict(file_path)
		return render_template('display.html',file_path=file_path,result=result)
	else:
		flash('Allowed image types are -> jpg,jpeg')
		return redirect(request.url)


if __name__ == "__main__":
    app.run()