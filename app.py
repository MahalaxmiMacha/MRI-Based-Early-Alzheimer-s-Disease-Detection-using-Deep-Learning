from flask import Flask, render_template, request, redirect, url_for, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong random key in production


# ✅ Create uploads folder automatically
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    'saved_folder',
    'mobilenetv2_alzheimer_model.keras'
)

model = load_model(MODEL_PATH)

# Class names
classes = ['AD', 'CN', 'EMCI', 'LMCI']

# Descriptions for each class
descriptions = {
    'AD': "Alzheimer's Disease: Significant memory loss, confusion, and behavioral changes. (Severe Stage)",
    'CN': "Cognitively Normal: No signs of memory problems or thinking issues.",
    'EMCI': "Early Mild Cognitive Impairment: Very slight memory problems, may not impact daily life much.",
    'LMCI': "Late Mild Cognitive Impairment: More obvious memory and thinking problems. High risk of progressing to Alzheimer's."
}

# Stage mapping
stage_mapping = {
    'CN': '1st Stage',
    'EMCI': '2nd Stage',
    'LMCI': '3rd Stage',
    'AD': '4th Stage'
}

# Hardcoded login (demo only)
USERNAME = 'admin'
PASSWORD = 'admin123'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get("logged_in"):
        return redirect(url_for('login'))

    if request.method == 'POST':

        if 'file' not in request.files:
            return "No file uploaded!", 400

        file = request.files['file']

        if file.filename == '':
            return "No selected file!", 400

        if file:
            # Save uploaded image to static/uploads
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Preprocess image for prediction
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            pred = model.predict(img_array)
            pred_class_idx = np.argmax(pred)
            pred_class = classes[pred_class_idx]

            stage = stage_mapping[pred_class]
            description = descriptions[pred_class]

            result = {
                'disease': pred_class,
                'stage': stage,
                'description': description,
                'uploaded_image': f'uploads/{file.filename}'
            }

            return render_template('result.html', result=result)

    # GET request → upload page
    return render_template('predict.html')


@app.route('/')
def index():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
