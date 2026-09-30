# GitHire

A scalable AI-powered hiring and career platform with three experiences:

- **Candidate** — learning feed, job discovery, applications, networking
- **Recruiter** — candidate discovery, job posting, messaging
- **Creator** — YouTube-style learning content platform

## Quickstart (local development)

**Backend** (FastAPI on http://localhost:8000, docs at `/api/v1/docs`):

```bash
cd backend
./.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8000
```

**Celery worker + scheduler:**

```bash
cd backend
./.venv/Scripts/python.exe -m celery -A app.workers.celery_app.celery_app worker -Q default,ai_heavy -l info
./.venv/Scripts/python.exe -m celery -A app.workers.celery_app.celery_app beat -l info
```

**Frontend** (Vite on http://localhost:5173):

```bash
cd frontend
npm run dev
```

**Migrations:** `cd backend && ./.venv/Scripts/python.exe -m alembic upgrade head`

## Local infrastructure

PostgreSQL 16 (db `githire`) and Memurai (Redis-compatible) run as native
Windows services — no Docker needed for daily development. `docker-compose.yml`
is ready for when Docker Desktop is installed.

## Environment

- `backend/.env.example` / `frontend/.env.example` — copy to `.env`, fill values
- Never commit real `.env` files (already gitignored)

## Status

🚧 Environment ready — feature modules implemented per roadmap.
