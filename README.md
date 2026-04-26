# 📖 AI Story Generator (Gemini-powered)

## Overview
This project is a web application that generates interactive stories using AI (Gemini).  
Users influence the story by choosing between **Option 1** and **Option 2**, creating a branching narrative.

---

## 🚀 Features

- AI-powered story generation (Gemini)
- Interactive branching (Option 1 / Option 2)
- FastAPI backend
- React frontend (Vite)
- Async job processing system
- Tree-based story structure

---

## 🔐 API Key (IMPORTANT)

You must provide your own Gemini API key.

Create a `.env` file in the backend folder:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ⚙️ Backend Setup

### 1. Clone repository

```
git clone <your-repo-url>
cd <repo>
```

### 2. Create backend

```
mkdir backend
cd backend
```

### 3. Install UV

UV is a fast Python package manager (like pip + venv combined).

```
pip install uv
uv --version
```

### 4. Initialize project

```
uv init .
```

### 5. Install dependencies

```
uv add fastapi[all] langchain-core python-dotenv sqlalchemy uvicorn psycopg2-binary
```

### 6. Project structure

```
backend/
│
├── core/
├── db/
├── models/
├── routers/
├── schemas/
```

Add `__init__.py` to all folders.

---

### 7. Environment config

```
DATABASE_URL=...
API_PREFIX=/api
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000
GEMINI_API_KEY=your_key
```

---

### 8. Run backend

```
uv run .\main.py
```

---

## 🧠 Architecture

### Story Structure

- Tree-based structure
- Each node has:
  - Option 1
  - Option 2

---

### Database

Using SQLAlchemy (ORM):

- Maps Python classes to DB tables
- No need to write SQL manually

Models:
- Story
- StoryNode

---

### Job System

Story generation is async.

States:
- in_progress
- complete
- failed

Flow:

Frontend:
```
Create job → Poll status
```

Backend:
```
Return status → If complete → Return story
```

---

## 📦 Schemas

Using Pydantic for:

- Request validation
- Response formatting

---

## 🌐 API Endpoints

### Create Story

**POST** `/api/stories/create`

Example request:

```bash
curl -X POST http://localhost:8000/api/stories/create \
-H "Content-Type: application/json" \
-d '{
  "prompt": "A knight enters a dark forest"
}'
```

Example response:

```json
{
  "job_id": "123",
  "status": "in_progress"
}
```

---

### Get Job Status

**GET** `/api/jobs/{job_id}`

Example:

```bash
curl http://localhost:8000/api/jobs/123
```

Response:

```json
{
  "job_id": "123",
  "status": "complete"
}
```

---

### Get Complete Story

**GET** `/api/stories/{story_id}/complete`

Example:

```bash
curl http://localhost:8000/api/stories/1/complete
```

Response:

```json
{
  "story_id": 1,
  "content": "Full generated story..."
}
```

---

## 💻 Frontend Setup

### 1. Create project

```
npm create vite@latest frontend -- --template react
cd frontend
npm install
```

### 2. Install dependencies

```
npm install axios
npm install react-router-dom
```

### 3. Run frontend

```
npm run dev
```

---

## 🚀 Deployment

Using Choreo:

- Build command:
```
npm run build
```

- Build path:
```
/dist
```

- Node version:
```
v20.20.2
```

---

## 🧩 Summary

This project combines:

- FastAPI backend
- React frontend
- Gemini AI story generation
- Branching narrative system
- Async job processing
