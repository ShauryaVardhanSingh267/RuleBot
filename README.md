# RuleBot 🤖

A rule-based chatbot platform where anyone can create and share custom bots.  
Currently in **Week 1** of development.

---

## 🚀Development Journal — Week 1

- **Database Layer (SQLite)**
  - Tables for bots, Q&A pairs, statistics, and users.
  - Sample data for testing (`cozy-cafe` and `tech-helper` bots).

- **Rule Engine**
  - Keyword, priority, similarity-based matching, and regex support.
  - Tunable weights + debug mode for transparent scoring.

- **Flask API**
  - `GET /health` for server checks.
  - `POST /chat` for real conversations with bots.
  - Fully verified locally using Postman.

---

## 🚀Development Journal — Week 2

- **Frontend & Backend Integration:**
- The chat interface now successfully sends user messages to the backend and receives responses in real-time.
- Smooth scroll-to-latest-message behavior implemented.


- **UI Styling & Theme:**
- Adopted a **blue-green theme** for branding, matching header and message bubbles.
- Doubled header font size and added glowing text-shadow for a polished, modern look.
- Clean, gradient background for the chat window with rounded corners.
- Responsive layout adjustments for mobile and tablet screens.


- **Animations & Interactions:**
- Messages now **fade in** smoothly when sent or received.
- Added animated **typing dots** instead of static “Bot is typing…” text for a dynamic user experience.
- Hover effects on message bubbles with subtle white glow for interactivity.


- **Code Cleanup:**
- Removed sound effects for sending/receiving messages for a distraction-free experience.
- Cleaned unnecessary complexity, keeping the code optimized and readable.


### **User Experience Improvements:**
- Smooth, polished feel of the interface with modern design touches.
- Typing indicator creates a realistic chat vibe.
- Better responsiveness means the chat works perfectly on both desktop and mobile devices.



Day 2 officially completed — **the chat app is functional, polished, and ready for the next build phase.**
