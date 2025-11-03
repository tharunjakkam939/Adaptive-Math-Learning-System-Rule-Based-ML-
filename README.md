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



## 🏗 Architecture

<img width="2850" height="1446" alt="adaptive_architecture" src="https://github.com/user-attachments/assets/ac38b629-5147-4a03-a5a3-fd0b7a687cc2" />





## 🔁 Learning Flow
<img width="2850" height="1446" alt="adaptive_learning_flow" src="https://github.com/user-attachments/assets/852db066-2eb5-4053-b6dd-f6519d94b362" />




## 📂 Project Structure

math-adaptive-prototype/
├─ README.md
├─ requirements.txt
└─ src/
    ├─ streamlit_app.py
    ├─ puzzle_generator.py
    ├─ tracker.py
    └─ adaptive_engine.py




## 🚀 Run Instructions

### 1️⃣ Create environment & install
bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
##2️⃣ Launch App
streamlit run src/streamlit_app.py
##📊 Output Example

Live adaptive questions

Feedback after each question

Real-time difficulty updates

Final learning summary report
<img width="1451" height="892" alt="Screenshot 2025-11-03 164801" src="https://github.com/user-attachments/assets/15c2012a-8eba-46a5-93ca-74bca4c2d360" />
<img width="1268" height="756" alt="Screenshot 2025-11-03 164815" src="https://github.com/user-attachments/assets/6ee26601-3562-4821-ab93-1feaf2733ca5" />



##🧠 Future Enhancements

Deep-learning based difficulty predictor

Student knowledge graph

Voice questions + speech response

More topics: algebra, fractions, geometry

##👨‍💻 Developed For

AI-Adaptive Learning Assignment
Demonstrates AI system for math learning personalization.
