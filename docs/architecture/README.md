# Architecture

This is the approved GitHire architecture — the source of truth for implementation.

- **Frontend:** one React SPA, three role experiences (`/candidate`, `/recruiter`, `/creator`), lazy-loaded and theme-scoped (indigo/purple · green · YouTube-style). Feature code lives in `src/modules/{candidate,recruiter,creator,auth}`; shared UI/stores/types live in `src/modules/shared`.
- **Backend:** FastAPI modular monolith — modules under `backend/app/modules/`, each shaped `router / schemas / models / repository / service` as they are implemented.
- **External systems** (GitHub, AI, S3, email) are reached only via `backend/app/adapters/`.
- **Slow work** (parsing, embeddings, GitHub analysis) runs on Celery workers (`backend/app/workers/`) over Redis queues.
- **Data:** PostgreSQL 16 (FTS + pg_trgm, pgvector when the extension is available), Redis/Memurai for cache and queues, S3 for files.
- **Deploy:** Vercel (frontend), AWS (backend), orchestrated by `.github/workflows/`.

Major decisions will be recorded here as ADRs as feature work begins.
