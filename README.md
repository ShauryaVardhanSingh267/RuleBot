# RuleBot 🤖

A rule-based chatbot platform where anyone can create and share custom bots.  
Currently in **Week 1** of development.

---

## 🚀 Week 1 Progress

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
