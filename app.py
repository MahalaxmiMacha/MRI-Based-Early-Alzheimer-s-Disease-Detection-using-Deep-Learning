from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong random key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered.")
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully. Please login.")

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session['logged_in'] = True
            session['username'] = user.username
            session['email'] = user.email

            return redirect(url_for('home'))

        return render_template(
            'login.html',
            error="Invalid email or password"
        )

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
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

    with app.app_context():
        db.create_all()

    app.run(debug=True)