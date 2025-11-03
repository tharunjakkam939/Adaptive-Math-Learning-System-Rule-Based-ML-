import streamlit as st
from puzzle_generator import generate_problem
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine
import time
from ml_engine import MLAdaptiveEngine

import pandas as pd

# ---- Initialize state ----
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"
if "tracker" not in st.session_state:
    st.session_state.tracker = PerformanceTracker()
if "engine" not in st.session_state:
    st.session_state.engine = st.session_state.engine = MLAdaptiveEngine()
if "problem" not in st.session_state:
    st.session_state.problem = None
if "answer" not in st.session_state:
    st.session_state.answer = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "session_started" not in st.session_state:
    st.session_state.session_started = False
if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = {"text":"","ok":None}

st.set_page_config(page_title="Adaptive Math Learning", layout="centered")

st.markdown("""
<div style='text-align:center'>
    <h1 style='font-size:42px;margin-bottom:2px;'>🎯 Adaptive Math Learning Prototype</h1>
    <p style='color:gray;margin-top:0;'>Rule-based adaptive engine — accuracy & response time driven</p>
</div>
""", unsafe_allow_html=True)

# Learner name & starting difficulty (as per assignment)
name = st.text_input("Enter learner name:", value="Student")
initial = st.selectbox("Select starting difficulty:", ["Easy","Medium","Hard"], index=0)

# Start session
if st.button("Start Session", key="start_btn") and not st.session_state.session_started:
    st.session_state.difficulty = initial
    st.session_state.session_started = True
    st.session_state.tracker = PerformanceTracker()

st.write("---")

# Controls when session active
if st.session_state.session_started:
    cols = st.columns([1,1,1])
    with cols[0]:
        if st.button("New Question", key="newq"):
            st.session_state.problem, st.session_state.answer = generate_problem(st.session_state.difficulty)
            st.session_state.start_time = time.time()
            st.session_state.last_feedback = {"text":"","ok":None}
    with cols[1]:
        if st.button("Show Difficulty", key="showd"):
            st.info(f"Current difficulty: {st.session_state.difficulty}")
    with cols[2]:
        if st.button("Reset Session", key="reset"):
            st.session_state.tracker = PerformanceTracker()
            st.session_state.difficulty = initial
            st.session_state.problem = None
            st.session_state.answer = None
            st.session_state.session_started = False
            st.rerun()

    st.write(f"**Current difficulty:** {st.session_state.difficulty}")
    st.write("---")

    # Display question if any
    if st.session_state.problem:
        st.markdown(f"### Question: `{st.session_state.problem}`")
        user_input = st.text_input("Your answer:", key="answer_box")
        if st.button("Submit Answer", key="submit"):
            try:
                ua = float(user_input) if '.' in user_input else int(user_input)
            except:
                ua = user_input
            time_taken = time.time() - st.session_state.start_time
            correct = False
            if isinstance(st.session_state.answer, float):
                try:
                    correct = abs(float(ua)-st.session_state.answer) < 0.01
                except:
                    correct = False
            else:
                try:
                    correct = int(ua) == st.session_state.answer
                except:
                    correct = False
            # log
            st.session_state.tracker.log(st.session_state.problem, st.session_state.difficulty, ua, correct, time_taken)
            # feedback
            if correct:
                st.success("Correct! 🎉")
                st.balloons()
                st.session_state.last_feedback = {"text":"Correct!","ok":True}
            else:
                st.error(f"Wrong. Correct answer: {st.session_state.answer}")
                st.session_state.last_feedback = {"text":f"Wrong. Answer: {st.session_state.answer}","ok":False}
            # adapt difficulty
            summary = st.session_state.tracker.summary()
            st.session_state.difficulty = st.session_state.engine.predict_next(
                summary["accuracy"], summary["avg_time"]
            )


    # show last feedback and next action
    if st.session_state.last_feedback.get('text'):
        fb = st.session_state.last_feedback
        if fb.get('ok'):
            st.markdown("<div style='background:#e6ffed;border-radius:8px;padding:12px'>✅ <strong>Correct! Great.</strong></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background:#ffe6e6;border-radius:8px;padding:12px'>❌ <strong>Incorrect.</strong></div>", unsafe_allow_html=True)
        if st.button("Next Question", key="nextq"):
            st.session_state.problem, st.session_state.answer = generate_problem(st.session_state.difficulty)
            st.session_state.start_time = time.time()
            st.session_state.last_feedback = {"text":"","ok":None}

    st.write("---")

    # End session
    if st.button("📑 End Session & Show Report"):
        summary = st.session_state.tracker.summary()

        st.subheader("📈 Session Summary")
        st.write(f"✅ Total Questions: **{summary['total']}**")
        st.write(f"🎯 Accuracy: **{summary['accuracy']*100:.2f}%**")
        st.write(f"⏱ Avg Time: **{summary['avg_time']:.2f}s**")
        st.write(f"🤖 Next Difficulty (ML Suggested): **{st.session_state.difficulty}**")

        df = pd.DataFrame(summary["records"])

        st.write("### 📊 Performance Logs")
        st.dataframe(df)

        if not df.empty:
            st.write("### ⏳ Response Time Chart")
            st.line_chart(df["time_taken"])

            st.write("### ✅ Correctness Chart")
            st.bar_chart(df["correct"].astype(int))

            # ✅ AUTO SAVE LOGS TO CSV
            # ✅ AUTO SAVE LOGS TO CSV
            import os

            logs_dir = "session_logs"
            os.makedirs(logs_dir, exist_ok=True)

            # Ensure student name exists
            if "name" not in st.session_state or not st.session_state.name:
                st.session_state.name = "Student"

            filename = f"{st.session_state.name.replace(' ','_')}_session.csv"
            filepath = os.path.join(logs_dir, filename)

            df.to_csv(filepath, index=False)
            st.success(f"📁 Session log saved at: **{filepath}**")

else:
    st.info("Start a session to begin practicing. Choose a difficulty and click Start Session.")

