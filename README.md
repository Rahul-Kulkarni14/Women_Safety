
# 👁️‍🗨️ Women Safety Analytics – Real-Time Gender, Emotion & Threat Detection

A real-time safety monitoring system for women that uses facial recognition, gender classification, emotion detection, and behavioral analysis to identify potential threats. This project leverages computer vision and deep learning models to analyze live video feeds and trigger alerts in high-risk scenarios.

> 🧠 Based on the published research paper: [Read it here (PDF)](docs/Research_Paper_Women_Safety_Analytics.pdf)

---

## 📌 Overview

This system uses camera-based input to:
- Detect **gender** and **facial expressions**
- Identify **emotional states** such as fear or distress
- Recognize **threatening behavior** (e.g. someone following too closely or group crowding)
- Provide potential for real-time **alerts** to guardians or authorities

It is implemented using Python with OpenCV, Deep Learning models (CNNs), and reinforcement learning logic.

---

## 🚀 Features

- 🔍 **Facial Recognition**
- 🙍‍♀️ **Gender Classification**
- 😨 **Emotion Detection (fear, anger, sadness)**
- 🧍‍♂️🧍‍♀️ **Threat Detection via Proximity & Behavior**
- 📈 **Modular & Extensible Codebase**
- 🧠 Based on **DeepFace**, CNNs, RNNs, and LSTM models


---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
````

## 🧪 Running the Code

### Gender & Emotion Detection:

```bash
python code/main.py
```

### Full System (including Threat Detection):

```bash
python code/threat.py
```

---

## 📄 Research Paper

📘 [Women Safety Analytics – Published Paper (PDF)](docs/Research_Paper_Women_Safety_Analytics.pdf)

Covers:

* Proposed model
* Facial recognition + emotion detection pipeline
* Threat analysis using behavioral modeling
* Reinforcement learning logic
* System architecture diagrams
* Use cases & societal impact

---

## 🧠 Models Used

* **DeepFace** for facial analysis
* **CNNs** for gender and emotion classification
* **YOLO / MobileNet** (planned) for behavioral gesture recognition
* **RNN / LSTM** for movement and proximity pattern learning
* **Reinforcement Learning** to optimize threat alert triggers over time

---

## 🚧 Future Scope

* Add **real-time alerts** to guardian via SMS or mobile app
* Train **custom emotion models** using FER2013
* Integrate **YOLOv8 or OpenPose** for gesture recognition
* Connect to **CCTV feeds** in smart city zones

