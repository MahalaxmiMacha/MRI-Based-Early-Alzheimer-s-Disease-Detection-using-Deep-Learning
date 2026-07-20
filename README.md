<div align="center">

# 🧠 MRI Image Based Early Alzheimer's Disease Detection using Deep Learning

### An AI-powered web application that predicts Alzheimer's disease stages from MRI brain scans using Deep Learning.

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
<img src="https://img.shields.io/badge/MobileNetV2-4285F4?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

</div>

---

# 🚀 Live Demo

> **Application URL**

**https://early-alzheimer-disease-detection-using-gw68.onrender.com/home**

---

# 📖 Overview

Alzheimer's disease is a progressive neurological disorder that gradually affects memory, thinking ability, and daily life. Early diagnosis plays a significant role in slowing disease progression and enabling timely medical intervention.

This project presents an AI-powered web application that predicts the stage of Alzheimer's disease from MRI brain images using a Deep Learning model based on **MobileNetV2**. The trained model is integrated into a Flask web application, allowing users to upload MRI scans and receive instant predictions through a simple and user-friendly interface.

The application also provides secure user authentication, enabling registered users to access the prediction service safely.

---

# 🎯 Disease Classification

The model classifies MRI brain images into one of the following stages:

| Stage | Description |
|--------|-------------|
| 🟢 CN | Cognitively Normal |
| 🟡 EMCI | Early Mild Cognitive Impairment |
| 🟠 LMCI | Late Mild Cognitive Impairment |
| 🔴 AD | Alzheimer's Disease |

---

# ✨ Features

- 🧠 MRI image-based Alzheimer's disease prediction
- 🤖 Deep Learning model powered by MobileNetV2
- 📤 MRI image upload through a web interface
- ⚙️ Automatic image preprocessing
- 🔐 Secure user registration and login
- 🔒 Password hashing for enhanced security
- 📊 Instant disease stage prediction
- 📄 Disease description displayed with prediction
- 💻 Responsive Bootstrap-based interface
- ☁️ Cloud deployment using Render

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
               Flask Web Application
                      │
                      ▼
          User Authentication Module
                      │
                      ▼
             MRI Image Upload
                      │
                      ▼
         Image Preprocessing Layer
      (Resize • Normalize • Convert)
                      │
                      ▼
        MobileNetV2 Deep Learning Model
                      │
                      ▼
          Alzheimer's Stage Prediction
                      │
                      ▼
           Prediction Result Page
```

---

# 📂 Project Structure

```text
MRI-Based-Early-Alzheimer-Detection/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── saved_folder/
│   └── mobilenetv2_alzheimer_model.keras
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── predict.html
│   └── result.html
│
├── static/
│   ├── images/
│   └── uploads/
│
└── README.md
```

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | HTML, CSS, Bootstrap |
| Backend | Python, Flask |
| Deep Learning | TensorFlow, Keras |
| Model Architecture | MobileNetV2 |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Image Processing | TensorFlow/Keras |
| Deployment | Render |
| Programming Language | Python 3.10+ |

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/MahalaxmiMacha/MRI-Based-Early-Alzheimer-s-Disease-Detection-using-Deep-Learning.git

cd Early-Alzheimer-Disease-Detection-using-Deep-Learning
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📋 Workflow

### Step 1

Create an account or log in securely.

### Step 2

Upload an MRI brain scan image.

### Step 3

The uploaded image is automatically resized and preprocessed.

### Step 4

The trained MobileNetV2 model analyzes the MRI scan.

### Step 5

The model predicts the Alzheimer's disease stage.

### Step 6

The application displays the predicted stage along with a brief explanation.

---

# 🗂️ Dataset

The Deep Learning model was trained on MRI brain scan images categorized into four stages of Alzheimer's disease progression.

### Classes

- 🟢 CN — Cognitively Normal
- 🟡 EMCI — Early Mild Cognitive Impairment
- 🟠 LMCI — Late Mild Cognitive Impairment
- 🔴 AD — Alzheimer's Disease

---

# 🌟 Key Highlights

- AI-powered medical image classification
- MobileNetV2 transfer learning architecture
- Secure authentication system
- Automatic MRI preprocessing
- Fast and accurate disease stage prediction
- Responsive web application
- Cloud deployment using Render
- User-friendly interface for healthcare research

---

# 🚀 Future Enhancements

- Google Sign-In authentication
- Email verification and password recovery
- Prediction history for registered users
- Confidence score visualization
- Explainable AI (Grad-CAM heatmaps)
- PostgreSQL integration
- REST API for hospital integration
- Doctor dashboard
- Multi-disease brain MRI classification

---

# ⚠️ Disclaimer

This project is intended **for educational and research purposes only**.

The predictions generated by this application should **not** be considered a substitute for professional medical diagnosis, clinical evaluation, or healthcare advice. Always consult qualified medical professionals for diagnosis and treatment decisions.

---

# 📄 License

This project is released under the **MIT License**.

---

# 👩‍💻 Author

**Mahalaxmi Macha**

Bachelor of Technology (Computer Science and Engineering)

This project was developed as part of academic learning and research in Deep Learning, Computer Vision, and Healthcare AI.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star on GitHub!

</div>
