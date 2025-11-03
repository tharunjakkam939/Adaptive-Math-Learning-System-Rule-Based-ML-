import time
from typing import List, Dict

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def start(self):
        return time.perf_counter()

    def stop(self, start_time):
        return time.perf_counter() - start_time

    def log(self, problem, difficulty, user_answer, correct, time_taken):
        self.records.append({
            "problem": problem,
            "difficulty": difficulty,
            "user_answer": user_answer,
            "correct": correct,
            "time_taken": time_taken
        })

    def summary(self) -> Dict:
        total = len(self.records)
        if total == 0:
            return {"total": 0, "accuracy": 0.0, "avg_time": 0.0, "records": []}
        correct_count = sum(1 for r in self.records if r.get("correct"))
        avg_time = sum(r["time_taken"] for r in self.records) / total
        return {"total": total, "accuracy": correct_count / total, "avg_time": avg_time, "records": self.records}
