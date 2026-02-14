from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str
    mode: str

# ---------- TEXT SIMPLIFICATION ----------
def simplify_text(text: str):
    t = text.lower()

    if "photosynthesis" in t:
        return {
            "title": "🌱 Photosynthesis (Simple)",
            "visual": [
                "☀️ Sunlight",
                "⬇️",
                "🍃 Leaves take CO₂",
                "💧 Roots take water",
                "⬇️",
                "🍬 Sugar (food)",
                "🫧 Oxygen released"
            ],
            "points": [
                "Plants use sunlight to make food",
                "Leaves take carbon dioxide from air",
                "Roots absorb water from soil",
                "Food (sugar) is made for energy",
                "Oxygen is released for us to breathe"
            ],
            "read_aloud": "Plants use sunlight, water, and carbon dioxide to make food and release oxygen."
        }

    return {
        "title": "Simple Explanation",
        "visual": ["📘 No diagram available"],
        "points": [
            "Try typing about photosynthesis",
            "This topic supports visual explanation"
        ],
        "read_aloud": "Please try another topic like photosynthesis."
    }

# ---------- MATH VISUAL ----------
def solve_math(expr: str):
    expr = expr.replace("x", "*").replace("×", "*")

    if "+" in expr:
        a, b = map(int, expr.split("+"))
        return {
            "title": "➕ Addition",
            "visual": ["🍎"*a, "➕", "🍊"*b, "=", "🍓"*(a+b)],
            "answer": a + b,
            "read_aloud": f"{a} plus {b} equals {a+b}"
        }

    if "*" in expr:
        a, b = map(int, expr.split("*"))
        return {
            "title": "✖️ Multiplication",
            "visual": [f"Group {i+1}: 🐶"*a for i in range(b)],
            "answer": a * b,
            "read_aloud": f"{a} times {b} equals {a*b}"
        }

    return {
        "title": "Math Result",
        "visual": ["🧮"],
        "answer": eval(expr),
        "read_aloud": f"The answer is {eval(expr)}"
    }

# ---------- API ----------
@app.post("/process")
def process(data: InputData):
    if data.mode == "text":
        return {"success": True, "data": simplify_text(data.text)}

    if data.mode == "math":
        return {"success": True, "data": solve_math(data.text)}

    return {"success": False, "error": "Invalid mode"}

@app.get("/")
def root():
    return {"message": "Backend running ✅"}

