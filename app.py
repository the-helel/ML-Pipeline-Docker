from  flask import Flask , render_template, request , redirect , url_for , flash 
import requests
import cv2
import tensorflow as tf
from PIL import Image
import numpy as np
from numpy import asarray

import os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'susskey'
app.config['SESSION_TYPE'] = 'filesystem'

async def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
async def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html',filename=filename)
            # return render_template(url_for(uploaded_file,filename=filename))
    return render_template('index.html')

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
async def uploaded_file(filename):
    if request.method == 'POST':
    	print("hello")
    	# from tensorflow.keras.models import load_model
    	# from tensorflow.keras.preprocessing import image
    	# from tensorflow.keras.initializers import glorot_uniform
        
    	with open('model_architecture.json', 'r') as json_file:
    		json_savedModel= json_file.read()
    	model_j = tf.keras.models.model_from_json(json_savedModel)
    	print("hello")
    	model_j.load_weights('model_weights.h5')
    	model_j.compile(loss='sparse_categorical_crossentropy',optimizer='SGD',metrics=['accuracy'])
    	path =  redirect(url_for('static', filename='img/' + filename), code=301)
    	filepath = './static/img/' + filename
    	print(filepath)
        
    	img = Image.open(filepath)
    	print('img loaded')
    
    	img = asarray(img)
    	print(type(img))
    	x = np.resize(img, (456,456,3))
    	x.reshape(1,456,456,3)
    	img_exp = np.expand_dims(x, axis=0)
    	result = model_j.predict(img_exp)
    	print(result)
    	
    	max_val = np.amax(result)
    	result = np.where(result == np.amax(result))
    	res   = max(result)
    	return render_template('index.html', filename=filename , path = path , res = res[0])


    path =  redirect(url_for('static', filename='img/' + filename), code=301)    
    return path
    


if __name__ == "__main__":
    app.run(debug=True)
