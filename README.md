# 🛡️ Cybersecurity Awareness Chatbot — PROG6221 POE

**Module:** Programming 2A (PROG6221/w)  
**Institution:** The Independent Institute of Education (IIE)  
**Assessment:** Portfolio of Evidence (POE) — All 3 Parts  
**Platform:** Windows Forms (WinForms) — .NET 8

---

## Features by Part

### Part 1 — Core Chatbot
- Voice Greeting — WAV audio plays on startup
- ASCII Art Header — Cybersecurity-themed banner
- Personalised Interaction — Name-based responses
- Basic Response System — Handles common queries
- Input Validation — Graceful handling of bad input
- Styled Dark UI — Coloured text, borders, spacing
- Code Structure — Models / Services / Forms layers

### Part 2 — GUI + Dynamic Responses
- Windows Forms GUI with TabControl layout
- Keyword Recognition — 8+ cybersecurity keywords
- Random Responses — Multiple varied answers per topic
- Conversation Flow — Follow-up detection
- Memory and Recall — Remembers name and topic
- Sentiment Detection — Adjusts tone to user emotion
- Error Handling — Default responses, no crashes

### Part 3 / POE — Advanced Features
- Task Assistant — Add, view, complete, delete tasks
- MySQL Database — Full CRUD task persistence
- Reminders — Natural language date parsing
- Mini Quiz — 12 questions, shuffled, scored
- NLP Simulation — Keyword-based intent detection
- Activity Log — Timestamped log with Show More

---

## Setup

1. Clone the repo
2. Open CybersecurityChatbot.sln in Visual Studio 2022
3. Replace Resources/greeting.wav with your voice recording
4. (Optional) Run database_setup.sql in MySQL
5. Update connection string in Services/DatabaseService.cs
6. Press F5 to run

---

## Database (optional)

Run database_setup.sql in MySQL Workbench. If MySQL is unavailable, the app runs in-memory automatically.

---

## CI Screenshot

Add GitHub Actions green check screenshot here after first push.

---

## References

Pieterse, H. 2021. The Cyber Threat Landscape in South Africa: A 10-Year Review. The African Journal of Information and Communication, 28(28). doi: https://doi.org/10.23962/10539/32213.
