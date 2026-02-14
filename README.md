
🧠 SYNAPSE - Dyslexia-Friendly Learning Platform
A web application designed to help students with dyslexia learn more effectively through text simplification, visual representations, audio support, and interactive quizzes.
✨ Features
1️⃣ Text Input Feature
Paste or type learning content such as paragraphs, notes, or textbook text. Supports various educational topics.
2️⃣ Dyslexia-Friendly Reader
Uses OpenDyslexic font for better readability, larger spacing between lines and letters, soft non-straining background colors, and a clean clutter-free interface.
3️⃣ Text-to-Speech (Audio Reading)
Provides read-aloud functionality with a natural voice. Includes play, pause, and stop controls, adjustable reading speed (slow, normal, fast), and is suitable for auditory learners.
4️⃣ AI Simplified Explanation
Converts complex text into simple language using short, clear sentences. Includes a built-in knowledge base for common topics such as photosynthesis, evaporation, gravity, cells, and more.
5️⃣ Visual Representations
Displays colorful visual cards with icons and step-by-step visual explanations to support visual learners.
6️⃣ Math Problem Solver
Converts numbers into visual objects like apples, oranges, or bananas and explains each step visually. Supports addition, subtraction, multiplication, and division using expressions like 5 + 3, 10 - 4, 3 * 4 or 3 x 4, and 12 / 3 or 12 ÷ 3.
7️⃣ Quick Questions (Understanding Check)
Provides 2–3 simple multiple-choice quiz questions with instant feedback to check understanding of the content.
8️⃣ Progress Tracking
Tracks quizzes completed, calculates average scores, records time spent learning, and displays recent sessions to help measure improvement.
🚀 Installation & Setup
Prerequisites
Python 3.8 or higher, pip (Python package manager), and a modern web browser such as Chrome, Firefox, Safari, or Edge.
Step 1: Install Backend Dependencies
Install FastAPI and Uvicorn using pip.
Step 2: Run the Backend Server
Navigate to the project directory and run the backend server. The server will start running at http://0.0.0.0:8000�.
Step 3: Open the Frontend
Open the frontend.html file directly in your web browser by double-clicking, right-clicking and choosing a browser, or dragging it into the browser window.
📖 How to Use
For text simplification, select the “Learn Text” mode, paste or type educational content, and click “Make it Easy.” The platform will display a simplified explanation, visual representations, audio support, quiz questions, and progress tracking.
For math problems, select the “Solve Math” mode, enter a math expression such as 5 + 3 or 12 / 3, and click “Make it Easy.” The platform will show a visual step-by-step explanation using objects along with audio support.
🎯 Student Journey Example
A student opens the Synapse website, pastes text about photosynthesis, and clicks “Make it Easy.” The website sends the content to the Python backend, which simplifies the text and prepares quiz questions. The frontend displays the simplified explanation, visual cards, audio controls, and quiz questions. The student reads, listens, answers the quiz, checks results, and the progress is automatically saved. The student can later view improvement in the progress section.
🎨 Design Features
Uses OpenDyslexic font, high-contrast text, generous spacing, color-coded sections, large buttons, smooth animations, and a responsive design that works on phones, tablets, and computers.
🧪 Testing Examples
Text topics such as photosynthesis, evaporation, gravity, and cells can be tested. Math problems like 5 + 3, 10 - 4, 3 * 4, 12 / 3, 7 + 2, and 15 - 6 are supported.
🔧 Customization
New topics can be added by updating the simplifications dictionary in backend.py with simple explanations, visuals, and quiz questions. UI colors, fonts, spacing, and layout can be modified in the style section of frontend.html.
📊 API Endpoints
POST /process is used to process text or math input. POST /save-progress saves quiz results and time spent learning. GET /get-progress/{user_id} retrieves user progress data.
🐛 Troubleshooting
If a connection error occurs, ensure the backend server is running. If audio does not work, check browser permissions and device volume or try Chrome. If quizzes do not appear, use supported topics. If the backend does not start, verify the Python version and reinstall dependencies.
🌟 Future Enhancements
Future plans include adding more topics, user accounts, multiple language support, advanced math, PDF uploads, a teacher dashboard, a mobile app, offline mode, custom quizzes, and AI-powered topic detection.
📝 Technical Stack
Backend is built using Python, FastAPI, and Pydantic. Frontend uses HTML, CSS, and JavaScript. OpenDyslexic font is used for accessibility, Web Speech API for audio, and in-memory storage with future database support.
📄 License
This project is created for educational purposes to help students with dyslexia learn more effectively.
Made with ❤️ for all learners
If you want, I can now:
✅ Make this 100% hackathon-scoring friendly
✅ Add a short pitch version
✅ Align it to TinkerHub judging criteria
Just tell me 💙
