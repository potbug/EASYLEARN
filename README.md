Synapse 🧠✨
Learning Made Simple, Visual & Audible
Basic Details
Team Name

Synapse

Team Members

Malavika M S – Computer Science Engineering Student

Hosted Project Link
http://127.0.0.1:5500/frontend/index.html

Project Description
Synapse is an accessible learning assistant designed to help students—especially those with learning difficulties—understand math problems and complex text through step-by-step explanations, simplified language, visual representations, and read-aloud support.

Problem Statement

*Many students struggle with:

*Understanding long, complex text

*Visualizing math concepts

*Reading difficulties (e.g., dyslexia)

*Lack of accessible learning tools

*Traditional learning platforms often fail to provide visual + audio + simplified explanations together.

The Solution

Synapse solves this by:

Breaking math problems into clear step-by-step logic

Simplifying difficult text into easy bullet-point explanations

Providing visual explanation placeholders

Adding read-aloud (Text-to-Speech) support

Showing large, readable output for better accessibility

Technical Details
Technologies / Components Used
For Software
Languages Used


HTML

CSS

JavaScript

Python

Frameworks Used

FastAPI (Backend)

Libraries Used

Web Speech API (Text-to-Speech)

Fetch API

Pydantic

Tools Used

VS Code

Git & GitHub

Uvicorn

Browser (Chrome)

Features


✅ Math Solver with step-by-step explanation


✅ Text Simplification (complex → simple language)


✅ Read-Aloud feature for output


✅ Large & accessible text output


✅ Visual explanation section (icons + placeholders)


✅ Beginner-friendly UI



Implementation
For Software
Installation
pip install fastapi uvicorn


Run Backend
cd backend
python -m uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000


Run Frontend
Open the file directly:
frontend/index.html
(No server required for frontend)

Project Documentation
Screenshots
Screenshot 1 – Math Solver
Shows step-by-step solution for math expressions.
Screenshot 2 – Text Simplification
Displays simplified explanation of complex biology text.
Screenshot 3 – Read Aloud Feature
Read-aloud button reading the output text.
(Add screenshots as images in your repo and link them here)

Diagrams
System Architecture
Frontend (HTML/CSS/JS)
⬇ Fetch API
Backend (FastAPI)
⬇ Logic Processing
Response (Text / Steps / Explanation)

Application Workflow


1.User selects mode (Math / Text Simplification)


2.User enters input


3.Frontend sends request to backend


4.Backend processes input


5.Output displayed with:


*Simplified text

*Steps

*Read-aloud option

*Visual placeholders





Additional Documentation
API Documentation
Base URL
http://127.0.0.1:8000


POST /process
Description
Processes math problems or simplifies text.
Request Body
{
  "text": "2+4*3",
  "mode": "math"
}

Response
{
  "steps": [
    "Follow BODMAS rule",
    "4 × 3 = 12",
    "2 + 12 = 14"
  ],
  "final_answer": "14"
}


AI Tools Used (Transparency Bonus)
Tool Used
ChatGPT

Purpose

Debugging backend errors

Designing accessible UI

Structuring FastAPI logic

README documentation support

Percentage of AI-generated code
~30%

Human Contributions


Project idea & planning

UI/UX decisions

Feature integration

Testing & debugging


Team Contributions
Malavika M S


  Frontend development
  Backend logic
  Accessibility features
  Documentation
  


