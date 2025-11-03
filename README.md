# Adaptive-Math-Learning-System-Rule-Based-ML
# 🎯 Adaptive Math Learning System (Rule-Based + ML)

This project implements an **Adaptive Learning Platform** that adjusts question difficulty based on student performance.  
It includes **rule-based logic + a Logistic Regression ML model** for predicting the next difficulty level.

## 🚀 Features
| Feature | Description |
|---|---|
✅ 3 Difficulty Levels | Easy / Medium / Hard  
✅ Adaptive Engine | Rule-based & ML-driven difficulty change  
✅ Performance Tracking | Accuracy + Speed + Trends  
✅ Visual Feedback | Balloons, success/error, charts  
✅ Automatic CSV Logs | Per-student learning history  
✅ Streamlit UI | Lightweight interactive interface  

---

## 🧠 Adaptive Logic

### 📌 Rule-Based Strategy
| Condition | Action |
|---|---|
3 correct fast | Increase difficulty  
2 wrong OR slow | Decrease difficulty  

### 🤖 ML Strategy (Logistic Regression)
Inputs:
- Accuracy
- Average time per question

Output:
- Next difficulty class (Easy / Medium / Hard)

---

## 🏗 Architecture
