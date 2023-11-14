from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from predict_classes import local_classes
import os
import tensorflow as tf
import numpy as np
import keras
import logging

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/inference', methods=['POST'])
def inference_image():
    if 'file' not in request.files:
        return jsonify({'error': 'File part is missing'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

        model_path = "model/effv2b0.h5"
        try:
            model = keras.models.load_model(model_path)
        except Exception as e:
            logging.error(f"Error loading the model from {model_path}: {e}")
            return jsonify({'error': 'Failed to load the model'}), 500

        img = tf.io.read_file(path)
        img = tf.io.decode_image(img, channels=3, dtype=tf.float32)
        img = tf.image.grayscale_to_rgb(tf.image.rgb_to_grayscale(img))
        img = (img - 0.5) / 0.5

        resized_img = tf.image.resize(img, [224, 224])
        resized_img = np.expand_dims(resized_img, axis=0)

        # Get prediction
        res = model.predict(resized_img)

        percentage = round(np.amax(res) * 100.0, 2)
        inference = local_classes[np.argmax(res)]  # Assuming local_classes is defined

        return jsonify({
            'filename': filename,
            'inference': inference,
            'percentage': percentage
        })

    else:
        return jsonify({'error': 'Allowed image types are -> png, jpg, jpeg, gif'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
