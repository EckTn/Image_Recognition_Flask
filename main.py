import os
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, render_template
import tensorflow as tf

from keras.models import load_model
import keras.applications.xception as xception

# ignore warning messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = load_model('CNN_garbage.h5')

# Add the missing constants
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANNELS = 3
categories = ['paper', 'cardboard', 'plastic', 'metal', 'trash', 'green-glass']

def preprocess_image(image):
    # Preprocess the image using Xception's preprocessing method
    img = xception.preprocess_input(image)
    return img

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded.'}), 400

    img = Image.open(request.files['image'].stream).convert('RGB')
    img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    img_array = np.array(img).reshape((1, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS))
    
    processed_image = preprocess_image(img_array)
    preds = model.predict(processed_image)
    predicted_class = categories[np.argmax(preds)]

    return jsonify({'prediction': predicted_class})
  
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))

language = "python"
packages = ["flask"]
run = "python main.py"


