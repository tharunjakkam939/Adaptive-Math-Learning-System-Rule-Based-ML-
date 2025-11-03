import random

OPS = { "add": "+", "sub": "-", "mul": "*", "div": "/" }

def generate_problem(difficulty: str):
    if difficulty == "Easy":
        a, b = random.randint(0, 10), random.randint(0, 10)
        op = random.choice(["add", "sub"])
    elif difficulty == "Medium":
        a, b = random.randint(0, 20), random.randint(1, 20)
        op = random.choice(["add", "sub", "mul"])
    else:
        a, b = random.randint(1, 100), random.randint(1, 20)
        op = random.choice(["add", "sub", "mul", "div"])

    if op == "add":
        ans = a + b
    elif op == "sub":
        ans = a - b
    elif op == "mul":
        ans = a * b
    else:
        ans = round(a / b, 2)

    return f"{a} {OPS[op]} {b}", ans
