# 🎯 Adaptive Math Learning System (Rule-Based + ML)

This project is an **Adaptive Learning Platform** that dynamically adjusts question difficulty based on student performance.  
It combines **rule-based logic + machine learning (Logistic Regression)** to personalize learning.

---

## 🚀 Features

| Feature | Description |
|---|---|
3 difficulty levels | Easy / Medium / Hard  
Adaptive Logic | Rule-based + ML model  
Feedback | ✅ Correct ❌ Wrong + Balloons 🎉  
Performance Tracking | Accuracy, time, streaks  
Auto Logs | CSV saved per student session  
Charts | Response time + Correctness trend  
UI | Streamlit interactive dashboard  

---

## 🧠 How It Works

### ✅ Rule-Based Engine
| Condition | Action |
|---|---|
3 fast correct answers | Increase difficulty  
2 wrong or slow answers | Decrease difficulty  

### 🤖 ML Engine (Logistic Regression)
**Input:** Accuracy + Avg time per question  
**Output:** Next difficulty level (E/M/H)

---

## 🏗 Architecture

![Architecture Flow](architecture_flow.png)

---

## 🔁 Learning Flow

![Learning Flow](learning_flow.png)

---

## 📂 Project Structure

math-adaptive-prototype/
├─ README.md
├─ requirements.txt
└─ src/
    ├─ streamlit_app.py
    ├─ puzzle_generator.py
    ├─ tracker.py
    └─ adaptive_engine.py


---

## 🚀 Run Instructions

### 1️⃣ Create environment & install
```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
2️⃣ Launch App
streamlit run src/streamlit_app.py
📊 Output Example

Live adaptive questions

Feedback after each question

Real-time difficulty updates

Final learning summary report

🧠 Future Enhancements

Deep-learning based difficulty predictor

Student knowledge graph

Voice questions + speech response

More topics: algebra, fractions, geometry

👨‍💻 Developed For

AI-Adaptive Learning Assignment
Demonstrates AI system for math learning personalization.
